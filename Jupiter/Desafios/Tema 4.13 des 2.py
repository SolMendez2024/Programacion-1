"""Desafío 2:
Modifica la clase Autor para que pueda tener una lista de libros escritos por el autor. 
Proporciona un método para agregar libros a esta lista."""


class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

class Autor:
    def __init__(self, nombre, nacionalidad):
        # Atributos privados: nombre y nacionalidad del autor
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        # Lista de libros escritos por el autor
        self.__libros = []

    # Método para agregar libros a la lista de libros del autor
    def agregar_libro(self, libro):
        self.__libros.append(libro)

    # Método para obtener la lista de libros
    def obtener_libros(self):
        return self.__libros
    
# Crear instancias de la clase Autor
autor1 = Autor("Gabriel García Márquez", "Colombiano")

# Crear libros para el autor
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "123-456")
libro2 = Libro("El Amor en los Tiempos del Cólera", "Gabriel García Márquez", "789-101")

# Agregar libros al autor
autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)

# Obtener la lista de libros del autor
for libro in autor1.obtener_libros():
    print(libro.get_titulo())
# Resultado:
# "Cien Años de Soledad"
# "El Amor en los Tiempos del Cólera"



