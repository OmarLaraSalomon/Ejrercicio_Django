from django.db import models

# Create your models here.

class Autores(models.Model):
    nombre = models.CharField(max_length=200)  
    fecha_nacimiento = models.DateField()  # tipo fecha

    def __str__(self):
        return self.nombre  # que me devuelva el nombre del autor



class Libros(models.Model):
    titulo = models.CharField(max_length=200) 
    autor = models.ForeignKey(Autores, on_delete=models.CASCADE)#relacion con autor por llave foranea
    fecha_publicacion = models.DateField()  # publicación del libro

    def __str__(self):
        return self.titulo  #me devulve el titulo 