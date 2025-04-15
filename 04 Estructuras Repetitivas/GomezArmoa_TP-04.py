# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range(101):  # El rango incluye desde 0 hasta 100 (101 no se incluye).
    print(numero)
print("Fin del programa")

#------------------------------------------------------------------------------------------
# 2) Desarrolla un programa que solicite al usuario un número entero positivo y determine la cantidad de
# dígitos que contiene.

numero = input("Ingrese un número: ")

if numero.isdigit(): 
    cantidad_digitos = len(numero)
    print(f"El número ingresado tiene {cantidad_digitos} dígito(s).")
else:
    print("El valor ingresado no es un número válido.")

print("Fin del programa")
#------------------------------------------------------------------------------------------
# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# Solicitar los dos valores al usuario
valor1 = input("Ingrese el primer valor: ")
valor2 = input("Ingrese el segundo valor: ")

# Validar que ambos valores sean números correctos
if valor1.isdigit() and valor2.isdigit():
    valor1 = int(valor1)
    valor2 = int(valor2)

    # Determinar los límites del rango
    inicio = min(valor1, valor2) + 1
    fin = max(valor1, valor2)

    # Calcular la suma de los números en el rango excluyendo los numeros ingresados
    suma = sum(range(inicio, fin))
    print(f"La suma de los números comprendidos entre {valor1} y {valor2}, excluyéndolos, es: {suma}")
else:
    print("Ambos valores deben ser números enteros positivos.")

print("Fin del programa")
#------------------------------------------------------------------------------------------
# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

print("Ingrese números enteros para sumarlos. Ingrese 0 para finalizar.")

total = 0  # Variable para acumular la suma

while True:
    numero = input("Ingrese un número: ")
    
    # Validar que el input sea un número entero
    if numero.lstrip('-').isdigit():
        numero = int(numero)
        if numero == 0:
            break  # Detiene bucle si el usuario ingresa 0
        total += numero  # Sumar el número al total
    else:
        print("Por favor, ingrese un número entero válido.")

print(f"La suma total acumulada es: {total}")

print("Fin del programa")
#------------------------------------------------------------------------------------------
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

print("Números pares entre 0 y 100 en orden decreciente:")

for numero in range(100, -1, -2):  # Itera desde 100 hasta 0, decrementando de 2 en 2
    print(numero)

print("Fin del programa")
#------------------------------------------------------------------------------------------ 
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero = input("Ingrese un número entero positivo: ")

# Validar que el input sea un número entero positivo
if numero.isdigit():
    numero = int(numero)
    suma = sum(range(numero + 1))  # Calcula la suma desde 0 hasta el número ingresado
    print(f"La suma de todos los números entre 0 y {numero} es: {suma}")
else:
    print("El valor ingresado no es un número entero positivo válido.")

print("Fin del programa")
#------------------------------------------------------------------------------------------
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros.
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares,
# cuántos son negativos y cuántos son positivos.

cantidad_numeros = 100  # Puedes cambiar este valor para probar con menos números
pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingrese {cantidad_numeros} números enteros:")

for _ in range(cantidad_numeros):
    numero = input("Ingrese un número: ")
    
    # Validar que el input sea un número entero
    if numero.lstrip('-').isdigit():
        numero = int(numero)
        
        # Clasificar el número
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
    else:
        print("Por favor, ingrese un número entero válido.")
        continue  # Reintentar el ingreso si no es válido

# Mostrar los resultados
print(f"\nResultados:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

print("Fin del programa")
#------------------------------------------------------------------------------------------
# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores.

cantidad_numeros = 100  # Puedes cambiar este valor para probar con menos números
suma_total = 0

print(f"Ingrese {cantidad_numeros} números enteros:")

for _ in range(cantidad_numeros):
    numero = input("Ingrese un número: ")
    
    # Validar que el input sea un número entero
    if numero.lstrip('-').isdigit():
        numero = int(numero)
        suma_total += numero  # Acumular la suma de los números
    else:
        print("Por favor, ingrese un número entero válido.")
        continue  # Reintentar el ingreso si no es válido

# Calcula la media
media = suma_total / cantidad_numeros

# Mostrar el resultado
print(f"\nLa media de los {cantidad_numeros} números ingresados es: {media}")

print("Fin del programa")
#------------------------------------------------------------------------------------------
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario.
# Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingrese un número entero: ")

# Validar que el input sea un número entero
if numero.lstrip('-').isdigit():
    # Invertir el número
    if numero.startswith('-'):
        numero_invertido = '-' + numero[:0:-1]  # Invertir los dígitos, manteniendo el signo negativo
    else:
        numero_invertido = numero[::-1]  # Invertir los dígitos para números positivos
    
    print(f"El número invertido es: {numero_invertido}")
else:
    print("El valor ingresado no es un número entero válido.")

print("Fin del programa")
#------------------------------------------------------------------------------------------
