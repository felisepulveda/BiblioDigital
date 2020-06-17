from django.contrib import admin

# Register your models here.

from api.models import Autor,Libro

admin.site.register(Autor)
admin.site.register(Libro)
