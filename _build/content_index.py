# Home page content. Audience-first: why download, how to take part. No technical detail.
NB = ' '

ICON = {
    'star': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l2.6 5.6 6.1.7-4.5 4.2 1.2 6L12 16.6 6.6 19.5l1.2-6L3.3 9.3l6.1-.7z"/></svg>',
    'camera': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="6" width="15" height="12" rx="2"/><path d="M17 10l5-3v10l-5-3"/></svg>',
    'tap': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/></svg>',
    'shield': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l7 4v5c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V7z"/><path d="M9 12l2 2 4-4"/></svg>',
    'download': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12M7 10l5 5 5-5M4 20h16"/></svg>',
    'battery': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="7" width="18" height="10" rx="2"/><path d="M22 11v2M6 11v2M10 11v2"/></svg>',
    'sun': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
}

FAQ = [
    ('Is REZOLQ free?', 'Yes. Download it, open it at the show, and you’re in.'),
    ('Do I need an account?', 'No. No account, no password. Your e-mail is only asked if you choose to sign up for news at the end of a show.'),
    ('When do I open the app?', 'Only when the show asks you to. The artist or the screens will give the signal — open REZOLQ, raise your phone, and you’re part of the picture.'),
    ('Will it drain my battery?', 'Barely. The app only runs during the moment itself, usually a few minutes. Close it the rest of the time.'),
    ('Do I need a connection?', 'Yes, mobile data or Wi-Fi during the show. Download the app before you arrive: networks get busy when thousands of people are in the same place.'),
    ('Why does it ask for Bluetooth?', 'So your screen shows the right colour at the right place in the picture. It is used for nothing else. More in our <a href="/privacy.html">Privacy Policy</a>.'),
    ('I’m sensitive to flashing lights.', 'Some moments use flashing colours. If flashing lights affect you, keep the app closed and look away from the screens around you during those moments.'),
    ('Something isn’t working.', 'See the <a href="/support.html">Support page</a> or write to us. We answer within two working days.'),
]

def build(rule):
    soon = ('<span class="btn btn-primary btn-soon">iPhone <small>coming soon</small></span>'
            '<span class="btn btn-secondary btn-soon">Android <small>coming soon</small></span>')
    return f'''<section class="hero">
  <div class="container">
    <p class="eyebrow">Every phone in the crowd becomes one pixel</p>
    <h1>Don’t just watch the show. Be the show.</h1>
    <p class="lead">With REZOLQ, your phone lights up as one pixel of a giant picture made by the whole crowd — waves, colours and images that move with the music, and you are in it.</p>
    <div class="actions" id="download">{soon}</div>
    <a class="link more" href="#why">Why you’ll want it</a>
    <div class="media"><img src="/assets/img/motif-hero.svg" alt="Phone screens across a crowd; the lit ones draw a wave of light" width="1200" height="520" fetchpriority="high"></div>
  </div>
</section>

<section class="section" aria-labelledby="why-title">
  <div class="container">
    {rule('Why download it', 'why')}
    <div class="section-head"><h2 id="why-title">The best seat in the house is your phone.</h2><p>At a REZOLQ show, the crowd is part of the production. Without the app, you watch it. With it, you’re on it.</p></div>
    <div class="cards cards-2 benefits">
      <article class="card reveal"><span class="ico">{ICON['star']}</span><h3>You’re part of the picture</h3><p>Your screen joins thousands of others to draw shapes, waves and images across the whole crowd. Without you, there’s a gap.</p></article>
      <article class="card reveal"><span class="ico">{ICON['camera']}</span><h3>A moment you’ll want to film</h3><p>Seen from the stage or from the stands, the crowd becomes one giant screen. It’s the shot everyone posts after the show.</p></article>
      <article class="card reveal"><span class="ico">{ICON['tap']}</span><h3>Nothing to set up</h3><p>Open the app when the show asks, raise your phone. That’s it — your screen knows what to do.</p></article>
      <article class="card reveal"><span class="ico">{ICON['shield']}</span><h3>Free, no account, no ads</h3><p>No sign-up, no personal details asked, nothing sold. The app only wakes up for the moment itself.</p></article>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="how-title">
  <div class="container">
    {rule('How to take part', 'how')}
    <div class="section-head"><h2 id="how-title">Three moves. That’s all.</h2></div>
    <div class="cards cards-3">
      <article class="card reveal"><div class="thumb"><img src="/assets/img/step-1.svg" alt="" width="600" height="340" loading="lazy"></div><p class="meta"><span>Step <b>01</b></span></p><h3>Download REZOLQ</h3><p>Before the show, while you still have a good connection.</p></article>
      <article class="card reveal"><div class="thumb"><img src="/assets/img/step-2.svg" alt="" width="600" height="340" loading="lazy"></div><p class="meta"><span>Step <b>02</b></span></p><h3>Open it on the signal</h3><p>When the artist or the screens give the signal, open the app and allow it when it asks.</p></article>
      <article class="card reveal"><div class="thumb"><img src="/assets/img/step-3.svg" alt="" width="600" height="340" loading="lazy"></div><p class="meta"><span>Step <b>03</b></span></p><h3>Raise your phone</h3><p>Screen towards the stage. You’re now one pixel of the picture — look around.</p></article>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="ready-title">
  <div class="container">
    {rule('Before you go', 'ready')}
    <div class="panel reveal">
      <div class="section-head flush"><h2 id="ready-title">Be ready when the lights go down.</h2></div>
      <div class="features">
        <div class="feature">{ICON['download']}<h3>Download it at home</h3><p>Networks get busy when thousands of people are in the same place.</p></div>
        <div class="feature">{ICON['battery']}<h3>Charge your phone</h3><p>The moment only lasts a few minutes, but you’ll want battery to film it.</p></div>
        <div class="feature">{ICON['sun']}<h3>Turn the brightness up</h3><p>The brighter your screen, the brighter the picture.</p></div>
        <div class="feature">{ICON['camera']}<h3>Film it, share it</h3><p>Ask a friend to film the crowd. You’re in that picture.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="faq-title">
  <div class="container">
    {rule('Questions')}
    <div class="section-head"><h2 id="faq-title">Questions people ask</h2></div>
    <div class="faq-list">
      {''.join(f'<details class="faq"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)}
    </div>
  </div>
</section>

<section class="section" aria-labelledby="final-title">
  <div class="container">
    <div class="final">
      <img src="/assets/img/motif-final.svg" alt="" width="1200" height="420" loading="lazy">
      <h2 id="final-title">The next show needs your pixel.</h2>
      <p>Coming soon to the App Store and Google Play.</p>
      <div class="actions">{soon}</div>
    </div>
    <p class="organisers">Organising a concert, a festival or a match? <a href="/support.html">Bring REZOLQ to your event</a>.</p>
  </div>
</section>'''
