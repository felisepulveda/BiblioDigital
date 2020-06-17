# BiblioDigital

## Preparación ambiente de trabajo, todo fue realizado en windows 10
Paquetes necesarios

- virtualenv 16.1.0
- virtualenvwrapper-win 1.2.5
- psycopg2 2.8.5  
- Django 3.0.7  
- djangorestframework 3.11.0 
- coverage 5.1 
- django-nose 1.4.6 

Ahora, instalamos Python 3.6.2, abrimos una terminal, e instalamos los siguientes paquetes
- pip install virtualenv==16.1.0
- pip install virtualenvwrapper-win==1.2.5

Luego en la misma terminal, escribimos lo siguiente
- 'mkvirtualenv BiblioDigital'  (Acá creas el ambiente virtual llamado 'BiblioDigital', e ingresas a él automáticamente)

Crea una carpeta con el mismo nombre del ambiente, es decir, 'BiblioDigital', e ingresa a ella en tu terminal y escribe lo siguiente
- 'setprojectdir .' (ahora cada vez que ingresemos a nuestro ambiente, nos dirigira a la carpeta 'BiblioDigital')
- 'workon BiblioDigital' (para ingresar al ambiente, 'deactivate' es para salir)

Clonamos mi repositorio dentro de 'BiblioDigital', y nos situamos al mismo nivel del archivo manage.py dentro de nuestra cmd.

Ahora instalamos paquetes de python con el comando
- pip install -r requerimientos.txt 

## Sistema de gestión de base de datos
Usamos postgresql como nuestro sistema de base de datos, por tanto, debe 
1) Abrir postgresql, y crear su base de datos con 'el nombre que quiera'
2) Se debe configurar en el archivo settings.py del proyecto los valores 
<pre>
- DATABASES = {        
    'default': {     
        'ENGINE': 'django.db.backends.postgresql_psycopg2',    
        'NAME': 'el nombre que quiera', # Nombre de la base de datos    
	'TEST': {
            'NAME': 'coverage_test_bibliodigital',   # Nombre de la base de datos para nuestros testeos
        },
        'USER': 'postgres',	# Aca      
        'PASSWORD': 'root',     # Aca        
        'HOST': 'localhost',	# Dependiendo en que servidor se almacena su sistema de gestion de base de datos     
        'DATABASE': '5432',	# El puerto del servidor    
    }       
}         
</pre>
## Ejecución Proyecto
Para ejecutar nuestro proyecto BiblioDigital, escribimos los siguientes comandos en nuestro ambiente 'BiblioDigital' (al mismo nivel archivo manage.py)
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser (Creamos a Apiux con todos los permisos, aunque se puede cambiar en caso de asi desearlo)
[username: Apiux, email: 'xxx@gmail.com', password: bibliotecadigital] 

Luego, en nuestro ambiente virtual 'BiblioDigita' escribimos
- python manage.py runserver

## Credenciales para BiblioDigital (django/admin)
- Username: Apiux
- Password: bibliotecadigital

## Pruebas 
Para generar un reporte, escribir (viene integrado django-nose y coverage):

- coverage run --branch --source=api ./manage.py test (ejecuta las pruebas unitarias)
- coverage report (muestra el reporte por consola)
- coverage html -d coverage-report (crea 'coverage-report' dentro del proyecto, y podemos acceder a 'index.html' para ver con detalle las pruebas)


## Explicación
Todos los link dados en las instrucciones de la prueba se cumplen:

- http://127.0.0.1:8000/api/autor/  -> muestra todos los autores con sus libros, además del textbox para incluir peticion post 
- http://127.0.0.1:8000/api/autor/1 -> muestra el autor con el id 1, con todos sus libros, además del textbox para incluir peticion post 
- http://127.0.0.1:8000/api/libro/ -> muestra el textbox para incluir peticion post, método get esta desactivado 
- Abajo se muestra la estructura de los json tanto para autor como libro.
- Puede ingresar a django/admin para ingresar datos mas facilmente con las credenciales dadas más arriba.
- Recalcar que el json de libro necesita la nacionalidad del autor, ya que en caso de que este no este registrado,
debe registrar primero el autor y luego el libro, si el autor esta registrado (coincidir tanto autor como nacionalidad),
entonces simplemente registra el libro. Cualquier error, se mostrara un mensaje en pantalla explicando que sucedio.
- Además, se incluye el modelo entidad relación dentro de la carpeta MER.

<pre>

- Json Autor
{
"autor": "tolkien",
"nacionalidad": "chileno"
}

- Json Libro
{
"libro": "el señor de las casas",
"editorial": "la comarca",
"autor": "tolkien",
"nacionalidad": "chileno"
}

</pre>

Autocritica
- Podria haber testeado mas, pero dado las restricciones de tiempo, solo alcance a testear los modelos, y no las vistas.