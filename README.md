# Proyecto para modelos de autos

## Instalación
Descargar el repositorio con:

```
git clone https://github.com/fedemarkco/proyectoEGO.git
```
El proyecto se encuentra en un contenedor Docker, para poder levantarlo, se tiene que ejecutar:

```
cd proyectoEGO
docker-compose up
```

El contenedor fue configurado para que ejecute
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
```

También he puesto que cree un superusuario con los siguientes datos:
<br>Username: Marco
<br>Password: 1234
<br>Email: fedemarkco@gmail.com
 
Estos datos serán utilizados por el sitio de administración del proyecto. La cual se puede acceder con:
```
 http://127.0.0.1:8000/admin
```

El proyecto tiene tests que pueden ser ejecutados de la siguiente manera:
```
docker-compose run web pytest
```

Las APIs que se pueden utilizar son:

Para poder ver todas las fichas de modelos de los autos:
```
http://localhost:8000/api/model-sheet
```

Para un id (ejemplo de id 1) de una ficha de modelo:
```
http://localhost:8000/api/model-sheet/1
```

Para poder ver todos modelos de los autos:
```
http://localhost:8000/api/model-cars
```

Para ordenar los modelos de los autos por precio ascendente:
```
http://localhost:8000/api/model-cars?ordering=price
```

Para ordenar los modelos de los autos por precio descendente:
```
http://localhost:8000/api/model-cars?ordering=-price
```

Para ordenar los modelos de los autos de más nuevo primero:
```
http://localhost:8000/api/model-cars?ordering=-year
```

Para ordenar los modelos de los autos de más viejo primero:
```
http://localhost:8000/api/model-cars?ordering=year
```

Para filtrar los modelos de los autos:

Hay 3 valores posibles para colocar en type_car:
- Cars
- Pickups and Commercials
- SUVS and Crossovers

```
http://localhost:8000/api/model-cars?type_car=Cars
http://localhost:8000/api/model-cars?type_car=Pickups and Commercials
http://localhost:8000/api/model-cars?type_car=SUVS and Crossovers
```


Nota: Para el estilo del código he utilizado flake8 y también he utilizado isort.
