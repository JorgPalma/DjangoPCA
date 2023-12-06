let noti = document.getElementById('news');

function Api_con_axios() {
    axios({
        method: 'GET',
        url: 'https://gnews.io/api/v4/search?q=perros&country=es&apikey=623369ee5fa721da983d130d2a836c6b'
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

var main = document.querySelector('#name');
var temp = document.querySelector('.temp');
var desc = document.querySelector('.desc');
var clouds = document.querySelector('.clouds');



fetch('https://api.openweathermap.org/data/2.5/weather?q=Santiago,cl&appid=92193a0bddde1d5ebcc9787c63185f53&lang=sp')
.then(response => response.json())
.then(data => {
  var tempValue = ((data['main']['temp'])-268.2).toFixed(1);
  var nameValue = data['name'];
  var descValue = data['weather'][0]['description'];

  main.innerHTML = nameValue;
  desc.innerHTML = "Actualmente hay: "+descValue;
  temp.innerHTML = "Temperatura - "+tempValue+"°C";

})


Api_con_axios();
