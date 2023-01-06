# api-tribalw

Se debe desarrollar un API RESTful que contenga un único endpoint el cual retorne un array con un rango definido de 25 objetos, diferentes 
unos de otros, es decir no debe existir ningún objeto que contenga el mismo id.
Los objetos serán obtenidos de un API de terceros, teniendo como restricción consumir estrictamente el siguiente endpoint:
https://api.chucknorris.io/jokes/random


## Requerimientos
 - python 3.10
 - django 4.1.5
 - djangorestframework 3.14.0
 - requests 2.28.1


## instrucciones
 - clonar el repositorio
 - crear un entorno virtual, si no lo tienes instalado puedes hacerlo con el siguiente comando:
    - `pip install virtualenv`
 - si lo tiene solo es activarlo con el siguiente comando:
    - `source venv/bin/activate`

- instalar las dependencias con el siguiente comando:
    - `pip install -r requirements.txt`

- arrancar el servidor con el siguiente comando:
    - `python manage.py runserver`

- para acceder a la api se debe hacer con el siguiente endpoint:
http://127.0.0.1:8000/api/chucknorris/


        

