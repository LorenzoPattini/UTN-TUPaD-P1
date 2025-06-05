###TP7 Recursividad###
##Inicio de Funciones##
def factorial(g): #Función para calcular la factorización del valor ingresado.
    if g == 0:
        return 1
    else:
        return g * factorial(g - 1)

def fibonacci_recursivo(posicion): #Función para calcular el valor Fibonacci de la variable ingresada.
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)

def base_elevado_exponente(n_base, n_expon): #Función para calcular la potencia de las variables ingresadas.
    if n_expon == 0:
        return 1
    elif n_expon == 1:
        return n_base
    else:
        return n_base * base_elevado_exponente(n_base, n_expon - 1)

def decimal_a_binario(num_decim): #Función para transformar un número decimal a su contraparte binaria.
    if num_decim < 2:
        return str(num_decim)
    else:
        return decimal_a_binario(num_decim // 2) + str(num_decim % 2)

def es_palindromo(palabra, invertida): #Función que comprueba si la palabra ingresada por el usuario, y la misma invertida son identicas, dando respuesta booleana.
    if palabra == invertida:
        return True
    else:
        return False

def invertida(palabra): #Función que invierte la palabra ingresada por el usuario.
    palabra_invertida = ""
    for i in palabra:
        palabra_invertida = i + palabra_invertida
    return palabra_invertida

def suma_digitos(g, suma): #Función suma los dígitos de un número ingresado por el usuario.
    digito = g % 10
    suma += digito
    g = g // 10
    if g == 0:
        return suma
    else:
        return suma_digitos(g, suma)

def contar_bloques(t, total_bloques): #Función que calcula el valor final de un valor ingresado por el usuario, el cual suma el mismo restado 1.
    if t > 1:
        total_bloques = total_bloques + t
        return contar_bloques(t - 1, total_bloques)
    else:
        return (total_bloques + 1)

def contar_digito(n, g, veces): #Función que cuenta la cantidad de veces que un digito ingresado por el usuario se repite en una cifra también ingresada por usuario.
    if (n < 10) and (n == g):
        veces = veces + 1
        return veces
    elif (n < 10) and (n != g):
        return veces
    elif (n % 10) == g:
        veces = veces + 1
        return contar_digito((n // 10), g, veces)
    elif n >= 10:
        return contar_digito((n // 10), g, veces)

##Fin de Funciones##

#Ejercicio 1: Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario.#
num_fact= int(input("Ingrese un numero para calcular su factorización: "))
print(f"La factorización de {num_fact} es: {factorial(num_fact)}")

#Ejercicio 2:  Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.#
x= int(input(print("Ingrese un número para descubrir su valor de Fibonacci")))
print(f"La secuendia Fibonacci del número {x} sucede de la siguiente forma.")
for i in range (x):
    print(fibonacci_recursivo(i))

#Ejercicio 3:  Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula (𝑛**𝑚) = 𝑛 ∗ (𝑛**(𝑚−1)). Prueba esta función en un algoritmo general.

base= int(input("Ingrese un número para que sea la base: "))
exponente =int(input("Ingrese un número para que sea el exponente: "))
print(f"{base} elevado a {exponente} es: {base_elevado_exponente(base, exponente)}")

#Ejercicio 4: Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

n= int(input(print("Ingrese un número de base decimal para transformarlo en su contraparte binaria.")))
print(decimal_a_binario(n))

#Ejercicio 5: Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

palabra = str(input(print("Ingrese una palabra para corroborar si es palindroma: ")))
es_palindromo(palabra, invertida(palabra))

#Ejercicio 6: Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.

n = int(input(print("Ingrese un número positivo: ")))
print(f"La suma de los dígitos de {n} es: {suma_digitos(n, 0)}")

#Ejercicio 7: Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.

n = int(input(print("Ingrese la cantidad de bloques de la base: ")))
print(f"Los bloques necesarios para hacer una piramide son: {contar_bloques(n, 0)}")

#Ejercicio 8: Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

numero = int(input(print("Ingrese un número positivo: ")))
digito = int(input(print("Elija un digito entre 0 y 9: ")))
print(f"En la cifra {numero} el dígito {digito} se repite {contar_digito(numero, digito, 0)} veces.")