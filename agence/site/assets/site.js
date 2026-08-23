/* Otonom Digital — scripts du site vitrine (aucune dépendance, dégradation propre).
   Agent web — 2026-08-23. */
(function () {
  "use strict";

  /* Année courante dans le pied de page */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* Compte à rebours facturation électronique (réception : 1er septembre 2026).
     Avant l'échéance : « J−N ». Après : bascule sur le texte "obligation en vigueur". */
  document.querySelectorAll("[data-deadline]").forEach(function (el) {
    var deadline = new Date(el.getAttribute("data-deadline") + "T00:00:00");
    if (isNaN(deadline)) return;
    var days = Math.ceil((deadline - new Date()) / 86400000);
    if (days > 0) {
      el.textContent = "J−" + days;
    } else {
      el.textContent = el.getAttribute("data-deadline-passed") || "En vigueur";
    }
  });

  /* Formulaire de contact : compose un email (mailto), aucun serveur.
     L'adresse est lue sur l'attribut data-mailto du formulaire —
     un seul endroit à modifier (voir README). */
  var form = document.querySelector("form[data-mailto]");
  if (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var to = form.getAttribute("data-mailto");
      var get = function (name) {
        var field = form.elements[name];
        return field && field.value ? field.value.trim() : "";
      };
      var subject = "[Site] " + (get("sujet") || "Demande de contact");
      var body = [
        "Nom : " + get("nom"),
        "Entreprise : " + get("entreprise"),
        "Commune : " + get("commune"),
        "Téléphone : " + get("telephone"),
        "",
        get("message"),
      ].join("\n");
      window.location.href =
        "mailto:" + encodeURIComponent(to) +
        "?subject=" + encodeURIComponent(subject) +
        "&body=" + encodeURIComponent(body);
      var status = document.getElementById("form-status");
      if (status) {
        status.hidden = false;
      }
    });
  }
})();
