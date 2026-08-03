/* Une 2CV, mille histoires — scripts communs */
(function(){
  var nav=document.getElementById('nav');
  var bg=document.getElementById('burger'), ul=document.querySelector('nav ul');
  if(bg&&ul){
    bg.addEventListener('click',function(){var o=ul.classList.toggle('ouvert');bg.setAttribute('aria-expanded',o?'true':'false');});
    ul.addEventListener('click',function(e){if(e.target.closest('a')){ul.classList.remove('ouvert');bg.setAttribute('aria-expanded','false');}});
  }
  function onScroll(){ if(nav) nav.classList.toggle('scrolled', scrollY>60); }
  addEventListener('scroll', onScroll); onScroll();

  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)e.target.classList.add('on');});},{threshold:.12});
  document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});

  var mq=document.getElementById('mq'); if(mq){ mq.innerHTML+=mq.innerHTML; }

  /* masque la bulle WhatsApp flottante quand un gros bouton WhatsApp est visible */
  var waFloat=document.querySelector('.wa-float');
  if(waFloat){
    var visibles=0;
    var ioWa=new IntersectionObserver(function(es){
      es.forEach(function(e){ visibles+=e.isIntersecting?1:-1; });
      if(visibles<0)visibles=0;
      waFloat.classList.toggle('cache-float', visibles>0);
    },{threshold:.4});
    document.querySelectorAll('.btn-wa').forEach(function(b){ if(b!==waFloat) ioWa.observe(b); });
  }

  var audio=document.getElementById('musique');
  var btnSon=document.getElementById('btn-son');
  if(audio&&btnSon){
    audio.volume=0.35;
    var musicOn=false;
    btnSon.classList.add('off');
    btnSon.addEventListener('click', function(e){
      e.stopPropagation();
      musicOn=!musicOn;
      if(musicOn){ audio.play().catch(function(){}); btnSon.classList.remove('off'); }
      else { audio.pause(); btnSon.classList.add('off'); }
    });
  }
})();
