

 // Función para realizar la búsqueda de libros
 function buscarLibros(query, maxResultados = 3) {
    const apiUrl = `https://www.googleapis.com/books/v1/volumes?q=${encodeURIComponent(query)}&maxResults=${maxResultados}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => mostrarResultados(data.items))
        .catch(error => console.error('Error al obtener datos:', error));
}

// Función para mostrar los resultados en la página
function mostrarResultados(libros) {
    const resultadosDiv = document.getElementById('resultados');

    // Limpiar resultados anteriores
    resultadosDiv.innerHTML = '';

    if (libros && libros.length > 0) {
        const listaLibros = document.createElement('ul');

        libros.forEach(libro => {
            const itemLibro = document.createElement('li');
            const titulo = document.createElement('h3');
            const portada = document.createElement('img');
            const descripcion = document.createElement('p');

            titulo.textContent = libro.volumeInfo.title;
            portada.src = libro.volumeInfo.imageLinks.thumbnail;
            portada.alt = 'Portada del libro';
            descripcion.textContent = libro.volumeInfo.description || 'Sin descripción disponible.';

            itemLibro.appendChild(titulo);
            itemLibro.appendChild(portada);
            itemLibro.appendChild(descripcion);

            listaLibros.appendChild(itemLibro);
        });

        resultadosDiv.appendChild(listaLibros);
    } else {
        resultadosDiv.innerHTML = '<p>No se encontraron resultados.</p>';
    }
}

// Función para realizar la búsqueda al hacer clic en el botón
function realizarBusqueda() {
    const inputBusqueda = document.getElementById('busqueda');
    const query = inputBusqueda.value.trim();

    if (query !== '') {
        buscarLibros(query);
    } else {
        alert('Ingrese un término de búsqueda válido.');
    }
}
