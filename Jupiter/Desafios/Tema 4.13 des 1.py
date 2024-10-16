

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn


"""Estos métodos permiten leer (getter) o  modificar (setter) los valores 
 de los atributos privados desde fuera de la clase."""
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
