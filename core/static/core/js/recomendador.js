var requestOptions = {
    method: 'GET'
};
// tokendante = GIMRjldigYu6qxayPnCPKmdruId4CgzWKYIIYSrA
// I7GOkn9lxJmdUeNpxk3C4fMbJ8suQupV1mDPmaAi
// Hn8ouDNWFhzd46n7HvIcMBGhrYg20OkCm6EgLYm3
// 4293ec2ff1cc4f9899e1bcf9b5c6a538
var params = {
    api_token: 'Hn8ouDNWFhzd46n7HvIcMBGhrYg20OkCm6EgLYm3',
    search: 'perros',
    language: 'es'
};

var esc = encodeURIComponent;
var query = Object.keys(params)
    .map(function(k) {return esc(k) + '=' + esc(params[k]);})
    .join('&');

fetch("https://api.thenewsapi.com/v1/news/all?" + query, requestOptions)
  .then(response => response.json())
  .then(result => {
      // Accede al elemento DOM donde deseas mostrar los artículos
      var blogContainer = document.getElementById('blogContainer');

      // Verifica si hay artículos en la respuesta
      if (result.data && result.data.length > 0) {
          // Recorre todos los artículos y crea elementos HTML para cada uno
          result.data.forEach(article => {
              // Filtra las noticias que no están en español
              if (article.language !== 'es') {
                  return;
              }

              var articleContainer = document.createElement('article');
              articleContainer.classList.add('op-post', 'mt-2', 'mb-2');

              var imageElement = document.createElement('div');
              imageElement.classList.add('op-post-cont-sm');
              imageElement.innerHTML = `
                  <div class="op-post-cont-sm">
                      <img class="op-post-img" src="${article.image_url}" alt="${article.title}">
                  </div>`;

                  let contentDiv = document.createElement('div');
                  contentDiv.classList.add('op-post-cont-xl');
                  contentDiv.innerHTML = `
                      <h1 class="op-post-title">${article.title}</h1>
                      <h6 class="op-post-description">${article.snippet}</h6>
                      <div class="op-post-barra"></div>
                      <a href="${article.url}" target="_blank" class="op-post-link">Seguir leyendo</a>
                  `;
                  
              // Crea elementos para cada propiedad del artículo
              var titleElement = document.createElement('h2');
              titleElement.textContent = article.title;

              var snippetElement = document.createElement('p');
              snippetElement.textContent = article.snippet;

              var linkElement = document.createElement('a');
              linkElement.href = article.url;
              linkElement.textContent = 'Leer más';

              articleContainer.appendChild(imageElement); 
              articleContainer.appendChild(contentDiv);

              blogContainer.appendChild(articleContainer);
          });
      } else {
          blogContainer.textContent = 'No se encontraron artículos';
      }
  })


  var paramsa = {
    api_token: 'Hn8ouDNWFhzd46n7HvIcMBGhrYg20OkCm6EgLYm3',
    search: 'gatos',
    language: 'es'
};

var esc = encodeURIComponent;
var querya = Object.keys(paramsa)
    .map(function(k) {return esc(k) + '=' + esc(paramsa[k]);})
    .join('&');

  fetch("https://api.thenewsapi.com/v1/news/all?" + querya, requestOptions)
  .then(response => response.json())
  .then(result => {
      // Accede al elemento DOM donde deseas mostrar los artículos
      var blogContainer = document.getElementById('blogContainerHembra');

      // Verifica si hay artículos en la respuesta
      if (result.data && result.data.length > 0) {
          // Recorre todos los artículos y crea elementos HTML para cada uno
          result.data.forEach(article => {
              // Filtra las noticias que no están en español
              if (article.language !== 'es') {
                  return;
              }

              var articleContainer = document.createElement('article');
              articleContainer.classList.add('op-post', 'mt-2', 'mb-2');

              var imageElement = document.createElement('div');
              imageElement.classList.add('op-post-cont-sm');
              imageElement.innerHTML = `
                  <div class="op-post-cont-sm">
                      <img class="op-post-img" src="${article.image_url}" alt="${article.title}">
                  </div>`;

                  let contentDiv = document.createElement('div');
                  contentDiv.classList.add('op-post-cont-xl');
                  contentDiv.innerHTML = `
                      <h1 class="op-post-title">${article.title}</h1>
                      <h6 class="op-post-description">${article.snippet}</h6>
                      <div class="op-post-barra"></div>
                      <a href="${article.url}" target="_blank" class="op-post-link">Seguir leyendo</a>
                  `;
                  
              // Crea elementos para cada propiedad del artículo
              var titleElement = document.createElement('h2');
              titleElement.textContent = article.title;

              var snippetElement = document.createElement('p');
              snippetElement.textContent = article.snippet;

              var linkElement = document.createElement('a');
              linkElement.href = article.url;
              linkElement.textContent = 'Leer más';

              articleContainer.appendChild(imageElement); 
              articleContainer.appendChild(contentDiv);

              blogContainer.appendChild(articleContainer);
          });
      } else {
          blogContainer.textContent = 'No se encontraron artículos';
      }
  })
  .catch(error => console.log('error', error));