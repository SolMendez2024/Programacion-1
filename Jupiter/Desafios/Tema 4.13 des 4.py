

"""Desafío 4:
Crea una función que tome un objeto Autor y devuelva una lista de 
todos los títulos de libros escritos por el autor. 
Asegúrate de que la lista de libros sea accesible solo a través de métodos de la clase Autor."""

def obtener_titulos_de_libros(autor):
    # Devuelve una lista de los títulos de los libros escritos por el autor
    return [libro.get_titulo() for libro in autor.obtener_libros()]

# Ejemplo de uso

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

    def get_titulo(self):
        return self.titulo

class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro): 
        self.libros.append(libro)

    def obtener_libros(self):
        return self.libros

# Creación de un autor y agregado de libros

autor = Autor("J.K. Rowling")
libro1 = Libro("Harry Potter y la Piedra Filosofal")
libro2 = Libro("Harry Potter y la Camara de Fuego")
libro3 = Libro("Harry Potter y el Principio del Curso")

autor.agregar_libro(libro1)

autor.agregar_libro(libro2)

autor.agregar_libro(libro3)

# Obtención de los títulos de libros escritos por el autor

print(obtener_titulos_de_libros(autor)) # Imprime: ['Harry Potter y la Piedra Filosofal', 'Harry Potter y la Camara de Fuego', 'Harry Potter y el Principio del Curso']

    
        
