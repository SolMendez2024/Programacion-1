
"""Desafío 3:
Implementa la clase Autor con métodos getter y setter utilizando decoradores @property para manejar 
los atributos privados nombre y nacionalidad."""
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__libros = []

    # Getter para el nombre (usando @property)
    @property
    def nombre(self):
        return self.__nombre

    # Setter para el nombre (usando @nombre.setter)
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    # Getter para la nacionalidad (usando @property)
    @property
    def nacionalidad(self):
        return self.__nacionalidad

    # Setter para la nacionalidad (usando @nacionalidad.setter)
    @nacionalidad.setter
    def nacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    def agregar_libro(self, libro):
        self.__libros.append(libro)

    def obtener_libros(self):
        return self.__libros
    
# Crear una instancia de la clase Autor
autor2 = Autor("Isabel Allende", "Chilena")

# Usar los métodos getter y setter a través de @property
print(autor2.nombre)  # "Isabel Allende"
print(autor2.nacionalidad)  # "Chilena"

# Modificar los atributos utilizando los setters
autor2.nombre = "Isabel A. Allende"
autor2.nacionalidad = "Estadounidense"
print(autor2.nombre)  # "Isabel A. Allende"
print(autor2.nacionalidad)  # "Estadounidense"
