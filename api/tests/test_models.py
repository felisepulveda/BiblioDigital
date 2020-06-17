from __future__ import unicode_literals

from django.test import TestCase

from api.models import Autor, Libro


class AutorTest(TestCase):
   

    def test_autor_create(self):
        

        autor = Autor.objects.create(
            autor = 'Dan Brown',
            nacionalidad = 'EEUU'
        )

        self.assertEqual(autor.autor,"Dan Brown")
        self.assertEqual(autor.nacionalidad,"EEUU")
        self.assertEqual(autor.id,1)

    def test_autor_delete(self):

        autor = Autor.objects.create(
            autor = 'Dan Brown',
            nacionalidad = 'EEUU'
        )

        autor.delete()

        self.assertEqual(Autor.objects.count(),0)

class LibroTest(TestCase):
   

    def test_libro_create(self):
        
        autor = Autor.objects.create(
            autor = 'Tolkien',
            nacionalidad = 'Chilena'
        )

        A = Autor.objects.get(autor="Tolkien") 

        libro = Libro.objects.create(
            libro = 'El señor de los anillos',
            editorial = 'casa',
            idAutor = A,
            autor = 'Tolkien',
            nacionalidad = 'Chilena',
        )

        self.assertEqual(libro.libro,"El señor de los anillos")
        self.assertEqual(libro.editorial,"casa")
        self.assertEqual(libro.autor,"Tolkien")
        self.assertEqual(libro.nacionalidad,"Chilena")

    def test_libro_delete(self):

        autor = Autor.objects.create(
            autor = 'Tolkien',
            nacionalidad = 'Chilena'
        )

        A = Autor.objects.get(autor="Tolkien") 

        libro = Libro.objects.create(
            libro = 'El señor de los anillos',
            editorial = 'casa',
            idAutor = A,
            autor = 'Tolkien',
            nacionalidad = 'Chilena',
        )

        autor.delete()

        self.assertEqual(Autor.objects.count(),0)
        self.assertEqual(Libro.objects.count(),0)
        

    