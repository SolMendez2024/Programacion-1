"""  Desafío 3: Convertidor de temperaturas
Realizar conversiones de una temperatura dada en Celsius a Fahrenheit y Kelvin 
utilizando operaciones directas sobre las variables. 
Los cálculos se realizarán directamente al asignar los valores a las variables. 
Alumno: Sol Mendez"""


#Ingresa una temperatura en celsius
Temperatura= 23

#Realiza la conversión a Fahrenheit
Fahrenheit= (Temperatura*9/5)+32
#Realiza la conversión a Kelvin
Kelvin= Temperatura+273.15

#Imprime los resultados
print(Temperatura, "grados celsius equivalen a", Fahrenheit,"grados Fahrenheit y a" ,Kelvin, "grados Kelvin")