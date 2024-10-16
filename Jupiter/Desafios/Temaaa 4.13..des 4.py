

"""Desafío 4:
Implementa una clase EscritorAcademico que herede de Escritor y Academico, e incluya un método adicional 
para publicar artículos académicos. Asegúrate de utilizar correctamente la función super() 
para inicializar las clases base."""

class Escritor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

class Academico:
    def __init__(self, universidad):
        self.universidad = universidad

class EscritorAcademico(Escritor, Academico):
    def __init__(self, nombre, nacionalidad, universidad):
        super().__init__(nombre, nacionalidad)
        self.universidad = universidad

    def publicar_articulo(self, titulo):
        print(f"El escritor {self.nombre} ha publicado el artículo: {titulo}")

# Prueba de la clase EscritorAcademico

escritor_academico = EscritorAcademico("Juan Pablo II", "Argentino", "Universidad Nacional de La Matanza")
escritor_academico.publicar_articulo("La Evolución de la Literatura en Argentina")


