# 1 -----------------------------------------------------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial (n - 1)

num = int(input("ingrese un numero: "))
print(f"El factorial de {num} es: {factorial(num)}")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    

# 2 -----------------------------------------------------
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Solicitar al usuario la posición hasta la que desea mostrar la serie de Fibonacci
pos = int(input("Ingrese un numero para la posición hasta la que desea ver la serie de Fibonacci: "))

print(f"Serie de Fibonacci hasta la posición {pos}:")
for i in range(pos + 1):
    print(f"Fibonacci({i}) = {fibonacci(i)}")

# 3 -----------------------------------------------------
def potencia(base, exponente):
    """Calcula la potencia de un número base elevado a un exponente de forma recursiva."""
    if exponente == 0:
        return 1  # Caso base: cualquier número elevado a 0 es 1
    else:
        return base * potencia(base, exponente - 1)  # Caso recursivo

# Solicitar la base y el exponente
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente:"))

print(f"{base} elevado a la {exponente} es: {potencia(base, exponente)}")

# 4 -----------------------------------------------------
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = 10
print(f"Conversión paso a paso de {numero} a binario:")
print("10 ÷ 2 = 5, resto: 0")
print("5 ÷ 2 = 2, resto: 1")
print("2 ÷ 2 = 1, resto: 0")
print("1 ÷ 2 = 0, resto: 1")
print("Los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es '1010'.")

num_usuario = int(input("Ingrese un número para convertir a binario: "))
if num_usuario == 0:
    print("El número binario es: 0")
else:
    print(f"El número binario es: {decimal_a_binario(num_usuario)}")

# 5 -----------------------------------------------------

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True  # Caso base: una letra o vacío es palíndromo
    if palabra[0] != palabra[-1]:
        return False  # Si los extremos no coinciden, no es palíndromo
    # Llamada recursiva con la palabra sin los extremos
    return es_palindromo(palabra[1:-1])


texto = input("Ingrese una palabra para verificar si es palíndromo: ")
if es_palindromo(texto):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")

# 6 -----------------------------------------------------

def suma_digitos(n):
    if n < 10:
        return n  # un solo dígito
    else:
        return n % 10 + suma_digitos(n // 10)  # Suma el último dígito y llama recursivamente con el resto

numero = int(input("Ingrese un número para sumar sus dígitos: "))
print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}")

# 7 -----------------------------------------------------
def contar_bloques(n):

    if n == 1:
        return 1  # Caso base: solo un bloque en el último nivel
    else:
        return n + contar_bloques(n - 1)  # Suma los bloques del nivel actual y los de los niveles superiores


niveles = int(input("Ingrese la cantidad de bloques en el nivel más bajo de la pirámide: "))
print(f"Total de bloques necesarios: {contar_bloques(niveles)}")

# 8 -----------------------------------------------------
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)


num = int(input("Ingrese un número: "))
d = int(input("Ingrese el dígito (0-9): "))
print(f"El dígito {d} aparece {contar_digito(num, d)} veces en {num}.")