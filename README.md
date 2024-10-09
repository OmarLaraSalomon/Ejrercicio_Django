# 4.API

“Diseña una API simple con Django que permita realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en un recurso llamado ‘Tareas’. Proporciona los endpoints necesarios.”

### Requisitos:

    - Tener instalado **Python** en el equipo.
    - Tener instaladas las extensiones de **Django** y **Python** en VSCode.
    - Si necesitas actualizar el pip:

    ```bash
            python -m pip install -U pip
    ```

## Configuración del proyecto

    1. Crear el espacio de trabajo (carpeta).


    2. Comprobar la versión de Python *La versión 4 de Django pide mínimo Python 3.8*.

        ```bash
            python --version
        ```

    3. Instalar el módulo para crear entornos virtuales.

        ```bash
            pip install virtualenv
        ```

    4. Crear el entorno virtual.

        ```bash
            python -m venv venv
        ```

*Si estás trabajando con VSCode, presiona “f1” y escribe “Python interpreter”, da clic a esa opción y selecciona la versión de Python venv (tiene una estrella o aparecerá como la recomendada).*

*Es posible que ahora notes que el indicador del entorno virtual no se ha modificado, es decir, que está ausente o que sigues viendo un indicador existente como (base). No obstante, ten la seguridad de que el entorno sigue activado.*

    5. Instalar las dependencias.

        ```bash
                python -m pip install pipfile 
                python -m pip install pipenv
                pip install django
                pip install pylint
        ```

    6. Crear el proyecto de Django. *El “.” es para que ya no me cree otra carpeta extra*.

        ```bash
                 django-admin startproject  biblioteca .
        ```

    7. Correr el servidor para comprobar el levantamiento.

            ```bash
                python manage.py runserver
            ```

    8. Pegar la URL que nos da la terminal en el navegador.

            ```
            http://127.0.0.1:8000/

            ```

*Cancelar la terminal con “ctrl + c”.*


    9. Crear la aplicación.

        ```bash
             python manage.py startapp appBiblioteca
        ```

    10. Configurar la aplicación en el proyecto mediante el archivo `settings.py`:

        ```python
            INSTALLED_APPS = [
                "django.contrib.admin",
                "django.contrib.auth",
                "django.contrib.contenttypes",
                "django.contrib.sessions",
                "django.contrib.messages",
                "django.contrib.staticfiles",
                "appBiblioteca",
        ]
        ```

    11. Realizar las migraciones.

        ```bash
            python manage.py migrate
        ```


    12. Correr el servidor para comprobar el levantamiento.

        ```bash
            python manage.py runserver
        ```

    4. Pegar la URL que nos da la terminal en el navegador.
        ```
        http://127.0.0.1:8000/
        ```

*Cancelar la terminal con “ctrl + c”.*



## Modelo de Tarea

    1. Ingresar a la carpeta de la aplicación "appBiblioteca" y abrir el archivo `models.py`:

        ```python
           
           class Autores(models.Model):
                nombre = models.CharField(max_length=200)  
                fecha_nacimiento = models.DateField()  # tipo fecha

                def __str__(self):
                return self.nombre  # que me devuelva el nombre del autor



            class Libros(models.Model):
                titulo = models.CharField(max_length=200) 
                autor = models.ForeignKey(Autores, on_delete=models.CASCADE)
                fecha_publicacion = models.DateField()  # publicación del libro

                def __str__(self):  
                return self.titulo  #me devulve el titulo 
        ```


    2. Crear la tabla mediante las migraciones.

        ```bash
            python manage.py makemigrations 
        ```

    3. Aplicar la migración.

        ```bash
            python manage.py migrate
        ```

    4. Crear un superusuario para acceder al panel del administrador.

        ```bash
            python manage.py createsuperuser
        ```

        - Crear el nombre de usuario.
        - Añadir correo electrónico.
        - Crear la contraseña.
        - Repetir la contraseña.

*Si aparece "Bypass password validation and create user anyway? [y/N]" confirmar con “y”.*

    5. Añadir el modelo al panel de administrador mediante la carpeta de la aplicación "appBiblioteca" y abrir el archivo `admin.py`:

        ```python
            from django.contrib import admin
            from .models import Autores, Libros
        
            admin.site.register(Autores)
            admin.site.register(Libros)
        ```

    6. Comprobar los resultados corriendo el servidor.

        ```bash
            python manage.py runserver
        ```

    7. Pegar la URL que nos da la terminal en el navegador.

        ```
        http://127.0.0.1:8000/

        ```

    8. Acceder a la ruta del panel administrativo.

        ```
            http://127.0.0.1:8000/admin
        ```

*Ingresar los datos del superusuario que se creó. Se puede acceder a la tabla y crear tareas mediante ese panel.*

*Cancelar la terminal con “ctrl + c”.*


*Si quieres ingresar daatos primero llenar el modelo de autores y posterior el de libros*
