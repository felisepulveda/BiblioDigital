from django.db import models

# Create your models here.

class Autor(models.Model):
    autor=models.CharField(max_length=50,unique=True)
    nacionalidad=models.CharField(blank=False,max_length=40)

class Libro(models.Model):
    libro=models.CharField(max_length=50,blank=False)
    editorial=models.CharField(max_length=50,blank=False)
    idAutor=models.ForeignKey(Autor,on_delete=models.CASCADE)
    autor=models.CharField(max_length=50,blank=False)
    nacionalidad=models.CharField(max_length=50,blank=False)
    fechaHora_registro=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (('libro', 'autor'),)


