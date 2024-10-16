
"""Desafío 5:
Crea una jerarquía de clases para representar diferentes tipos de empleados en una biblioteca, 
utilizando herencia múltiple y composición. Por ejemplo, implementa clases como 
Empleado, Gerente, Tecnico, y Voluntario, donde Gerente y Tecnico hereden de Empleado, y
 algunos puedan tener roles adicionales mediante composición con otras clases 
como Administrador o Mantenimiento."""

class Empleado:
    def __init__(self, nombre, edad, puesto):
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Puesto: {self.puesto}"

class Gerente(Empleado):
    def __init__(self, nombre, edad, puesto, departamento):
        super().__init__(nombre, edad, puesto)
        self.departamento = departamento

    def mostrar_informacion(self):
        return super().mostrar_informacion() + f", Departamento: {self.departamento}"

class Tecnico(Empleado):
    def __init__(self, nombre, edad, puesto, especialidad):
        super().__init__(nombre, edad, puesto)
        self.especialidad = especialidad

    def mostrar_informacion(self):
        return super().mostrar_informacion() + f", Especialidad: {self.especialidad}"

class Voluntario(Empleado):
    def __init__(self, nombre, edad, puesto, proyecto):
        super().__init__(nombre, edad, puesto)
        self.proyecto = proyecto

    def mostrar_informacion(self):
        return super().mostrar_informacion() + f", Proyecto: {self.proyecto}"

class Administrador:
    def __init__(self, nombre, edad, puesto, proyectos):
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto
        self.proyectos = proyectos

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Puesto: {self.puesto}, Proyectos: {', '.join(self.proyectos)}"


class Mantenimiento:
    def __init__(self, nombre, edad, puesto, herramientas):
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto
        self.herramientas = herramientas

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Puesto: {self.puesto}, Herramientas: {', '.join(self.herramientas)}"


# Creación de objetos

gerente = Gerente("Juan", 35, "Gerente", "Sistemas")
tecnico = Tecnico("Maria", 28, "Tecnico", "Redes")
voluntario = Voluntario("Pedro", 22, "Voluntario", "Apoyo a niños")

administrador = Administrador("Ana", 38, "Administrador", ["Proyecto 1", "Proyecto 2"])

mantenimiento = Mantenimiento("Luis", 40, "Mantenimiento", ["Herramienta 1", "Herramienta 2"])

# Mostrar información

print(gerente.mostrar_informacion())
print(tecnico.mostrar_informacion())
print(voluntario.mostrar_informacion())
print(administrador.mostrar_informacion())
print(mantenimiento.mostrar_informacion())
