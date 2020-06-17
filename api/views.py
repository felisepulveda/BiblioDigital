from django.shortcuts import render
from rest_framework import viewsets
from api.models import Autor, Libro
from api.serializers import AutorSerializer, LibroSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def gestionAutor(request,id=None):
    if request.method == 'GET':
        autor = Autor.objects.filter(id=id)
        if autor: # Si el autor existe
            Au=Autor.objects.get(id=id)
            serializerAu = AutorSerializer(Au)
            return Response(serializerAu.data)
        else:
            if id is None:
                autor = Autor.objects.all()
                serializer = AutorSerializer(autor, many=True)
                return Response(serializer.data)
            else:
                mensaje="Este Autor no esta registrado en la base de datos."
                return Response({"Mensaje": mensaje},status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serializer=AutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        mensaje="Este autor ya esta registrado, o introdujo valores en los campos no adecuados."
        return Response({"Mensaje": mensaje},status=status.HTTP_400_BAD_REQUEST)   
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def gestionLibro(request):
    autor = Autor.objects.filter(autor=request.data['autor'],nacionalidad=request.data['nacionalidad'])
    if autor: # Si el autor existe, asocio el libro con el autor
        Au=Autor.objects.get(autor=request.data['autor'],nacionalidad=request.data['nacionalidad'])
        librodict={'libro':request.data['libro'],'editorial':request.data['editorial'],'idAutor':Au.id,'autor':request.data['autor'],'nacionalidad':request.data['nacionalidad']}
        serializer=LibroSerializer(data=librodict)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else: # Si autor no existe, debo agregarlo a la base de datos, y luego agrego el libro
        autordict={'autor': request.data['autor'],'nacionalidad': request.data['nacionalidad']}
        serializerAu=AutorSerializer(data=autordict)
        serializerLi=LibroSerializer(data=request.data)
        if serializerAu.is_valid():
            serializerAu.save()
            if serializerLi.is_valid():
                serializerLi.save()
                return Response(serializerLi.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializerLi.errors, status=status.HTTP_400_BAD_REQUEST)  
        else:
            return Response(serializerAu.errors, status=status.HTTP_400_BAD_REQUEST) 