import math
# definir la función


# 1. Crear una función llamada imprimir_hola_mundo que imprima por
#  pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#  programa principal

def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
# Llamar a esta función desde el programa principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    print(f"Hola {nombre.capitalize()} !")

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.
def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# 4 Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados
def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

# 5 Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva
# la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función

def segundos_a_horas(segundos):
    horas = segundos // 3600
    return print(f"{segundos} segundos son {horas} horas.")

# 6 Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla
# de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for n in range(1, 11):
        print(f"{numero} x {n} = {numero * n}")

# 7 Crear una función llamada operaciones_basicas(a, b) que recibados números como parámetros y devuelva una tupla
#  con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "Error: División por cero"
    
    return (suma, resta, multiplicacion, division)

#8 Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva
# el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

#9 Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. 
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# 10 Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

#------------------------

#programa principal
# 1. Llamar a la función imprimir_hola_mundo
imprimir_hola_mundo()

#2. Llamar a la función saludar_usuario solicitando el nombre al usuario
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

#3. Llamar a la función informacion_personal solicitando los datos al usuario
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#4 solicitar el radio al usuario y llamar a las funciones calcular_area_circulo y calcular_perimetro_circulo
radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")


#5 solicitar los segundos al usuario y llamar a la función segundos_a_horas
segundos = int(input("Ingrese la cantidad de segundos: "))
segundos_a_horas(segundos)

#6 solicitar el número al usuario y llamar a la función tabla_multiplicar
num_ingresado = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(num_ingresado)


#7 solicitar los números al usuario y llamar a la función operaciones_basicas

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(a, b)

print(f"Resultados de las operaciones básicas:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
if isinstance(resultados[3], str):
    print(resultados[3])  # Imprimir mensaje de error si es división por cero
else:
    print(f"División: {resultados[3]:.2f}")

#8 solicitar el peso y la altura al usuario y llamar a la función calcular_imc
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

#9 solicitar la temperatura en Celsius al usuario y llamar a la función celsius_a_fahrenheit
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}")

#10 solicitar los tres números al usuario y llamar a la función calcular_promedio
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(num1, num2, num3)

print(f"El promedio de los números ingresados es: {promedio:.2f}")







