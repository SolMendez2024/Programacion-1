
"""Desafío 1: 
Crea una clase Libro que tenga atributos privados para el título, autor y ISBN. 
Proporciona métodos getter y setter para cada atributo."""

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

    # Getters
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_isbn(self):
        return self.__isbn

    # Setters
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def set_isbn(self, isbn):
        self.__isbn = isbn

"""Estos métodos permiten leer (getter) o  modificar (setter) los valores 
 de los atributos privados desde fuera de la clase."""

# Crear instancias de la clase Libro
libro1 = Libro("El Quijote", "Miguel de Cervantes", "978-3-16-148410-0")

# Obtener valores utilizando getters
print(libro1.get_titulo())  # "El Quijote"
print(libro1.get_autor())   # "Miguel de Cervantes"
print(libro1.get_isbn())    # "978-3-16-148410-0"

# Modificar valores utilizando setters
libro1.set_titulo("Don Quijote de la Mancha")
print(libro1.get_titulo())  # "Don Quijote de la Mancha"


