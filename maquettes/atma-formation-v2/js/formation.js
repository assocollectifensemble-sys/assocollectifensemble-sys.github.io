(function(){
'use strict';
var d=document,root=d.documentElement;
var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
var $=function(s,c){return (c||d).querySelector(s)};
var $$=function(s,c){return Array.prototype.slice.call((c||d).querySelectorAll(s))};
root.dataset.ok='1';
setTimeout(function(){root.classList.add('static')},3500);

/* ---- révélations au défilement ---- */
var rvs=$$('.rv');
if('IntersectionObserver' in window&&!reduce){
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -6% 0px',threshold:.08});
  rvs.forEach(function(el,i){io.observe(el)});
}else{rvs.forEach(function(el){el.classList.add('in')})}

/* ---- barre de progression + étape ---- */
var bar=$('#xpbar'),steptxt=$('#steptxt'),secs=$$('main > section[data-step]');
function onScroll(){
  var h=root.scrollHeight-root.clientHeight;
  bar.style.transform='scaleX('+(h>0?Math.min(1,Math.max(0,window.scrollY/h)):0)+')';
}
window.addEventListener('scroll',onScroll,{passive:true});onScroll();
var tabs=$$('.tabbar a[data-t]');
function setStep(sec){
  if(!sec)return;
  steptxt.textContent='Étape '+sec.dataset.step+'/6 · '+sec.dataset.name;
  tabs.forEach(function(a){a.classList.toggle('act',a.dataset.t===sec.id)});
}
if('IntersectionObserver' in window){
  var vis={};
  var so=new IntersectionObserver(function(es){
    es.forEach(function(e){vis[e.target.id]=e.isIntersecting?e.intersectionRatio:0});
    var best=null,bv=0;secs.forEach(function(s){if((vis[s.id]||0)>bv){bv=vis[s.id];best=s}});
    if(best)setStep(best);
  },{threshold:[0,.1,.25,.5,.75]});
  secs.forEach(function(s){so.observe(s)});
}

/* ---- menu ---- */
var bg=$('.burger'),nav=$('#nav');
bg.addEventListener('click',function(){var o=nav.classList.toggle('open');bg.setAttribute('aria-expanded',o);bg.setAttribute('aria-label',o?'Fermer le menu':'Ouvrir le menu')});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&nav.classList.contains('open')){bg.click();bg.focus()}});

/* ---- compteurs ---- */
if(!reduce&&'IntersectionObserver' in window){
  var co=new IntersectionObserver(function(es){es.forEach(function(e){
    if(!e.isIntersecting)return;co.unobserve(e.target);
    var el=e.target,end=+el.dataset.count,t0=null;
    (function f(t){if(!t0)t0=t;var p=Math.min(1,(t-t0)/1100);el.textContent=Math.round(end*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(f)})(performance.now());
  })},{threshold:.6});
  $$('[data-count]').forEach(function(el){el.textContent='0';co.observe(el)});
}

/* ---- niveaux repliables ---- */
$$('.lvl-head').forEach(function(b,i){
  var p=d.getElementById(b.getAttribute('aria-controls'));
  if(i>0){b.setAttribute('aria-expanded','false');p.hidden=true}
  b.addEventListener('click',function(){var o=b.getAttribute('aria-expanded')==='true';b.setAttribute('aria-expanded',!o);p.hidden=o});
});

/* ---- jongleur ---- */
var stage=$('#jgstage'),cap=$('#jgcap');
var caps={1:['Niveau 1.','Un premier outil bien en main : l’IA au quotidien.'],2:['Niveau 2.','Deux gestes qui s’enchaînent : l’IA et les automatisations travaillent ensemble.'],3:['Niveau 3.','Trois balles en l’air : votre assistant IA relie le tout.']};
$$('.seg button').forEach(function(b){b.addEventListener('click',function(){
  var n=b.dataset.n;stage.dataset.n=n;
  $$('.seg button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});
  cap.innerHTML='<b>'+caps[n][0]+'</b> '+caps[n][1];
})});

/* ---- onglets formats ---- */
var tl=$$('[role=tab]');
function selTab(t,focus){
  tl.forEach(function(x){var on=x===t;x.setAttribute('aria-selected',on);x.tabIndex=on?0:-1;d.getElementById(x.getAttribute('aria-controls')).hidden=!on});
  if(focus)t.focus();
}
tl.forEach(function(t,i){
  t.addEventListener('click',function(){selTab(t)});
  t.addEventListener('keydown',function(e){
    var k=e.key,j=i;
    if(k==='ArrowRight')j=(i+1)%tl.length;else if(k==='ArrowLeft')j=(i+tl.length-1)%tl.length;else if(k==='Home')j=0;else if(k==='End')j=tl.length-1;else return;
    e.preventDefault();selTab(tl[j],true);
  });
});

/* ---- quiz (100 % local, rien n'est envoyé) ---- */
var steps=$$('.q-step'),res=$('#qres'),back=$('#qback'),count=$('#qcount'),dots=$$('.dots i'),box=$('#quizbox');
var ans=[],cur=0;
var LV={1:'Niveau 1 · L’IA au quotidien',2:'Niveau 2 · Automatiser avec Make ou n8n',3:'Niveau 3 · Votre assistant ou agent IA'};
var TX={
  1:'Vous gagnez du temps sur l’écriture : mails, avis, contenus. ChatGPT et Claude deviennent vos alliés de chaque jour, à partir de vos vrais messages.',
  2:'Vos tâches répétitives méritent de se dérouler toutes seules : un rendez-vous Calendly qui déclenche des notifications, un formulaire qui alimente un Google Sheets, un paiement Stripe qui génère un contrat.',
  3:'Un assistant ou agent IA adapté à votre activité peut répondre à votre place aux questions qui reviennent, et vous savez le régler, le corriger et le faire évoluer.'
};
var FM={1:'Format conseillé : accompagnement individuel, centré sur votre activité, sur place à La Réunion ou à distance.',2:'Format conseillé : atelier en petit groupe entre professionnels, chacun avec ses outils, sur place à La Réunion ou à distance.',3:'Format conseillé : intervention auprès de votre structure de formation, en animation ou co-animation d’un module.'};
var FW={1:'en accompagnement individuel',2:'en petit groupe',3:'dans ma structure de formation'};
function show(i){
  cur=i;
  steps.forEach(function(s,k){s.hidden=k!==i});
  res.hidden=true;back.hidden=i===0;
  count.textContent='Question '+(i+1)+' sur 3';
  dots.forEach(function(x,k){x.classList.toggle('on',k<=i)});
  var t=$('.q-title',steps[i]);if(t&&box.dataset.touched)t.focus({preventScroll:true});
}
function result(){
  steps.forEach(function(s){s.hidden=true});back.hidden=false;
  count.textContent='Résultat';dots.forEach(function(x){x.classList.add('on')});
  var want=ans[0],lvl=want,start=want,lead='';
  if(ans[1]===1&&want>1){lvl=1;lead='Pour poser des bases solides, démarrez par le niveau 1, puis poursuivez vers le niveau '+want+'. '}
  $('#resLvl').textContent=LV[lvl];
  $('#resTxt').textContent=lead+TX[lvl];
  $('#resFmt').textContent=FM[ans[2]];
  var msg='Bonjour Jonathan, j’ai fait le quiz sur votre page formation : le parcours conseillé est « '+LV[lvl]+' », '+FW[ans[2]]+'. Pouvons-nous en parler 20 minutes ?';
  $('#resCta').href='https://wa.me/262693828108?text='+encodeURIComponent(msg);
  res.hidden=false;
  var t=$('#resTitle');if(t)t.focus({preventScroll:true});
}
$$('.opt').forEach(function(b){b.addEventListener('click',function(){
  box.dataset.touched='1';
  var q=+b.closest('.q-step').dataset.q;
  $$('.opt',steps[q]).forEach(function(o){o.classList.toggle('sel',o===b)});
  ans[q]=+b.dataset.v;
  setTimeout(function(){if(q<2)show(q+1);else result()},reduce?0:220);
})});
back.addEventListener('click',function(){
  if(!res.hidden){show(2)}else if(cur>0){show(cur-1)}
});
$('#qreset').addEventListener('click',function(){ans=[];$$('.opt').forEach(function(o){o.classList.remove('sel')});show(0)});
window.__quiz={answers:function(){return ans.slice()}};
})();
