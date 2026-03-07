// Function to remove the Google Translate banner
function removeTranslateBanner() {
  // Try multiple selectors to find and remove the banner
  const selectors = [
    '#gtx-app', 
    '.goog-te-banner-frame',
    '.skiptranslate',
    '#\\:0\\.container',
    '#\\:1\\.container',
    '.goog-te-banner',
    '.goog-te-menu-value'
  ];
  
  for (const selector of selectors) {
    const element = document.querySelector(selector);
    if (element) {
      element.style.display = 'none';
      element.remove();
    }
  }
  
  // Also try to remove the top margin that Google Translate adds
  document.body.style.marginTop = '0';
  document.body.style.top = '0';
  
  // Remove iframe that might contain the banner
  const iframes = document.querySelectorAll('iframe');
  for (const iframe of iframes) {
    if (iframe.src.includes('translate.google.com')) {
      iframe.style.display = 'none';
      iframe.remove();
    }
  }
}

// Run the function when the page loads
removeTranslateBanner();

// Also run it periodically to catch any dynamically loaded elements
setInterval(removeTranslateBanner, 1000);