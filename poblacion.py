
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PetCareAnalytics.settings")
import django
django.setup()
from django.contrib.auth.models import User
from core.models import Persona, Raza, Mascota

def poblar_db():
    # Poblar la tabla Usuario (COMENTAR CODIGO 'CTRL+K+C')
    # user1 = User.objects.create_user('acarnaman0', 'jproudlove0@ft.com', 'rF27123s?#o')
    # user2 = User.objects.create_user('wfullilove1', 'wwoodthorpe1@unicef.org', 'kV4123P&Lhp')
    # user3 = User.objects.create_user('mwright2', 'cnorthcliffe2@sciencedaily.com', 'c123C213l')
    # user4 = User.objects.create_user('ckiloh3', 'ahealeas3@vinaora.com', 'uH954688bV6SlI')
    # user5 = User.objects.create_user('dleechman4', 'paspling4@comcast.net', 'tV7Pj4kE%zy')
    # user6 = User.objects.create_user('mmulcahy5', 'cleverett5@washingost.com', 'mS9!uD54654Rl1?y')
    # user7 = User.objects.create_user('npenhalluck6', 'mhugo6@japanpost.jp', 'dQ1unBI')
    # user8 = User.objects.create_user('alancaster7', 'pangliss7@w3.org', 'nS8%4=Fj115588')
    # user9 = User.objects.create_user('sthurlow8', 'jpauls8@icio.us', 'gI1115VLAx.j5TRI8z')
    # user10 = User.objects.create_user('aivanishchev9', 'wscurrah9@nymag.com', 'iB4555YY#MZ')
    # user11 = User.objects.create_user('ndekeepa', 'aoughtrighta@vistaprint.com', 'rL6%54477wbe')
    # user12 = User.objects.create_user('egruszczakb', 'egligoracib@feedburner.com', 'eX9>cBtM')
    # user13 = User.objects.create_user('tmeiklejohnc', 'bczaplec@spotify.com', 'nN0*1454RA@')
    
    # Persona.objects.create(nombre_usuario=user1, rut=20442076, digito_ver=8, primer_nombre="Bancroft", segundo_nombre="Woodrow", apellido_pat="Vidineev", apellido_mate="Heitz", telefono=972476108, edad=25, imagen=None, dinamico="")
    # Persona.objects.create(nombre_usuario=user2, rut=10005933, digito_ver=7, primer_nombre="Querida", segundo_nombre="Daphna", apellido_pat="Monelli", apellido_mate="Effnert", telefono=972476108, edad=25, imagen=None, dinamico="")
    # Persona.objects.create(nombre_usuario=user3, rut=26331288, digito_ver=5, primer_nombre="Gerda", segundo_nombre="Emanuel", apellido_pat="Heale", apellido_mate="Gowthorpe", telefono=972476108, edad=25, imagen=None, dinamico="")
    # Persona.objects.create(nombre_usuario=user4, rut=7290086, digito_ver=7, primer_nombre="Leilah", segundo_nombre="Sawyere", apellido_pat="Diver", apellido_mate="Esom", telefono=972476108, edad=25, imagen=None, dinamico="")
    # Persona.objects.create(nombre_usuario=user5, rut=13744889, digito_ver=6, primer_nombre="Sisely", segundo_nombre="Diann", apellido_pat="Kristiansen", apellido_mate="Estabrook", telefono=972476108, edad=25, imagen=None, dinamico="")
    # Persona.objects.create(nombre_usuario=user6, rut=12671158, digito_ver=3, primer_nombre="Danny", segundo_nombre="Melina", apellido_pat="Manterfield", apellido_mate="Bendel", telefono=972476108, edad=25, imagen=None, dinamico="")
    # Persona.objects.create(nombre_usuario=user7, rut=27833713, digito_ver=4, primer_nombre="Jeremias", segundo_nombre="Fianna", apellido_pat="Sindell", apellido_mate="Rosenzveig", telefono=972476108, edad=25, imagen=None, dinamico="")
    # Persona.objects.create(nombre_usuario=user8, rut=21836918, digito_ver=5, primer_nombre="Cassondra", segundo_nombre="Paolo", apellido_pat="Macveigh", apellido_mate="Riddlesden", telefono=972476108, edad=25, imagen=None, dinamico="")
    # Persona.objects.create(nombre_usuario=user9, rut=17991933, digito_ver=9, primer_nombre="Francine", segundo_nombre="Marjory", apellido_pat="Frow", apellido_mate="Bodocs", telefono=972476108, edad=25, imagen=None, dinamico="")
    # Persona.objects.create(nombre_usuario=user10, rut=26173736, digito_ver=5, primer_nombre="Stinky", segundo_nombre="Bendicty", apellido_pat="Geddes", apellido_mate="Troubridge", telefono=972476108, edad=25, imagen=None, dinamico="")
    # Persona.objects.create(nombre_usuario=user11, rut=6941715, digito_ver=1, primer_nombre="Ariadne", segundo_nombre="Elmore", apellido_pat="Heape", apellido_mate="Bavidge", telefono=972476108, edad=25, imagen=None, dinamico="")
    # Persona.objects.create(nombre_usuario=user12, rut=24282881, digito_ver=3, primer_nombre="Kristin", segundo_nombre="Paolo", apellido_pat="Sweedland", apellido_mate="Messiter", telefono=972476108, edad=25, imagen=None, dinamico="")
    # Persona.objects.create(nombre_usuario=user13, rut=11064590, digito_ver=1, primer_nombre="Kathie", segundo_nombre="Caron", apellido_pat="Redit", apellido_mate="Luffman", telefono=972476108, edad=25, imagen=None, dinamico="")
    
    # Raza.objects.create(nombre_raza="Siamés")
    # Raza.objects.create(nombre_raza="Maine Coon")
    # Raza.objects.create(nombre_raza="Esfinge")
    # Raza.objects.create(nombre_raza="Bengalí")
    # Raza.objects.create(nombre_raza="Exótico Pelo Corto")
    # Raza.objects.create(nombre_raza="British Shorthair")
    # Raza.objects.create(nombre_raza="Mestizo")
    # Raza.objects.create(nombre_raza="Poodle o caniche")
    # Raza.objects.create(nombre_raza="Pastor alemán")
    # Raza.objects.create(nombre_raza="Yorkshire")
    # Raza.objects.create(nombre_raza="Fox terrier")
    # Raza.objects.create(nombre_raza="Beagle")
    # Raza.objects.create(nombre_raza="Labrador retriever")
    # Raza.objects.create(nombre_raza="Golden retriever")
    # Raza.objects.create(nombre_raza="Pug")
    # Raza.objects.create(nombre_raza="Bulldog")
    # Raza.objects.create(nombre_raza="Quiltro")

    #Mascota.objects.create(User.objects.get(username='deffnert1'), vacunas=2, ac_fisica=) 






poblar_db()