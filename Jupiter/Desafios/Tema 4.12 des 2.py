
"""Desafío 2:  Crea una clase `Libro` con atributos como título, género e ISBN. ¿Cómo
 podrías relacionar esta clase con la clase `Autor`?
Materia:Programación 1
Alumno: Sol Méndez"""

# Clase Libro
class Libro:
    # Constructor de la clase
    def __init__(self, titulo="", genero="", isbn=""):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn

    # Método para mostrar detalles del libro
    def mostrar_libro(self):
        print(f"Título: {self.titulo}, Género: {self.genero}, ISBN: {self.isbn}")


# Clase Autor
class Autor:
    # Constructor de la clase
    def __init__(self, nombre="", nacionalidad=""):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []  # Lista de objetos de la clase Libro

    # Método para agregar un libro al autor
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"\nLibro '{libro.titulo}' agregado correctamente al autor {self.nombre}.")

    # Método para eliminar un libro de la lista del autor
    def eliminar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)
                print(f"\nLibro '{titulo}' eliminado correctamente.")
                return
        print(f"\nEl libro '{titulo}' no se encuentra en la lista del autor.")

    # Método para mostrar los detalles del autor y sus libros
    def mostrar_autor(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print("Libros:")
        if self.libros:
            for libro in self.libros:
                libro.mostrar_libro()  # Mostrar los detalles de cada libro
        else:
            print("Este autor no tiene libros agregados.")


# Ejemplo de uso
# Crear un autor
autor1 = Autor("Gabriel García Márquez", "Colombiana")

# Crear libros
libro1 = Libro("Cien años de soledad", "Realismo Mágico", "978-84-376-0494-7")
libro2 = Libro("El amor en los tiempos del cólera", "Novela", "978-84-376-0495-4")

# Agregar libros al autor
autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)

# Mostrar detalles del autor y sus libros
autor1.mostrar_autor()

# Eliminar un libro
autor1.eliminar_libro("Cien años de soledad")

# Mostrar detalles actualizados del autor y sus libros
autor1.mostrar_autor()
