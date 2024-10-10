
"""Desafío 1: Sistemas con Múltiples Entidades Interconectadas (Biblioteca)
Imagina un sistema de gestión de biblioteca que maneja libros, 
usuarios, préstamos y multas. 
Usar TADs separados  para cada uno de estos elementos 
podría complicar la  interacción y gestión de relaciones entre ellos.
Materia:Programación 1
Alumno: Sol Méndez
Fecha: 07-10-2024"""

# Listas para almacenar los datos

libros = []
usuarios = []
prestamos = []
multas = []


# Definir la lista de libros

def agregar_libros (titulo, autor, año): 
    libro = { "titulo": titulo, "autor": autor, "año": año}
    libros.append(libro)
    print(f"Libro'{titulo}'agregando correctamente")

#Definir la lista de usuarios
def agregar_usuario(nombre, apellido, edad):
    usuario = { "nombre": nombre, "apellido": apellido, "edad": edad}
    usuarios.append(usuario)
    print(f"Usuario '{nombre} {apellido}' agregado correctamente")

#Definir la lista de prestamo 
def agregar_prestamo(libro, fecha, usuario, devolucion):
    prestamo = { "libro": libro, "fecha": fecha, "usuario": usuario, "devolucion": devolucion}
    prestamos.append(prestamo)
    print(f"Prestamo de libro '{libro['titulo']}' para el usuario '{usuario['nombre']} {usuario['apellido']}' agregado correctamente")

#Definir la lista de multas
def agregar_multa(prestamo, monto, usuario):
    multa = { "prestamo": prestamo, "monto": monto, "usuario": usuario}
    multas.append(multa)
    print(f"Multa de monto '{monto}' agregada correctamente para el usuario '{usuario['nombre']} {usuario['apellido']}'") 

#Ejemplos de uso

agregar_libros ("El Quijote", "Miguel de Cervantes", 1605)
agregar_libros ("La Divina Comedia", "J.B.R. Tolkien", 1937)

agregar_usuario= ("Juan", "Perez", 25)
agregar_usuario= ("Maria", "Garcia", 30)

agregar_prestamo (libros[0], "01-05-2024", usuarios[0], "05-10-2024")

agregar_multa (prestamos[0], 10, usuarios[0])

    
