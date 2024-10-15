"""Desafío 3: Considera un sistema de manejo de inventario para una cadena de tiendas minoristas.
Tienes que tratar con datos de productos, tiendas, empleados, y transacciones,
 donde cada tienda podría tener múltiples productos y empleados.
Materia:Programación 1
Alumno: Sol Méndez"""

# Inicializar listas vacías para tiendas, productos, empleados y transacciones
tiendas = []
productos = []
empleados = []
transacciones = []

# Función para crear una tienda
def crear_tienda(nombre, ubicacion):
    tienda = {
        "nombre": nombre,
        "ubicacion": ubicacion,
        "productos": [],
        "empleados": []
    }
    tiendas.append(tienda)

# Función para crear un producto
def crear_producto(nombre, precio, cantidad, categoria):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria
    }
    productos.append(producto)

# Función para crear un empleado
def crear_empleado(nombre, cargo, salario):
    empleado = {
        "nombre": nombre,
        "cargo": cargo,
        "salario": salario
    }
    empleados.append(empleado)

# Función para agregar un producto a una tienda
def agregar_producto_tienda(tienda_nombre, producto_nombre):
    tienda = next((t for t in tiendas if t["nombre"] == tienda_nombre), None)
    if tienda is None:
        print("Error: La tienda no existe.")
        return

    producto = next((p for p in productos if p["nombre"] == producto_nombre), None)
    if producto is None:
        print("Error: El producto no existe.")
        return

    tienda["productos"].append(producto)

# Función para agregar un empleado a una tienda
def agregar_empleado_tienda(tienda_nombre, empleado_nombre):
    tienda = next((t for t in tiendas if t["nombre"] == tienda_nombre), None)
    if tienda is None:
        print("Error: La tienda no existe.")
        return

    empleado = next((e for e in empleados if e["nombre"] == empleado_nombre), None)
    if empleado is None:
        print("Error: El empleado no existe.")
        return

    tienda["empleados"].append(empleado)

# Función para crear una transacción
def crear_transaccion(tienda_nombre, producto_nombre, cantidad, empleado_nombre, fecha):
    tienda = next((t for t in tiendas if t["nombre"] == tienda_nombre), None)
    if tienda is None:
        print("Error: La tienda no existe.")
        return

    producto = next((p for p in productos if p["nombre"] == producto_nombre), None)
    if producto is None:
        print("Error: El producto no existe.")
        return

    empleado = next((e for e in empleados if e["nombre"] == empleado_nombre), None)
    if empleado is None:
        print("Error: El empleado no existe.")
        return

    transaccion = {
        "tienda": tienda_nombre,
        "producto": producto_nombre,
        "cantidad": cantidad,
        "empleado": empleado_nombre,
        "fecha": fecha
    }
    transacciones.append(transaccion)

# Función para mostrar la lista de tiendas
def mostrar_tiendas():
    print("\nTiendas:")
    for tienda in tiendas:
        print(f"{tienda['nombre']} - Ubicación: {tienda['ubicacion']}")

# Función para mostrar la lista de productos
def mostrar_productos():
    print("\nProductos:")
    for producto in productos:
        print(f"{producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']} - Categoría: {producto['categoria']}")

# Función para mostrar la lista de empleados
def mostrar_empleados():
    print("\nEmpleados:")
    for empleado in empleados:
        print(f"{empleado['nombre']} - Cargo: {empleado['cargo']} - Salario: {empleado['salario']}")

# Función para mostrar la lista de transacciones
def mostrar_transacciones():
    print("\nTransacciones:")
    for transaccion in transacciones:
        print(f"Tienda: {transaccion['tienda']} - Producto: {transaccion['producto']} - Cantidad: {transaccion['cantidad']} - Empleado: {transaccion['empleado']} - Fecha: {transaccion['fecha']}")

# Crear tiendas
crear_tienda("La Esquina Verde", "Calle Principal 45, Buenos Aires")
crear_tienda("Electro Mundo", "Avenida Tecnológica 101, Bogotá")
crear_tienda("Casa del Hogar", "Bulevar Central 55, Lima")

# Crear productos
crear_producto("Refrigerador Samsung", 25000, 10, "Electrodomésticos")
crear_producto("Lavadora LG", 15000, 15, "Electrodomésticos")
crear_producto("Aire Acondicionado Daikin", 20000, 5, "Electrodomésticos")
crear_producto("Sofá Modular", 12000, 8, "Muebles")
crear_producto("Mesa de Centro", 6000, 20, "Muebles")

# Crear empleados
crear_empleado("Carlos Fernández", "Gerente", 40000)
crear_empleado("María Suárez", "Vendedor", 18000)
crear_empleado("Luis Torres", "Cajero", 16000)
crear_empleado("Ana Jiménez", "Gerente", 38000)
crear_empleado("Sofía Martínez", "Vendedor", 17000)

# Agregar productos a tiendas
agregar_producto_tienda("La Esquina Verde", "Refrigerador Samsung")
agregar_producto_tienda("La Esquina Verde", "Lavadora LG")
agregar_producto_tienda("Electro Mundo", "Aire Acondicionado Daikin")
agregar_producto_tienda("Casa del Hogar", "Sofá Modular")
agregar_producto_tienda("Casa del Hogar", "Mesa de Centro")

# Agregar empleados a tiendas
agregar_empleado_tienda("La Esquina Verde", "Carlos Fernández")
agregar_empleado_tienda("La Esquina Verde", "María Suárez")
agregar_empleado_tienda("Electro Mundo", "Ana Jiménez")
agregar_empleado_tienda("Casa del Hogar", "Luis Torres")
agregar_empleado_tienda("Casa del Hogar", "Sofía Martínez")

# Crear transacciones
crear_transaccion("La Esquina Verde", "Refrigerador Samsung", 3, "Carlos Fernández", "13-10-2024")
crear_transaccion("Electro Mundo", "Aire Acondicionado Daikin", 2, "Ana Jiménez", "14-10-2024")
crear_transaccion("Casa del Hogar", "Sofá Modular", 4, "Luis Torres", "15-10-2024")

# Mostrar tiendas, productos, empleados y transacciones
mostrar_tiendas()
mostrar_productos()
mostrar_empleados()
mostrar_transacciones()
