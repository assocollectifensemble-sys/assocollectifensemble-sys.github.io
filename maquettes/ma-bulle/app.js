/* Ma bulle — V1. Tout reste sur le téléphone : aucun compte, aucun serveur. */
(() => {
const C = window.CONTENUS;
const $ = (s, el = document) => el.querySelector(s);
const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const pad = n => String(n).padStart(2, "0");
const cle = d => `${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}`;
const auj = () => cle(new Date());
const MOIS = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"];
const JOURS = ["dimanche","lundi","mardi","mercredi","jeudi","vendredi","samedi"];
const dateLongue = k => { const d = new Date(k + "T12:00"); return `${JOURS[d.getDay()]} ${d.getDate()} ${MOIS[d.getMonth()]}`; };

/* ---------- Stockage local ---------- */
const S = {
  get(k, def) { try { const v = localStorage.getItem("mb_" + k); return v == null ? def : JSON.parse(v); } catch { return def; } },
  set(k, v) { localStorage.setItem("mb_" + k, JSON.stringify(v)); }
};
const journal = () => S.get("journal", {});           // { "2026-10-15": {humeur, emotions[], envie, positif, dur, t} }
const setJournal = j => S.set("journal", j);
const exosFaits = () => S.get("exos", {});              // { "2026-10-18": ["coherence", ...] }
const rituels = () => S.get("rituel", {});             // { "2026-10-23": {motiv:true, defi:true} }
function rituel(k) { const r = rituels()[k] || {}; const exo = (exosFaits()[k] || []).length > 0;
  const n = (r.motiv ? 1 : 0) + (exo ? 1 : 0) + (r.defi ? 1 : 0); return { motiv: !!r.motiv, exo, defi: !!r.defi, n }; }
function cocherRituel(champ) { const r = rituels(), k = auj(); r[k] = Object.assign({}, r[k], { [champ]: true }); S.set("rituel", r); }
function serie() { // jours de suite avec le rituel complet (aujourd'hui compte s'il est fini, sinon on part d'hier)
  const d = new Date(); if (rituel(cle(d)).n < 3) d.setDate(d.getDate() - 1);
  let n = 0; while (rituel(cle(d)).n === 3) { n++; d.setDate(d.getDate() - 1); } return n; }
function rappelSauvegarde() { // une fois par mois, dès qu'il y a une semaine de journal
  if (Object.keys(journal()).length < 7) return false;
  return Date.now() - Math.max(S.get("derniereSauvegarde", 0), S.get("sauverPlusTard", 0)) > 30 * 864e5;
}
const idxJour = () => Math.floor(new Date(auj()).getTime() / 864e5);
function marquerExo(id) { const e = exosFaits(), k = auj(); e[k] = [...new Set([...(e[k] || []), id])]; S.set("exos", e); }

/* Photos : IndexedDB (trop lourdes pour localStorage) */
const idb = () => new Promise((ok, ko) => {
  const r = indexedDB.open("mabulle", 1);
  r.onupgradeneeded = () => r.result.createObjectStore("photos", { keyPath: "id" });
  r.onsuccess = () => ok(r.result); r.onerror = () => ko(r.error);
});
const photos = {
  async tout() { const db = await idb(); return new Promise(ok => { const q = db.transaction("photos").objectStore("photos").getAll(); q.onsuccess = () => ok(q.result.sort((a,b)=>a.t-b.t)); q.onerror = () => ok([]); }); },
  async ajouter(blob) { const db = await idb(); return new Promise(ok => { const tx = db.transaction("photos", "readwrite"); tx.objectStore("photos").put({ id: crypto.randomUUID ? crypto.randomUUID() : String(Date.now()+Math.random()), t: Date.now(), blob }); tx.oncomplete = ok; }); },
  async suppr(id) { const db = await idb(); return new Promise(ok => { const tx = db.transaction("photos", "readwrite"); tx.objectStore("photos").delete(id); tx.oncomplete = ok; }); },
  async vider() { const db = await idb(); return new Promise(ok => { const tx = db.transaction("photos", "readwrite"); tx.objectStore("photos").clear(); tx.oncomplete = ok; }); }
};
const compresser = file => new Promise((ok, ko) => {
  const img = new Image(); const url = URL.createObjectURL(file);
  img.onload = () => { const m = 1100, k = Math.min(1, m / Math.max(img.width, img.height));
    const c = document.createElement("canvas"); c.width = Math.round(img.width * k); c.height = Math.round(img.height * k);
    c.getContext("2d").drawImage(img, 0, 0, c.width, c.height); URL.revokeObjectURL(url);
    c.toBlob(b => b ? ok(b) : ko(new Error("compression")), "image/jpeg", 0.82); };
  img.onerror = () => { URL.revokeObjectURL(url); ko(new Error("image")); };
  img.src = url;
});

/* ---------- Outils d'interface ---------- */
const ecran = $("#ecran");
let minuteurs = [];
const stopMinuteurs = () => { minuteurs.forEach(clearInterval); minuteurs.forEach(clearTimeout); minuteurs = []; };
function toast(t) { const el = $("#toast"); el.textContent = t; el.hidden = false; clearTimeout(toast.t); toast.t = setTimeout(() => el.hidden = true, 2200); }
function ouvrir(html, apres) {
  stopMinuteurs(); $("#feuilleContenu").innerHTML = html; $("#feuille").hidden = false;
  document.body.style.overflow = "hidden"; if (apres) apres($("#feuilleContenu"));
}
function fermer() { stopMinuteurs(); $("#feuille").hidden = true; document.body.style.overflow = ""; }
$("#feuille").addEventListener("click", e => { if (e.target.closest("[data-fermer]")) fermer(); });
document.addEventListener("keydown", e => { if (e.key === "Escape" && !$("#feuille").hidden) fermer(); });

/* ---------- Installation sur l'écran d'accueil ---------- */
const enAppli = () => matchMedia("(display-mode: standalone)").matches || navigator.standalone === true;
const estIOS = () => /iphone|ipad|ipod/i.test(navigator.userAgent) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
let promptInstall = null;
addEventListener("beforeinstallprompt", e => { e.preventDefault(); promptInstall = e; if (vue === "accueil" && $("#ecran")) afficher("accueil", true); });
addEventListener("appinstalled", () => { S.set("installee", true); promptInstall = null; toast("Ma bulle est sur ton écran d'accueil 🎉"); if (vue === "accueil") afficher("accueil", true); });
function montrerBandeauInstall() {
  if (enAppli() || S.get("installee", false)) return false;
  const plusTard = S.get("installPlusTard", 0); return Date.now() - plusTard > 3 * 864e5;
}
function guideInstall(html = "") {
  if (promptInstall) { promptInstall.prompt(); promptInstall.userChoice.then(c => { if (c.outcome === "accepted") S.set("installee", true); promptInstall = null; }); return; }
  ouvrir(`<div style="font-size:2.2rem">📲</div><h1>Mettre Ma bulle sur ton écran d'accueil</h1>
    ${estIOS() ? `<ol class="etapes-install">
        <li>En bas de Safari, touche le bouton <b>Partager</b> <span class="pict">⬆️</span></li>
        <li>Fais défiler et choisis <b>« Sur l'écran d'accueil »</b> <span class="pict">➕</span></li>
        <li>Touche <b>Ajouter</b>, puis ouvre Ma bulle depuis son icône.</li></ol>
        <p class="petit doux">Sur iPhone, l'appli installée garde ses propres données : installe-la avant de commencer à écrire, c'est plus simple.</p>`
      : `<ol class="etapes-install">
        <li>Touche le menu du navigateur <span class="pict">⋮</span> (en haut à droite)</li>
        <li>Choisis <b>« Installer l'application »</b> ou <b>« Ajouter à l'écran d'accueil »</b></li>
        <li>Ouvre Ma bulle depuis son icône.</li></ol>`}
    ${html}<button class="bouton plein" data-fermer>J'ai compris</button>`);
}

/* ---------- Garder les données ---------- */
async function demanderPersistance() { try { if (navigator.storage && navigator.storage.persist && !(await navigator.storage.persisted())) await navigator.storage.persist(); } catch {} }
const blobEnTexte = b => new Promise(ok => { const fr = new FileReader(); fr.onload = () => ok(fr.result); fr.readAsDataURL(b); });
async function sauvegarder() {
  const donnees = {}; Object.keys(localStorage).filter(k => k.startsWith("mb_") && k !== "mb_pin").forEach(k => donnees[k] = localStorage.getItem(k));
  const ph = []; for (const p of await photos.tout()) ph.push({ id: p.id, t: p.t, d: await blobEnTexte(p.blob) });
  const nom = `ma-bulle-sauvegarde-${auj()}.json`;
  const fichier = new File([JSON.stringify({ appli: "ma-bulle", version: 1, date: new Date().toISOString(), donnees, photos: ph })], nom, { type: "application/json" });
  S.set("derniereSauvegarde", Date.now());
  if (navigator.canShare && navigator.canShare({ files: [fichier] })) {
    try { await navigator.share({ files: [fichier], title: "Sauvegarde Ma bulle" }); toast("Sauvegarde prête 💾"); return; } catch (e) { if (e.name === "AbortError") return; }
  }
  const a = document.createElement("a"); a.href = URL.createObjectURL(fichier); a.download = nom; document.body.appendChild(a); a.click(); a.remove();
  toast("Sauvegarde téléchargée 💾");
}
async function restaurer(f) {
  try {
    const j = JSON.parse(await f.text()); if (j.appli !== "ma-bulle") throw 0;
    if (!confirm("Remplacer ce qu'il y a dans l'appli par cette sauvegarde ?")) return;
    Object.keys(localStorage).filter(k => k.startsWith("mb_") && k !== "mb_pin").forEach(k => localStorage.removeItem(k));
    Object.entries(j.donnees || {}).forEach(([k, v]) => { if (k.startsWith("mb_") && k !== "mb_pin") localStorage.setItem(k, v); });
    await photos.vider();
    const db = await idb();
    for (const p of j.photos || []) { const blob = await (await fetch(p.d)).blob();
      await new Promise(ok => { const tx = db.transaction("photos", "readwrite"); tx.objectStore("photos").put({ id: p.id, t: p.t, blob }); tx.oncomplete = ok; }); }
    S.set("accueilFait", true); toast("Tout est revenu 💛"); afficher("accueil");
  } catch { toast("Ce fichier n'est pas une sauvegarde Ma bulle"); }
}

/* ---------- Première ouverture ---------- */
function bienvenue(etape = 0) {
  const el = $("#bienvenue"); el.hidden = false; document.body.style.overflow = "hidden";
  const fin = () => { S.set("accueilFait", true); el.hidden = true; document.body.style.overflow = ""; demanderPersistance(); afficher("accueil"); };
  const points = n => `<div class="bv-points">${[0,1,2,3].map(i => `<i class="${i === n ? "on" : ""}"></i>`).join("")}</div>`;
  const E = [
    () => `<div class="bv-logo"><span class="marque-pastille"></span></div><h1>Bienvenue dans<br>${esc(C.nomAppli)}</h1>
      <p>Ton espace à toi pour prendre soin de toi, jour après jour.</p>
      <p class="bv-note">🔒 Tout reste sur ton téléphone. Pas de compte, rien n'est envoyé.</p>
      ${enAppli() ? "" : `<div class="bv-install"><b>📲 Installe-la d'abord sur ton écran d'accueil</b><small>${estIOS() ? "Sur iPhone, ce que tu écris dans Safari ne passe pas dans l'appli installée." : "Elle s'ouvrira comme une vraie appli, même sans internet."}</small>
        <button class="bouton blanc" data-bv="install">Comment faire ?</button></div>`}
      <button class="bouton blanc plein" data-bv="suite">${enAppli() ? "C'est parti" : "Continuer ici"}</button>
      <button class="lien bv-lien" data-bv="restaurer">J'ai une sauvegarde</button><input type="file" id="bvFichier" accept=".json,application/json" hidden>`,
    () => `${points(1)}<div class="bv-emoji">👋</div><h1>Comment tu t'appelles ?</h1><p>Ton prénom ou un surnom, juste pour que l'appli te dise bonjour.</p>
      <form data-bvform="prenom"><input class="champ" name="v" maxlength="30" autocomplete="given-name" placeholder="Ton prénom" value="${esc(S.get("prenom", ""))}">
      <button class="bouton blanc plein" style="margin-top:14px">Suivant</button></form><button class="lien bv-lien" data-bv="suite">Passer</button>`,
    () => `${points(2)}<div class="bv-emoji">⏱️</div><h1>On lance ton compteur ?</h1><p>Il compte les jours depuis que tu as décidé d'arrêter ou de lever le pied. Tu pourras le changer quand tu veux.</p>
      <button class="bouton blanc plein" data-bv="cpt-auj">À partir d'aujourd'hui</button>
      <form data-bvform="compteur" class="bv-date"><label>Depuis une autre date :</label><input class="champ" type="date" name="v" max="${auj()}"><button class="bouton blanc">OK</button></form>
      <button class="lien bv-lien" data-bv="suite">Plus tard</button>`,
    () => `${points(3)}<div class="bv-emoji">💛</div><h1>Pourquoi tu le fais ?</h1><p>Écris une chose qui te donne envie d'avancer. Tu la reliras chaque jour dans ton rituel.</p>
      <form data-bvform="motiv"><input class="champ" name="v" maxlength="140" placeholder="Ex. : me sentir libre"><button class="bouton blanc plein" style="margin-top:14px">Suivant</button></form>
      <button class="lien bv-lien" data-bv="suite">Passer</button>`,
    () => `<div class="bv-emoji">🌟</div><h1>C'est prêt${S.get("prenom", "") ? ", " + esc(S.get("prenom")) : ""} !</h1>
      <p>Chaque jour, ton rituel t'attend sur l'accueil : 3 petits pas, quelques minutes.</p>
      <p class="bv-note">Le bouton <b>Besoin d'aide</b>, en haut, est toujours là si ça ne va pas.</p>
      <button class="bouton blanc plein" data-bv="fin">Entrer dans ma bulle</button>`
  ];
  el.innerHTML = `<div class="bv-carte">${E[etape]()}</div>`;
  const suite = () => bienvenue(etape + 1);
  el.querySelectorAll("[data-bv]").forEach(b => b.onclick = () => {
    const a = b.dataset.bv;
    if (a === "suite") suite(); if (a === "fin") fin(); if (a === "install") guideInstall();
    if (a === "cpt-auj") { S.set("compteur", auj()); suite(); }
    if (a === "restaurer") $("#bvFichier", el).click();
  });
  const fi = $("#bvFichier", el); if (fi) fi.onchange = async () => { if (fi.files[0]) { await restaurer(fi.files[0]); if (S.get("accueilFait", false)) { el.hidden = true; document.body.style.overflow = ""; demanderPersistance(); } } };
  el.querySelectorAll("[data-bvform]").forEach(f => f.onsubmit = e => { e.preventDefault(); const v = f.v.value.trim(), t = f.dataset.bvform;
    if (t === "prenom" && v) S.set("prenom", v);
    if (t === "compteur") { if (!v) return; S.set("compteur", v); }
    if (t === "motiv" && v) S.set("motivations", [...S.get("motivations", []), v]);
    suite(); });
  const inp = el.querySelector("input.champ:not([type=date])"); if (inp) setTimeout(() => inp.focus(), 300);
}

/* ---------- Compteur ---------- */
function joursSans() {
  const d = S.get("compteur", null); if (!d) return null;
  return Math.max(0, Math.floor((new Date(auj() + "T12:00") - new Date(d + "T12:00")) / 864e5));
}

/* ---------- Écrans ---------- */
const VUES = {
accueil() {
  const j = journal(), today = j[auj()], n = joursSans();
  const idx = Math.floor(new Date(auj()).getTime() / 864e5);
  const ex = C.exercices[idx % C.exercices.length], defi = C.defis[idx % C.defis.length];
  const r = rituel(auj()), se = serie();
  const exFait = C.exercices.find(e => e.id === (exosFaits()[auj()] || []).slice(-1)[0]); const exR = exFait || ex;
  const ordre = C.phrases.map((p, i) => C.phrases[(i + idx) % C.phrases.length]);
  const coul = ["peche","rose","menthe","ciel","lavande","jaune"];
  const prenom = S.get("prenom", "");
  return `
  <h1>${prenom ? "Coucou " + esc(prenom) + " 👋" : "Coucou 👋"}</h1>
  <p class="doux">${dateLongue(auj())}</p>

  <section class="carte orange compteur">
    <div class="compteur-rond">${n == null ? "<b>–</b><small>jours</small>" : `<b>${n}</b><small>jour${n > 1 ? "s" : ""}</small>`}</div>
    <div>
      ${n == null
        ? `<h2>Mon compteur</h2><p>Compte les jours depuis que tu as décidé de faire une pause.</p><button class="bouton blanc" data-act="compteur">Démarrer</button>`
        : `<h2>${n === 0 ? "C'est le début 🌱" : "Bravo, continue 💪"}</h2><p class="petit">Depuis le ${dateLongue(S.get("compteur"))}</p><button class="lien" style="color:#fff" data-act="compteur">Modifier</button>`}
    </div>
  </section>

  ${montrerBandeauInstall() ? `<section class="carte orange bandeau-install">
    <div><b>📲 Mets ${esc(C.nomAppli)} sur ton écran d'accueil</b><small>Elle s'ouvrira comme une vraie appli, même sans internet.</small></div>
    <div class="bandeau-btns"><button class="bouton blanc" data-act="installer">Installer</button><button class="lien-blanc" data-act="install-plus-tard">Plus tard</button></div>
  </section>` : ""}
  ${rappelSauvegarde() ? `<section class="carte jaune bandeau-install">
    <div><b>💾 Pense à faire une sauvegarde</b><small>Pour garder ta progression si tu changes de téléphone ou si tu supprimes l'appli.</small></div>
    <div class="bandeau-btns"><button class="bouton" data-act="sauver">Sauvegarder</button><button class="lien" data-act="sauver-plus-tard">Plus tard</button></div>
  </section>` : ""}

  <section class="carte rituel">
    <div class="rituel-tete"><h2>Mon rituel du jour</h2>${se ? `<span class="serie">🔥 ${se} jour${se > 1 ? "s" : ""} de suite</span>` : ""}</div>
    <p class="petit doux" style="margin:0">${r.n === 3 ? "Rituel terminé, bravo 💛 À demain !" : "3 petits pas, quelques minutes."}</p>
    <div class="barre"><i style="width:${r.n / 3 * 100}%"></i></div>
    <button class="etape-r ${r.motiv ? "ok" : ""}" data-act="r-motiv"><span class="coche">${r.motiv ? "✓" : "1"}</span><span><b>Je relis pourquoi je le fais</b><small>Mes motivations</small></span></button>
    <button class="etape-r ${r.exo ? "ok" : ""}" data-ex="${exR.id}"><span class="coche">${r.exo ? "✓" : "2"}</span><span><b>Mon exercice : ${esc(exR.titre)}</b><small>${exR.ico} ${exR.duree}${r.exo ? "" : " · ou celui de ton choix"}</small></span></button>
    <button class="etape-r ${r.defi ? "ok" : ""}" data-act="r-defi"><span class="coche">${r.defi ? "✓" : "3"}</span><span><b>Mon petit défi</b><small>${esc(defi)}</small></span></button>
  </section>

  <section class="carte">
    <h2>Comment tu te sens ?</h2>
    <div class="humeurs">${C.humeurs.map(h => `<button class="humeur ${today && today.humeur === h.n ? "on" : ""}" data-humeur="${h.n}"><span>${h.e}</span>${h.mot}</button>`).join("")}</div>
    ${today ? `<p class="petit doux" style="margin:10px 0 0">Noté aujourd'hui. <button class="lien" data-vue-go="journal">Compléter mon journal</button></p>` : ""}
  </section>

  <div class="titre-section"><h2>Phrases pour toi</h2></div>
  <div class="defile" id="defile">${ordre.map((p, i) => `<div class="phrase ${coul[i % coul.length]}">${esc(p)}</div>`).join("")}</div>
  <div class="points" id="points">${ordre.map((_, i) => `<i class="${i ? "" : "on"}"></i>`).join("")}</div>


  <section class="carte peche bientot" style="margin-top:22px">
    <span class="badge">BIENTÔT</span>
    <h2 style="margin-top:8px">Le carnet complet</h2>
    <p class="doux" style="margin:0">Plus d'outils, d'explications et d'exercices pour aller plus loin.</p>
  </section>`;
},

journal() {
  const j = journal(), k = journal.jour || auj(), e = j[k] || {};
  const m = journal.mois || auj().slice(0, 7);
  return `
  <h1>Mon journal</h1>
  <p class="doux">Rien que pour toi. Tout reste sur ton téléphone.</p>

  <section class="carte">
    <div class="cal-entete" style="margin-bottom:4px"><h2 style="margin:0">${k === auj() ? "Aujourd'hui" : esc(dateLongue(k))}</h2>
      ${k !== auj() ? `<button class="lien" data-jour="${auj()}">Revenir à aujourd'hui</button>` : ""}</div>
    <label class="etiquette">Mon humeur</label>
    <div class="humeurs">${C.humeurs.map(h => `<button class="humeur ${e.humeur === h.n ? "on" : ""}" data-j-humeur="${h.n}"><span>${h.e}</span>${h.mot}</button>`).join("")}</div>

    <label class="etiquette">Ce que je ressens</label>
    <div class="puces">${C.emotions.map(x => `<button class="puce ${(e.emotions || []).includes(x) ? "on" : ""}" data-emo="${esc(x)}">${esc(x)}</button>`).join("")}</div>

    <label class="etiquette" for="envie">Mon envie aujourd'hui <span class="curseur-val" id="envieVal">${e.envie ?? 0}</span>/10</label>
    <input type="range" min="0" max="10" value="${e.envie ?? 0}" class="curseur" id="envie">

    <label class="etiquette" for="positif">Un moment positif ✨</label>
    <textarea id="positif" rows="2" placeholder="Même tout petit…">${esc(e.positif || "")}</textarea>

    <label class="etiquette" for="dur">Un moment où ça n'allait pas</label>
    <textarea id="dur" rows="2" placeholder="Qu'est-ce qui s'est passé ? Qu'est-ce qui m'a aidé·e ?">${esc(e.dur || "")}</textarea>

    <button class="bouton plein" style="margin-top:14px" data-act="enregistrer">Enregistrer</button>
  </section>

  <section class="carte">
    <div class="cal-entete"><button data-mois="-1" aria-label="Mois précédent">‹</button><h2 style="margin:0">${MOIS[+m.slice(5) - 1]} ${m.slice(0, 4)}</h2><button data-mois="1" aria-label="Mois suivant">›</button></div>
    ${calendrier(m, j)}
    <div class="legende">${C.humeurs.map(h => `<span><i style="background:${h.c}"></i>${h.mot}</span>`).join("")}</div>
  </section>

  <section class="carte">
    <h2>Mon parcours (14 jours)</h2>
    ${courbe(j)}
    <p class="petit doux" style="margin:6px 0 0"><span style="color:var(--orange-f);font-weight:900">●</span> humeur &nbsp; <span style="color:#9B87E8;font-weight:900">●</span> envie</p>
  </section>

  <div class="titre-section"><h2>Mes badges</h2></div>
  <section class="carte"><div class="badges">${(g => badgesTous().map(b => `<div class="bdg ${g[b.id] ? "on" : ""}"><span>${b.ico}</span><small>${esc(b.nom)}</small></div>`).join(""))(S.get("badges", {}))}</div>
    <p class="petit doux" style="margin:10px 0 0">Un badge gagné reste gagné, même si tu repars de zéro.</p></section>

  ${Object.keys(j).length ? `<div class="titre-section"><h2>Mes dernières notes</h2></div>
  <section class="carte">${Object.keys(j).sort().reverse().slice(0, 7).map(d => { const x = j[d]; const h = C.humeurs.find(h => h.n === x.humeur);
    return `<div class="entree"><time>${esc(dateLongue(d))} ${h ? h.e : ""}</time>
      ${x.emotions && x.emotions.length ? `<div class="petit doux">${x.emotions.map(esc).join(" · ")}</div>` : ""}
      ${x.positif ? `<p style="margin:4px 0 0">✨ ${esc(x.positif)}</p>` : ""}${x.dur ? `<p style="margin:4px 0 0">☁️ ${esc(x.dur)}</p>` : ""}</div>`; }).join("")}</section>` : ""}`;
},

exercices() {
  return `
  <h1>Exercices</h1>
  <p class="doux">Pour te calmer, revenir dans ton corps, laisser passer une envie.</p>
  <div class="tuiles">${C.exercices.map(x => `<button class="tuile ${x.couleur}" data-ex="${x.id}"><span class="ico">${x.ico}</span><span><b>${esc(x.titre)}</b><small>${x.duree}</small></span></button>`).join("")}</div>
  <p class="provisoire">Exercices à valider par Cindy</p>`;
},

comprendre() {
  return `
  <h1>Comprendre</h1>
  <p class="doux">De petits articles, à lire quand tu veux.</p>
  ${C.articles.map(a => `<button class="rangee" data-art="${a.id}"><span class="ico">${a.ico}</span><span><b>${esc(a.titre)}</b><small>${a.lecture} de lecture</small></span><span class="fleche">›</span></button>`).join("")}
  <p class="provisoire">Textes provisoires, à valider par Cindy</p>`;
},

coffre() {
  const motiv = S.get("motivations", []), musiques = S.get("musiques", []), victoires = S.get("victoires", []);
  return `
  <h1>Mon coffre</h1>
  <p class="doux">Ce qui te donne de la force, à garder sous la main.</p>

  <section class="carte jaune">
    <h2>Mes motivations</h2>
    <p class="petit doux">Pourquoi je fais ça ? Pour qui ? Pour quoi ?</p>
    <ul class="liste-perso">${motiv.map((x, i) => `<li><span>💛 ${esc(x)}</span><button data-suppr-motiv="${i}" aria-label="Supprimer">×</button></li>`).join("")}</ul>
    <form class="ajout-ligne" data-form="motiv"><input class="champ" name="v" maxlength="140" placeholder="Ex. : me sentir libre"><button class="bouton">+</button></form>
  </section>

  <section class="carte menthe">
    <h2>Mes victoires 🏆</h2>
    <p class="petit doux">Une bonne nouvelle, un moment dont tu es fier·e, une envie que tu as laissée passer… Tu les reliras les jours difficiles.</p>
    <ul class="liste-perso">${victoires.map((x, i) => [x, i]).reverse().map(([x, i]) => `<li><span><small class="doux">${esc(dateLongue(x.d))}</small><br>🏆 ${esc(x.t)}</span><button data-suppr-victoire="${i}" aria-label="Supprimer">×</button></li>`).join("")}</ul>
    <form class="ajout-ligne" data-form="victoire"><input class="champ" name="v" maxlength="160" placeholder="Ex. : j'ai dit non ce soir"><button class="bouton">+</button></form>
  </section>

  <section class="carte">
    <h2>Mes photos qui font du bien</h2>
    <p class="petit doux">Famille, amis, endroits que j'aime… Elles restent sur ton téléphone.</p>
    <div class="galerie" id="galerie"><label class="ajout-photo" aria-label="Ajouter une photo">+<input type="file" accept="image/*" multiple hidden id="filePhoto"></label></div>
  </section>

  <section class="carte ciel">
    <h2>Mes musiques calmes</h2>
    <p class="petit doux">Colle le lien d'une musique ou d'une playlist (YouTube, Spotify, Deezer…).</p>
    <ul class="liste-perso">${musiques.map((x, i) => `<li><span>🎵 <a class="lien" href="${esc(x.url)}" target="_blank" rel="noopener">${esc(x.nom)}</a></span><button data-suppr-musique="${i}" aria-label="Supprimer">×</button></li>`).join("")}</ul>
    <form class="ajout-ligne" data-form="musique"><input class="champ" name="v" inputmode="url" placeholder="https://…"><button class="bouton">+</button></form>
  </section>

  <section class="carte">
    <h2>Réglages</h2>
    <button class="rangee" data-act="prenom"><span class="ico">🙂</span><span><b>Mon prénom</b><small>${esc(S.get("prenom", "") || "Pas encore choisi")}</small></span><span class="fleche">›</span></button>
    <button class="rangee" data-act="code"><span class="ico">🔒</span><span><b>Code secret</b><small>${S.get("pin", null) ? "Activé" : "Désactivé"} · protège l'ouverture de l'appli</small></span><span class="fleche">›</span></button>
    <button class="rangee" data-act="compteur"><span class="ico">⏱️</span><span><b>Mon compteur</b><small>${S.get("compteur", null) ? "Depuis le " + esc(dateLongue(S.get("compteur"))) : "Pas démarré"}</small></span><span class="fleche">›</span></button>
    ${enAppli() || S.get("installee", false) ? "" : `<button class="rangee" data-act="installer"><span class="ico">📲</span><span><b>Mettre sur l'écran d'accueil</b><small>Pour l'ouvrir comme une vraie appli</small></span><span class="fleche">›</span></button>`}
    <button class="rangee" data-act="sauver"><span class="ico">💾</span><span><b>Sauvegarder mes données</b><small>${S.get("derniereSauvegarde", 0) ? "Dernière : " + esc(dateLongue(cle(new Date(S.get("derniereSauvegarde"))))) : "Un fichier à garder (fichiers, mail, Drive…)"}</small></span><span class="fleche">›</span></button>
    <button class="rangee" data-act="restaurer"><span class="ico">📂</span><span><b>Restaurer une sauvegarde</b><small>Nouveau téléphone, appli réinstallée…</small></span><span class="fleche">›</span></button>
    <input type="file" id="fichierRestau" accept=".json,application/json" hidden>
    <button class="rangee" data-act="effacer"><span class="ico">🗑️</span><span><b>Tout effacer</b><small>Supprime toutes tes données de ce téléphone</small></span><span class="fleche">›</span></button>
  </section>
  <p class="petit doux" style="text-align:center;margin:4px 12px 0">🔒 Tout reste sur ton téléphone : rien n'est envoyé. Fermer ou rouvrir l'appli ne perd rien. Si tu la supprimes ou changes de téléphone, utilise une sauvegarde.</p>`;
}
};

function calendrier(m, j) {
  const [y, mo] = m.split("-").map(Number);
  const premier = new Date(y, mo - 1, 1), nb = new Date(y, mo, 0).getDate();
  const decal = (premier.getDay() + 6) % 7;
  let h = ["L","M","M","J","V","S","D"].map(x => `<div class="j">${x}</div>`).join("");
  for (let i = 0; i < decal; i++) h += `<div class="c vide"></div>`;
  for (let d = 1; d <= nb; d++) {
    const k = `${y}-${pad(mo)}-${pad(d)}`, e = j[k], hu = e && C.humeurs.find(x => x.n === e.humeur);
    const fx = (exosFaits()[k] || []).length;
    h += `<button class="c ${k === auj() ? "auj" : ""} ${fx ? "ex" : ""}" data-jour="${k}" style="${hu ? "background:" + hu.c : ""}" aria-label="${d}${fx ? ", exercice fait" : ""}">${hu ? hu.e : d}</button>`;
  }
  return `<div class="cal">${h}</div>`;
}

function courbe(j) {
  const W = 320, H = 130, P = 16, jours = [];
  for (let i = 13; i >= 0; i--) { const d = new Date(); d.setDate(d.getDate() - i); jours.push(cle(d)); }
  const x = i => P + i * (W - 2 * P) / 13;
  const ligne = (val, max, coul) => {
    const pts = jours.map((k, i) => j[k] && val(j[k]) != null ? [x(i), H - P - (val(j[k]) / max) * (H - 2 * P)] : null);
    let d = "", deb = true; pts.forEach(p => { if (!p) { deb = true; return; } d += (deb ? "M" : "L") + p[0].toFixed(1) + " " + p[1].toFixed(1) + " "; deb = false; });
    return `<path d="${d}" fill="none" stroke="${coul}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>` +
      pts.filter(Boolean).map(p => `<circle cx="${p[0].toFixed(1)}" cy="${p[1].toFixed(1)}" r="4" fill="${coul}"/>`).join("");
  };
  const vide = !jours.some(k => j[k]);
  return `<svg class="courbe" viewBox="0 0 ${W} ${H}" role="img" aria-label="Courbe d'humeur et d'envie">
    ${[0, .5, 1].map(f => `<line x1="${P}" x2="${W - P}" y1="${P + f * (H - 2 * P)}" y2="${P + f * (H - 2 * P)}" stroke="#F3E2D6" stroke-dasharray="4 4"/>`).join("")}
    ${ligne(e => e.envie ?? null, 10, "#9B87E8")}${ligne(e => e.humeur ? e.humeur - 1 : null, 4, "#FF8A3D")}
    ${vide ? `<text x="${W / 2}" y="${H / 2 + 5}" text-anchor="middle" fill="#7A675C" font-size="13" font-weight="700">Remplis ton journal pour voir ta courbe</text>` : ""}
  </svg>`;
}

/* ---------- Navigation ---------- */
let vue = "accueil";
const TITRES = { accueil: C.nomAppli, journal: "Journal", exercices: "Exercices", comprendre: "Comprendre", coffre: "Mon coffre" };
function afficher(v, garderJour) {
  vue = v; if (!garderJour && v === "journal") { journal.jour = null; }
  majBadges();
  ecran.innerHTML = VUES[v]();
  $("#titreEcran").textContent = TITRES[v];
  document.querySelectorAll(".onglets button").forEach(b => b.classList.toggle("actif", b.dataset.vue === v));
  if (v === "coffre") chargerGalerie();
  if (v === "accueil") brancherDefile();
  window.scrollTo(0, 0);
}
document.querySelector(".onglets").addEventListener("click", e => { const b = e.target.closest("[data-vue]"); if (b) afficher(b.dataset.vue); });

function brancherDefile() {
  const d = $("#defile"), pts = [...document.querySelectorAll("#points i")]; if (!d) return;
  d.addEventListener("scroll", () => { const i = Math.round(d.scrollLeft / (d.firstElementChild.offsetWidth + 12)); pts.forEach((p, k) => p.classList.toggle("on", k === i)); }, { passive: true });
}

/* ---------- Journal : sauvegarde ---------- */
function majJour(modif) {
  const j = journal(), k = journal.jour || auj(); j[k] = Object.assign({ emotions: [] }, j[k], modif, { t: Date.now() }); setJournal(j);
}
function lireFormulaire() {
  const k = journal.jour || auj(), e = journal()[k] || {};
  return { envie: +$("#envie").value, positif: $("#positif").value.trim(), dur: $("#dur").value.trim(), emotions: e.emotions || [] };
}

/* ---------- Clics ---------- */
ecran.addEventListener("click", async e => {
  const t = e.target.closest("button, [data-jour]"); if (!t) return;
  const d = t.dataset;
  if (d.humeur) { majJour({ humeur: +d.humeur }); toast("C'est noté 💛"); afficher("accueil"); return; }
  if (d.vueGo) { afficher(d.vueGo); return; }
  if (d.jHumeur) { majJour(Object.assign(lireFormulaire(), { humeur: +d.jHumeur })); afficher("journal", true); return; }
  if (d.emo) { const k = journal.jour || auj(), j = journal(), em = new Set((j[k] && j[k].emotions) || []);
    em.has(d.emo) ? em.delete(d.emo) : em.add(d.emo); majJour(Object.assign(lireFormulaire(), { emotions: [...em] })); t.classList.toggle("on"); return; }
  if (d.jour) { journal.jour = d.jour === auj() ? null : d.jour; journal.mois = d.jour.slice(0, 7); afficher("journal", true); return; }
  if (d.mois) { const [y, m] = (journal.mois || auj().slice(0, 7)).split("-").map(Number); const n = new Date(y, m - 1 + +d.mois, 1);
    journal.mois = `${n.getFullYear()}-${pad(n.getMonth() + 1)}`; afficher("journal", true); return; }
  if (d.ex) { ouvrirExercice(d.ex); return; }
  if (d.art) { const a = C.articles.find(x => x.id === d.art);
    ouvrir(`<div style="font-size:2.4rem">${a.ico}</div><h1>${esc(a.titre)}</h1>${a.texte.map(p => `<p>${esc(p)}</p>`).join("")}<p class="provisoire">Texte provisoire, à valider par Cindy</p>`); return; }
  if (d.supprMotiv != null) { const m = S.get("motivations", []); m.splice(+d.supprMotiv, 1); S.set("motivations", m); afficher("coffre"); return; }
  if (d.supprVictoire != null) { const m = S.get("victoires", []); m.splice(+d.supprVictoire, 1); S.set("victoires", m); afficher("coffre"); return; }
  if (d.supprMusique != null) { const m = S.get("musiques", []); m.splice(+d.supprMusique, 1); S.set("musiques", m); afficher("coffre"); return; }
  if (d.supprPhoto) { if (confirm("Supprimer cette photo ?")) { await photos.suppr(d.supprPhoto); chargerGalerie(); } return; }
  const act = d.act;
  if (act === "enregistrer") { majJour(lireFormulaire()); toast("Journal enregistré 💛"); afficher("journal", true); }
  if (act === "compteur") reglerCompteur();
  if (act === "installer") guideInstall();
  if (act === "install-plus-tard") { S.set("installPlusTard", Date.now()); afficher("accueil", true); }
  if (act === "sauver") { await sauvegarder(); afficher(vue, true); }
  if (act === "sauver-plus-tard") { S.set("sauverPlusTard", Date.now()); afficher("accueil", true); }
  if (act === "restaurer") $("#fichierRestau").click();
  if (act === "r-defi") { if (!rituel(auj()).defi) { cocherRituel("defi"); toast("Défi relevé, bravo 💪"); } afficher("accueil"); }
  if (act === "r-motiv") ouvrirMotivations();
  if (act === "victoires") ouvrirVictoires();
  if (act === "prenom") { ouvrir(`<h2>Mon prénom</h2><p class="doux">Pour que l'appli te dise bonjour. Optionnel.</p>
      <form data-form="prenom"><input class="champ" name="v" maxlength="30" value="${esc(S.get("prenom", ""))}"><button class="bouton plein" style="margin-top:12px">Enregistrer</button></form>`); }
  if (act === "code") reglerCode();
  if (act === "effacer") { if (confirm("Effacer TOUT ce que tu as noté sur ce téléphone ? Ça ne peut pas être annulé.")) {
      Object.keys(localStorage).filter(k => k.startsWith("mb_")).forEach(k => localStorage.removeItem(k)); await photos.vider(); toast("Tout est effacé"); afficher("accueil"); bienvenue(0); } }
});
ecran.addEventListener("input", e => { if (e.target.id === "envie") $("#envieVal").textContent = e.target.value; });
ecran.addEventListener("change", async e => {
  if (e.target.id === "envie") majJour(lireFormulaire());
  if (e.target.id === "filePhoto") {
    for (const f of e.target.files) { try { await photos.ajouter(await compresser(f)); } catch { toast("Cette image n'a pas pu être ajoutée"); } }
    e.target.value = ""; chargerGalerie();
  }
});
ecran.addEventListener("focusout", e => { if (e.target.id === "positif" || e.target.id === "dur") majJour(lireFormulaire()); });
document.addEventListener("submit", e => {
  const f = e.target.closest("[data-form]"); if (!f) return; e.preventDefault();
  const v = f.v.value.trim(), type = f.dataset.form;
  if (type === "prenom") { S.set("prenom", v); fermer(); afficher(vue); return; }
  if (!v) return;
  if (type === "motivR") { S.set("motivations", [...S.get("motivations", []), v]); fermer(); ouvrirMotivations(); return; }
  if (type === "victoire") { S.set("victoires", [...S.get("victoires", []), { d: auj(), t: v }]); toast("Bravo, c'est une vraie victoire 🏆"); afficher("coffre"); return; }
  if (type === "motiv") { S.set("motivations", [...S.get("motivations", []), v]); afficher("coffre"); }
  if (type === "musique") { let url = v; if (!/^https?:\/\//i.test(url)) url = "https://" + url;
    try { const u = new URL(url); S.set("musiques", [...S.get("musiques", []), { url: u.href, nom: u.hostname.replace(/^www\./, "") + (u.pathname.length > 1 ? u.pathname.slice(0, 24) : "") }]); afficher("coffre"); }
    catch { toast("Ce lien n'a pas l'air valide"); } }
});

async function chargerGalerie() {
  const g = $("#galerie"); if (!g) return;
  g.querySelectorAll("figure").forEach(f => { const i = f.querySelector("img"); if (i) URL.revokeObjectURL(i.src); f.remove(); });
  const liste = await photos.tout();
  const ajout = g.querySelector(".ajout-photo");
  liste.forEach(p => { const f = document.createElement("figure"); f.innerHTML = `<img alt="Photo" src="${URL.createObjectURL(p.blob)}"><button class="suppr" data-suppr-photo="${p.id}" aria-label="Supprimer">×</button>`; g.insertBefore(f, ajout); });
}

/* ---------- Rituel : motivations ---------- */
function ouvrirMotivations() {
  const m = S.get("motivations", []);
  ouvrir(`<div style="font-size:2.2rem">💛</div><h1>Pourquoi je le fais</h1>
    ${m.length ? `<p class="doux">Relis-les doucement. Prends le temps de les sentir.</p><ul class="liste-perso">${m.map(x => `<li><span>💛 ${esc(x)}</span></li>`).join("")}</ul>
      <button class="bouton plein" id="luMotiv">Je les ai relues ✓</button>`
    : `<p class="doux">Écris ce qui te donne envie d'avancer : pour toi, pour quelqu'un, pour une chose que tu veux vivre.</p>
      <form class="ajout-ligne" data-form="motivR"><input class="champ" name="v" maxlength="140" placeholder="Ex. : me sentir libre"><button class="bouton">+</button></form>`}
    <p class="petit doux" style="margin-top:14px">Tu peux les changer quand tu veux dans « Mon coffre ».</p>`, el => {
    const b = $("#luMotiv", el); if (b) b.onclick = () => { cocherRituel("motiv"); fermer(); afficher("accueil"); toast("Bien joué 💛"); };
  });
}

/* ---------- Mes victoires ---------- */
function ouvrirVictoires() {
  const v = S.get("victoires", []);
  ouvrir(`<div style="font-size:2.2rem">🏆</div><h1>Mes victoires</h1>
    <p class="doux">Tout ce que tu as déjà réussi. Tu l'as fait une fois, tu peux le refaire.</p>
    ${v.length ? `<ul class="liste-perso">${v.slice().reverse().map(x => `<li><span><small class="doux">${esc(dateLongue(x.d))}</small><br>🏆 ${esc(x.t)}</span></li>`).join("")}</ul>` : `<p class="petit doux">Pas encore de victoire notée. Elles se remplissent depuis « Mon coffre ».</p>`}`);
}

/* ---------- Badges ---------- */
function badgesTous() {
  const n = joursSans() || 0, se = serie(), ex = Object.values(exosFaits()).reduce((a, x) => a + x.length, 0);
  const nj = Object.keys(journal()).length, nv = S.get("victoires", []).length;
  return [
    { id: "j1", ico: "🌱", nom: "1er jour", ok: n >= 1 }, { id: "j7", ico: "🌿", nom: "7 jours", ok: n >= 7 },
    { id: "j30", ico: "🌳", nom: "1 mois", ok: n >= 30 }, { id: "j90", ico: "🏔️", nom: "3 mois", ok: n >= 90 },
    { id: "s3", ico: "🔥", nom: "Rituel 3 jours de suite", ok: se >= 3 }, { id: "s7", ico: "☀️", nom: "Rituel 7 jours de suite", ok: se >= 7 },
    { id: "e10", ico: "🧘", nom: "10 exercices", ok: ex >= 10 }, { id: "n7", ico: "📓", nom: "7 jours de journal", ok: nj >= 7 },
    { id: "v1", ico: "🏆", nom: "1re victoire notée", ok: nv >= 1 }
  ];
}
function majBadges() { // les badges gagnés restent gagnés, même si le compteur repart à zéro
  const g = S.get("badges", {}), neufs = [];
  badgesTous().forEach(b => { if (b.ok && !g[b.id]) { g[b.id] = auj(); neufs.push(b); } });
  if (neufs.length) { S.set("badges", g); toast(`Nouveau badge : ${neufs[0].ico} ${neufs[0].nom} 🎉`); }
  return g;
}

/* ---------- Ressenti après un exercice ---------- */
function ressentiApres(x, el) {
  el.innerHTML = `<div style="font-size:2.4rem">💛</div><h1>Bravo, c'est fait !</h1><p class="doux">Et maintenant, tu te sens comment ?</p>
    <div class="humeurs">${C.humeurs.map(h => `<button class="humeur" data-apres="${h.n}"><span>${h.e}</span>${h.mot}</button>`).join("")}</div>
    <button class="lien" style="margin-top:16px" id="passer">Passer</button>`;
  const fin = () => { fermer(); afficher(vue, true); };
  el.querySelector(".humeurs").onclick = e => { const b = e.target.closest("[data-apres]"); if (!b) return;
    const r = S.get("ressentis", {}), k = auj(); r[k] = [...(r[k] || []), { ex: x.id, n: +b.dataset.apres }]; S.set("ressentis", r);
    if (!(journal()[k] || {}).humeur) { const sv = journal.jour; journal.jour = null; majJour({ humeur: +b.dataset.apres }); journal.jour = sv; }
    toast("C'est noté 💛"); fin(); };
  $("#passer", el).onclick = fin;
}

/* ---------- Compteur & code ---------- */
function reglerCompteur() {
  ouvrir(`<h2>Mon compteur</h2><p class="doux">Depuis quand as-tu arrêté ? Si tu as craqué, tu peux repartir d'aujourd'hui : ce n'est pas un échec, c'est un nouveau départ.</p>
    <input type="date" class="champ" id="dateCompteur" max="${auj()}" value="${S.get("compteur", auj())}">
    <button class="bouton plein" style="margin-top:12px" id="okCompteur">Enregistrer</button>
    <button class="bouton ligne plein" style="margin-top:10px" id="zeroCompteur">Repartir d'aujourd'hui</button>
    ${S.get("compteur", null) ? `<button class="lien" style="margin-top:14px" id="stopCompteur">Arrêter le compteur</button>` : ""}`, el => {
    $("#okCompteur", el).onclick = () => { const v = $("#dateCompteur", el).value; if (v) { S.set("compteur", v > auj() ? auj() : v); fermer(); afficher(vue); toast("Compteur enregistré"); } };
    $("#zeroCompteur", el).onclick = () => { S.set("compteur", auj()); fermer(); afficher(vue); toast("Nouveau départ 🌱"); };
    const s = $("#stopCompteur", el); if (s) s.onclick = () => { localStorage.removeItem("mb_compteur"); fermer(); afficher(vue); };
  });
}
function reglerCode() {
  const actif = !!S.get("pin", null);
  ouvrir(`<h2>Code secret</h2><p class="doux">Un code à 4 chiffres pour ouvrir l'appli. ${actif ? "" : "Attention : si tu l'oublies, il faudra tout effacer."}</p>
    ${actif ? `<button class="bouton ligne plein" id="offPin">Désactiver le code</button>` :
    `<input class="champ" id="pin1" inputmode="numeric" maxlength="4" placeholder="4 chiffres" autocomplete="off">
     <input class="champ" id="pin2" inputmode="numeric" maxlength="4" placeholder="Encore une fois" autocomplete="off" style="margin-top:10px">
     <button class="bouton plein" style="margin-top:12px" id="okPin">Activer</button>`}`, el => {
    if (actif) { $("#offPin", el).onclick = () => { localStorage.removeItem("mb_pin"); fermer(); afficher(vue); toast("Code désactivé"); }; return; }
    $("#okPin", el).onclick = async () => { const a = $("#pin1", el).value, b = $("#pin2", el).value;
      if (!/^\d{4}$/.test(a)) return toast("Il faut 4 chiffres"); if (a !== b) return toast("Les deux codes sont différents");
      S.set("pin", await hache(a)); fermer(); afficher(vue); toast("Code activé 🔒"); };
  });
}
async function hache(s) {
  if (crypto.subtle) { const b = await crypto.subtle.digest("SHA-256", new TextEncoder().encode("mabulle:" + s)); return [...new Uint8Array(b)].map(x => x.toString(16).padStart(2, "0")).join(""); }
  return "p" + s;
}
function verrou() {
  const pin = S.get("pin", null); if (!pin) return;
  const v = $("#verrou"), pave = $("#pave"), pts = [...document.querySelectorAll("#pinPoints i")]; let saisie = "";
  v.hidden = false;
  pave.innerHTML = [1,2,3,4,5,6,7,8,9,"",0,"⌫"].map(x => x === "" ? "<span></span>" : `<button data-k="${x}">${x}</button>`).join("");
  pave.onclick = async e => { const k = e.target.closest("[data-k]"); if (!k) return; $("#pinErreur").hidden = true;
    saisie = k.dataset.k === "⌫" ? saisie.slice(0, -1) : (saisie + k.dataset.k).slice(0, 4);
    pts.forEach((p, i) => p.classList.toggle("on", i < saisie.length));
    if (saisie.length === 4) { if (await hache(saisie) === pin) v.hidden = true; else { $("#pinErreur").hidden = false; saisie = ""; pts.forEach(p => p.classList.remove("on")); } } };
}

/* ---------- Exercices ---------- */
function ouvrirExercice(id) {
  const x = C.exercices.find(e => e.id === id);
  if (x.type === "respiration") {
    ouvrir(`<div style="font-size:2.2rem">${x.ico}</div><h1>${esc(x.titre)}</h1><p>${esc(x.intro)}</p>
      <div class="souffle"><div class="bulle" id="bulle"><span id="consigne">Prêt·e ?</span></div>
      <div class="chrono" id="chrono">${Math.floor(x.total / 60)}:00</div>
      <button class="bouton" id="go">Commencer</button></div>`, el => {
      const bulle = $("#bulle", el), cons = $("#consigne", el), chrono = $("#chrono", el);
      $("#go", el).onclick = ev => { ev.target.hidden = true; let reste = x.total, ph = 0;
        const phases = [["Inspire", .95], ["Bloque", .95], ["Expire", .45], ["Bloque", .45]];
        const pas = () => { while (!x.rythme[ph % 4]) ph++; const i = ph % 4, s = x.rythme[i];
          bulle.style.setProperty("--t", s + "s"); bulle.style.setProperty("--s", phases[i][1]); cons.textContent = phases[i][0];
          ph++; minuteurs.push(setTimeout(pas, s * 1000)); };
        pas();
        minuteurs.push(setInterval(() => { reste--; chrono.textContent = `${Math.floor(reste / 60)}:${pad(reste % 60)}`;
          if (reste <= 0) { stopMinuteurs(); cons.textContent = "Bravo 💛"; bulle.style.setProperty("--s", .7); marquerExo(x.id); minuteurs.push(setTimeout(() => ressentiApres(x, el), 1500)); } }, 1000)); };
    });
  } else {
    let i = 0;
    const rendu = el => {
      const fin = i >= x.etapes.length - 1;
      el.querySelector("#etapes").innerHTML = `<div class="barre"><i style="width:${(i + 1) / x.etapes.length * 100}%"></i></div>
        <div class="etape-num">Étape ${i + 1} sur ${x.etapes.length}</div><p class="etape-texte">${esc(x.etapes[i])}</p>
        ${x.minuteur && i === 3 ? `<div class="chrono" id="chrono" style="margin-bottom:12px">10:00</div><button class="bouton ligne" id="lanceMin" style="margin-bottom:12px">Lancer 10 minutes</button>` : ""}
        <div style="display:flex;gap:10px">${i ? `<button class="bouton ligne" id="prec">Retour</button>` : ""}
        <button class="bouton" style="flex:1" id="suiv">${fin ? "Terminer" : "Suivant"}</button></div>`;
      const p = $("#prec", el); if (p) p.onclick = () => { i--; stopMinuteurs(); rendu(el); };
      $("#suiv", el).onclick = () => { if (fin) { marquerExo(x.id); stopMinuteurs(); ressentiApres(x, el); } else { i++; rendu(el); } };
      const lm = $("#lanceMin", el); if (lm) lm.onclick = () => { lm.hidden = true; let r = x.minuteur;
        minuteurs.push(setInterval(() => { r--; $("#chrono", el).textContent = `${Math.floor(r / 60)}:${pad(r % 60)}`; if (r <= 0) { stopMinuteurs(); $("#chrono", el).textContent = "C'est passé 🌊"; } }, 1000)); };
    };
    ouvrir(`<div style="font-size:2.2rem">${x.ico}</div><h1>${esc(x.titre)}</h1><p class="doux">${esc(x.intro)}</p><div id="etapes"></div>`, rendu);
  }
}

/* ---------- Aide ---------- */
$("#btnAide").addEventListener("click", () => ouvrir(`<h1>Besoin d'aide ?</h1>
  <p class="doux">Tu n'es pas seul·e. Ces lignes sont là pour t'écouter, sans te juger.</p>
  ${C.aide.map(a => `<a class="num ${a.urgent ? "urgent" : ""}" href="tel:${a.tel}"><span><b>${esc(a.nom)}</b><small>${esc(a.detail)}</small></span><span class="tel">${esc(a.aff || a.tel)}</span></a>`).join("")}
  <p class="petit doux">Tu peux aussi parler à un adulte de confiance : parent, infirmier·e scolaire, éducateur·rice.</p>
  ${S.get("victoires", []).length ? `<button class="bouton ligne plein" id="aideVict" style="margin-bottom:10px">Relire mes victoires 🏆</button>` : ""}
  <button class="bouton ligne plein" data-fermer>Faire un exercice de calme</button>`, el => {
    const av = el.querySelector("#aideVict"); if (av) av.onclick = () => { fermer(); setTimeout(ouvrirVictoires, 50); };
    el.querySelector("[data-fermer]").addEventListener("click", () => setTimeout(() => ouvrirExercice("coherence"), 50));
  }));

document.addEventListener("change", e => { if (e.target.id === "fichierRestau" && e.target.files[0]) restaurer(e.target.files[0]); });

/* ---------- Démarrage ---------- */
if (S.get("accueilFait", false) || Object.keys(localStorage).some(k => k.startsWith("mb_journal") || k === "mb_prenom")) { S.set("accueilFait", true); afficher("accueil"); demanderPersistance(); }
else { afficher("accueil"); bienvenue(0); }
verrou();
if ("serviceWorker" in navigator && location.protocol === "https:") navigator.serviceWorker.register("sw.js").catch(() => {});
})();
