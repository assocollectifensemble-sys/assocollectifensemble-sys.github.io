/* ==========================================================================
   Page « Spectacles, ateliers & animations » — le mouvement.
   --------------------------------------------------------------------------
   Deux effets, un seul écouteur de défilement :
     1. la photo du bandeau glisse plus lentement que la page (parallaxe) ;
     2. les objets de jonglage montent, descendent et tournent quand on avance.

   Tout passe par des variables CSS (--para, --y, --r) : le navigateur
   compose, le JS se contente de calculer. Les positions sont écrites dans
   une seule frame via requestAnimationFrame pour éviter les à-coups.

   Respect de prefers-reduced-motion : rien ne démarre, les objets restent
   masqués par la CSS.
   ========================================================================== */
(function () {
  'use strict';

  var douce = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (douce.matches) { return; }

  var scene = document.querySelector('.scene');
  var fond = scene && scene.querySelector('.fond');
  var piste = scene && scene.querySelector('.balles');
  if (!scene || !piste) { return; }

  /* Les objets : position en %, taille, couleur, vitesse et sens de rotation.
     Les vitesses négatives font descendre l'objet : le lot donne l'impression
     d'une jonglerie en l'air plutôt que d'un simple décalage d'ensemble. */
  var MODELES = [
    { x: 7,  y: 16, d: 62, c: '#e8a33a', v: 0.26,  r: 0.10, forme: '' },
    { x: 86, y: 22, d: 48, c: '#d2523f', v: -0.19, r: -0.14, forme: '' },
    { x: 18, y: 68, d: 40, c: '#f0c76a', v: 0.15,  r: 0.18, forme: '' },
    { x: 78, y: 70, d: 70, c: '#8fb6a2', v: -0.24, r: 0.08, forme: 'massue' },
    { x: 46, y: 12, d: 34, c: '#e6d5b8', v: 0.21,  r: -0.20, forme: '' },
    { x: 61, y: 82, d: 54, c: '#c9743c', v: -0.13, r: 0.12, forme: 'massue' },
    { x: 30, y: 38, d: 28, c: '#f2e2c4', v: 0.29,  r: 0.22, forme: '' }
  ];

  var objets = MODELES.map(function (m) {
    var el = document.createElement('span');
    el.className = 'balle' + (m.forme ? ' ' + m.forme : '');
    el.style.left = m.x + '%';
    el.style.top = m.y + '%';
    el.style.setProperty('--d', m.d + 'px');
    el.style.setProperty('--c', m.c);
    el.setAttribute('aria-hidden', 'true');
    piste.appendChild(el);
    return { el: el, v: m.v, r: m.r };
  });

  var attente = false;

  function placer() {
    attente = false;
    var boite = scene.getBoundingClientRect();
    /* Progression : 0 quand le bandeau entre, 1 quand il sort par le haut. */
    var avance = -boite.top;

    if (fond) {
      fond.style.setProperty('--para', (avance * 0.18).toFixed(1) + 'px');
    }
    for (var i = 0; i < objets.length; i++) {
      var o = objets[i];
      o.el.style.setProperty('--y', (avance * o.v).toFixed(1) + 'px');
      o.el.style.setProperty('--r', (avance * o.r).toFixed(1) + 'deg');
    }
  }

  function auDefilement() {
    if (!attente) {
      attente = true;
      window.requestAnimationFrame(placer);
    }
  }

  /* On ne calcule que tant que le bandeau touche l'écran : au-delà, l'écouteur
     tourne dans le vide et mange de la batterie sur mobile. */
  var visible = true;
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (entrees) {
      visible = entrees[0].isIntersecting;
      if (visible) { auDefilement(); }
    }, { rootMargin: '120px' }).observe(scene);
  }

  window.addEventListener('scroll', function () {
    if (visible) { auDefilement(); }
  }, { passive: true });
  window.addEventListener('resize', auDefilement, { passive: true });

  placer();
}());
