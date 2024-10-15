
"""Amplía la clase `Autor` para incluir una lista de libros escritos por el autor. 
Implementa métodos para agregar y eliminar libros de esta lista."""

          
#Definir la clase autor
class Autor: 
     def __init__(self, nombre, nacionalidad):
          self.nombre = nombre
          self.nacionalidad = nacionalidad
          self.libros = []  # Lista para almacenar los libros del autor

     # Método para agregar un libro al autor
     def agregar_libro(self, libro):
         self.libros.append(libro)
         print(f"\nLibro '{libro.titulo}' agregado correctamente al autor {self.nombre}.")

     # Método para eliminar un libro de la lista del autor  
     def eliminar_libro(self, titulo_libro):
          for libro in self.libros:
              if libro.titulo == titulo_libro:
                  self.libros.remove(libro)
                  print(f"\nLibro '{titulo_libro}' eliminado correctamente.")
                  return
          print(f"\nEl libro '{titulo_libro}' no se encuentra en la lista del autor.")

#Modo de uso 
autor_nombre= input("\nIgrese nombre del autor/a:")
nacionalidad_autor= input("\nIngrese la nacionalidad:")

autor = Autor(autor_nombre, nacionalidad_autor)

#Mostrar el autor

print("\nAutor:", autor.nombre)
print("Nacionalidad:", autor.nacionalidad)

#Ciclo principal del programa 
while True:
     print("\nOpciones:")
     print("1. Agregar libro")
     print("2. Eliminar libro")
     print("3. Salir")

     opcion = input("\nIngrese la opción: ")

     if opcion == "1":
          titulo_libro = input("\nIngrese título del libro: ")
          autor.agregar_libro(Libro(titulo_libro))
     elif opcion == "2":
          titulo_libro = input("\nIngrese título del libro a eliminar: ")
          autor.eliminar_libro(titulo_libro)
     elif opcion == "3":
    #Muestra los datos
        print("\nAutor:", autor.nombre)
        print("Nacionalidad:", autor.nacionalidad)
        print("Libros:", [libro.titulo for libro in autor.libros])
        break
     else:
          print("\nOpción fallida.")

          



