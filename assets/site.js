/* Une 2CV, mille histoires — scripts communs */
(function(){
  var nav=document.getElementById('nav');
  var bg=document.getElementById('burger'), ul=document.querySelector('nav ul');
  if(bg&&ul){
    var setMenu=function(o){
      ul.classList.toggle('ouvert',o);
      bg.setAttribute('aria-expanded',o?'true':'false');
      bg.setAttribute('aria-label',o?'Fermer le menu':'Ouvrir le menu');
      if(nav) nav.classList.toggle('menu-ouvert',o);
      document.documentElement.classList.toggle('menu-ouvert',o);
    };
    bg.addEventListener('click',function(e){ e.stopPropagation(); setMenu(!ul.classList.contains('ouvert')); });
    ul.addEventListener('click',function(e){ if(e.target.closest('a')) setMenu(false); });
    if(nav) nav.addEventListener('click',function(e){
      if(!ul.classList.contains('ouvert')) return;
      if(e.target.closest('#burger')||e.target.closest('nav ul')) return;
      setMenu(false);
    });
    addEventListener('keydown',function(e){ if(e.key==='Escape') setMenu(false); });
    addEventListener('resize',function(){ if(innerWidth>1080) setMenu(false); });
  }
  function onScroll(){ if(nav) nav.classList.toggle('scrolled', scrollY>60); }
  addEventListener('scroll', onScroll); onScroll();

  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)e.target.classList.add('on');});},{threshold:.12});
  document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});

  var mq=document.getElementById('mq'); if(mq){ mq.innerHTML+=mq.innerHTML; }

  /* bulle WhatsApp : absente à l'arrivée, elle apparaît quand on atteint les prestations,
     et s'efface quand un grand bouton WhatsApp est déjà à l'écran */
  var waFloat=document.querySelector('.wa-float');
  if(waFloat){
    var declencheur=document.getElementById('prestations');
    if(declencheur&&'IntersectionObserver' in window){
      waFloat.classList.add('pas-encore');
      var ioApparition=new IntersectionObserver(function(es){
        es.forEach(function(e){
          if(e.isIntersecting){ waFloat.classList.remove('pas-encore'); ioApparition.disconnect(); }
        });
      },{rootMargin:'0px 0px -18% 0px'});
      ioApparition.observe(declencheur);
    }
    var visibles=0;
    var ioWa=new IntersectionObserver(function(es){
      es.forEach(function(e){ visibles+=e.isIntersecting?1:-1; });
      if(visibles<0)visibles=0;
      waFloat.classList.toggle('cache-float', visibles>0);
    },{threshold:.4});
    document.querySelectorAll('.btn-wa').forEach(function(b){ if(b!==waFloat) ioWa.observe(b); });
    // La bulle occupe en permanence le coin bas droit : elle s'efface aussi devant le pied
    // de page, ou vivent le telephone, l'adresse et les liens des reseaux.
    var pied=document.querySelector('footer'); if(pied) ioWa.observe(pied);
  }

  var audio=document.getElementById('musique');
  var btnSon=document.getElementById('btn-son');
  if(audio&&btnSon){
    var VOL=0.32, musicOn=false, coupee=false, minuteur=null;
    audio.volume=0;
    btnSon.classList.add('off');
    function fondu(vers,duree){
      clearInterval(minuteur);
      var depart=audio.volume, t0=Date.now();
      minuteur=setInterval(function(){
        var k=Math.min(1,(Date.now()-t0)/duree);
        audio.volume=depart+(vers-depart)*k;
        if(k>=1){ clearInterval(minuteur); if(vers===0) audio.pause(); }
      },40);
    }
    function allumer(){
      var p=audio.play();
      if(p&&p.then){ p.then(reussi).catch(function(){}); } else { reussi(); }
    }
    function reussi(){
      musicOn=true; btnSon.classList.remove('off');
      btnSon.setAttribute('aria-label','Couper la musique');
      fondu(VOL,2200); retirerGestes();
    }
    var gestes=['touchend','click','pointerup','pointerdown','touchstart','keydown','wheel','scroll'];
    function surGeste(){ if(!musicOn&&!coupee) allumer(); }
    function retirerGestes(){ gestes.forEach(function(g){ removeEventListener(g,surGeste); }); }
    gestes.forEach(function(g){ addEventListener(g,surGeste,{passive:true}); });
    btnSon.addEventListener('click', function(e){
      e.stopPropagation();
      if(musicOn){
        musicOn=false; coupee=true; retirerGestes();
        btnSon.classList.add('off'); btnSon.setAttribute('aria-label','Écouter la musique');
        fondu(0,500);
      } else {
        coupee=false;
        gestes.forEach(function(g){ addEventListener(g,surGeste,{passive:true}); });
        allumer();
      }
    });
  }

})();
/* ---- formulaires : téléphone obligatoire + envoi résistant aux pannes ---- */
(function(){
  var forms=document.querySelectorAll('form.formulaire');
  if(!forms.length) return;
  function nbChiffres(v){ return (v.match(/[0-9]/g)||[]).length; }
  Array.prototype.forEach.call(forms, function(f){
    var tel=f.querySelector('[name="telephone"]');
    function verifTel(){
      if(!tel) return;
      var n=nbChiffres(tel.value);
      if(n===0) tel.setCustomValidity("Merci d'indiquer un numéro de téléphone : c'est par là que je vous réponds le plus vite.");
      else if(n<9) tel.setCustomValidity("Ce numéro semble incomplet. Écrivez-le en entier, par exemple 0692 12 34 56.");
      else tel.setCustomValidity("");
    }
    if(tel){
      tel.setAttribute('required','required');
      tel.addEventListener('input',verifTel);
      tel.addEventListener('blur',verifTel);
      verifTel();
    }
    function lienMail(){
      var g=function(n){ var e=f.querySelector('[name="'+n+'"]'); return e? e.value : ''; };
      var corps="Prénom et nom : "+g('nom')+"\n"
        +"Téléphone : "+g('telephone')+"\n"
        +"Email : "+g('email')+"\n"
        +"Type d'évènement : "+g('evenement')+"\n"
        +"Date envisagée : "+g('date')+"\n\n"+g('message');
      return "mailto:asso.collectif.ensemble@gmail.com?subject="
        +encodeURIComponent("Demande — Une 2CV, mille histoires")
        +"&body="+encodeURIComponent(corps);
    }
    f.addEventListener('submit',function(e){
      verifTel();
      if(tel && nbChiffres(tel.value)<9){
        e.preventDefault(); e.stopPropagation();
        if(f.reportValidity) f.reportValidity(); else tel.focus();
        tel.focus();
        return false;
      }
      if(!f.checkValidity()){ return; }
      if(!window.fetch){ return; }
      e.preventDefault();
      var btn=f.querySelector('button[type=submit]'); var txt=btn.textContent;
      btn.disabled=true; btn.textContent='Envoi en cours…';
      var url=f.action.replace('formsubmit.co/','formsubmit.co/ajax/');
      fetch(url,{method:'POST',body:new FormData(f),headers:{'Accept':'application/json'}})
        .then(function(r){ return r.json(); })
        .then(function(d){ if(d && d.success==='true'){ window.location.href='/merci'; } else { throw new Error('ko'); } })
        .catch(function(){
          btn.disabled=false; btn.textContent=txt;
          var d=f.parentNode.querySelector('.secours');
          if(d){ d.hidden=false; var a=d.querySelector('a.secours-mail'); if(a) a.href=lienMail();
                 d.scrollIntoView({behavior:'smooth',block:'center'}); }
        });
    }, true);
  });
})();
