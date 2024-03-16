from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):   # Esta función sirve para que dentro de admin se puedan ver los nombres de los proyectos.
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200) # Charfiel para textos no tan largos
    description = models.TextField() # TextField para textos largos
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # El on_delete=models.CASCADE es para que se elimine todo lo que tenga relación al proyecto, si se elimina el proyecto
    done = models.BooleanField(default=False)

    def __str__(self):  
        return self.title + " - " + self.project.name