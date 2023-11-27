# mi_aplicacion/utils.py
import requests

def get_user_location(request):
    # Obtener la dirección IP del usuario
    ip_address = request.META.get('REMOTE_ADDR')

    # Puedes usar servicios como ipinfo.io para obtener la ubicación basada en la IP
    response = requests.get(f'https://ipinfo.io/{ip_address}?token=927f9002221769')
    data = response.json()

    # Obtener la latitud y longitud
    lat, lon = map(float, data['loc'].split(','))

    return lat, lon



def get_nearby_veterinaries(lat, lon):
    # Usar la API de Google Maps Geocoding o Mapbox para obtener lugares cercanos
    # Reemplaza 'TU_CLAVE_DE_API' con tu clave de API
    url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/veterinaria.json?access_token=sk.eyJ1IjoicGV0Y2FyZWFkbWluIiwiYSI6ImNscGg1cG9xdTAzem0ya3FzYnp6MDlxdjEifQ.6ECFVJfdow7bEebfuoslHg&proximity={lon},{lat}&types=poi'

    response = requests.get(url)
    data = response.json()

    # Procesar los resultados
    nearby_veterinaries = []
    for feature in data['features']:
        name = feature['text']
        address = feature['properties']['address']
        coordinates = feature['geometry']['coordinates']
        distance = feature['properties']['distance']

        nearby_veterinaries.append({
            'name': name,
            'address': address,
            'coordinates': coordinates,
            'distance': distance
        })

    return nearby_veterinaries