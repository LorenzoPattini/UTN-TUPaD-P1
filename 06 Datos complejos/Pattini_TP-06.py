#### Práctico 6: Estructuras de datos complejas ####
### Funciones: ###

def consultar_agenda_fecha(consulta):                                                                                                  # Función recursiva que utiliza una variable string, esta toma utilidad dentro de la función ya que hace de control para detener la misma.
    if (consulta == "NO") or (consulta == ""):                                                                                          # Secuencia condicional que realiza una igualdad entre la variable "consulta" y una cadena de carácteres. Si es distinta la función prosigue.
        return print("Ha terminado la consulta.")
    else:
        fecha = input(("Ingrese un dia de la semana: ")).lower()                                                                        # Se le pide al usuario que ingrese un dia de la semana, el cual se utilizará en el diccionario
        hora = input(("Elija un horario: 10:00 o 12:00 ")).lower()                                                                      # Se le pide al usuario que ingrese un horario, el cual se utilizará en el diccionario
        if (fecha,hora) in agenda:                                                                                                      # Inicia una secuencia condicional donde utiliza 2 items ("fecha" y "hora"), los cuales conforman el índice o llave en el diccionario "agenda"
            print(f"En el día {fecha}, en el horario {hora} tiene agendado: {agenda[(fecha,hora)]}")                                    # Se imprime un mensaje con la información pedida por el usuario.
        elif (fecha,hora) not in agenda:
            print("La fecha u horario ingresado no tienen evento agendado.")                                                            # En el caso de que el usuario ingrese un valor que no se encuentre en el diccionario, se le informará de esto. 
    consulta = input(("¿Quiere consultar otra fecha/ horario? SI/NO ")).upper()                                                         # Se le pregunta al usuario si quiere continuar revisando el diccionario, lo que elija el usuario será utilizado para reiniciar la función o terminarla.
    consultar_agenda_fecha(consulta)


## Actividad 1 ##
precios_frutas = {"Banana" : 1200, "Ananá" : 2500, "Melón" : 3000, "Uva" : 1450}                                                        # Se genera un diccionario con frutas como llaves y precios como valores
precios_frutas["Naranja"] = 1200                                                                                                        # Como esta fruta no se encuentra en el diccionario, se agrega una nueva fruta con su propio valor
precios_frutas["Manzana"] = 1500                                                                                                        # Mismo caso que el anterior
precios_frutas["Pera"] = 2300                                                                                                           # Mismo caso que el anterior
print(precios_frutas)                                                                                                                   # Se imprime el diccionario final.

## Actividad 2 ##
precios_frutas["Banana"] = 1330                                                                                                         # Como esta fruta se encuentra en el diccionario, se actualiza su valor
precios_frutas["Manzana"] = 1700                                                                                                        # Mismo caso que el anterior
precios_frutas["Melón"] = 2800                                                                                                          # Mismo caso que el anterior

## Actividad 3 ##
lista_precios_frutas = []                                                                                                               # Se crea una lista vacia
for index in precios_frutas:                                                                                                            # Realiza una iteración en el diccionario "precios_frutas"
    lista_precios_frutas.append(index)                                                                                                  # En la iteracion se guardan unicamente las llaves en la lista "lista_precios_frutas"
print(lista_precios_frutas)                                                                                                             # Se imprime la lista final.

## Actividad 4 ##
print(f"A continuación iniciará la agenda de contactos telefónicos. Se ingresaran 5 personas con sus números telefónicos.")
agenda_telefonica = {}                                                                                                                  # Se crea un diccionario vacio
consulta_telefonica = ""                                                                                                                # Se crea una variable string que sirve de bandera
for i in range(5):                                                                                                                      # Se realiza una iteracion for hasta 5 ciclos, donde se guardaran contactos y numeros en el diccionario "agenda_telefonica"
    contacto = input(("Ingrese un contacto: ")).upper()
    numero = int(input(("Ingrese un número de teléfono: ")))
    agenda_telefonica[contacto] = numero
while consulta_telefonica != "NO":                                                                                                      # Inicia un cilco while, que se mantiene siempre que la variable/bandera "consulta_telefonica" sea distinta a "NO"
    contacto = input(("¿Que contacto quiere consultar? ")).upper()                                                                      # Se le pide al usuario que ingrese el contacto que quiere visualizar del diccionario
    if contacto in agenda_telefonica:                                                                                                   # Si dicho contacto esta agendado, mostrara el contacto con su número
        print(f"El número de {contacto} es: {agenda_telefonica[contacto]}")
        consulta_telefonica = input(("¿Quiere continuar? SI/NO ")).upper()                                                              # Se le pregunta al usuario si quiere continuar, si desea terminar el programa ingresando "NO", la bandera del ciclo while cumplira la condición y finalizará.
    else:                                                                                                                               # Caso contrario, si el contacto no se encuentra en el diccionario, se le informará al usuario.
        print(f"El contacto {contacto} no se encuentra en la agenda teléfonica.")
        consulta_telefonica = input(("¿Quiere consultar otro contacto? SI/NO ")).upper()
print("Ha terminado de ver sus contactos, este programa finalizará ahora.")

## Actividad 5 ##
frase = str(input(("Ingrese una frase: "))).lower().split()                                                                             # Se le pide al usuario que ingrese una frase (cadena de carácteres), que se guardará en minúsculas, y utilizando la fucion split solo se guardarán palabras, y no espacios intermedios
frecuencia_palabras = {}                                                                                                                # Se crea un dicccionario vacio

for palabra in frase:                                                                                                                   # Comienza un ciclo for, donde se iterará todas las palabras dentro de la variable "frase"
    if palabra in frecuencia_palabras:                                                                                                  # Se crea una condición, que se cumple si la palabra en la posición correspondiente a la iteración de la frase se encuentra dentro del diccionario "frecuencia_palabras". En el primer ciclo no es utilizado.
        frecuencia_palabras[palabra] += 1                                                                                               # Al cumplirse la condición, se abre el diccionario y se posiciona donde esta esa palabra, y le suma en 1 su valor (value)
    else:
        frecuencia_palabras[palabra] = 1                                                                                                # Caso contrario, si la palabra no se encuentra en el diccionario, esta es agregada y su valor (value) inicia en 1.
print(f"El recuento de palabras repetidas es: {frecuencia_palabras}")                                                                   # Se imprime un mensaje y muestra todas las palabras del diccionario y la cantidad de veces que se repiten en la frase original

## Actividad 6 ##
print("A continuación ingresara los 3 alumnos:")
alumnos = {str(input(("Ingrese el primer alumno: ")).upper()) : " ", str(input(("Ingrese el segundo alumno: ")).upper()) : " ", str(input(("Ingrese el tercer alumno: ")).upper()) : " "}       # Se genera un diccionario y se guarda por ingreso de usuario 3 nombres de alumnos como llave, los valores estan iniciados como strings de manera temporal
promedio_lista = []                                                                                                                     # Se genera una lista vacia
for i in alumnos:                                                                                                                       # Inicia un ciclo for que iterará uno por uno en el diccionario de alumnos
    print(f"Ingrese las notas del alumno {i}: ")
    nota1, nota2, nota3 = int(input(("Nota 1: "))), int(input(("Nota 2: "))), int(input(("Nota 3: ")))                                  # Se le pedirá al usuario que ingrese 3 notas del alumno correspondiente a la iteración, se guardaran en 3 variables un valor integer/numérico
    notas = (nota1, nota2, nota3)                                                                                                       # Las 3 variables se convertirán en una tupla llamada "notas"
    alumnos[i] = notas                                                                                                                  # Se guardará la tupla de notas como value en el diccionario respectiva al alumno (llave)
    promedio = round(((nota1 + nota2 + nota3) / 3),2)                                                                                   # Se realiza un promedio redondeado en 2 decimales
    promedio_lista.append(promedio)                                                                                                     # El promedio se guardará en la lista "promedio_lista"
print(f"El listado de los alumnos y sus notas es: {alumnos}, y el promedio de cada uno respectivamente es: {promedio_lista}.")

## Actividad 7 ##    ### En este ejercicio la consigna pide de por si dos listas de estudiantes que estan aprobados y dos sets de numeros de dichos estudiantes aprobados, no vi necesario utilizar los sets de números
lista_aprob_1 = ["ANA","KEVIN","DIEGO","SERGIO"]                                                                                        # Se crea la lista 1 de estudiantes aprobados
lista_aprob_2 = ["JUAN","KEVIN","DIEGO","ROGER"]                                                                                        # Se crea la lista 2 de estudiantes aprobados
nota_parcial_1 = {6,8,10,9}                                                                                                             # Se crea un set de las notas de los estudiantes de la lista 1
nota_parcial_2 = {6,10,9,7}                                                                                                             # Se crea un set de las notas de los estudiantes de la lista 2
aprob_ambos = []                                                                                                                        # Se crea una lista vacía
lista_total_aprob = set(lista_aprob_1 + lista_aprob_2)                                                                                  # Se genera un set con ambas listas de estudiantes aprobados, ya que se busca a los que hayan aprovado al menos 1 vez
for i in lista_aprob_1:                                                                                                                 # Se realiza un ciclo for de i, que iterará la lista 1 de estudiantes aprobados
    for j in lista_aprob_2:                                                                                                             # Se realiza un ciclo for de j, que iterará la lista 2 de estudiantes aprobados
        if i == j:                                                                                                                      # Se realiza una condición donde si "i" y "j" son idénticos, significa que un estudiante está en ambas listas, si no coinciden la iteración toma de vuelta hasta que termine la primera lista
            aprob_ambos.append(i)                                                                                                       # Se guardará en la lista "aprob_ambos" i (alumno que se encuentra en ambas listas)

print(f"Las notas de los estudiantes que aprobaron ambos parciales son: {aprob_ambos}")                                                 # Se imprime un mensaje que muestra quienes se encuentran en ambas listas de aprobados
print(f"Las notas de los estudiantes que aprobaron solo uno de los parciales son: {lista_total_aprob}")                                 # Se imprime un mensaje que muestra quienes aprobaron solo un parcial utilizando el set "lista_total_aprob"
print(f"Las notas de los estudiantes que aprobaron al menos uno de los parciales son: {lista_total_aprob}")                             # Se imprime un mensaje que muestra quienes aprobaron al menos un parcial, utiliza la misma variable que el anterior, ya que ambas listas parten de estudiantes ya aprobados al menos una vez

## Actividad 8 ##
almacen = {"TORNILLOS":30, "CLAVOS":50}                                                                                                 # Se crea un diccionario con dos elementos iniciales
consulta_stock = "SI"                                                                                                                   # Se crea una variable que servirá de bandera
print("A continuación le mostraré las operaciones a realizar")
while consulta_stock != "NO":                                                                                                           # Se inicia una secuencia ciclo while que terminará una vez la variable coincida con la igualdad "NO"
    opcion = input(("Ingrese 1 para consultar un produccto en stock, 2 para agregar unidades de un producto en stock, o 3 para agregar productos al stock. "))       # Se genera una variable string donde el usuario elige entre 3 opciones numéricas, que será utilizada para una condición mas adelante
    producto = input(("¿Con cual producto quiere hacer una operación?: ")).upper()                                                      # Se crea una variable str que será utilizada como llave de diccionario
    if opcion == "1":                                                                                                                   # Se realiza una condición con la variable si coincide con el carácter "1", esta primera instancia sirve para consultar al diccionario un elemento ya existente
        if producto in almacen:                                                                                                         # Se realiza una condición donde se cumple si la cadena de carácteres ingresada por el usuario se encuentra dentro del diccionario
            print(f"Tenemos stock de {producto}, {almacen[producto]} unidades.")                                                        # Se imprime un mensaje que muestra la llave con  su valor del diccionario
        else:
            print(f"{producto} no se encuentra en stock.")                                                                              # De otra forma se imprime un mensaje informando que no se encuentra en el diccionario
    elif opcion == "2":                                                                                                                 # Se realiza una condición con la variable si coincide con el carácter "2", esta instancia agregará valor a un elemento ya existente
        unidades = int(input(("¿Cuantas unidades quiere agregar al stock?")))                                                           # Se guarda en una variable un valor integer ingresado por el usuario
        almacen[producto] += unidades                                                                                                   # La variable numérica "unidades" va a ser sumada con el valor actual del elemento correspondiente del diccionario
    elif opcion == "3":                                                                                                                 # Se realiza una condición con la variable si coincide con el carácter "3", que servirá para agregar elementos llave con valores al diccionario
        unidades = int(input((f"¿Cuantas unidades tiene el/los producto {producto} que quiere agregar? ")))
        almacen[producto] = unidades
    else:
        print("No ha ingresado una operacion válida.")                                                                                  # Si la variable "opcion" contiene una cadena que no coincide en las condicionales previas, se imprime un mensaje informando que no es una operación válida
    consulta_stock = input(("¿Quiere continuar? SI/NO ")).upper()                                                                       # Se reutiliza la variable "consulta_stock", esta determina si este ciclo while continúa o no
print("Ha terminado la consulta sobre el stock.")

## Actividad 9 ##
agenda = {("lunes","10:00"):"Llevar gato al veterinario", ("lunes","12:00"):"Compras del super",                                        # Se crea un diccionario llamado "agenda", donde las llaves están compuestas por dos valores: valor 1 es un día/fecha de la semana, y valor 2 es un horario que tiene solo dos variedades
            ("martes","10:00"):"Meeting", ("martes","12:00"):"Llevar auto al mecánico",                                                 # Las llaves de los elementos son eventos que requieren un horario puntual
            ("miercoles","10:00"):"Entregar reporte mensual", ("miercoles","12:00"):"Partido de fútbol",
            ("jueves","10:00"):"Presentar propuesta", ("jueves","12:00"):"Barbería",
            ("viernes","10:00"):"Meeting", ("viernes","12:00"):"Almuerzo familiar"}
consultar_agenda_fecha("consulta de agenda")                                                                                           # Se hace un llamado a la función "consultar_agenda_feacha"

## Actividad 10 ##
original = {"Francia":"Paris","Bolivia":"Sucre","Brasil":"Brasilia","Canada":"Ottawa","Alemania":"Berlin","Italia":"Roma",             # Se crea un diccionario "original" donde las llaves son países y los valores son sus capitales
            "Rusia":"Moscu","Egipto":"El Cairo","Australia":"Canberra","Marruecos":"Rabat","Argelia":"Argel","Nigeria":"Abuya"}
print(f"El diccionario de paíeses y capitales es: {original}")
invertido = {}                                                                                                                         # Se crea un diccionario vacío "invertido"
for i,j in original.items():                                                                                                           # Inicia un ciclo for donde se hará una iteración de 2 elementos i y j, esto abrirá el diccionario y utilizando la función items() i será la llave y j el valor del diccionario
    invertido[j] = i                                                                                                                   # Se guardará j (el valor del diccionario original) como llave e i (la llave del diccionario original) como valor consiguiendo invertir los elementos dentro del diccionario "invertido"
print(f"El diccionario de países y capitales invertido es: {invertido}")