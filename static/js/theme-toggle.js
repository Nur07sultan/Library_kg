(function(){
  const storageKey = 'librarykg_theme';
  const rootEl = document.documentElement || document.body;

  function safeLocalGet(key){
    try { return localStorage.getItem(key); } catch(e){ return null; }
  }
  function safeLocalSet(key, val){
    try { localStorage.setItem(key, val); } catch(e){ }
  }

  function setButtonState(btn, theme){
    if(!btn) return;
    const isLight = theme === 'light';
    btn.setAttribute('aria-pressed', isLight ? 'true' : 'false');
    btn.textContent = isLight ? '☀️' : '🌙';
    // trigger animation
    btn.classList.remove('active');
    void btn.offsetWidth; // reflow
    btn.classList.add('active');
  }

  function applyTheme(theme){
    if(!rootEl) return;
    const html = document.documentElement;
    const body = document.body;
    // add explicit classes for both states on html and body
    if(theme === 'light'){
      html.classList.add('theme-light'); html.classList.remove('theme-dark');
      body.classList.add('theme-light'); body.classList.remove('theme-dark');
    } else {
      html.classList.remove('theme-light'); html.classList.add('theme-dark');
      body.classList.remove('theme-light'); body.classList.add('theme-dark');
    }
    // add a temporary class to enable smooth transition only during theme change
    html.classList.add('theme-transition'); body.classList.add('theme-transition');
    window.setTimeout(() => { html.classList.remove('theme-transition'); body.classList.remove('theme-transition'); }, 320);
    const btn = document.getElementById('theme-toggle');
    setButtonState(btn, theme);
    console.debug('[theme-toggle] applied theme:', theme);
  }


  function detectSystemPreference(){
    try{
      return window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
    }catch(e){ return 'dark'; }
  }

  function init(){
    const btn = document.getElementById('theme-toggle');
    const saved = safeLocalGet(storageKey);
    const initial = saved || detectSystemPreference();
    applyTheme(initial);

    // ensure button reflects state immediately
    if(btn){
      const isLight = document.documentElement.classList.contains('theme-light');
      btn.setAttribute('aria-pressed', isLight ? 'true' : 'false');
      btn.classList.add('active');
    }

    // Listen to system changes (but don't override saved preference)
    try{
      if(window.matchMedia){
        window.matchMedia('(prefers-color-scheme: light)').addEventListener('change', e => {
          const hasSaved = !!safeLocalGet(storageKey);
          if(!hasSaved){
            applyTheme(e.matches ? 'light' : 'dark');
          }
        });
      }
    }catch(e){ /* ignore */ }

    if(!btn) return;

    btn.addEventListener('click', function(){
      const isLightNow = rootEl.classList.contains('theme-light');
      const next = isLightNow ? 'dark' : 'light';
      applyTheme(next);
      safeLocalSet(storageKey, next);
    });
  }

  // Run on DOM ready
  if(document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();

})();
