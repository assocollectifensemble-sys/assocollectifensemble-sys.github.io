/* Une 2CV, mille histoires — interactions */
(function(){
  // Nav : fond opaque après défilement
  var nav = document.getElementById('nav');
  if (nav) {
    var majNav = function(){ nav.classList.toggle('scrolled', window.scrollY > 40); };
    window.addEventListener('scroll', majNav, {passive:true});
    majNav();
  }

  // Apparitions au défilement
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if (e.isIntersecting) { e.target.classList.add('on'); io.unobserve(e.target); }
      });
    }, {threshold: 0.12});
    els.forEach(function(el){ io.observe(el); });
  } else {
    els.forEach(function(el){ el.classList.add('on'); });
  }

  // Musique d'ambiance (page d'accueil)
  var audio = document.getElementById('musique');
  var btn = document.getElementById('btn-son');
  if (audio && btn) {
    audio.volume = 0.35;
    var maj = function(){ btn.classList.toggle('off', audio.paused); };
    var lancer = function(){ audio.play().then(maj).catch(maj); };
    btn.addEventListener('click', function(ev){
      ev.stopPropagation();
      if (audio.paused) lancer(); else { audio.pause(); maj(); }
    });
    // L'autoplay est souvent bloqué : on retente au premier geste du visiteur
    var premierGeste = function(){
      if (audio.paused && !btn.dataset.coupe) lancer();
      document.removeEventListener('click', premierGeste);
      document.removeEventListener('touchstart', premierGeste);
      window.removeEventListener('scroll', premierGeste);
    };
    btn.addEventListener('click', function(){ btn.dataset.coupe = audio.paused ? '1' : ''; });
    lancer();
    document.addEventListener('click', premierGeste);
    document.addEventListener('touchstart', premierGeste, {passive:true});
    window.addEventListener('scroll', premierGeste, {passive:true});
  }
})();
