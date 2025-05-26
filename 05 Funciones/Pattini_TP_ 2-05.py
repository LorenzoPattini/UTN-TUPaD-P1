####////// Comienzo Funciones Programa Principal //////####
#Inicio de Funciones Actividad 1
def imprimir_hola_mundo():
    return print("Hola Mundo!")
#Fin de Funciones Actividad 1

#Inicio de Funciones Actividad 2
def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")
#Fin de Funciones Actividad 2

#Inicio de Funciones Actividad 3
def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
#Fin de Funciones Actividad 3

#Inicio de Funciones Actividad 4
from math import pi
def calcular_area_circulo(radio):
    area = (pi) * (radio **2)
    return print(f"El área del círculo es {area}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * radio * (pi)
    return print(f"El perímetro del círculo es {perimetro}")
#Fin de Funciones Actividad 4

#Inicio de Funciones Actividad 5
def segundos_a_horas(segundos):
    horas = float(segundos / 3600)
    return print(f"{segundos} segundos equivalen a {horas} horas.")
#Fin de Funciones Actividad 5

#Inicio de Funciones Actividad 6
multiplos = []
def tabla_multiplicar(numero):
    for i in range(1, 10 + 1):
        num = i * numero
        multiplos.append(num)
    return multiplos
#Fin de Funciones Actividad 6

#Inicio de Funciones Actividad 7
def texto():
    mensaje = print("El resultado de: ")
    return mensaje

def operaciones_basicas(a, b):
    texto(), print(f"{a} + {b} es: {float(a + b)}")
    texto(), print(f"{a} - {b} es: {float(a - b)}")
    texto(), print(f"{a} * {b} es: {float(a * b)}")
    texto(), print(f"{a} / {b} es: {float(a / b)}")
#Fin de Funciones Actividad 7

#Inicio de Funciones Actividad 8
def calcular_imc(peso, altura):
    imc = round( peso / (altura**2),2)
    return imc
#Fin de Funciones Actividad 8

#Inicio de Funciones Actividad 9
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.")
#Fin de Funciones Actividad 9

#Inicio de Funciones Actividad 10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return print(f"El promedio de los números ingresados es: {promedio}")
#Fin de Funciones Actividad 10

#####////// Final Funciones Programa Principal //////####

### Actividad 1

imprimir_hola_mundo()

### Actividad 2

saludar_usuario("Lorenzo")

### Actividad 3

informacion_personal("Lorenzo", "Pattini", "25", "Ushuaia TdF.")

### Actividad 4

radio = int(input("Ingrese el radio del círculo"))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

### Actividad 5

segundos = int(input(print("Ingrese una cantidad de segundos.")))
segundos_a_horas(segundos)

### Actividad 6

numero = int(input(print("Ingrese un numero.")))
tabla_multiplicar(numero)

### Actividad 7

a = int(input(print("Ingrese un número.")))
b = int(input(print("Ingrese otro número.")))
operaciones_basicas(a, b)

### Actividad 8

peso = float(input(print("Ingrese su peso en kilogramos.")))
altura = float(input(print("Ingrese su altura en metros.")))
calcular_imc(peso, altura)

### Actividad 9

celsius = int(input(print("Ingrese la temperatura en grados Celsius.")))
celsius_a_fahrenheit(celsius)

### Actividad 10

a = int(input(print("Ingrese un número.")))
b = int(input(print("Ingrese otro número.")))
c = int(input(print("Ingrese otro número.")))
calcular_promedio(a, b, c)