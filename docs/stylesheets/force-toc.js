// force-toc.js
// MutationObserver-based solution to always show the right sidebar TOC in MkDocs Material
(function() {
  function showTOC() {
    var toc = document.querySelector('.md-sidebar--secondary');
    if (toc) {
      toc.removeAttribute('hidden');
      toc.style.display = 'block';
      toc.style.visibility = 'visible';
      toc.style.opacity = '1';
      toc.style.pointerEvents = 'auto';
    }
  }

  // Initial attempt
  document.addEventListener('DOMContentLoaded', showTOC);

  // Observe DOM changes and re-apply if needed
  var observer = new MutationObserver(showTOC);
  observer.observe(document.body, { childList: true, subtree: true, attributes: true });
})(); 