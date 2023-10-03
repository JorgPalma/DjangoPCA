/*let noti = document.getElementById('news');

function  Api_con_axios(){
    axios({
        method: 'GET',
        url: 'https://gnews.io/api/v4/search?q=animal&country=es&apikey=5d4c96acf6f182b045ac8bcaee0ee580'
        5d4c96acf6f182b045ac8bcaee0ee580 
    }).then(res => {
        let noticias = res.data.articles;
        console.log(noticias);
        noticias.map((elemento)=>{
            let div = document.createElement('div');
            div.innerHTML = 
            `<img style= 'max-width:600px'src=${elemento.image}
            <br>
            <h1>${elemento.title}</h1>
            <h3>${elemento.description}</h3>
            <h3>${elemento.content}</h3>           
            <h3>${elemento.publishedAt}</h3>
            <h3>${elemento.source.name}</h3>
            <a href=${elemento.url}>Seguir leyendo</a>`;
            
            noti.appendChild(div);
        })
    })
}
*/

let noti = document.getElementById('news');

function  Api_con_axios(){
    axios({
        method: 'GET',
        url: 'https://gnews.io/api/v4/search?q=animal&country=es&apikey=5d4c96acf6f182b045ac8bcaee0ee580'
        /*5d4c96acf6f182b045ac8bcaee0ee580 */
    }).then(res => {
        let noticias = res.data.articles;
        console.log(noticias);
        noticias.map((elemento)=>{
            let div = document.createElement('div');
            div.innerHTML = 
            `<div class="op-post-cont-sm">
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

        noti.appendChild(div);
    })
})
}

Api_con_axios();

