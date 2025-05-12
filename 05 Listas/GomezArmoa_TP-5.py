# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range.

num_multiplos_4 = list(range(4, 101, 4 ))

print("Los números múltiplos de 4 entre 1 y 100 son:")
print(num_multiplos_4)

#-----------------------------------------------------------------------------------------------
# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

elementos = ["Perro", "Gato", "Elefante", "Tigre", "Pato"]
print("El penúltimo elemento de la lista es:", elementos[-2])

#-----------------------------------------------------------------------------------------------
# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
# ejemplo:
# lista_vacia = []

lista_vacia = []
lista_vacia.append("Perro")
lista_vacia.append("Gato")
lista_vacia.append("Pato")
print("Lista resultante:", lista_vacia)
#-----------------------------------------------------------------------------------------------
# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!
# animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"  # Reemplazar el segundo elemento
animales[-1] = "oso"  # Reemplazar el último elemento
print("Lista resultante:", animales)
#-----------------------------------------------------------------------------------------------
# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# numeros = [8, 15, 3, 22, 8]numeros.remove(max(numeros))
# print(numeros)

# El programa crea una lista llamada "numeros" con cinco elementos. Luego, utiliza la función max() para
#  encontrar el valor máximo de la lista y lo elimina con el método remove(). Finalmente, imprime la
#  lista resultante sin el número máximo.

#-----------------------------------------------------------------------------------------------
# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.

numeros = list(range(10, 31, 5))
print("Los dos primeros números de la lista son:", numeros[:2])
#-----------------------------------------------------------------------------------------------
# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.
# autos = ["sedan", "polo", "suran", "gol"]

autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camioneta", "camion"]  # Reemplazar los valores en los índices 1 y 2

print("Lista resultante:", autos)
#-----------------------------------------------------------------------------------------------
# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Lista resultante:", dobles)
#-----------------------------------------------------------------------------------------------
# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
# ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"
# c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")
# d) Imprimir la lista resultante por pantalla
print("Lista resultante:", compras)
#-----------------------------------------------------------------------------------------------
# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("Lista anidada:", lista_anidada)

