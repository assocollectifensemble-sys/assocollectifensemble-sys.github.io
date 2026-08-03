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
/* ---- formulaire : téléphone obligatoire + envoi résistant aux pannes ---- */
(function(){
  var f=document.querySelector('form.formulaire'); if(!f) return;
  var tel=f.querySelector('#f-tel');
  function nbChiffres(v){ return (v.match(/[0-9]/g)||[]).length; }
  function verifTel(){
    if(!tel) return;
    var n=nbChiffres(tel.value);
    if(n===0) tel.setCustomValidity("Merci d'indiquer un numéro de téléphone : c'est par là que je vous réponds le plus vite.");
    else if(n<9) tel.setCustomValidity("Ce numéro semble incomplet. Écrivez-le en entier, par exemple 0692 12 34 56.");
    else tel.setCustomValidity("");
  }
  if(tel){ tel.addEventListener('input',verifTel); tel.addEventListener('blur',verifTel); verifTel(); }
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
    if(!f.checkValidity()){ return; }
    if(!window.fetch){ return; }
    e.preventDefault();
    var btn=f.querySelector('button[type=submit]'); var txt=btn.textContent;
    btn.disabled=true; btn.textContent='Envoi en cours…';
    var url=f.action.replace('formsubmit.co/','formsubmit.co/ajax/');
    fetch(url,{method:'POST',body:new FormData(f),headers:{'Accept':'application/json'}})
      .then(function(r){ if(!r.ok) throw new Error('ko'); window.location.href='/merci'; })
      .catch(function(){
        btn.disabled=false; btn.textContent=txt;
        var d=document.getElementById('form-secours');
        if(d){ d.hidden=false; var a=d.querySelector('a.secours-mail'); if(a) a.href=lienMail();
               d.scrollIntoView({behavior:'smooth',block:'center'}); }
      });
  });
})();
