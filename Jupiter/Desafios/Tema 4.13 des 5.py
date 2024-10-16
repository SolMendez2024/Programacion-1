

"""Desafío 5:
Desarrolla una función que reciba una lista de objetos Autor y 
devuelva el autor que ha escrito el mayor número de libros. 
Utiliza el encapsulamiento para acceder a la información necesaria de cada objeto Autor."""

def autor_con_mas_libros(lista_autores):
    if not lista_autores:
        return None
    return max(lista_autores, key=lambda autor: len(autor.obtener_libros()))

# Pruebas

class Autor:
    def __init__(self, nombre, libros):
        self.nombre = nombre
        self.libros = libros

    def obtener_libros(self):
        return self.libros

# Test 1

autores = [
    Autor("Jane Austen", ["Pride and Prejudice", "Sense and Sensibility"]),
    Autor("Charles Dickens", ["Great Expectations", "A Tale of Two Cities"]),
    Autor("William Shakespeare", ["Hamlet", "Macbeth", "Romeo and Juliet"]),
]

print(autor_con_mas_libros(autores))  # Output: Jane Austen

# Test 2

autores = [
    Autor("Jane Austen", ["Pride and Prejudice", "Sense and Sensibility"]),
    Autor("Charles Dickens", ["Great Expectations", "A Tale of Two Cities"]),
]

print(autor_con_mas_libros(autores))  # Output: Charles Dickens

# Test 3

autores = []

print(autor_con_mas_libros(autores))  # Output: None

