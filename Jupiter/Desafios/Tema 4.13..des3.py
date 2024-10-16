
"""Desafío 3:
Crea una clase Libro que tenga atributos específicos como título, autor, 
editorial, y año_publicación."""

# Clase Libro

class Libro:
    def __init__(self, titulo, autor, editorial, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.año_publicacion = año_publicacion

    def mostrar_datos(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Editorial:", self.editorial)
        print("Año de publicación:", self.año_publicacion)

# Prueba de la clase Libro

libro = Libro("El Quijote de la Mancha", "J.U. Salazar", "Editorial Cortazar", 1605)
libro.mostrar_datos()


