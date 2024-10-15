


# Clase Autor
class Autor:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento, biografia):
        # Inicializa un objeto Autor con nombre, nacionalidad, fecha de nacimiento y biografía.
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.biografia = biografia
        self.libros = []  # Lista para almacenar los libros del autor
        self.premios = []  # Lista para almacenar los premios del autor

    def agregar_libro(self, libro):
        # Agrega un libro a la lista de libros del autor.
        if libro not in self.libros:
            self.libros.append(libro)

    def mostrar_libros(self):
        # Muestra los libros del autor.
        print(f"\nLibros de {self.nombre}:")
        for libro in self.libros:
            print(f"- {libro.titulo}")

    def eliminar_libro(self, titulo_libro):
        # Elimina un libro de la lista de libros del autor.
        self.libros = [libro for libro in self.libros if libro.titulo != titulo_libro]

    def agregar_premio(self, premio):
        # Agrega un premio a la lista de premios del autor.
        if premio not in self.premios:
            self.premios.append(premio)

    def mostrar_premios(self):
        # Muestra los premios del autor.
        print(f"\nPremios de {self.nombre}:")
        for premio in self.premios:
            print(f"- {premio}")

    def mostrar_biografia(self):
        # Muestra la biografía del autor.
        print(f"\nBiografía de {self.nombre}:")
        print(self.biografia)

    def mostrar_info(self):
        # Muestra la información completa del autor.
        print(f"\nInformación de {self.nombre}:")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Biografía: {self.biografia}")
        self.mostrar_libros()
        self.mostrar_premios()

# Clase Libro
class Libro:
    def __init__(self, titulo, genero, isbn, autor, descripcion=""):
        # Inicializa un objeto Libro con título, género, ISBN y autor.
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.autor = autor
        self.descripcion = descripcion

    def mostrar_detalle(self):
        # Muestra los detalles del libro.
        print(f"\nTítulo: {self.titulo}")
        print(f"Género: {self.genero}")
        print(f"ISBN: {self.isbn}")
        print(f"Autor: {self.autor.nombre}")
        print(f"Descripción: {self.descripcion}")

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        # Inicializa una biblioteca vacía.
        self.autores = {}  # Diccionario para almacenar los autores
        self.libros = {}  # Diccionario para almacenar los libros

    def agregar_autor(self, autor):
        # Agrega un autor a la biblioteca.
        if autor.nombre not in self.autores:
            self.autores[autor.nombre] = autor

    def agregar_libro(self, libro):
        # Agrega un libro a la biblioteca y lo asocia con su autor.
        if libro.titulo not in self.libros:
            self.libros[libro.titulo] = libro
            libro.autor.agregar_libro(libro)

    def mostrar_autores(self):
        # Muestra los autores de la biblioteca.
        print("\nAutores:")
        for autor in self.autores.values():
            print(f"- {autor.nombre}")

    def mostrar_libros(self):
        # Muestra los libros de la biblioteca.
        print("\nLibros:")
        for libro in self.libros.values():
            print(f"- {libro.titulo}")

    def buscar_libros_por_autor(self, nombre_autor):
        # Busca los libros de un autor en la biblioteca.
        autor = self.autores.get(nombre_autor)
        return autor.libros if autor else []

    def buscar_autores_por_libro(self, titulo_libro):
        # Busca el autor de un libro en la biblioteca.
        libro = self.libros.get(titulo_libro)
        return libro.autor if libro else None

    def buscar_libro(self, titulo_libro):
        # Busca un libro en la biblioteca.
        return self.libros.get(titulo_libro)

    def buscar_autor(self, nombre_autor):
        # Busca un autor en la biblioteca.
        return self.autores.get(nombre_autor)

# Crear biblioteca
biblioteca = Biblioteca()

# Crear autores y libros
autor1 = Autor("Juan Pérez", "Mexicano", "12/02/1980", "Juan Pérez es un escritor mexicano.")
autor2 = Autor("María García", "Española", "25/05/1975", "María García es una escritora española.")

libro1 = Libro("La vida es un sueño", "Ficción", "1234567890", autor1, "Una obra que explora la realidad y los sueños.")
libro2 = Libro("La casa de los espíritus", "Ficción", "9876543210", autor1, "Una historia sobre el amor y la familia.")
libro3 = Libro("El amor en los tiempos del cólera", "Ficción", "1111111111", autor2, "Una novela sobre el amor eterno.")

# Agregar autores y libros a la biblioteca
biblioteca.agregar_autor(autor1)
biblioteca.agregar_autor(autor2)
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Agregar premios a Juan Pérez
autor1.agregar_premio("Premio Nacional de Literatura")
autor1.agregar_premio("Premio Internacional de Narrativa")

# Buscar un libro
titulo_libro = "La vida es un sueño"
libro = biblioteca.buscar_libro(titulo_libro)
if libro:
    print(f"\n** Libro encontrado: {titulo_libro} **")
    libro.mostrar_detalle()
else:
    print(f"\n** No se encontró el libro '{titulo_libro}' **")

# Buscar un autor
nombre_autor = "Juan Pérez"
autor = biblioteca.buscar_autor(nombre_autor)
if autor:
    print(f"\n** Autor encontrado: {nombre_autor} **")
    autor.mostrar_info()
else:
    print(f"\n** No se encontró el autor '{nombre_autor}' **")

# Buscar libros por autor
nombre_autor = "Juan Pérez"
libros = biblioteca.buscar_libros_por_autor(nombre_autor)
if libros:
    print(f"\n** Libros de {nombre_autor}: **")
    for libro in libros:
        print(f"- {libro.titulo}")
else:
    print(f"\n** No se encontraron libros de {nombre_autor} **")

# Buscar autor por libro
titulo_libro = "La vida es un sueño"
autor = biblioteca.buscar_autores_por_libro(titulo_libro)
if autor:
    print(f"\n** Autor del libro '{titulo_libro}': **")
    autor.mostrar_info()
else:
    print(f"\n** No se encontró el autor del libro '{titulo_libro}' **")
