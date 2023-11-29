var requestOptions = {
    method: 'GET'
};
// tokendante = GIMRjldigYu6qxayPnCPKmdruId4CgzWKYIIYSrA
var params = {
    api_token: 'I7GOkn9lxJmdUeNpxk3C4fMbJ8suQupV1mDPmaAi',
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

              var articleContainer = document.createElement('div');
              articleContainer.classList.add('blog-post');

              // Crea elementos para cada propiedad del artículo
              var titleElement = document.createElement('h2');
              titleElement.textContent = article.title;

              var snippetElement = document.createElement('p');
              snippetElement.textContent = article.snippet;

              var imageElement = document.createElement('img');
              imageElement.src = article.image_url;
              imageElement.alt = article.title;

              var sourceElement = document.createElement('p');
              sourceElement.textContent = 'Source: ' + article.source;

              var linkElement = document.createElement('a');
              linkElement.href = article.url;
              linkElement.textContent = 'Leer más';

              // Agrega todos los elementos al contenedor del artículo
              articleContainer.appendChild(titleElement);
              articleContainer.appendChild(snippetElement);
              articleContainer.appendChild(imageElement);
              articleContainer.appendChild(sourceElement);
              articleContainer.appendChild(linkElement);

              // Agrega el contenedor del artículo al contenedor del blog
              blogContainer.appendChild(articleContainer);
          });
      } else {
          blogContainer.textContent = 'No se encontraron artículos';
      }
  })


  var paramsa = {
    api_token: 'I7GOkn9lxJmdUeNpxk3C4fMbJ8suQupV1mDPmaAi',
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

              var articleContainer = document.createElement('div');
              articleContainer.classList.add('blog-post');

              // Crea elementos para cada propiedad del artículo
              var titleElement = document.createElement('h2');
              titleElement.textContent = article.title;

              var snippetElement = document.createElement('p');
              snippetElement.textContent = article.snippet;

              var imageElement = document.createElement('img');
              imageElement.src = article.image_url;
              imageElement.alt = article.title;

              var sourceElement = document.createElement('p');
              sourceElement.textContent = 'Source: ' + article.source;

              var linkElement = document.createElement('a');
              linkElement.href = article.url;
              linkElement.textContent = 'Leer más';

              // Agrega todos los elementos al contenedor del artículo
              articleContainer.appendChild(titleElement);
              articleContainer.appendChild(snippetElement);
              articleContainer.appendChild(imageElement);
              articleContainer.appendChild(sourceElement);
              articleContainer.appendChild(linkElement);

              // Agrega el contenedor del artículo al contenedor del blog
              blogContainer.appendChild(articleContainer);
          });
      } else {
          blogContainer.textContent = 'No se encontraron artículos';
      }
  })
  .catch(error => console.log('error', error));