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



  function Api_con_axios() {
    const noticiasPorDia = 100;
    const tiempoEsperaEntreSolicitudes = 1000; // 1 segundo
  
    // Hacer un bucle para obtener noticias hasta que alcances el límite diario
    for (let i = 0; i < noticiasPorDia; i++) {
      // Llama a la función para obtener noticias después de esperar el tiempo necesario
      setTimeout(() => obtenerNoticias(), i * tiempoEsperaEntreSolicitudes);
    }
  }
  
  function obtenerNoticias() {
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
        <br>
        `;
  
        // Obtener el contenedor con el ID correspondiente
        let containerId = `news${index + 1}`;
        let container = document.getElementById(containerId);
  
        // Verificar si el contenedor está disponible antes de intentar agregar la noticia
        if (container) {
          container.appendChild(div);
        }
      });
    }).catch(error => {
      console.error('Error en la solicitud a la API:', error);
  
      // Puedes implementar lógica para manejar el error, como reintentar después de un tiempo
    });
  }
  
  document.addEventListener('DOMContentLoaded', function () {
    Api_con_axios();
  });
  