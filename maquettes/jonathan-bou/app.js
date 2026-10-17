(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Nav */
  const nav = $('#nav'), burger = $('#burger');
  const onScroll = () => nav.classList.toggle('solid', scrollY > 40);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();
  burger.addEventListener('click', () => {
    const o = nav.classList.toggle('open');
    burger.setAttribute('aria-expanded', o);
    document.body.style.overflow = o ? 'hidden' : '';
  });
  $$('#menu a').forEach(a => a.addEventListener('click', () => {
    nav.classList.remove('open'); burger.setAttribute('aria-expanded', false); document.body.style.overflow = '';
  }));

  /* Title letters */
  $$('.split').forEach((el, w) => {
    const t = el.textContent; el.textContent = '';
    [...t].forEach((c, i) => {
      const s = document.createElement('span'); s.className = 'ch'; s.textContent = c;
      s.style.animationDelay = (0.15 + w * 0.25 + i * 0.05) + 's'; el.appendChild(s);
    });
  });

  /* Reveal */
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }), { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  $$('.reveal').forEach((el, i) => { el.style.transitionDelay = (i % 4) * 0.08 + 's'; io.observe(el); });

  /* Juggling balls in hero (canvas) */
  const cv = $('#juggle');
  if (cv && !reduce) {
    const ctx = cv.getContext('2d'); let W, H, dpr;
    const cols = ['#f2b134', '#e2563b', '#2f8f8a', '#f6efe3', '#f2b134'];
    const resize = () => { dpr = Math.min(devicePixelRatio || 1, 2); W = cv.clientWidth; H = cv.clientHeight; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); };
    resize(); addEventListener('resize', resize);
    const N = 5, period = 3.2;
    let mx = 0.5, my = 0.5;
    addEventListener('pointermove', e => { mx = e.clientX / innerWidth; my = e.clientY / innerHeight; }, { passive: true });
    let visible = true;
    new IntersectionObserver(([e]) => visible = e.isIntersecting).observe(cv);
    const draw = t => {
      requestAnimationFrame(draw);
      if (!visible) return;
      ctx.clearRect(0, 0, W, H);
      const cx = W * (W > 900 ? 0.74 : 0.6) + (mx - 0.5) * 30, base = H * (W > 900 ? 0.6 : 0.42) + (my - 0.5) * 20;
      const spread = Math.min(W, 900) * 0.16, height = H * 0.32, r = Math.max(7, Math.min(W, H) * 0.014);
      for (let i = 0; i < N; i++) {
        const p = ((t / 1000) / period + i / N) % 1;          // cascade
        const side = Math.floor(((t / 1000) / period + i / N) * 2) % 2; // alternate hands
        const ph = (p * 2) % 1;
        const x0 = side ? -spread : spread, x1 = -x0;
        const x = cx + x0 + (x1 - x0) * ph;
        const y = base - 4 * height * ph * (1 - ph);
        // trail
        for (let k = 1; k <= 6; k++) {
          const q = Math.max(0, ph - k * 0.018);
          const tx = cx + x0 + (x1 - x0) * q, ty = base - 4 * height * q * (1 - q);
          ctx.globalAlpha = 0.10 * (1 - k / 7); ctx.fillStyle = cols[i];
          ctx.beginPath(); ctx.arc(tx, ty, r * (1 - k * 0.08), 0, 7); ctx.fill();
        }
        ctx.globalAlpha = 0.95;
        const g = ctx.createRadialGradient(x - r * .35, y - r * .35, r * .1, x, y, r);
        g.addColorStop(0, '#fff8e8'); g.addColorStop(0.35, cols[i]); g.addColorStop(1, cols[i]);
        ctx.fillStyle = g; ctx.beginPath(); ctx.arc(x, y, r, 0, 7); ctx.fill();
      }
      ctx.globalAlpha = 1;
    };
    requestAnimationFrame(draw);
  }

  /* Parallax */
  const par = $$('.parallax');
  if (!reduce && par.length) {
    const upd = () => par.forEach(el => {
      const r = el.parentElement.getBoundingClientRect();
      const d = (r.top + r.height / 2 - innerHeight / 2);
      el.style.transform = `translateY(${d * parseFloat(el.dataset.speed)}px)`;
    });
    addEventListener('scroll', () => requestAnimationFrame(upd), { passive: true }); upd();
  }

  /* Route: the 2CV drives along the path while scrolling */
  const route = $('#route'), path = $('#routePath'), done = $('#routeDone'), car = $('#car'), stops = $$('.stop');
  if (route && path) {
    const L = path.getTotalLength();
    done.style.strokeDasharray = L; done.style.strokeDashoffset = L;
    const svg = path.ownerSVGElement;
    const upd = () => {
      const r = route.getBoundingClientRect();
      let p = (innerHeight * 0.85 - r.top) / (innerHeight * 0.75);
      p = Math.max(0, Math.min(1, p));
      if (reduce) p = 1;
      done.style.strokeDashoffset = L * (1 - p);
      const pt = path.getPointAtLength(L * p), pt2 = path.getPointAtLength(Math.min(L, L * p + 1));
      const sx = svg.clientWidth / 1000, sy = svg.clientHeight / 120;
      const ang = Math.atan2((pt2.y - pt.y) * sy, (pt2.x - pt.x) * sx) * 180 / Math.PI;
      car.style.transform = `translate(${pt.x * sx}px, ${pt.y * sy}px) translate(-50%,-85%) rotate(${ang * 0.6}deg)`;
      stops.forEach((s, i) => s.classList.toggle('on', p >= i / (stops.length - 1) - 0.02));
    };
    addEventListener('scroll', () => requestAnimationFrame(upd), { passive: true });
    addEventListener('resize', upd); upd();
  }

  /* Card tilt */
  if (!reduce && matchMedia('(hover:hover)').matches) {
    $$('.tilt').forEach(c => {
      c.addEventListener('pointermove', e => {
        const r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
        c.style.transform = `perspective(900px) rotateY(${x * 6}deg) rotateX(${-y * 6}deg) translateY(-6px)`;
      });
      c.addEventListener('pointerleave', () => c.style.transform = '');
    });
  }

  /* Teaser modal */
  const modal = $('#modal'), teaser = $('#teaser');
  const closeM = () => { modal.hidden = true; teaser.pause(); document.body.style.overflow = ''; };
  $$('[data-teaser]').forEach(b => b.addEventListener('click', () => {
    modal.hidden = false; document.body.style.overflow = 'hidden'; teaser.currentTime = 0; teaser.play().catch(() => {});
  }));
  $('.modal-x').addEventListener('click', closeM);
  modal.addEventListener('click', e => { if (e.target === modal) closeM(); });

  /* Gallery filter + lightbox */
  const items = $$('#masonry a');
  $$('.filters button').forEach(b => b.addEventListener('click', () => {
    $$('.filters button').forEach(x => x.classList.toggle('on', x === b));
    items.forEach(a => a.classList.toggle('hide', b.dataset.f !== 'all' && a.dataset.cat !== b.dataset.f));
  }));
  const lb = $('#lightbox'), lbImg = $('img', lb); let cur = 0;
  const vis = () => items.filter(a => !a.classList.contains('hide'));
  const show = i => { const v = vis(); cur = (i + v.length) % v.length; lbImg.src = v[cur].href; lbImg.alt = $('img', v[cur]).alt; };
  items.forEach(a => a.addEventListener('click', e => {
    e.preventDefault(); show(vis().indexOf(a)); lb.hidden = false; document.body.style.overflow = 'hidden';
  }));
  const closeL = () => { lb.hidden = true; document.body.style.overflow = ''; };
  $('.lb-x').addEventListener('click', closeL);
  $('.lb-prev').addEventListener('click', () => show(cur - 1));
  $('.lb-next').addEventListener('click', () => show(cur + 1));
  lb.addEventListener('click', e => { if (e.target === lb) closeL(); });
  addEventListener('keydown', e => {
    if (e.key === 'Escape') { if (!lb.hidden) closeL(); if (!modal.hidden) closeM(); }
    if (!lb.hidden && e.key === 'ArrowLeft') show(cur - 1);
    if (!lb.hidden && e.key === 'ArrowRight') show(cur + 1);
  });
  let sx0 = 0;
  lb.addEventListener('touchstart', e => sx0 = e.touches[0].clientX, { passive: true });
  lb.addEventListener('touchend', e => { const d = e.changedTouches[0].clientX - sx0; if (Math.abs(d) > 50) show(cur + (d < 0 ? 1 : -1)); });
})();
