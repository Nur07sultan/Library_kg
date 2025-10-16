(function(){
  function $(sel, root=document) { return root.querySelector(sel); }
  function $all(sel, root=document) { return Array.from(root.querySelectorAll(sel)); }

  function createSuggestion(text){
    const el = document.createElement('div');
    el.className = 'genre-suggestion';
    el.textContent = text;
    return el;
  }

  function attachAutocomplete(root){
    const input = $('.genre-input', root);
    const box = $('.genre-suggestions', root);
    if(!input || !box) return;
    let items = GENRES || [];
    let index = -1;

    function render(list){
      box.innerHTML = '';
      if(!list.length){ box.style.display='none'; return; }
      list.forEach(v => box.appendChild(createSuggestion(v)));
      box.style.display='block';
    }

    function filter(val){
      if(!val) return items.slice(0,6);
      const q = val.toLowerCase();
      return items.filter(i => i.toLowerCase().includes(q)).slice(0,6);
    }

    input.addEventListener('input', function(){
      const list = filter(this.value);
      index = -1;
      render(list);
    });

    input.addEventListener('keydown', function(e){
      const suggs = $all('.genre-suggestion', box);
      if(e.key === 'ArrowDown'){
        e.preventDefault(); index = Math.min(index+1, suggs.length-1); if(suggs[index]) suggs[index].classList.add('active');
      } else if(e.key === 'ArrowUp'){
        e.preventDefault(); if(index>=0) { suggs[index].classList.remove('active'); index = Math.max(index-1, -1); if(index>=0) suggs[index].classList.add('active'); }
      } else if(e.key === 'Enter'){
        if(index >=0 && suggs[index]){ e.preventDefault(); input.value = suggs[index].textContent; box.style.display='none'; }
      }
    });

    box.addEventListener('click', function(e){
      const target = e.target.closest('.genre-suggestion');
      if(target){ input.value = target.textContent; box.style.display='none'; input.focus(); }
    });

    document.addEventListener('click', function(e){ if(!root.contains(e.target)) box.style.display='none'; });

    // init suggestions on focus
    input.addEventListener('focus', function(){ render(filter(this.value)); });
  }

  document.addEventListener('DOMContentLoaded', function(){
    $all('.genre-wrap').forEach(attachAutocomplete);
  });
})();
