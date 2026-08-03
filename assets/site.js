/* Une 2CV, mille histoires — scripts communs */
(function(){
  var ic=document.getElementById('intro-cine');
  if(ic){
    var vu=false; try{vu=!!sessionStorage.getItem('introVue');}catch(e){}
    if(vu){ ic.parentNode.removeChild(ic); }
    else{
      document.documentElement.classList.add('intro-lock');
      var iv=document.getElementById('intro-vid');
      var fini=false;
      var fin=function(){ if(fini)return; fini=true;
        try{sessionStorage.setItem('introVue','1');}catch(e){}
        ic.classList.add('fini');
        document.documentElement.classList.remove('intro-lock');
        setTimeout(function(){ if(ic&&ic.parentNode)ic.parentNode.removeChild(ic); },1000); };
      iv.addEventListener('ended',fin);
      iv.addEventListener('error',fin);
      ic.querySelector('.intro-passer').addEventListener('click',fin);
      var p=iv.play(); if(p&&p.catch){p.catch(fin);}
      setTimeout(fin,9000);
    }
  }

  var nav=document.getElementById('nav');
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
    var musicOn=true;
    function tryPlay(){ if(musicOn && audio.paused){ audio.play().catch(function(){}); } }
    tryPlay();
    document.addEventListener('DOMContentLoaded', tryPlay);
    addEventListener('load', tryPlay);
    var essais=0, relance=setInterval(function(){ essais++; if(!audio.paused||essais>16){clearInterval(relance);return;} tryPlay(); },600);
    ['pointerdown','touchstart','keydown','scroll','click'].forEach(function(ev){ addEventListener(ev, tryPlay, {passive:true}); });
    btnSon.addEventListener('click', function(e){
      e.stopPropagation();
      musicOn=!musicOn;
      if(musicOn){ audio.play().catch(function(){}); btnSon.classList.remove('off'); }
      else { audio.pause(); btnSon.classList.add('off'); }
    });
  }
})();
