# -*- coding: utf-8 -*-
"""Générateur du site « Une 2CV, mille histoires »."""
import os, json
from urllib.parse import quote

OUT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://une2cvmillehistoires.re"
wa_link = lambda msg: "https://wa.me/262693828108?text=" + quote(msg)
WA = "https://wa.me/262693828108?text=Bonjour%20Jonathan%20!%20Je%20souhaite%20%C3%A9crire%20une%20histoire%20avec%20la%202CV%20%F0%9F%8C%BF"
WA_MARIAGE = "https://wa.me/262693828108?text=Bonjour%20!%20Nous%20nous%20marions%20et%20la%202CV%20nous%20fait%20r%C3%AAver%20%F0%9F%92%8D"
WA_BALADE = "https://wa.me/262693828108?text=Bonjour%20Jonathan%20!%20Je%20souhaite%20r%C3%A9server%20une%20balade%20en%202CV%20%F0%9F%8C%BF"
WA_SHOOT = "https://wa.me/262693828108?text=Bonjour%20!%20J%27ai%20un%20projet%20de%20shooting%2Fanimation%20avec%20la%202CV%20%F0%9F%93%B8"

D = lambda i, w=1200: "https://lh3.googleusercontent.com/d/%s=w%d" % (i, w)
IMG = {
    "cover":      "1NjNyYuacmAvG1c_-7PBwufJfvmw9mf7S",
    "logo":       "1lu2qT2IH4eq5LVziqZFny9bxDXRXNJuF",
    "eglise":     "1JHuD1eSM4EEqVxI6D7EwvVeBKyvFifj1",
    "sunset_couple":"1Gy5zH_t3Zl5u-45CXWDzcE1R1kUWNxQD",
    "shooting_nb":"1RbFyL6dWLyeURUL4nQ7jtws2vO75DoJV",
    "couple_rosalie":"1SSYopYxHdc7zoMp4OFbQYYqX1lzVm8gt",
    "creole":     "1q2pxV5ULTtETu_qCWBdenC0TDp9ATlB-",
    "sunset_soizig":"1l2zlg5zSE6Sc-RoXg_sfH49CoGWsplwR",
    "interieur":  "1TyIx3gJIyWa6fCPther92B2FdGIEZGZn",
    "rosalie":    "16BMC5e7VygkIoFSiYnJwqY2rNteevcTP",
    "soizig":     "1mJEleJ0RWXJeRdRT7bhvPmeogdzWOLd_",
    "jonathan":   "1ZQOOoIi5Jyo48L69FG4ajjr5lB6sK3A6",
    "homme_rosalie":"1rM_GBNRjxUD95_5-8SEC6pAcAwuXOTN4",
    "slackline":  "1SWpGGfAjPftjy0m24fjehv2cG0HBIusX",
    "rosalie_deco":"1XrRn3E2LBfN67WXv8kPuoDNyqPNcO6rn",
    "coffre":     "1Rh98q64ssm7AbMxzQGfp9DIwnrCDO5UF",
    "grand1":     "1vQs4v02tbcMTqCGIRPnqusMN1XAcKNU0",
    "grand2":     "1GzjxQrBywQPhAAKnCYyOqh343YJz7-Zk",
}

WSVG = '<svg viewBox="0 0 24 24" class="wa-ico"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.885-9.885 9.885m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>'

INSTA = "https://www.instagram.com/une2cv.millehistoires/"
FB = "https://www.facebook.com/profile.php?id=61586545132399"

def head(title, desc, path, jsonld=None, noindex=False):
    j = ""
    if jsonld:
        j = '<script type="application/ld+json">%s</script>' % json.dumps(jsonld, ensure_ascii=False)
    robots = '<meta name="robots" content="noindex">' if noindex else ""
    return """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s%s">
%s
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:image" content="%s">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:url" content="%s%s">
<link rel="icon" type="image/png" href="%s">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Jost:wght@300;400;500&family=Pinyon+Script&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
%s
</head>
<body>
""" % (title, desc, DOMAIN, path, robots, title, desc, D(IMG["cover"], 1200), DOMAIN, path, D(IMG["logo"], 200), j)

def navbar(active="", opaque=False):
    links = [("mariage.html","Mariage","mariage"),("balades.html","Balades","balades"),
             ("shooting-evenements.html","Shootings","shooting"),
             ("rosalie-et-soizig.html","Rosalie & Soizig","voitures"),("faq.html","Questions","faq")]
    lis = "".join('<li><a href="/%s"%s>%s</a></li>' % (h, ' class="actif"' if k==active else "", t) for h,t,k in links)
    return """<nav id="nav"%s>
  <a class="logo-lien" href="/"><img src="%s" alt="Une 2CV, mille histoires — logo"></a>
  <ul>%s<li class="keep"><a class="nav-wa" href="%s">%s WhatsApp</a></li></ul>
</nav>
<a class="wa-float" href="%s" aria-label="Discuter sur WhatsApp">%s</a>
""" % (' class="opaque"' if opaque else "", D(IMG["logo"], 400), lis, WA, WSVG, WA, WSVG)

def footer():
    return """<footer>
  <img class="logo-pied" src="%s" alt="Une 2CV, mille histoires">
  <br>2CV avec chauffeur VTC agréé — mariages, balades, shootings & évènements — toute l'île de La Réunion
  <div class="liens-pages"><a href="/mariage.html">Mariage</a> · <a href="/balades.html">Balades</a> · <a href="/shooting-evenements.html">Shootings</a> · <a href="/rosalie-et-soizig.html">Rosalie & Soizig</a> · <a href="/faq.html">FAQ</a> · <a href="/contact.html">Contact</a></div>
  <a href="%s">Instagram</a> · <a href="%s">Facebook</a> · <a href="%s">WhatsApp</a> · <a href="tel:+262693828108">0693 82 81 08</a><br>
  Projet porté par l'association Collectif Ensemble — Saint-Leu, La Réunion · <a href="/mentions-legales.html">Mentions légales</a>
</footer>
<script src="/assets/site.js"></script>
</body>
</html>""" % (D(IMG["logo"], 400), INSTA, FB, WA)

def btn_wa(txt, url):
    return '<a class="btn btn-wa" href="%s">%s %s</a>' % (url, WSVG, txt)

def page_hero(img_key, kicker, h1, accroche):
    return """<div class="page-hero">
  <img class="fond" src="%s" alt="">
  <div class="voile"></div>
  <div class="contenu">
    <p class="kicker">%s</p>
    <h1>%s</h1>
    <p class="accroche">%s</p>
  </div>
</div>
""" % (D(IMG[img_key], 1920), kicker, h1, accroche)

def cta_band(titre, script, btxt, burl):
    return """<section class="cta-band">
  <h2 class="titre reveal">%s <span class="script">%s</span></h2>
  <div class="reveal">%s</div>
  <p class="sous-note reveal">Ou par téléphone : <a href="tel:+262693828108" style="color:var(--terre)">0693 82 81 08</a> · <a href="/contact.html" style="color:var(--terre)">formulaire de contact</a></p>
</section>
""" % (titre, script, btn_wa(btxt, burl))

pages = {}

# ============================================================ INDEX
biz_jsonld = {
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Une 2CV, mille histoires",
  "description": "Location de 2CV avec chauffeur VTC agréé pour mariages, balades, shootings et évènements à La Réunion.",
  "url": DOMAIN,
  "telephone": "+262693828108",
  "email": "asso.collectif.ensemble@gmail.com",
  "image": D(IMG["cover"], 1200),
  "logo": D(IMG["logo"], 400),
  "address": {"@type": "PostalAddress", "addressLocality": "Saint-Leu", "addressRegion": "La Réunion", "addressCountry": "RE"},
  "areaServed": {"@type": "AdministrativeArea", "name": "Île de La Réunion"},
  "priceRange": "Sur devis",
  "sameAs": [INSTA, FB],
  "makesOffer": [
    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Voiture de mariage 2CV avec chauffeur", "url": DOMAIN + "/mariage.html"}},
    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Balades en 2CV avec chauffeur", "url": DOMAIN + "/balades.html"}},
    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Location 2CV shooting photo, cinéma et évènements", "url": DOMAIN + "/shooting-evenements.html"}}
  ]
}

index_body = navbar() + """
<audio id="musique" loop preload="auto">
  <source src="https://cdn.pixabay.com/audio/2026/03/21/14-39-25-311.mp3" type="audio/mpeg">
  <source src="https://cdn.pixabay.com/audio/2026/01/22/08-13-37-150.mp3" type="audio/mpeg">
</audio>
<button class="sound" id="btn-son" title="Couper / remettre la musique" aria-label="Couper ou remettre la musique">🎷</button>

<header class="hero">
  <div class="hero-visuel">
    <img class="hero-img" src="%(cover)s" alt="Rosalie et Soizig, nos deux 2CV décorées pour un mariage face à l'océan à La Réunion">
    <div class="hero-veil"></div>
    <div class="il-etait">Il était une fois…</div>
  </div>
  <div class="hero-bas">
    <img class="hero-logo" src="%(logo)s" alt="Une 2CV, mille histoires">
    <div class="hero-mots">Mariages · Balades · Shootings — La Réunion</div>
    <div class="hero-actions">
      %(btnwa)s
      <a class="btn btn-ligne" href="#prestations">Découvrir</a>
    </div>
  </div>
</header>

<div class="marquee"><div class="track" id="mq">
  <span>Mariages</span>·<span>EVJF & EVJG</span>·<span>Balades coucher de soleil</span>·<span>Brunch péï</span>·<span>Lever de soleil</span>·<span>EVJF & EVJG</span>·<span>Shootings</span>·<span>Cinéma</span>·<span>Spectacles</span>·<span>Chauffeur VTC agréé</span>·
</div></div>

<section id="prestations" class="doux">
  <p class="kicker reveal">Les possibilités</p>
  <h2 class="titre reveal">Quelle histoire écrirons-nous <span class="script">ensemble ?</span></h2>
  <div class="prestas">
    <a class="presta reveal" href="/mariage.html">
      <div class="cadre"><div class="imgbox"><img src="%(eglise)s" alt="Sortie d'église en 2CV à La Réunion" loading="lazy"></div></div>
      <h3>Évènements</h3>
      <p class="souligne">Mariage · Elopement · EVJF / EVJG · Anniversaire · Demande en mariage</p>
      <span class="plus">Découvrir</span>
    </a>
    <a class="presta reveal" href="/balades.html">
      <div class="cadre"><div class="imgbox"><img src="%(sunset)s" alt="Balade en 2CV au coucher de soleil à La Réunion" loading="lazy"></div></div>
      <h3>Balades</h3>
      <p class="souligne">Coucher de soleil · Brunch péï · Lever de soleil · Journées à thème</p>
      <span class="plus">Choisir sa balade</span>
    </a>
    <a class="presta reveal" href="/shooting-evenements.html">
      <div class="cadre"><div class="imgbox"><img src="%(shoot)s" alt="Shooting photo de couple avec la 2CV" loading="lazy"></div></div>
      <h3>Shootings</h3>
      <p class="souligne">Photo · Cinéma · Clips · Évènement particulier</p>
      <span class="plus">Proposer un projet</span>
    </a>
  </div>
  <p class="sous-note reveal">Toutes les prestations sont <strong>avec chauffeur VTC agréé</strong> — vous profitez, je conduis. En option : décoration florale (votre fleuriste ou le nôtre), animations & spectacles.</p>
</section>

<section id="mariage" class="fond-mariage">
  <div class="cadre-univers">
  <div class="feature">
    <div class="photo reveal"><img src="%(couple)s" alt="Les mariés montent à bord de Rosalie, 2CV blanche décorée" loading="lazy"></div>
    <div class="reveal">
      <p class="kicker" style="text-align:left">Le plus beau jour</p>
      <h2>Votre mariage <span class="script">en 2CV</span></h2>
      <p>Le plus beau des cortèges est aussi le plus simple : une 2CV blanche, des rubans, et vous deux. Je viens vous chercher, je vous conduis, je klaxonne votre bonheur — vous n'avez plus qu'à vivre l'instant.</p>
      <ul class="liste-opts">
        <li>Cortège & sortie de cérémonie, partout sur l'île</li>
        <li>Séance photo des mariés sur les plus beaux paysages</li>
        <li>Décoration personnalisée — votre fleuriste ou le nôtre</li>
        <li>EVJF / EVJG & demandes en mariage en toute complicité</li>
        <li>En option : spectacle de feu, jonglage, animations pour les enfants</li>
      </ul>
      <a class="btn btn-brun" href="/mariage.html" style="margin-right:10px;margin-bottom:10px">La page mariage</a>
      %(btnwa_mariage)s
    </div>
  </div>
  </div>
</section>

<div class="pause" style="background-image:url('%(creole)s')">
  <div class="voile"></div>
  <div class="mot">« Chaque trajet devient un souvenir »</div>
</div>

<section id="balades" class="doux">
  <p class="kicker reveal">Prendre le temps</p>
  <h2 class="titre reveal">Nos balades <span class="script">avec chauffeur</span></h2>
  <p class="intro reveal">Cheveux au vent, toit ouvert sur le ciel de l'île. Choisissez votre chapitre — chaque balade s'adapte à vos envies.</p>
  <div class="balades">
    <div class="balade reveal">
      <div class="imgbox"><img src="%(sunset_soizig)s" alt="Coucher de soleil en 2CV à La Réunion" loading="lazy"></div>
      <div class="corps"><span class="meta">± 2h30 · 150 €</span><h3>Coucher de soleil & apéro</h3>
      <p>Entre forêt et littoral, puis pause face à l'océan pour l'apéro au soleil couchant. Le classique qui ne déçoit jamais.</p>
      <a href="/balades.html#sunset">En savoir plus</a></div>
    </div>
    <div class="balade reveal">
      <div class="imgbox"><img src="%(interieur)s" alt="À bord de la 2CV, ambiance cosy" loading="lazy"></div>
      <div class="corps"><span class="meta">± 3h · 175 € pour 2</span><h3>Balade brunch péï</h3>
      <p>Une virée matinale sur les belles routes, puis un coffret de ti gato péï dans un joli spot. Douceur de vivre garantie.</p>
      <a href="/balades.html#brunch">En savoir plus</a></div>
    </div>
    <div class="balade reveal">
      <div class="imgbox"><img src="%(grand1)s" alt="Lever de soleil en 2CV" loading="lazy"></div>
      <div class="corps"><span class="meta">± 3h · 160 €</span><h3>Lever de soleil</h3>
      <p>Départ avant l'aube, plaids et boissons chaudes à bord, pour accueillir le soleil depuis un beau point de vue.</p>
      <a href="/balades.html#lever">En savoir plus</a></div>
    </div>
    <div class="balade reveal">
      <div class="imgbox"><img src="%(creole)s" alt="EVJF en 2CV à La Réunion" loading="lazy"></div>
      <div class="corps"><span class="meta">½ journée · 250 € par voiture</span><h3>Demi-journée EVJF & EVJG</h3>
      <p>Quatre heures de virée, arrêts photos, jeu de piste et jonglage en bonus. De 3 à 6 personnes.</p>
      <a href="/balades.html#evjf">En savoir plus</a></div>
    </div>
    <div class="balade reveal">
      <div class="imgbox"><img src="%(jonathan)s" alt="Journée à thème en 2CV" loading="lazy"></div>
      <div class="corps"><span class="meta">Journée · 450 €</span><h3>Journées à thème</h3>
      <p>Anniversaires, EVJF/EVJG, surprises en amoureux, sorties entre amis… On imagine ensemble le fil rouge.</p>
      <a href="/balades.html#theme">En savoir plus</a></div>
    </div>
    <div class="balade reveal">
      <div class="imgbox"><img src="%(grand2)s" alt="Balade sur-mesure en 2CV" loading="lazy"></div>
      <div class="corps"><span class="meta">60 €/h · 3h minimum</span><h3>Sur-mesure</h3>
      <p>Un lieu qui vous est cher, une idée précise, un moment à marquer ? Racontez-moi votre rêve de balade.</p>
      <a href="/balades.html#surmesure">En savoir plus</a></div>
    </div>
  </div>
  <div class="note-balades reveal">
    %(btnwa_balade)s
    <p>🌿 Chauffeur, arrêts photos et petites attentions inclus dans toutes les balades.</p>
  </div>
</section>

<section id="voitures">
  <p class="kicker reveal">Deux héroïnes</p>
  <h2 class="titre reveal">Choisissez votre <span class="script">complice</span></h2>
  <div class="duo">
    <div class="fiche reveal">
      <div class="cadre2">
        <img src="%(rosalie)s" alt="Rosalie, 2CV blanche de 1983" loading="lazy">
        <span class="badge">Blanche · 1983</span>
      </div>
      <div class="corps">
        <h3>Rosalie <span class="script">la pureté</span></h3>
        <p>Toute de blanc vêtue, trois générations d'histoires dans le rétroviseur. Sa robe immaculée accueille toutes les décorations, à l'effigie de votre mariage.</p>
      </div>
    </div>
    <div class="fiche reveal">
      <div class="cadre2">
        <img src="%(soizig)s" alt="Soizig, 2CV bleue et blanche de 1990" loading="lazy">
        <span class="badge">Bleue & blanche · 1990</span>
      </div>
      <div class="corps">
        <h3>Soizig <span class="script">la dolce vita</span></h3>
        <p>Bleue et blanche comme un air de vacances éternelles. Elle roule aux côtés de Rosalie — deux 2CV, deux ambiances, le double de possibilités.</p>
      </div>
    </div>
  </div>
  <p class="centre reveal" style="margin-top:36px"><a class="btn btn-brun" href="/rosalie-et-soizig.html">Leur histoire complète</a></p>
</section>

<section class="doux" id="histoire">
  <p class="kicker reveal">La vraie histoire</p>
  <h2 class="titre reveal">Rosalie, <span class="script">de mémoire de famille</span></h2>
  <div class="histoire-grille">
    <div class="timeline reveal">
      <div class="etape"><span class="date">Au commencement</span><h4>Rosalie entre dans la famille</h4><p>Elle appartient à ma maman et à mon grand-père. Sur les genoux de ce dernier, les mains sur ce volant, je conduis pour la toute première fois.</p></div>
      <div class="etape"><span class="date">La restauration</span><h4>Trois cousins, mille boulons</h4><p>Avec mon frère et mon cousin, nous la restaurons de fond en comble. Chaque pièce démontée est un souvenir remonté.</p></div>
      <div class="etape"><span class="date">Le grand jour</span><h4>Mon propre mariage</h4><p>C'est à son bord que je me marie. Rosalie devient officiellement la voiture des plus beaux jours.</p></div>
      <div class="etape"><span class="date">Aujourd'hui</span><h4>La traversée vers La Réunion</h4><p>Par passion pour cette voiture et son histoire, je la fais voyager jusqu'à l'île — pour perpétuer ces histoires et écrire les vôtres.</p></div>
    </div>
    <div class="polas reveal">
      <figure class="pola"><div class="imgbox"><img src="%(homme_rosalie)s" alt="Jonathan avec Rosalie" loading="lazy"></div><figcaption>Comme un air de mariage…</figcaption></figure>
      <figure class="pola"><div class="imgbox"><img src="%(slackline)s" alt="Slackline sur la 2CV en spectacle" loading="lazy"></div><figcaption>L'artiste & sa complice</figcaption></figure>
      <figure class="pola"><div class="imgbox"><img src="%(rosalie_deco)s" alt="Rosalie décorée pour un mariage" loading="lazy"></div><figcaption>Prête pour le grand jour</figcaption></figure>
      <figure class="pola"><div class="imgbox"><img src="%(coffre)s" alt="Souvenir en 2CV" loading="lazy"></div><figcaption>Des histoires plein le coffre</figcaption></figure>
    </div>
  </div>
  <div class="au-volant reveal">
    <div class="rond"><img src="%(jonathan600)s" alt="Jonathan, votre chauffeur" loading="lazy"></div>
    <div>
      <h4>Au volant : Jonathan, <span class="script">votre chauffeur</span></h4>
      <p>Artiste jongleur et danseur, <strong>chauffeur VTC agréé</strong>, passionné de ce modèle mythique et de son histoire. Le projet est porté par l'association Collectif Ensemble, à Saint-Leu.</p>
    </div>
  </div>
</section>

<section id="faq">
  <p class="kicker reveal">Les questions qu'on me pose</p>
  <h2 class="titre reveal">Petites questions, <span class="script">grandes histoires</span></h2>
  <div class="faq reveal">
    <details><summary>Ma robe de mariée va-t-elle rentrer dans la 2CV ?</summary><div class="rep">Oui ! Même les robes les plus volumineuses trouvent leur place — c'est un petit rituel que je maîtrise parfaitement, et le toit ouvrant aide beaucoup. <span class="video-tag">🎬 Vidéo : une grande robe embarque à bord</span></div></details>
    <details><summary>La 2CV peut-elle monter dans les hauts ?</summary><div class="rep">Oui : elle grimpe sans rougir les grandes côtes et les hauts de l'île, de quoi célébrer avec la vue. Pour les routes de montagne les plus longues, on regarde ensemble le trajet et je vous dis simplement ce qui est possible.</div></details>
    <details><summary>Est-ce que je conduis moi-même ?</summary><div class="rep">Non — et c'est tant mieux : toutes les prestations sont <strong>avec chauffeur VTC agréé</strong>. Pas de permis à fournir, pas de caution, pas de stress.</div></details>
    <details><summary>Combien ça coûte ?</summary><div class="rep">Les balades sont à prix fixe, par voiture et jusqu'à 3 passagers : 150 € le coucher de soleil et apéro (± 2h30), 175 € la balade brunch péï (± 3h), 160 € le lever de soleil (± 3h), 250 € la demi-journée EVJF ou EVJG par voiture, 450 € la journée à thème. Chauffeur, carburant et déplacement compris ; nous roulons dans l'Ouest et le Sud, le Nord sur demande. Pour un mariage, le tarif dépend de la zone et de la durée de présence : écrivez-moi sur WhatsApp avec votre date et votre projet, vous recevrez une proposition claire et rapide, sans engagement.</div></details>
  </div>
  <p class="centre reveal" style="margin-top:32px"><a class="btn btn-brun" href="/faq.html">Toutes les questions</a></p>
</section>

<section class="social-band">
  <p class="kicker reveal" style="color:var(--nude)">Les histoires continuent</p>
  <h2 class="titre reveal">Suivez les aventures <span class="script" style="color:#e6d3ba">de Rosalie & Soizig</span></h2>
  <p class="intro reveal" style="color:#e3d8c8">Mariages, balades, coulisses et klaxons : tout est sur les réseaux. Venez feuilleter l'album !</p>
  <div class="social-links reveal">
    <a class="social-pill" href="%(insta)s" target="_blank" rel="noopener">
      <svg viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zm0 10.162a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
      @une2cv.millehistoires</a>
    <a class="social-pill" href="%(fb)s" target="_blank" rel="noopener">
      <svg viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
      Une 2CV, mille histoires</a>
  </div>
</section>

<section id="contact" class="doux">
  <p class="kicker reveal">Le premier chapitre</p>
  <h2 class="titre reveal">Écrivons <span class="script">votre histoire</span></h2>
  <p class="intro reveal">Le plus simple et le plus rapide : un petit message WhatsApp. Racontez-moi votre projet, je vous réponds vite avec une proposition sur mesure.</p>
  <div class="contact-grille">
    <div class="wa-carte reveal">
      <div class="grand-wa">%(wsvg)s</div>
      <h3>Par WhatsApp <span class="script">c'est mieux !</span></h3>
      <p>C'est vivant, c'est rapide, et on peut s'envoyer photos et idées en direct. Je réponds généralement dans la journée.</p>
      <a class="btn btn-wa" href="%(wa)s">Démarrer la conversation</a>
      <a class="tel" href="tel:+262693828108">📞 0693 82 81 08</a>
      <a class="tel" href="mailto:asso.collectif.ensemble@gmail.com">✉️ asso.collectif.ensemble@gmail.com</a>
    </div>
    <form class="formulaire reveal" method="POST" action="https://formsubmit.co/asso.collectif.ensemble@gmail.com">
      <input type="hidden" name="_subject" value="🌿 Nouvelle demande — Une 2CV, mille histoires">
      <input type="hidden" name="_template" value="table">
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="_next" value="https://assocollectifensemble-sys.github.io/merci.html">
      <input type="text" name="_honey" class="cache">
      <label>Ou par formulaire</label>
      <input type="text" name="nom" placeholder="Votre prénom & nom" required>
      <input type="tel" name="telephone" placeholder="Votre téléphone / WhatsApp">
      <select name="evenement"><option>Type d'événement…</option><option>Mariage</option><option>EVJF / EVJG</option><option>Balade</option><option>Shooting / tournage</option><option>Autre histoire</option></select>
      <input type="date" name="date" title="Date envisagée">
      <textarea rows="4" name="message" placeholder="Racontez-moi votre projet : lieu, date, envies…"></textarea>
      <button class="btn btn-brun" type="submit" style="border-radius:0;justify-content:center">Envoyer ma demande</button>
    </form>
  </div>
</section>
""" % {
    "cover": D(IMG["cover"], 1920), "logo": D(IMG["logo"], 600),
    "btnwa": btn_wa("Écrire votre histoire", WA),
    "eglise": D(IMG["eglise"]), "sunset": D(IMG["sunset_couple"]), "shoot": D(IMG["shooting_nb"]),
    "couple": D(IMG["couple_rosalie"], 1400), "btnwa_mariage": btn_wa("Parler de votre mariage", WA_MARIAGE),
    "creole": D(IMG["creole"], 1920),
    "sunset_soizig": D(IMG["sunset_soizig"], 1000), "interieur": D(IMG["interieur"], 1000),
    "grand1": D(IMG["grand1"], 1000), "grand2": D(IMG["grand2"], 1000),
    "jonathan": D(IMG["jonathan"], 1000), "jonathan600": D(IMG["jonathan"], 600),
    "btnwa_balade": btn_wa("Je réserve une balade", WA_BALADE),
    "rosalie": D(IMG["rosalie"]), "soizig": D(IMG["soizig"]),
    "homme_rosalie": D(IMG["homme_rosalie"], 800), "slackline": D(IMG["slackline"], 800),
    "rosalie_deco": D(IMG["rosalie_deco"], 800), "coffre": D(IMG["coffre"], 800),
    "insta": INSTA, "fb": FB, "wsvg": WSVG, "wa": WA,
}

pages["index.html"] = head(
    "Une 2CV, mille histoires 🌿 — Voiture de mariage & balades en 2CV à La Réunion",
    "Mariages, balades coucher de soleil, shootings et évènements à bord de Rosalie et Soizig, 2CV de collection avec chauffeur VTC agréé. Toute l'île de La Réunion.",
    "/", biz_jsonld) + index_body + footer()

# ============================================================ MARIAGE
mariage_jsonld = {
  "@context": "https://schema.org", "@type": "Service",
  "name": "Voiture de mariage 2CV avec chauffeur à La Réunion",
  "serviceType": "Location de voiture de mariage avec chauffeur",
  "provider": {"@type": "LocalBusiness", "name": "Une 2CV, mille histoires", "telephone": "+262693828108", "url": DOMAIN},
  "areaServed": {"@type": "AdministrativeArea", "name": "Île de La Réunion"},
  "url": DOMAIN + "/mariage.html",
  "image": D(IMG["eglise"], 1200)
}

mariage_body = navbar("mariage") + page_hero("eglise", "Le plus beau jour",
    "Votre voiture de mariage à La Réunion : la 2CV, avec chauffeur",
    "Un cortège qui fait sourire toute la rue, des photos hors du temps, un chauffeur qui prend soin de vous — et une voiture qui a une âme.") + """

<section>
  <div class="prose reveal">
    <p>Chercher une <strong>voiture de mariage à La Réunion</strong>, c'est chercher bien plus qu'un moyen de transport : c'est choisir l'image que garderont vos invités, la douceur du trajet entre la cérémonie et la fête, le décor de vos plus belles photos. À bord de <strong>Rosalie</strong>, 2CV blanche de 1983, ou de <strong>Soizig</strong>, bleue et blanche de 1990, votre mariage prend des airs de film — klaxon d'honneur inclus.</p>
    <p>Toutes les prestations se font <strong>avec chauffeur VTC agréé</strong> : pas de permis à fournir, pas de caution, pas de stress. Vous vivez l'instant, je m'occupe de la route — de Saint-Leu à Saint-Philippe, sur toute l'île de La Réunion.</p>
  </div>
</section>

<section class="fond-mariage">
  <div class="cadre-univers">
    <p class="kicker reveal">Votre journée</p>
    <h2 class="titre reveal">Comment se déroule <span class="script">votre histoire ?</span></h2>
    <div class="deroule reveal">
      <div class="temps"><div class="num">1</div><div><h3>On imagine ensemble</h3><p>Un message WhatsApp, votre date, vos lieux, vos envies — je vous propose un déroulé sur mesure et une proposition claire, sans engagement.</p></div></div>
      <div class="temps"><div class="num">2</div><div><h3>La décoration</h3><p>Rubans, fleurs fraîches, panneaux personnalisés : votre fleuriste s'en charge, ou je vous conseille le nôtre, qui connaît Rosalie par cœur. La robe blanche de Rosalie accueille toutes les couleurs de votre mariage.</p></div></div>
      <div class="temps"><div class="num">3</div><div><h3>Le jour J</h3><p>J'arrive en avance, la voiture est prête et étincelante. Préparatifs, mairie, église ou cérémonie laïque : je vous conduis à chaque étape, au rythme de votre journée. Et même les plus grandes robes embarquent sans souci — toit ouvrant à l'appui.</p></div></div>
      <div class="temps"><div class="num">4</div><div><h3>Les photos</h3><p>Pendant le cocktail, escapade avec votre photographe : la 2CV se prête à tous les cadrages, capot, portières, toit ouvert. Des images que personne d'autre n'aura.</p></div></div>
      <div class="temps"><div class="num">5</div><div><h3>La touche spectacle <em>(en option)</em></h3><p>Artiste jongleur et danseur, je peux aussi faire durer la magie : jonglage pour les enfants, spectacle de feu en soirée, animations… La 2CV n'est jamais très loin du spectacle.</p></div></div>
    </div>
  </div>
</section>

<section class="doux">
  <p class="kicker reveal">Aussi pour</p>
  <h2 class="titre reveal">Elopement, EVJF, demandes <span class="script">en mariage…</span></h2>
  <div class="prose reveal">
    <p><strong>Elopement & petits comités</strong> — un mariage intime à deux ou presque : la 2CV vous emmène vers un lieu secret, face à l'océan ou dans les hauts, pour échanger vos vœux loin du monde.</p>
    <p><strong>EVJF & EVJG</strong> — une virée entre copines ou entre copains, décorations embarquées, musique, arrêts photos et fous rires garantis. La future mariée voyage comme une star.</p>
    <p><strong>Demande en mariage</strong> — je vous aide à organiser la surprise : trajet complice, spot de rêve au coucher du soleil, et la bague au fond du coffre… chut.</p>
    <p><strong>Anniversaires de mariage</strong> — refaire le trajet des années plus tard, dans la même voiture ou presque : c'est exactement le genre d'histoires que Rosalie adore.</p>
  </div>
</section>

<section>
  <p class="kicker reveal">En images</p>
  <h2 class="titre reveal">Des mariages <span class="script">plein le rétro</span></h2>
  <div class="galerie reveal">
    <div class="gitem"><img src="%(eglise)s" alt="Sortie d'église en 2CV blanche à La Réunion" loading="lazy"></div>
    <div class="gitem"><img src="%(couple)s" alt="Mariés montant à bord de la 2CV Rosalie" loading="lazy"></div>
    <div class="gitem"><img src="%(rosalie_deco)s" alt="2CV blanche décorée de fleurs pour un mariage" loading="lazy"></div>
    <div class="gitem"><img src="%(cover)s" alt="Les deux 2CV décorées face à l'océan" loading="lazy"></div>
    <div class="gitem"><img src="%(coffre)s" alt="Souvenirs de mariage en 2CV" loading="lazy"></div>
    <div class="gitem"><img src="%(shoot)s" alt="Shooting de couple avec la 2CV" loading="lazy"></div>
  </div>
</section>
""" % {
    "eglise": D(IMG["eglise"], 1000), "couple": D(IMG["couple_rosalie"], 1000),
    "rosalie_deco": D(IMG["rosalie_deco"], 1000), "cover": D(IMG["cover"], 1000),
    "coffre": D(IMG["coffre"], 1000), "shoot": D(IMG["shooting_nb"], 1000),
} + cta_band("Parlons de votre", "mariage", "Écrire notre histoire", WA_MARIAGE)

pages["mariage.html"] = head(
    "Voiture de mariage à La Réunion — 2CV avec chauffeur | Une 2CV, mille histoires",
    "Location de 2CV avec chauffeur VTC agréé pour votre mariage à La Réunion : cortège, sortie de cérémonie, photos, décoration florale, EVJF/EVJG. Devis rapide par WhatsApp.",
    "/mariage.html", mariage_jsonld) + mariage_body + footer()

# ============================================================ BALADES
balades_jsonld = {
  "@context": "https://schema.org", "@type": "Service",
  "name": "Balades en 2CV avec chauffeur à La Réunion",
  "serviceType": "Balade touristique en voiture de collection avec chauffeur",
  "provider": {"@type": "LocalBusiness", "name": "Une 2CV, mille histoires", "telephone": "+262693828108", "url": DOMAIN},
  "areaServed": {"@type": "AdministrativeArea", "name": "Île de La Réunion"},
  "url": DOMAIN + "/balades.html",
  "image": D(IMG["sunset_couple"], 1200)
}

def bloc_balade(anchor, img, meta, titre, texte, alt, wa_msg):
    """wa_msg : message WhatsApp pré-rempli propre à la formule, pour savoir
    laquelle a été cliquée."""
    return """<div class="balade reveal" id="%s">
      <div class="imgbox"><img src="%s" alt="%s" loading="lazy"></div>
      <div class="corps"><span class="meta">%s</span><h3>%s</h3><p>%s</p>
      <a href="%s">Réserver cette balade</a></div>
    </div>""" % (anchor, img, alt, meta, titre, texte, wa_link(wa_msg))

balades_body = navbar("balades") + page_hero("sunset_couple", "Prendre le temps",
    "Balades en 2CV à La Réunion, avec chauffeur",
    "Cheveux au vent, toit ouvert sur le ciel de l'île : une façon unique et insolite de découvrir La Réunion, en couple, en famille ou entre amis.") + """

<section>
  <div class="prose reveal">
    <p>Envie d'une <strong>activité insolite à La Réunion</strong> ? Montez à bord d'une vraie 2CV de collection et laissez-vous conduire. Chaque balade est pensée comme une petite histoire : un itinéraire qui prend son temps, des arrêts photos, des attentions à bord — et un chauffeur passionné qui connaît les plus beaux détours de l'île. Le toit s'ouvre en grand, les fenêtres aussi : parfait pour les photos sans reflet et le vent dans les cheveux.</p>
  </div>
</section>

<section class="doux">
  <p class="kicker reveal">Nos formules</p>
  <h2 class="titre reveal">Choisissez votre <span class="script">chapitre</span></h2>
  <div class="balades">
    %(b1)s
    %(b2)s
    %(b3)s
    %(b4)s
    %(b5)s
    %(b6)s
  </div>
  <div class="inclus-liste reveal">
    <div class="col"><h3>Inclus dans toutes les balades</h3>
      <ul><li>Chauffeur VTC agréé — vous profitez</li><li>Jusqu'à 3 passagers par 2CV, 6 avec les deux voitures</li><li>Arrêts photos à volonté</li><li>Petites attentions à bord</li><li>Itinéraire adapté à vos envies</li><li>La bonne humeur de rigueur</li></ul></div>
    <div class="col"><h3>À prévoir</h3>
      <ul><li>Lunettes de soleil & chapeau</li><li>Un lainage pour les hauts ou l'aube</li><li>Votre plus beau sourire</li><li>Appareil photo (ou pas : je vous en prends !)</li></ul></div>
  </div>
  <div class="note-balades reveal">
    %(btnwa)s
    <p>Tarifs par voiture, jusqu'à 3 passagers — chauffeur, carburant et déplacement compris. Rosalie et Soizig roulent dans l'Ouest et le Sud ; le Nord sur demande. Le règlement se fait à la réservation.</p>
  </div>
</section>
""" % {
    "b1": bloc_balade("sunset", D(IMG["sunset_soizig"], 1000), "± 2h30 · 150 €", "Coucher de soleil & apéro",
        "Départ en fin d'après-midi, entre forêt et littoral, puis pause face à l'océan pour l'apéro au soleil couchant. Le classique qui ne déçoit jamais — idéal en amoureux ou entre amis.",
        "Balade coucher de soleil en 2CV à La Réunion",
        "Bonjour Jonathan ! Je souhaite réserver la balade « Coucher de soleil & apéro » (± 2h) 🌿"),
    "b2": bloc_balade("brunch", D(IMG["interieur"], 1000), "± 3h · 175 € pour 2", "Balade brunch péï",
        "Une virée matinale sur les belles routes de l'île, puis pause gourmande dans un joli spot : un coffret de ti gato péï artisanaux et de confitures maison, avec les boissons chaudes préparées à bord. La douceur de vivre, version quatre roues.",
        "Balade brunch en 2CV à La Réunion",
        "Bonjour Jonathan ! Je souhaite réserver la « Balade brunch » (± 3h) 🌿"),
    "b3": bloc_balade("lever", D(IMG["grand1"], 1000), "± 3h · 160 €", "Lever de soleil",
        "Départ avant l'aube, plaids et boissons chaudes à bord, pour accueillir le premier rayon depuis un beau point de vue. Redescente par les plus jolis détours, pause bouchons-samoussas en option.",
        "Lever de soleil en 2CV à La Réunion",
        "Bonjour Jonathan ! Je souhaite réserver la balade « Lever de soleil » (± 5h) 🌿"),
    "b4": bloc_balade("evjf", D(IMG["creole"], 1000), "½ journée · 250 € par voiture", "Demi-journée EVJF & EVJG",
        "L'enterrement de vie de jeune fille ou de garçon qui ne ressemble à aucun autre : quatre heures de virée en 2CV, arrêts photos, jeu de piste ou rallye si vous voulez, et le jonglage en bonus. 250 € par voiture, de 3 à 6 personnes selon qu'on sort Rosalie seule ou les deux ensemble.",
        "EVJF et EVJG en 2CV à La Réunion",
        "Bonjour Jonathan ! Je souhaite organiser une demi-journée EVJF / EVJG en 2CV 🌿"),
    "b5": bloc_balade("theme", D(IMG["jonathan"], 1000), "Journée · 450 €", "Journées à thème",
        "Anniversaire, EVJF/EVJG, surprise en amoureux, sortie entre amis, rallye photo… On imagine ensemble le fil rouge de la journée, je m'occupe du reste — jonglage en bonus si le cœur vous en dit. 450 € la journée, dans l'Ouest et le Sud. À deux voitures, Rosalie et Soizig emmènent jusqu'à 6 passagers : 750 € la journée.",
        "Journée à thème en 2CV à La Réunion",
        "Bonjour Jonathan ! Je souhaite organiser une journée à thème en 2CV 🌿"),
    "b6": bloc_balade("surmesure", D(IMG["grand2"], 1000), "60 €/h · 3h minimum", "Sur-mesure",
        "Un lieu qui vous est cher, une idée précise, un moment à marquer ? Racontez-moi votre rêve de balade : nous l'écrirons ensemble, au rythme qui vous ressemble.",
        "Balade sur-mesure en 2CV à La Réunion",
        "Bonjour Jonathan ! J'aimerais imaginer une balade sur-mesure en 2CV 🌿"),
    "btnwa": btn_wa("Je réserve une balade", WA_BALADE),
} + cta_band("Une question, une", "envie ?", "Discuter sur WhatsApp", WA_BALADE)

pages["balades.html"] = head(
    "Balades en 2CV à La Réunion — coucher de soleil, brunch péï, lever de soleil | Une 2CV, mille histoires",
    "Balade insolite à La Réunion en 2CV avec chauffeur : coucher de soleil & apéro, brunch péï, lever de soleil, journées à thème et sur-mesure. Réservation simple par WhatsApp.",
    "/balades.html", balades_jsonld) + balades_body + footer()

# ============================================================ SHOOTING
shoot_body = navbar("shooting") + page_hero("shooting_nb", "Lumière !",
    "Shootings photo, cinéma & évènements avec une 2CV à La Réunion",
    "Une voiture de collection qui crève l'écran : shootings, tournages, clips, salons, anniversaires — Rosalie et Soizig volent la vedette avec élégance.") + """

<section>
  <div class="prose reveal">
    <h2>Un décor qui roule</h2>
    <p>Photographes, vidéastes, réalisateurs : une <strong>2CV de collection à La Réunion</strong>, c'est un décor à elle toute seule. Lignes rondes, chromes, capot ouvert sur l'océan — elle donne du caractère à un shooting couple ou grossesse, une séance mode, un clip, une publicité ou un film. Je me déplace sur toute l'île avec la voiture, et je reste sur place pendant votre séance : la 2CV est toujours accompagnée de son chauffeur. Le tarif est simple : <strong>60 € de l'heure, trois heures minimum</strong>, voiture et chauffeur compris. Au-delà d'une demi-journée ou pour un dispositif particulier, écrivez-moi et je vous fais une proposition.</p>
    <h2>Pour vos évènements</h2>
    <p>Anniversaires, fêtes de famille, salons, inaugurations, marchés et festivals : la 2CV attire tous les regards — en exposition, en arrivée surprise ou en séance photo souvenir pour vos invités. Et comme je suis aussi <strong>artiste jongleur et danseur</strong>, l'animation peut suivre : jonglage pour les enfants, spectacle de feu, numéro de slackline sur le toit de Rosalie… du jamais-vu dans un évènement.</p>
  </div>
</section>

<section class="doux">
  <p class="kicker reveal">En images</p>
  <h2 class="titre reveal">Elle adore <span class="script">la caméra</span></h2>
  <div class="galerie reveal">
    <div class="gitem"><img src="%(shoot)s" alt="Shooting photo noir et blanc avec la 2CV Soizig" loading="lazy"></div>
    <div class="gitem"><img src="%(homme_rosalie)s" alt="Shooting avec Rosalie, 2CV blanche" loading="lazy"></div>
    <div class="gitem"><img src="%(slackline)s" alt="Spectacle de slackline sur la 2CV" loading="lazy"></div>
    <div class="gitem"><img src="%(interieur)s" alt="Intérieur vintage de la 2CV" loading="lazy"></div>
    <div class="gitem"><img src="%(sunset)s" alt="La 2CV au coucher de soleil" loading="lazy"></div>
    <div class="gitem"><img src="%(soizig)s" alt="Soizig, 2CV bleue et blanche en bord de mer" loading="lazy"></div>
  </div>
</section>
""" % {
    "shoot": D(IMG["shooting_nb"], 1000), "homme_rosalie": D(IMG["homme_rosalie"], 1000),
    "slackline": D(IMG["slackline"], 1000), "interieur": D(IMG["interieur"], 1000),
    "sunset": D(IMG["sunset_soizig"], 1000), "soizig": D(IMG["soizig"], 1000),
} + cta_band("Un projet, une", "idée folle ?", "Proposer mon projet", WA_SHOOT)

pages["shooting-evenements.html"] = head(
    "Location 2CV pour shooting photo, cinéma & évènements à La Réunion | Une 2CV, mille histoires",
    "Louez une 2CV de collection avec chauffeur pour vos shootings photo, tournages, clips et évènements à La Réunion. Options spectacle : jonglage, feu, animations.",
    "/shooting-evenements.html") + shoot_body + footer()

# ============================================================ ROSALIE & SOIZIG
voitures_body = navbar("voitures") + page_hero("cover", "Deux héroïnes",
    "Rosalie & Soizig, nos 2CV de collection",
    "Deux Citroën 2CV, deux caractères, une même mission : transformer chaque trajet en souvenir.") + """

<section>
  <div class="duo">
    <div class="fiche reveal">
      <div class="cadre2">
        <img src="%(rosalie)s" alt="Rosalie, 2CV blanche de 1983" loading="lazy">
        <span class="badge">Blanche · 1983</span>
      </div>
      <div class="corps">
        <h3>Rosalie <span class="script">la pureté</span></h3>
        <p>Toute de blanc vêtue, née en 1983, trois générations d'histoires dans le rétroviseur. Sa robe immaculée est une toile blanche : rubans, fleurs, couleurs de votre cérémonie — elle se décore à l'effigie de votre mariage. C'est elle qui a traversé l'océan Indien pour continuer d'écrire des histoires sur les routes de l'île.</p>
      </div>
    </div>
    <div class="fiche reveal">
      <div class="cadre2">
        <img src="%(soizig)s" alt="Soizig, 2CV bleue et blanche de 1990" loading="lazy">
        <span class="badge">Bleue & blanche · 1990</span>
      </div>
      <div class="corps">
        <h3>Soizig <span class="script">la dolce vita</span></h3>
        <p>Bleue et blanche comme un air de vacances éternelles, née en 1990, Soizig respire la dolce vita. Elle appartient à une propriétaire complice et roule aux côtés de Rosalie : deux 2CV, deux ambiances — et le double de possibilités pour vos cortèges et vos balades en bande.</p>
      </div>
    </div>
  </div>
</section>

<section class="doux" id="histoire">
  <p class="kicker reveal">La vraie histoire</p>
  <h2 class="titre reveal">Rosalie, <span class="script">de mémoire de famille</span></h2>
  <div class="histoire-grille">
    <div class="timeline reveal">
      <div class="etape"><span class="date">Au commencement</span><h4>Rosalie entre dans la famille</h4><p>Elle appartient à ma maman et à mon grand-père. Sur les genoux de ce dernier, les mains sur ce volant, je conduis pour la toute première fois.</p></div>
      <div class="etape"><span class="date">La restauration</span><h4>Trois cousins, mille boulons</h4><p>Avec mon frère et mon cousin, nous la restaurons de fond en comble. Chaque pièce démontée est un souvenir remonté.</p></div>
      <div class="etape"><span class="date">Le grand jour</span><h4>Mon propre mariage</h4><p>C'est à son bord que je me marie. Rosalie devient officiellement la voiture des plus beaux jours.</p></div>
      <div class="etape"><span class="date">Aujourd'hui</span><h4>La traversée vers La Réunion</h4><p>Par passion pour cette voiture et son histoire, je la fais voyager jusqu'à l'île — pour perpétuer ces histoires et écrire les vôtres.</p></div>
    </div>
    <div class="polas reveal">
      <figure class="pola"><div class="imgbox"><img src="%(homme_rosalie)s" alt="Jonathan avec Rosalie" loading="lazy"></div><figcaption>Comme un air de mariage…</figcaption></figure>
      <figure class="pola"><div class="imgbox"><img src="%(slackline)s" alt="Slackline sur la 2CV en spectacle" loading="lazy"></div><figcaption>L'artiste & sa complice</figcaption></figure>
      <figure class="pola"><div class="imgbox"><img src="%(rosalie_deco)s" alt="Rosalie décorée" loading="lazy"></div><figcaption>Prête pour le grand jour</figcaption></figure>
      <figure class="pola"><div class="imgbox"><img src="%(coffre)s" alt="Souvenir en 2CV" loading="lazy"></div><figcaption>Des histoires plein le coffre</figcaption></figure>
    </div>
  </div>
  <div class="au-volant reveal">
    <div class="rond"><img src="%(jonathan)s" alt="Jonathan, votre chauffeur" loading="lazy"></div>
    <div>
      <h4>Au volant : Jonathan, <span class="script">votre chauffeur</span></h4>
      <p>Artiste jongleur et danseur, <strong>chauffeur VTC agréé</strong>, passionné de ce modèle mythique et de son histoire. Le projet est porté par l'association Collectif Ensemble, à Saint-Leu.</p>
    </div>
  </div>
</section>
""" % {
    "rosalie": D(IMG["rosalie"]), "soizig": D(IMG["soizig"]),
    "homme_rosalie": D(IMG["homme_rosalie"], 800), "slackline": D(IMG["slackline"], 800),
    "rosalie_deco": D(IMG["rosalie_deco"], 800), "coffre": D(IMG["coffre"], 800),
    "jonathan": D(IMG["jonathan"], 600),
} + cta_band("Laquelle conduira", "votre histoire ?", "Écrire votre histoire", WA)

pages["rosalie-et-soizig.html"] = head(
    "Rosalie & Soizig — nos 2CV de collection à La Réunion | Une 2CV, mille histoires",
    "Découvrez Rosalie, 2CV blanche de 1983 à l'histoire familiale unique, et Soizig, 2CV bleue et blanche de 1990. Deux voitures de collection avec chauffeur à La Réunion.",
    "/rosalie-et-soizig.html") + voitures_body + footer()

# ============================================================ FAQ
faqs = [
 ("Ma robe de mariée va-t-elle rentrer dans la 2CV ?",
  "Oui ! Même les robes les plus volumineuses trouvent leur place — c'est un petit rituel que je maîtrise parfaitement, et le toit ouvrant aide beaucoup. Une vidéo le montre en images sur nos réseaux."),
 ("La 2CV peut-elle monter dans les hauts ?",
  "Oui : elle grimpe sans rougir les grandes côtes et les hauts de l'île, de quoi célébrer avec la vue. Pour les routes de montagne les plus longues, on regarde ensemble le trajet et je vous dis simplement ce qui est possible."),
 ("Est-ce que je conduis moi-même ?",
  "Non — et c'est tant mieux : toutes les prestations sont avec chauffeur VTC agréé. Pas de permis à fournir, pas de caution, pas de stress. Vous profitez, je m'occupe de la route."),
 ("Combien de personnes peuvent monter à bord ?",
  "Jusqu'à 3 passagers par 2CV en plus du chauffeur. Et pour les grands cortèges, Rosalie et Soizig peuvent rouler ensemble !"),
 ("Combien coûte une voiture de mariage ou une balade en 2CV à La Réunion ?",
  "Les balades sont à prix fixe, par voiture et jusqu'à 3 passagers : 150 € le coucher de soleil et apéro (± 2h30), 175 € la balade brunch péï pour deux (± 3h), 160 € le lever de soleil (± 3h), 250 € la demi-journée EVJF ou EVJG par voiture, 450 € la journée à thème à une voiture et 750 € à deux voitures, 60 € de l'heure en sur-mesure. Chauffeur, carburant et déplacement compris ; Rosalie et Soizig roulent dans l'Ouest et le Sud, le Nord sur demande. Pour un mariage, le tarif dépend de la zone et de la durée de présence de la voiture : écrivez-nous sur WhatsApp au 0693 82 81 08 avec votre date et votre projet, vous recevrez une proposition claire et rapide, sans engagement."),
 ("Peut-on décorer la voiture ?",
  "Avec plaisir : rubans, fleurs, panneaux personnalisés… Vous pouvez confier la décoration florale à votre fleuriste, ou nous vous conseillons le nôtre, qui connaît Rosalie par cœur."),
 ("Et s'il pleut ?",
  "La capote se ferme en un instant et la balade continue, ambiance cocooning. Pour les mariages, on ajuste le déroulé ensemble — à La Réunion, le soleil n'est jamais bien loin."),
 ("Vous déplacez-vous partout sur l'île ?",
  "Oui, toute l'île de La Réunion, de Saint-Denis à Saint-Philippe. Les frais de déplacement sont simplement intégrés à la proposition selon le lieu de votre événement."),
 ("Combien de temps à l'avance faut-il réserver ?",
  "Pour un mariage, le plus tôt est le mieux — les samedis de la saison partent vite. Pour une balade, quelques jours suffisent souvent. Dans tous les cas, écrivez-nous : on trouve des solutions."),
 ("Peut-on privatiser la 2CV pour un tournage ou un shooting professionnel ?",
  "Oui : cinéma, clips, publicités, shootings mode ou grossesse… La voiture vient toujours accompagnée de son chauffeur, sur toute l'île. Parlons de votre projet !"),
]
faq_jsonld = {
  "@context": "https://schema.org", "@type": "FAQPage",
  "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]
}
faq_items = "".join('<details%s><summary>%s</summary><div class="rep">%s</div></details>' % (" open" if i==0 else "", q, a) for i,(q,a) in enumerate(faqs))
faq_body = navbar("faq") + page_hero("interieur", "On vous dit tout",
    "Questions fréquentes",
    "La robe, la pluie, les hauts, les tarifs… toutes les réponses avant d'embarquer.") + """
<section>
  <div class="faq reveal">%s</div>
</section>
""" % faq_items + cta_band("Une autre", "question ?", "Poser ma question", WA)

pages["faq.html"] = head(
    "FAQ — 2CV mariage & balades à La Réunion | Une 2CV, mille histoires",
    "Robe de mariée dans une 2CV, trajets dans les hauts, tarifs, réservation, météo : toutes les réponses sur nos prestations de 2CV avec chauffeur à La Réunion.",
    "/faq.html", faq_jsonld) + faq_body + footer()

# ============================================================ CONTACT
contact_body = navbar() + page_hero("sunset_couple", "Le premier chapitre",
    "Écrivons votre histoire",
    "WhatsApp, téléphone ou formulaire : racontez-nous votre projet, la réponse arrive vite.") + """
<section>
  <div class="contact-grille">
    <div class="wa-carte reveal">
      <div class="grand-wa">%(wsvg)s</div>
      <h3>Par WhatsApp <span class="script">c'est mieux !</span></h3>
      <p>C'est vivant, c'est rapide, et on peut s'envoyer photos et idées en direct. Je réponds généralement dans la journée.</p>
      <a class="btn btn-wa" href="%(wa)s">Démarrer la conversation</a>
      <a class="tel" href="tel:+262693828108">📞 0693 82 81 08</a>
      <a class="tel" href="mailto:asso.collectif.ensemble@gmail.com">✉️ asso.collectif.ensemble@gmail.com</a>
      <p style="margin-top:18px;font-size:13.5px;color:#4c6b53">Basé à Saint-Leu · déplacements sur toute l'île de La Réunion</p>
    </div>
    <form class="formulaire reveal" method="POST" action="https://formsubmit.co/asso.collectif.ensemble@gmail.com">
      <input type="hidden" name="_subject" value="🌿 Nouvelle demande — Une 2CV, mille histoires">
      <input type="hidden" name="_template" value="table">
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="_next" value="https://assocollectifensemble-sys.github.io/merci.html">
      <input type="text" name="_honey" class="cache">
      <label>Ou par formulaire</label>
      <input type="text" name="nom" placeholder="Votre prénom & nom" required>
      <input type="tel" name="telephone" placeholder="Votre téléphone / WhatsApp">
      <select name="evenement"><option>Type d'événement…</option><option>Mariage</option><option>EVJF / EVJG</option><option>Balade</option><option>Shooting / tournage</option><option>Autre histoire</option></select>
      <input type="date" name="date" title="Date envisagée">
      <textarea rows="5" name="message" placeholder="Racontez-moi votre projet : lieu, date, envies…"></textarea>
      <button class="btn btn-brun" type="submit" style="border-radius:0;justify-content:center">Envoyer ma demande</button>
    </form>
  </div>
</section>
""" % {"wsvg": WSVG, "wa": WA}

pages["contact.html"] = head(
    "Contact — Une 2CV, mille histoires | 2CV avec chauffeur à La Réunion",
    "Contactez Une 2CV, mille histoires : WhatsApp 0693 82 81 08, formulaire ou email. Mariages, balades et shootings en 2CV avec chauffeur sur toute l'île de La Réunion.",
    "/contact.html") + contact_body + footer()

# ============================================================ MERCI
merci_body = navbar(opaque=True) + """
<section style="min-height:70vh;display:flex;flex-direction:column;justify-content:center;padding-top:130px" class="centre">
  <p class="kicker">Message bien reçu</p>
  <h1 class="titre">Merci ! <span class="script">à très vite</span></h1>
  <p class="intro">Votre demande est arrivée dans notre boîte. Nous revenons vers vous rapidement — et si vous voulez une réponse encore plus vite, continuons sur WhatsApp :</p>
  <p>%s</p>
  <p style="margin-top:26px"><a href="/" style="color:var(--terre)">← Retour à l'accueil</a></p>
</section>
""" % btn_wa("Continuer sur WhatsApp", WA)

pages["merci.html"] = head(
    "Merci — Une 2CV, mille histoires", "Votre demande a bien été envoyée.",
    "/merci.html", noindex=True) + merci_body + footer()

# ============================================================ MENTIONS
mentions_body = navbar(opaque=True) + """
<section style="padding-top:150px">
  <div class="prose">
    <h1 style="font-size:clamp(28px,4vw,40px);margin-bottom:24px">Mentions légales</h1>
    <h2>Éditeur du site</h2>
    <p>« Une 2CV, mille histoires » est un projet porté par l'association <strong>Collectif Ensemble</strong> — Saint-Leu, La Réunion.<br>
    SIRET : 934 556 036 00010 · Email : asso.collectif.ensemble@gmail.com · Téléphone : 0693 82 81 08.</p>
    <h2>Hébergement</h2>
    <p>Site hébergé par GitHub Pages — GitHub, Inc., 88 Colin P. Kelly Jr Street, San Francisco, CA 94107, États-Unis.</p>
    <h2>Propriété intellectuelle</h2>
    <p>L'ensemble des textes, photographies et vidéos de ce site sont la propriété de l'association Collectif Ensemble ou de leurs auteurs respectifs. Toute reproduction sans autorisation est interdite. Musique d'ambiance : contenu libre de droits (licence Pixabay).</p>
    <h2>Données personnelles</h2>
    <p>Les informations transmises via le formulaire de contact sont utilisées uniquement pour répondre à votre demande. Elles ne sont ni cédées ni utilisées à des fins publicitaires. Vous pouvez demander leur suppression à tout moment par email.</p>
  </div>
</section>
"""
pages["mentions-legales.html"] = head(
    "Mentions légales — Une 2CV, mille histoires", "Mentions légales du site une2cvmillehistoires.re.",
    "/mentions-legales.html", noindex=True) + mentions_body + footer()

# ============================================================ ROBOTS / SITEMAP
robots = "User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % DOMAIN
urls = ["/", "/mariage.html", "/balades.html", "/shooting-evenements.html", "/rosalie-et-soizig.html", "/faq.html", "/contact.html"]
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
    "".join("  <url><loc>%s%s</loc></url>\n" % (DOMAIN, u) for u in urls) + "</urlset>\n"

with open(os.path.join(OUT, "robots.txt"), "w") as f: f.write(robots)
with open(os.path.join(OUT, "sitemap.xml"), "w") as f: f.write(sitemap)
for name, html in pages.items():
    with open(os.path.join(OUT, name), "w") as f: f.write(html)
    print("OK", name, len(html))
print("Terminé.")
