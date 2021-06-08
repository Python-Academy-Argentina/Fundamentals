# PAF CRUD API

##### Una simple API CRUD que hace de back end para Tuits.

## Configuración

Antes de ejecutarla, tenés que asegurarte de contar con todas las dependencias. Para eso podés ejecutar:

```bash
python -m pip install -r requirements.txt
```


O haciendo un entorno virtual (recomendado):

> Linux / MacOS

```bash
python -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
```

> Windows

```cmd
python -m venv env
env\Scripts\activate.bat
python -m pip install -r requirements.txt
```


Ahora vas a tener que decirle a Django que genere la base de datos donde se va a guardar la información, incluyendo sus tablas:

```bash
python manage.py makemigrations
python manage.py migrate
```


Crear un súper usuario (opcional):

```bash
python manage.py createsuperuser
```


## Ejecutar

Ya podés ejecutar tu API haciendo:

```bash
python manage.py runserver 0.0.0.0:8000
```

##### *Se recomienda usar ```0.0.0.0```, pero el puerto puede ser el que quieras.
##### **Podés usar ```nohup``` en Linux / MacOS.
