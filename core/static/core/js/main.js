/*document.addEventListener('DOMContentLoaded', function () {
    Api_con_axios();
  });
  
  function Api_con_axios() {
    axios({
      method: 'GET',
      url: 'https://gnews.io/api/v4/search?q=animal&country=es&apikey=5d4c96acf6f182b045ac8bcaee0ee580'
    }).then(res => {
      let noticias = res.data.articles;
  
      noticias.forEach((elemento, index) => {
        let div = document.createElement('div');
        div.innerHTML = `
          <div class="op-post-cont-sm">
            <img class="op-post-img" src=${elemento.image} alt="Bellota">
          </div>
          <br>
          <br>
          <div class="op-post-cont-xl">
            <h1 class="op-post-title">${elemento.title}</h1>
            <h5 class="op-post-title2">${elemento.description}</h5>
            <div class="op-post-barra"></div>
            <p class="op-post-text">
              ${elemento.content}
            </p>
            <h4 class="op-post-title2time">${elemento.publishedAt}</h3>
            <h4 class="op-post-title2time">${elemento.source.name}</h3>
            <a href=${elemento.url}>Seguir leyendo</a>
          </div>
          <br>
          <br>
          <div class="op-post-barra"></div>
          <br>`;
  
        // Obtener todos los contenedores con la clase 'news-container'
        let containers = document.querySelectorAll('.news-container');
  
        // Verificar si hay un contenedor disponible antes de intentar agregar la noticia
        if (containers[index]) {
          containers[index].appendChild(div);
        }
      });
    });
  }
  

*/



let noti = document.getElementById('news');

function Api_con_axios() {
    axios({
        method: 'GET',
        url: 'https://gnews.io/api/v4/search?q=animal&country=es&apikey=5d4c96acf6f182b045ac8bcaee0ee580'
    }).then(res => {
        let noticias = res.data.articles;
        console.log(noticias);
        
        noticias.forEach(elemento => {
            let article = document.createElement('article');
            article.classList.add('op-post', 'mt-2', 'mb-2');

            let imageDiv = document.createElement('div');
            imageDiv.classList.add('op-post-cont-sm');
            imageDiv.innerHTML = `<img class="op-post-img" src="${elemento.image}" alt="Bellota">`;
            
            let contentDiv = document.createElement('div');
            contentDiv.classList.add('op-post-cont-xl');
            contentDiv.innerHTML = `
                <h1 class="op-post-title">${elemento.title}</h1>
                <h5 class="op-post-description">${elemento.description}</h5>
                <div class="op-post-barra"></div>
                <p class="op-post-text">${elemento.content}</p>
                <h4 class="op-post-time">${elemento.publishedAt}</h4>
                <h4 class="op-post-time">${elemento.source.name}</h4>
                <a href="${elemento.url}" target="_blank" class="op-post-link">Seguir leyendo</a>
            `;
            
            article.appendChild(imageDiv);
            article.appendChild(contentDiv);

            noti.appendChild(article);
        });
    }).catch(error => {
        console.error('Error al cargar noticias:', error);
    });
}

Api_con_axios();
