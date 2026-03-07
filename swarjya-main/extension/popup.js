document.getElementById("translate").addEventListener("click", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const tabId = tabs[0].id;
    const url = tabs[0].url;
    const targetLang = document.getElementById("language").value;
    
    const translateUrl = `https://translate.google.com/translate?sl=auto&tl=${targetLang}&u=${encodeURIComponent(url)}`;

    chrome.tabs.update(tabId, { url: translateUrl });
  });
});