from rest_framework import serializers
from api.models import Autor, Libro

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Libro
        fields = ('libro','editorial','autor','idAutor','nacionalidad','fechaHora_registro')

class AutorSerializer(serializers.ModelSerializer):
    libros = LibroSerializer(many=True, read_only=True, source='libro_set')
    class Meta:
        model=Autor
        fields = ('autor','nacionalidad','libros')