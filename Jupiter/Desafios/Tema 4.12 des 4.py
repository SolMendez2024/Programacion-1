
"""Desafío 4:   Piensa en otros atributos y métodos que podrías agregar a la clase `Autor` para
hacerla más completa.
Materia:Programación 1
Alumno: Sol Méndez"""


from datetime import datetime

# Clase Libro
class Libro:
    def __init__(self, titulo, genero, isbn, descripcion=""):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.descripcion = descripcion

    def mostrar_libro(self):
        print(f" - {self.titulo} (Género: {self.genero}, ISBN: {self.isbn})")

# Clase Autor mejorada
class Autor:
    def __init__(self, nombre="", nacionalidad="", fecha_nacimiento=None, fecha_fallecimiento=None, genero_literario=""):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.nacionalidades_secundarias = []
        self.fecha_nacimiento = fecha_nacimiento  # Formato: "YYYY-MM-DD"
        self.fecha_fallecimiento = fecha_fallecimiento  # Formato: "YYYY-MM-DD" (si falleció)
        self.biografia = ""
        self.premios = []
        self.genero_literario = genero_literario
        self.libros = []

    # Método para agregar un libro
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado correctamente al autor {self.nombre}.")

    # Método para eliminar un libro
    def eliminar_libro(self, titulo_libro):
        for libro in self.libros:
            if libro.titulo == titulo_libro:
                self.libros.remove(libro)
                print(f"Libro '{titulo_libro}' eliminado correctamente.")
                return
        print(f"El libro '{titulo_libro}' no se encuentra en la lista de libros del autor.")

    # Método para contar cuántos libros tiene el autor
    def contar_libros(self):
        return len(self.libros)

    # Método para mostrar la biografía del autor
    def mostrar_biografia(self):
        print(f"Biografía de {self.nombre}: {self.biografia}")

    # Método para actualizar la biografía
    def actualizar_biografia(self, nueva_biografia):
        self.biografia = nueva_biografia
        print(f"Biografía actualizada para {self.nombre}.")

    # Método para agregar un premio
    def agregar_premio(self, premio):
        self.premios.append(premio)
        print(f"Premio '{premio}' agregado correctamente al autor {self.nombre}.")

    # Método para mostrar los premios
    def mostrar_premios(self):
        print(f"\nPremios de {self.nombre}:")
        if self.premios:
            for premio in self.premios:
                print(f"- {premio}")
        else:
            print("Este autor no ha recibido premios.")

    # Método para agregar nacionalidades secundarias
    def agregar_nacionalidad(self, nacionalidad):
        if nacionalidad not in self.nacionalidades_secundarias:
            self.nacionalidades_secundarias.append(nacionalidad)
            print(f"Nacionalidad '{nacionalidad}' agregada correctamente a {self.nombre}.")
        else:
            print(f"{self.nombre} ya tiene la nacionalidad '{nacionalidad}'.")

    # Método para calcular la edad o los años desde su fallecimiento
    def calcular_edad(self):
        if self.fecha_nacimiento:
            fecha_nac = datetime.strptime(self.fecha_nacimiento, "%Y-%m-%d")
            if self.fecha_fallecimiento:
                fecha_fall = datetime.strptime(self.fecha_fallecimiento, "%Y-%m-%d")
                edad_fallecimiento = fecha_fall.year - fecha_nac.year
                print(f"{self.nombre} falleció a los {edad_fallecimiento} años.")
            else:
                hoy = datetime.today()
                edad_actual = hoy.year - fecha_nac.year
                print(f"{self.nombre} tiene {edad_actual} años.")
        else:
            print("Fecha de nacimiento no disponible.")

    # Método para mostrar los detalles completos del autor
    def mostrar_autor(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        if self.nacionalidades_secundarias:
            print(f"Otras nacionalidades: {', '.join(self.nacionalidades_secundarias)}")
        if self.genero_literario:
            print(f"Género Literario: {self.genero_literario}")
        self.mostrar_biografia()
        self.mostrar_premios()
        print(f"\nLibros de {self.nombre}:")
        if self.libros:
            for libro in self.libros:
                libro.mostrar_libro()
        else:
            print("Este autor no tiene libros agregados.")


# Ejemplo de uso
autor1 = Autor("Gabriel García Márquez", "Colombiana", "1927-03-06", "2014-04-17", "Realismo Mágico")
autor1.agregar_libro(Libro("Cien años de soledad", "Realismo Mágico", "978-84-376-0494-7", "Una novela sobre la familia Buendía."))
autor1.actualizar_biografia("Gabriel García Márquez fue un novelista, cuentista y periodista colombiano.")
autor1.agregar_premio("Premio Nobel de Literatura 1982")

# Mostrar detalles completos del autor
autor1.mostrar_autor()

# Calcular edad o años desde su fallecimiento
autor1.calcular_edad()

# Agregar una nacionalidad secundaria
autor1.agregar_nacionalidad("Mexicana")
