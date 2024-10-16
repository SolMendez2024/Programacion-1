
""" Desafío 1: 
Implementa una clase Poeta que herede de Autor y 
tenga un atributo para el tipo de poesía que escribe."""


# Clase Autor, que es la base para la clase Poeta
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def obtener_informacion(self):
        return f"{self.nombre} ({self.nacionalidad})"

# Clase Poeta que hereda de Autor
class Poeta(Autor):
    def __init__(self, nombre, nacionalidad, tipo_poesia):
        # Llamada al constructor de la clase base Autor
        super().__init__(nombre, nacionalidad)
        # Atributo específico para el tipo de poesía
        self.tipo_poesia = tipo_poesia

    def describir(self):
        return f"{self.nombre} es un poeta de {self.nacionalidad} que escribe {self.tipo_poesia}."

# Crear una instancia de Poeta
poeta1 = Poeta("Pablo Neruda", "Chileno", "poesía romántica")
print(poeta1.describir())  # "Pablo Neruda es un poeta de Chileno que escribe poesía romántica."



