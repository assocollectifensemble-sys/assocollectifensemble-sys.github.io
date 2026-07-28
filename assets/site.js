/* Une 2CV, mille histoires — scripts communs */
(function(){
  var nav=document.getElementById('nav');
  function onScroll(){ if(nav) nav.classList.toggle('scrolled', scrollY>60); }
  addEventListener('scroll', onScroll); onScroll();

  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)e.target.classList.add('on');});},{threshold:.12});
  document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});

  var mq=document.getElementById('mq'); if(mq){ mq.innerHTML+=mq.innerHTML; }

  var audio=document.getElementById('musique');
  var btnSon=document.getElementById('btn-son');
  if(audio&&btnSon){
    audio.volume=0.35;
    var musicOn=true;
    function tryPlay(){ if(musicOn && audio.paused){ audio.play().catch(function(){}); } }
    addEventListener('load', tryPlay);
    ['pointerdown','touchstart','keydown','scroll'].forEach(function(ev){ addEventListener(ev, tryPlay, {passive:true}); });
    btnSon.addEventListener('click', function(e){
      e.stopPropagation();
      musicOn=!musicOn;
      if(musicOn){ audio.play().catch(function(){}); btnSon.classList.remove('off'); }
      else { audio.pause(); btnSon.classList.add('off'); }
    });
  }
})();
