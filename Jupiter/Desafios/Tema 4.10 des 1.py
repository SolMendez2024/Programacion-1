
"""Desafío 1: Sistemas con Múltiples Entidades Interconectadas (Biblioteca)
Imagina un sistema de gestión de biblioteca que maneja libros, 
usuarios, préstamos y multas. 
Usar TADs separados  para cada uno de estos elementos 
podría complicar la  interacción y gestión de relaciones entre ellos.
Materia:Programación 1
Alumno: Sol Méndez
Fecha: 07-10-2024"""

# Inicializar listas vacías para libros, usuarios, préstamos y multas
libros = []
usuarios = []
prestamos = []
multas = []

# Función para agregar un libro
def agregar_libro(titulo, autor, genero, stock, codigolibro):
    # Crear un diccionario para el libro con título, autor, género, stock y código
    libro = {
        "Título": titulo,
        "Autor": autor,
        "Género": genero,
        "Stock": stock,
        "CódigoL": codigolibro
    }
    # Agregar el libro a la lista de libros
    libros.append(libro)
    # Imprimir un mensaje de confirmación de la acción
    print(f"Libro '{titulo}' agregado correctamente.")

# Función para agregar un usuario
def agregar_usuario(nombre, codigousuario):
    # Crear un diccionario para el usuario con nombre y código
    usuario = {
        "Nombre": nombre,
        "CódigoU": codigousuario
    }
    # Agregar el usuario a la lista de usuarios
    usuarios.append(usuario)
    # Imprimir un mensaje de confirmación de la acción
    print(f"Usuario '{nombre}' agregado correctamente.")

# Función para agregar un préstamo
def agregar_prestamo(codigolibro, codigousuario, fechaprestamo, fechadevolucion, codigoprestamo):
    # Verificar que el código de usuario exista en la lista de usuarios
    usuario = next((u for u in usuarios if u["CódigoU"] == codigousuario), None)
    if usuario is None:
        # Si el usuario no existe, imprimir un mensaje de error
        print("Error: El código de usuario no existe.")
        return

    # Verificar que el código de libro exista en la lista de libros
    libro = next((l for l in libros if l["CódigoL"] == codigolibro), None)
    if libro is None:
        # Si el libro no existe, imprimir un mensaje de error
        print("Error: El código de libro no existe.")
        return

    # Verificar que el libro tenga stock disponible
    if libro["Stock"] <= 0:
        # Si el libro no tiene stock disponible, imprimir un mensaje de error
        print("Error: El libro no tiene stock disponible.")
        return

    # Crear un diccionario para el préstamo con código de préstamo, libro, usuario, fecha de préstamo y fecha de devolución
    prestamo = {
        "CódigoP": codigoprestamo,
        "Libro": codigolibro,
        "Usuario": codigousuario,
        "Fecha préstamo": fechaprestamo,
        "Fecha devolución": fechadevolucion
    }
    # Agregar el préstamo a la lista de préstamos
    prestamos.append(prestamo)
    # Imprimir un mensaje de confirmación de la acción
    print(f"Préstamo de libro de título '{libro['Título']}', con código: '{libro['CódigoL']}' para el usuario de nombre '{usuario['Nombre']}, código: '{usuario['CódigoU']}' agregado correctamente.")

# Función para agregar una multa
def agregar_multa(codigoprestamo, monto):
    # Verificar que el código de préstamo exista en la lista de préstamos
    prestamo = next((p for p in prestamos if p["CódigoP"] == codigoprestamo), None)
    if prestamo is None:
        # Si el préstamo no existe, imprimir un mensaje de error
        print("Error: El código de préstamo no existe.")
        return

    # Crear un diccionario para la multa con código de préstamo, monto y usuario
    multa = {
        "CódigoP": codigoprestamo,
        "Monto": monto,
        "Usuario": prestamo["Usuario"]
    }
    # Agregar la multa a la lista de multas
    multas.append(multa)
    # Imprimir un mensaje de confirmación de la acción
    print(f"Multa de monto {monto} pesos, agregada correctamente al usuario con código: '{prestamo['Usuario']}'.")

# Función para borrar un libro
def borrar_libro(codigolibro):
    # Verificar que el código de libro exista en la lista de libros
    libro = next((l for l in libros if l["CódigoL"] == codigolibro), None)
    if libro is None:
        # Si el libro no existe, imprimir un mensaje de error
        print("Error: El código de libro no existe.")
        return

    # Verificar que el libro tenga stock disponible
    if libro["Stock"] > 1:
        # Disminuir el stock del libro en 1
        libro["Stock"] -= 1
        # Imprimir un mensaje de confirmación de la acción
        print(f"Un ejemplar del libro '{libro['Título']}' ha sido eliminado. Quedan {libro['Stock']} ejemplares.")
    elif libro["Stock"] == 1:
        # Verificar si hay préstamos pendientes para este libro
        prestamos_pendientes = [p for p in prestamos if p["Libro"] == codigolibro]
        if prestamos_pendientes:
            # Si hay préstamos pendientes, imprimir un mensaje de error
            print("Error: No se puede eliminar el libro porque hay préstamos pendientes.")
            return
        else:
            # Eliminar el libro de la lista de libros
            libros.remove(libro)
            # Imprimir un mensaje de confirmación de la acción
            print(f"El libro '{libro['Título']}' ha sido eliminado.")
    else:
        # Imprimir un mensaje de error
        print("Error.")
        return

# Función para borrar un usuario
def borrar_usuario(codigousuario):
    # Verificar que el código de usuario exista en la lista de usuarios
    usuario = next((u for u in usuarios if u["CódigoU"] == codigousuario), None)
    if usuario is None:
        # Si el usuario no existe, imprimir un mensaje de error
        print("Error: El código de usuario no existe.")
        return

    # Verificar que el usuario no tenga préstamos pendientes
    prestamos_pendientes = [p for p in prestamos if p["Usuario"] == codigousuario]
    if prestamos_pendientes:
        # Si el usuario tiene préstamos pendientes, imprimir un mensaje de error
        print("Error: El usuario tiene préstamos pendientes.")
        return

    # Eliminar el usuario de la lista de usuarios
    usuarios.remove(usuario)
    # Imprimir un mensaje de confirmación de la acción
    print(f"El usuario '{usuario['Nombre']}' ha sido eliminado.")

# Función para borrar un préstamo
def borrar_prestamo(codigoprestamo):
    # Verificar que el código de préstamo exista en la lista de préstamos
    prestamo = next((p for p in prestamos if p["CódigoP"] == codigoprestamo), None)
    if prestamo is None:
        # Si el préstamo no existe, imprimir un mensaje de error
        print("Error: El código de préstamo no existe.")
        return

    # Eliminar el préstamo de la lista de préstamos
    prestamos.remove(prestamo)
    # Imprimir un mensaje de confirmación de la acción
    print(f"El préstamo con código '{codigoprestamo}' ha sido eliminado.")

# Función para borrar una multa
def borrar_multa(codigoprestamo):
    # Verificar que el código de préstamo exista en la lista de multas
    multa = next((m for m in multas if m["CódigoP"] == codigoprestamo), None)
    if multa is None:
        # Si la multa no existe, imprimir un mensaje de error
        print("Error: El código de préstamo no existe.")
        return

    # Eliminar la multa de la lista de multas
    multas.remove(multa)
    # Imprimir un mensaje de confirmación de la acción
    print(f"La multa con código '{codigoprestamo}' ha sido eliminada.")

# Ejemplos de uso

# Agregar libros
agregar_libro("El Quijote de la Mancha", "J.U. Salinger", "Fantasía", 3, 1)
agregar_libro("To Kill a Mockingbird", "Harper Lee", "Novela", 2, 2)
agregar_libro("1984", "George Orwell", "Drama", 3, 3)

# Agregar usuarios
agregar_usuario("Juan Pablo", 1)

# Agregar préstamos
agregar_prestamo(1, 1, "2024-05-01", "2024-05-15", 1)

# Agregar multas
agregar_multa(1, 50)

# Mostrar libros en sistema
print("\n** Libros en sistema **")
print("==============")
for libro in libros:
    print(f"** Título:** {libro['Título']}")
    print(f"** Autor:** {libro['Autor']}")
    print(f"** Género:** {libro['Género']}")
    print(f"** Stock:** {libro['Stock']}")
    print(f"** Código:** {libro['CódigoL']}")
    print("------------------------")

# Mostrar usuarios en sistema
print("\n** Usuarios en sistema **")
print("===============")
for usuario in usuarios:
    print(f"** Nombre:** {usuario['Nombre']}")
    print(f"** Código:** {usuario['CódigoU']}")
    print("------------------------")

# Mostrar préstamos en sistema
print("\n** Préstamos en sistema **")
print("===============")
for prestamo in prestamos:
    print(f"** Código de préstamo:** {prestamo['CódigoP']}")
    print(f"** Libro:** {prestamo['Libro']}")
    print(f"** Usuario:** {prestamo['Usuario']}")
    print(f"** Fecha de préstamo:** {prestamo['Fecha préstamo']}")
    print(f"** Fecha de devolución:** {prestamo['Fecha devolución']}")
    print("------------------------")

# Mostrar multas en sistema
print("\n** Multas en sistema **")
print("=============")
for multa in multas:
    print(f"** Código de préstamo:** {multa['CódigoP']}")
    print(f"** Monto:** {multa['Monto']}")
    print(f"** Usuario:** {multa['Usuario']}")
    print("------------------------")

# Borrar libro, préstamo, usuario y multa
print("\n** Borrando libro, préstamo, usuario y multa... **")
borrar_libro(1)
borrar_prestamo(1)
borrar_usuario(1)
borrar_multa(1)

# Mostrar libros después de borrar
print("\n** Libros después de borrar **")
print("================================")
for libro in libros:
    print(f"** Título:** {libro['Título']}")
    print(f"** Autor:** {libro['Autor']}")
    print(f"** Género:** {libro['Género']}")
    print(f"** Stock:** {libro['Stock']}")
    print(f"** Código:** {libro['CódigoL']}")
    print("------------------------")

# Mostrar usuarios después de borrar
print("\n** Usuarios después de borrar **")
print("=================================")
for usuario in usuarios:
    print(f"** Nombre:** {usuario['Nombre']}")
    print(f"** Código:** {usuario['CódigoU']}")
    print("------------------------")

# Mostrar préstamos después de borrar
print("\n** Préstamos después de borrar **")
print("=================================")
for prestamo in prestamos:
    print(f"** Código de préstamo:** {prestamo['CódigoP']}")
    print(f"** Libro:** {prestamo['Libro']}")
    print(f"** Usuario:** {prestamo['Usuario']}")
    print(f"** Fecha de préstamo:** {prestamo['Fecha préstamo']}")
    print(f"** Fecha de devolución:** {prestamo['Fecha devolución']}")
    print("------------------------")

# Mostrar multas después de borrar
print("\n** Multas después de borrar **")
print("==============================")
for multa in multas:
    print(f"** Código de préstamo:** {multa['CódigoP']}")
    print(f"** Monto:** {multa['Monto']}")
    print(f"** Usuario:** {multa['Usuario']}")
    print("------------------------")