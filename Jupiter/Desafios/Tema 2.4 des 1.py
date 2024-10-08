"""Grupo: Programación
Creador:bau21062014
Colaboradores:
Fecha:03-04-24
Dado tres números distintos, clasificarlos en orden ascendente 
utilizando comparaciones encadenadas y 
operadores lógicos. """

#ingreso tres numeros distintos
a=23
b=45
c=67

#ordenar los numeros de menor a mayor
if a < b and a < c:
  if b < c:
      print(a, b, c)  # a < b < c
  else:
      print(a, c, b)  # a < c < b
elif b < a and b < c:
  if a < c:
      print(b, a, c)  # b < a < c
  else:
      print(b, c, a)  # b < c < a
else:
  if a < b:
      print(c, a, b)  # c < a < b
  else:
      print(c, b, a)  # c < b < a
  


