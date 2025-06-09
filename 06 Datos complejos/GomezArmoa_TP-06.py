# 1 Diccionario de precios de frutas y agregar nuevas frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2 Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3 lista solo con los nombres de las frutas
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)

# 4 Agenda de contactos telefónicos
contactos = {}
print("\nCargar 5 contactos:")
for i in range(5):
    nombre = input(f"Ingresá nombre del contacto {i+1}: ")
    numero = input(f"Ingresá número de {nombre}: ")
    contactos[nombre] = numero

consulta = input("\nIngresá el nombre del contacto: ")
if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print("Contacto no encontrado.")

# 5 Palabras únicas y recuento de palabras.

frase = input("Ingresr frase: ")
palabras = frase.split()

# Palabras únicas usando set
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

# Recuento de palabras.
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1
print("Recuento:", recuento)

# 6 Ingresar 3 alumnos y sus 3 notas, mostrar el promedio de c/u.

alumnos = {}
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas = input(f"Ingresá 3 notas separando con comas {nombre}: ")
    # Convertir las notas a enteros y guardarlas como tupla
    tupla_notas = tuple(int(nota.strip()) for nota in notas.split(","))
    alumnos[nombre] = tupla_notas

print("\nPromedio de cada alumno:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

# 7) Operaciones con sets de estudiantes que aprobaron

aprobados_parcial1 = {11, 12, 13, 14, 15}
aprobados_parcial2 = {14, 15, 16, 17}

# Estudiantes que aprobaron ambos parciales intersección
ambos = aprobados_parcial1 & aprobados_parcial2
print("Aprobaron ambos parciales:", ambos)

# Estudiantes que aprobaron solo uno de los dos dif
solo_uno = aprobados_parcial1 ^ aprobados_parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

# Lista total de estudiantes que aprobaron al menos un parcial unión
total = aprobados_parcial1 | aprobados_parcial2
print("Aprobaron al menos un parcial:", total)

# 8) Diccionario de productos y stock

productos = {
    "Arroz": 20,
    "Fideos": 15,
    "Aceite": 10,
    "Azúcar": 8
}

producto = input("Ingresá el nombre del producto a consultar o agregar: ")

if producto in productos:
    print(f"Stock actual de {producto}: {productos[producto]}")
    agregar = input("¿Querés agregar unidades al stock? (s/n): ").lower()
    if agregar == "s":
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        productos[producto] += unidades
        print(f"Nuevo stock de {producto}: {productos[producto]}")
else:
    print(f"{producto} no existe en el inventario.")
    agregar_nuevo = input("¿Querés agregar este producto? (s/n): ").lower()
    if agregar_nuevo == "s":
        unidades = int(input("¿Cuántas unidades tiene?: "))
        productos[producto] = unidades
        print(f"{producto} agregado con stock: {productos[producto]}")

# 9) Agenda con claves (día, hora) y valores eventos

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

dia = input("Ingresá el día a consultar: ").lower()
hora = input("Ingresá la hora a consultar (ej: 10:00): ")

clave = (dia, hora)
if clave in agenda:
    print(f"Actividad para {dia} a las {hora}: {agenda[clave]}")
else:
    print(f"No hay actividad agendada para {dia} a las {hora}.")


# 10) Invertir diccionario de países y capitales

original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {capital: pais for pais, capital in original.items()}

print("Diccionario original:", original)
print("Diccionario invertido:", invertido)







