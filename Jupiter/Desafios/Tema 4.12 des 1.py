"""Desafío : Amplía la clase `Autor` para incluir una lista de libros escritos por
# el autor. Implementa métodos para agregar y eliminar libros de esta lista.
Materia:Programación 1
Alumno: Sol Méndez"""

class Autor:
    # Constructor de la clase
    # Inicializa los atributos del autor, incluyendo el nombre, la nacionalidad y una lista vacía de libros
    def __init__(self, nombre="", nacionalidad=""):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []

    # Método para mostrar los detalles del autor
    # Imprime el nombre, la nacionalidad y la lista de libros del autor
    def mostrar_autor(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print("Libros:")
        for libro in self.libros:
            print(f"- {libro}")

    # Método para agregar un libro a la lista de libros del autor
    # Agrega el libro a la lista y muestra un mensaje de confirmación
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"\nLibro '{libro}' agregado correctamente.")

    # Método para eliminar un libro de la lista de libros del autor
    # Verifica si el libro existe en la lista y lo elimina si es así, mostrando un mensaje de confirmación
    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"\nLibro '{libro}' eliminado correctamente.")
        else:
            print(f"\nEl libro '{libro}' no se encuentra en la lista de libros del autor.")

# Ejemplo de uso
# Solicita al usuario que ingrese el nombre y la nacionalidad del autor
nombre_autor = input("\nIngrese el nombre del autor: ")
nacionalidad_autor = input("Ingrese la nacionalidad del autor: ")

# Crea un objeto Autor con los datos ingresados
autor = Autor(nombre_autor, nacionalidad_autor)

# Muestra los detalles del autor
autor.mostrar_autor()

# Ciclo principal del programa
while True:
    # Muestra las opciones disponibles
    print("\nOpciones:")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Mostrar autor")
    print("4. Salir")

    # Solicita al usuario que ingrese la opción deseada
    opcion = input("Ingrese la opción deseada: ")

    # Procesa la opción seleccionada
    if opcion == "1":
        # Agrega un libro a la lista de libros del autor
        libro = input("Ingrese el título del libro: ")
        autor.agregar_libro(libro)
    elif opcion == "2":
        # Elimina un libro de la lista de libros del autor
        libro = input("Ingrese el título del libro a eliminar: ")
        autor.eliminar_libro(libro)
    elif opcion == "3":
        # Muestra los detalles del autor
        autor.mostrar_autor()
    elif opcion == "4":
        # Sale del programa
        print("Adiós!")
        break
    else:
        # Muestra un mensaje de error si la opción es inválida
        print("Opción inválida. Por favor, intente de nuevo.")
