$.ajax({
    url: 'https://api.mediastack.com/v1/news',
    data: {
        access_key: '719be09b2bf0dcfd899ce97aaf74601b',
        languages: 'es',
        countries: 'us',
        limit: 30,
        offset: 30,
    },
    success: function(data) {
        console.log('Datos recibidos:', data);
    },
    error: function(xhr, status, error) {
        console.error('Error en la solicitud:', status, error);
        console.log(xhr.responseText); // Puede proporcionar más detalles del error
    }
});
