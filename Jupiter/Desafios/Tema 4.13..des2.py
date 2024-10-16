
""" Desafío 2:
Crea una clase Bibliotecario que herede de Usuario y 
tenga atributos específicos como sección y años_experiencia."""

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario

class Bibliotecario(Usuario):
    def __init__(self, nombre, id_usuario, seccion, años_experiencia):
        # Llamada al constructor de la clase base Usuario
        super().__init__(nombre, id_usuario)
        # Atributos específicos de Bibliotecario
        self.seccion = seccion
        self.años_experiencia = años_experiencia

    def info_bibliotecario(self):
        return f"{self.nombre}, Sección: {self.seccion}, Experiencia: {self.años_experiencia} años."

# Prueba de la clase Bibliotecario

biblio = Bibliotecario("Juanito", 123456, "Biblioteca General", 15)
print(biblio.info_bibliotecario())  # Imprime la información del bibliotecario: Juanito, Sección: Biblioteca General, Experiencia: 15 años.



