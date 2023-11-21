# Python 3
import http.client, urllib.parse
from django.shortcuts import render  # Asumiendo que estás utilizando Django

def obtener_noticias(request):
    conn = http.client.HTTPConnection('api.mediastack.com')

    params = urllib.parse.urlencode({
        'access_key': '541f6179f9ff7f91c3e9b91f7164e79e',
        'categories': '-general,-sports',
        'sort': 'published_desc',
        'limit': 10,
    })

    conn.request('GET', '/v1/news?{}'.format(params))

    res = conn.getresponse()
    data = res.read()

    noticias = data.decode('utf-8')

    return render(request, 'test.html', {'noticias': noticias})
