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
            imageDiv.innerHTML = `
           
            <div class="op-post-cont-sm">
              <img class="op-post-img" src="${elemento.image}" alt="Bellota">
            </div>`;
            
            
            let contentDiv = document.createElement('div');
            contentDiv.classList.add('op-post-cont-xl');
            contentDiv.innerHTML = `
                <h1 class="op-post-title">${elemento.title}</h1>
                <h6 class="op-post-description">${elemento.description}</h6>
                <div class="op-post-barra"></div>
                <p class="op-post-text">${elemento.content}</p>
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



document.addEventListener("DOMContentLoaded", (event) => {
    console.log("DOM fully loaded and parsed");
    Swal.fire('SweetAlert2 is working!');
  });

Api_con_axios();
