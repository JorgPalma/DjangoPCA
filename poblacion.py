
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PetCareAnalytics.settings")
import django
django.setup()
from django.contrib.auth.models import User
from core.models import Persona, Raza, Mascota, Animal, Alergia, Formulario

def poblar_db():
    # Poblar la tabla Usuario (COMENTAR CODIGO 'CTRL+K+C')(DESCOMENTAR 'CTRL+K+U')
    user1 = User.objects.create_user('acarnaman0', 'jproudlove0@ft.com', 'rF27123s?#o')
    user2 = User.objects.create_user('wfullilove1', 'wwoodthorpe1@unicef.org', 'kV4123P&Lhp')
    user3 = User.objects.create_user('mwright2', 'cnorthcliffe2@sciencedaily.com', 'c123C213l')
    user4 = User.objects.create_user('ckiloh3', 'ahealeas3@vinaora.com', 'uH954688bV6SlI')
    user5 = User.objects.create_user('dleechman4', 'paspling4@comcast.net', 'tV7Pj4kE%zy')
    user6 = User.objects.create_user('mmulcahy5', 'cleverett5@washingost.com', 'mS9!uD54654Rl1?y')
    user7 = User.objects.create_user('npenhalluck6', 'mhugo6@japanpost.jp', 'dQ1unBI')
    user8 = User.objects.create_user('alancaster7', 'pangliss7@w3.org', 'nS8%4=Fj115588')
    user9 = User.objects.create_user('sthurlow8', 'jpauls8@icio.us', 'gI1115VLAx.j5TRI8z')
    user10 = User.objects.create_user('aivanishchev9', 'wscurrah9@nymag.com', 'iB4555YY#MZ')
    user11 = User.objects.create_user('ndekeepa', 'aoughtrighta@vistaprint.com', 'rL6%54477wbe')
    user12 = User.objects.create_user('egruszczakb', 'egligoracib@feedburner.com', 'eX9>cBtM')
    user13 = User.objects.create_user('tmeiklejohnc', 'bczaplec@spotify.com', 'nN0*1454RA@')
    
    Persona.objects.create(nombre_usuario=user1, rut=20442076, digito_ver=8, primer_nombre="Bancroft", segundo_nombre="Woodrow", apellido_pat="Vidineev", apellido_mate="Heitz", telefono=972476108, edad=25, dinamico="asdfghj")
    Persona.objects.create(nombre_usuario=user2, rut=10005933, digito_ver=7, primer_nombre="Querida", segundo_nombre="Daphna", apellido_pat="Monelli", apellido_mate="Effnert", telefono=972476108, edad=25, dinamico="lkjfisnfcvhba")
    Persona.objects.create(nombre_usuario=user3, rut=26331288, digito_ver=5, primer_nombre="Gerda", segundo_nombre="Emanuel", apellido_pat="Heale", apellido_mate="Gowthorpe", telefono=972476108, edad=25, dinamico="hurohuiaskjnfbjk")
    Persona.objects.create(nombre_usuario=user4, rut=7290086, digito_ver=7, primer_nombre="Leilah", segundo_nombre="Sawyere", apellido_pat="Diver", apellido_mate="Esom", telefono=972476108, edad=25, dinamico="g1d456afg156as894")
    Persona.objects.create(nombre_usuario=user5, rut=13744889, digito_ver=6, primer_nombre="Sisely", segundo_nombre="Diann", apellido_pat="Kristiansen", apellido_mate="Estabrook", telefono=972476108, edad=25, dinamico="gasd89f7asf789")
    Persona.objects.create(nombre_usuario=user6, rut=12671158, digito_ver=3, primer_nombre="Danny", segundo_nombre="Melina", apellido_pat="Manterfield", apellido_mate="Bendel", telefono=972476108, edad=25, dinamico="fbdbsa1f23as84")
    Persona.objects.create(nombre_usuario=user7, rut=27833713, digito_ver=4, primer_nombre="Jeremias", segundo_nombre="Fianna", apellido_pat="Sindell", apellido_mate="Rosenzveig", telefono=972476108, edad=25, dinamico="asfefgqcfdq1187")
    Persona.objects.create(nombre_usuario=user8, rut=21836918, digito_ver=5, primer_nombre="Cassondra", segundo_nombre="Paolo", apellido_pat="Macveigh", apellido_mate="Riddlesden", telefono=972476108, edad=25, dinamico="asf51as1v2a546")
    Persona.objects.create(nombre_usuario=user9, rut=17991933, digito_ver=9, primer_nombre="Francine", segundo_nombre="Marjory", apellido_pat="Frow", apellido_mate="Bodocs", telefono=972476108, edad=25, dinamico="bnvnrtn45re456894")
    Persona.objects.create(nombre_usuario=user10, rut=26173736, digito_ver=5, primer_nombre="Stinky", segundo_nombre="Bendicty", apellido_pat="Geddes", apellido_mate="Troubridge", telefono=972476108, edad=25, dinamico="dsafgsdgbg89f")
    Persona.objects.create(nombre_usuario=user11, rut=6941715, digito_ver=1, primer_nombre="Ariadne", segundo_nombre="Elmore", apellido_pat="Heape", apellido_mate="Bavidge", telefono=972476108, edad=25, dinamico="dv894as897qf9asg")
    Persona.objects.create(nombre_usuario=user12, rut=24282881, digito_ver=3, primer_nombre="Kristin", segundo_nombre="Paolo", apellido_pat="Sweedland", apellido_mate="Messiter", telefono=972476108, edad=25, dinamico="a15v15a897asf")
    Persona.objects.create(nombre_usuario=user13, rut=11064590, digito_ver=1, primer_nombre="Kathie", segundo_nombre="Caron", apellido_pat="Redit", apellido_mate="Luffman", telefono=972476108, edad=25, dinamico="asgv211gv89q4f8")
    

    perro = Animal.objects.create(nombre_animal="Perro")
    gato = Animal.objects.create(nombre_animal="Gato")

    Raza.objects.create(animal = gato, nombre_raza="Siamés")
    Raza.objects.create(animal = gato, nombre_raza="Maine Coon")
    Esfinge=Raza.objects.create(animal = gato, nombre_raza="Esfinge")
    Raza.objects.create(animal = gato, nombre_raza="Bengalí")
    Raza.objects.create(animal = gato, nombre_raza="Exótico Pelo Corto")
    British=Raza.objects.create(animal = gato, nombre_raza="British Shorthair")
    Mestizo=Raza.objects.create(animal = perro, nombre_raza="Mestizo")
    Raza.objects.create(animal = perro, nombre_raza="Poodle o caniche")
    Pastor=Raza.objects.create(animal = perro, nombre_raza="Pastor alemán")
    Yorkshire=Raza.objects.create(animal = perro, nombre_raza="Yorkshire")
    Raza.objects.create(animal = perro, nombre_raza="Fox terrier")
    Beagle=Raza.objects.create(animal = perro, nombre_raza="Beagle")
    Raza.objects.create(animal = perro, nombre_raza="Labrador retriever")
    Golden=Raza.objects.create(animal = perro, nombre_raza="Golden retriever")
    Pug=Raza.objects.create(animal = perro, nombre_raza="Pug")
    Raza.objects.create(animal = perro, nombre_raza="Bulldog")
    Quiltro=Raza.objects.create(animal = perro, nombre_raza="Quiltro")


    Mascota.objects.create(nombre_usuario=user1, nombre_masc="Cachupin", sexo='M', anio_nac=2010, raza=Esfinge)
    Mascota.objects.create(nombre_usuario=user2, nombre_masc="Pelet", sexo='H', anio_nac=2013, raza=Esfinge)
    Mascota.objects.create(nombre_usuario=user3, nombre_masc="Rodilla", sexo='H', anio_nac=2013, raza=British)
    Mascota.objects.create(nombre_usuario=user4, nombre_masc="Sanhueza", sexo='M', anio_nac=2014, raza=Pastor)
    Mascota.objects.create(nombre_usuario=user5, nombre_masc="Calulemelendes", sexo='M', anio_nac=2019, raza=Yorkshire)
    Mascota.objects.create(nombre_usuario=user6, nombre_masc="Boby", sexo='M', anio_nac=2020, raza=Beagle)
    Mascota.objects.create(nombre_usuario=user7, nombre_masc="Duff", sexo='H', anio_nac=2011, raza=Golden)
    Mascota.objects.create(nombre_usuario=user8, nombre_masc="AIDS", sexo='M', anio_nac=2009, raza=Quiltro)
    Mascota.objects.create(nombre_usuario=user9, nombre_masc="Farol", sexo='H', anio_nac=2012, raza=Pug)
    Mascota.objects.create(nombre_usuario=user10, nombre_masc="Chiquitinkaku", sexo='M', anio_nac=2013, raza=Mestizo)
    Mascota.objects.create(nombre_usuario=user11, nombre_masc="Maria", sexo='H', anio_nac=2017, raza=Pug)
    Mascota.objects.create(nombre_usuario=user12, nombre_masc="Sable", sexo='H', anio_nac=2015, raza=Pug)
    Mascota.objects.create(nombre_usuario=user13, nombre_masc="Tongo", sexo='M', anio_nac=2021, raza=Pug)
    


    

    Alergia.objects.create(tipo_alergia="N/A")
    Alergia.objects.create(tipo_alergia="Orina")
    Alergia.objects.create(tipo_alergia="Caspa")
    Alergia.objects.create(tipo_alergia="Saliva")
    Alergia.objects.create(tipo_alergia="Alimentaria")
    Alergia.objects.create(tipo_alergia="Ambiental")
    Alergia.objects.create(tipo_alergia="Picadura")
    Alergia.objects.create(tipo_alergia="Medicamento")
    Alergia.objects.create(tipo_alergia="Producto quimico")


    Formulario.objects.create(nombre_usuario=User.objects.get(id=1), mascota=Mascota.objects.get(id=1), alergia=Alergia.objects.get(id=1), act_fisica="S", sintomas="NO", antec_enfermedades="NO", edad=8, tamanio=972476108, peso=25, operaciones=1, comida_tiempo=25, num_vacunas=1)
    Formulario.objects.create(nombre_usuario=User.objects.get(id=2), mascota=Mascota.objects.get(id=2), alergia=Alergia.objects.get(id=1), act_fisica="S", sintomas="NO", antec_enfermedades="NO", edad=7, tamanio=972476108, peso=25, operaciones=0, comida_tiempo=25, num_vacunas=1)
    Formulario.objects.create(nombre_usuario=User.objects.get(id=3), mascota=Mascota.objects.get(id=3), alergia=Alergia.objects.get(id=3), act_fisica="S", sintomas="Tiene mucho dolor", antec_enfermedades="NO", edad=9, tamanio=972476108, peso=25, operaciones=2, comida_tiempo=25, num_vacunas=1)
    Formulario.objects.create(nombre_usuario=User.objects.get(id=4), mascota=Mascota.objects.get(id=4), alergia=Alergia.objects.get(id=1), act_fisica="N", sintomas="NO", antec_enfermedades="NO", edad=2, tamanio=972476108, peso=25, operaciones=2, comida_tiempo=25, num_vacunas=1)
    Formulario.objects.create(nombre_usuario=User.objects.get(id=5), mascota=Mascota.objects.get(id=5), alergia=Alergia.objects.get(id=1), act_fisica="N", sintomas="NO", antec_enfermedades="NO", edad=3, tamanio=972476108, peso=25, operaciones=3, comida_tiempo=25, num_vacunas=1)
    Formulario.objects.create(nombre_usuario=User.objects.get(id=6), mascota=Mascota.objects.get(id=6), alergia=Alergia.objects.get(id=1), act_fisica="S", sintomas="NO", antec_enfermedades="NO", edad=5, tamanio=972476108, peso=25, operaciones=5, comida_tiempo=25, num_vacunas=1)
    Formulario.objects.create(nombre_usuario=User.objects.get(id=7), mascota=Mascota.objects.get(id=7), alergia=Alergia.objects.get(id=7), act_fisica="N", sintomas="Tiene mucho dolor", antec_enfermedades="NO", edad=5, tamanio=972476108, peso=25, operaciones=1, comida_tiempo=25, num_vacunas=1)
    Formulario.objects.create(nombre_usuario=User.objects.get(id=8), mascota=Mascota.objects.get(id=8), alergia=Alergia.objects.get(id=7), act_fisica="S", sintomas="Se le hincho la cara", antec_enfermedades="NO", edad=6, tamanio=972476108, peso=25, operaciones=1, comida_tiempo=25, num_vacunas=1)
    Formulario.objects.create(nombre_usuario=User.objects.get(id=9), mascota=Mascota.objects.get(id=9), alergia=Alergia.objects.get(id=1), act_fisica="N", sintomas="NO", antec_enfermedades="NO", edad=7, tamanio=972476108, peso=25, operaciones=1, comida_tiempo=25, num_vacunas=1)
    Formulario.objects.create(nombre_usuario=User.objects.get(id=10), mascota=Mascota.objects.get(id=10), alergia=Alergia.objects.get(id=7), act_fisica="S", sintomas="Tiene mucho dolor", antec_enfermedades="NO", edad=8, tamanio=972476108, peso=25, operaciones=0, comida_tiempo=25, num_vacunas=1)
    Formulario.objects.create(nombre_usuario=User.objects.get(id=11), mascota=Mascota.objects.get(id=11), alergia=Alergia.objects.get(id=4), act_fisica="N", sintomas="Se le hincho la cara", antec_enfermedades="NO", edad=4, tamanio=972476108, peso=25, operaciones=0, comida_tiempo=25, num_vacunas=1)
    Formulario.objects.create(nombre_usuario=User.objects.get(id=12), mascota=Mascota.objects.get(id=12), alergia=Alergia.objects.get(id=2), act_fisica="N", sintomas="Tiene mucho dolor", antec_enfermedades="NO", edad=4, tamanio=972476108, peso=25, operaciones=1, comida_tiempo=25, num_vacunas=1)
    Formulario.objects.create(nombre_usuario=User.objects.get(id=13), mascota=Mascota.objects.get(id=13), alergia=Alergia.objects.get(id=1), act_fisica="S", sintomas="NO", antec_enfermedades="NO", edad=5, tamanio=972476108, peso=25, operaciones=1, comida_tiempo=25, num_vacunas=1)
    
    
    # print(Mascota.objects.get(id=1))
    
    # formulariomodel= Formulario.objects.all()

    # mascotamodel= Mascota.objects.all()
    # # Listas para almacenar los datos del archivo CSV
    # vacunas = []
    # comida_tiempo = []

    # labels = ['H','M']
    # sexo = []
    
    # contador_H = 0
    # contador_M = 0

    

    # for c in formulariomodel:
    #     comida_tiempo.append(c.comida_tiempo)
    #     vacunas.append(c.id)
    
    # for mas in mascotamodel:
    #     if mas.sexo == 'H':
    #         contador_H += 1
    #     elif mas.sexo == 'M':
    #         contador_M += 1
        
    # sexo.append(contador_H)
    # sexo.append(contador_M)
    #     # jk = 0
    #     # kj = 0
    #     # if mas.sexo == "H":
    #     #     jk=jk+1
    #     #     sexo[0]=sexo[0]+jk
    #     # if mas.sexo == "M":
    #     #     kj = kj+1
    #     #     sexo[1]=sexo[1]+kj


    # print(sexo)

poblar_db()