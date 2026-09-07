document.addEventListener('DOMContentLoaded', function() {
  // Fix image paths for GitHub Pages
  const baseUrl = document.location.pathname.startsWith('/devops-release-notes') 
    ? '/devops-release-notes' 
    : '';
  
  // Find all images with relative paths
  document.querySelectorAll('img').forEach(function(img) {
    const src = img.getAttribute('src');
    
    // Only adjust relative paths that don't already have the baseUrl
    if (src && src.startsWith('../') && baseUrl) {
      // Replace the first part of the path to include the base URL if needed
      const newSrc = src.replace('../', baseUrl + '/');
      img.setAttribute('src', newSrc);
    }
  });
}); 