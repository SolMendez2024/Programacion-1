
"""Desafío 3:  Considera cómo podrías implementar una biblioteca que 
almacene múltiples autores y libros. ¿Qué estructuras de datos usarías?
Materia:Programación 1
Alumno: Sol Méndez"""

# Clase Libro
class Libro:
    def __init__(self, titulo="", genero="", isbn=""):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn

    def mostrar_libro(self):
        print(f"Título: {self.titulo}, Género: {self.genero}, ISBN: {self.isbn}")

# Clase Autor
class Autor:
    def __init__(self, nombre="", nacionalidad=""):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []  # Lista de objetos Libro

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado correctamente al autor {self.nombre}.")

    def mostrar_libros(self):
        print(f"\nLibros de {self.nombre}:")
        if self.libros:
            for libro in self.libros:
                libro.mostrar_libro()
        else:
            print("Este autor no tiene libros agregados.")

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.autores = {}  # Diccionario con nombre de autor como clave y objeto Autor como valor

    # Método para agregar un autor a la biblioteca
    def agregar_autor(self, autor):
        if autor.nombre not in self.autores:
            self.autores[autor.nombre] = autor
            print(f"Autor '{autor.nombre}' agregado a la biblioteca.")
        else:
            print(f"El autor '{autor.nombre}' ya existe en la biblioteca.")

    # Método para agregar un libro a un autor
    def agregar_libro_a_autor(self, nombre_autor, libro):
        if nombre_autor in self.autores:
            self.autores[nombre_autor].agregar_libro(libro)
        else:
            print(f"El autor '{nombre_autor}' no existe en la biblioteca.")

    # Método para mostrar todos los autores y sus libros
    def mostrar_biblioteca(self):
        print("\nBiblioteca:")
        if self.autores:
            for autor in self.autores.values():
                print(f"\nAutor: {autor.nombre} ({autor.nacionalidad})")
                autor.mostrar_libros()
        else:
            print("La biblioteca está vacía.")

    # Método para eliminar un autor
    def eliminar_autor(self, nombre_autor):
        if nombre_autor in self.autores:
            del self.autores[nombre_autor]
            print(f"Autor '{nombre_autor}' eliminado de la biblioteca.")
        else:
            print(f"El autor '{nombre_autor}' no existe en la biblioteca.")

    # Método para eliminar un libro de un autor
    def eliminar_libro_de_autor(self, nombre_autor, titulo_libro):
        if nombre_autor in self.autores:
            autor = self.autores[nombre_autor]
            for libro in autor.libros:
                if libro.titulo == titulo_libro:
                    autor.libros.remove(libro)
                    print(f"Libro '{titulo_libro}' eliminado del autor {nombre_autor}.")
                    return
            print(f"El libro '{titulo_libro}' no se encuentra entre los libros de {nombre_autor}.")
        else:
            print(f"El autor '{nombre_autor}' no existe en la biblioteca.")


# Ejemplo de uso
biblioteca = Biblioteca()

# Crear autores
autor1 = Autor("Gabriel García Márquez", "Colombiana")
autor2 = Autor("Isabel Allende", "Chilena")

# Crear libros
libro1 = Libro("Cien años de soledad", "Realismo Mágico", "978-84-376-0494-7")
libro2 = Libro("El amor en los tiempos del cólera", "Novela", "978-84-376-0495-4")
libro3 = Libro("La casa de los espíritus", "Novela", "978-84-376-0496-1")

# Agregar autores a la biblioteca
biblioteca.agregar_autor(autor1)
biblioteca.agregar_autor(autor2)

# Agregar libros a autores
biblioteca.agregar_libro_a_autor("Gabriel García Márquez", libro1)
biblioteca.agregar_libro_a_autor("Gabriel García Márquez", libro2)
biblioteca.agregar_libro_a_autor("Isabel Allende", libro3)

# Mostrar toda la biblioteca
biblioteca.mostrar_biblioteca()

# Eliminar un libro de un autor
biblioteca.eliminar_libro_de_autor("Gabriel García Márquez", "Cien años de soledad")

# Mostrar biblioteca actualizada
biblioteca.mostrar_biblioteca()

# Eliminar un autor
biblioteca.eliminar_autor("Isabel Allende")

# Mostrar biblioteca actualizada
biblioteca.mostrar_biblioteca()
