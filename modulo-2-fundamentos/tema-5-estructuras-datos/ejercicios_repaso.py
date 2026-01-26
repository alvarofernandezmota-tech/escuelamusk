# modulo-2-fundamentos/tema-5-estructuras-datos/listas-tuplas/practica_bucles_listas.py

"""
🎯 PRÁCTICA INTEGRADA: Bucles + Listas + Tuplas
Repaso de for/while aplicados a estructuras de datos
"""

print("=" * 50)
print("NIVEL 1: FOR CON LISTAS - Recorrido básico")
print("=" * 50)

# Ejercicio 1: Recorrer lista y mostrar cada elemento
print("\n--- Ejercicio 1: Imprimir elementos ---")
frutas = ["manzana", "pera", "naranja", "plátano"]
for fruta in  frutas:
    print(f"fruta: {fruta}")

# TODO: Recorre la lista con for y muestra cada fruta
# for fruta in frutas:
#     print(f"Fruta: {fruta}")


# Ejercicio 2: Recorrer con índice usando range()
print("\n--- Ejercicio 2: Recorrer con índice ---")
numeros = [10, 20, 30, 40, 50]
for i in range(len(numeros)):
    print(f"posicion: {i} and numero {numeros[i]}")
# TODO: Usa for i in range(len(numeros)) para mostrar índice y valor
# for i in range(len(numeros)):
#     print(f"Posición {i}: {numeros[i]}")


# Ejercicio 3: Sumar todos los elementos
print("\n--- Ejercicio 3: Suma con for ---")
valores = [5, 10, 15, 20, 25]
suma = 0 
for numeros in valores:
    suma += numeros
print(f"la suma total es : {suma}")





# TODO: Suma todos los valores usando un bucle for
# suma = 0
# for valor in valores:
#     suma += valor
# print(f"Suma total: {suma}")


print("\n" + "=" * 50)
print("NIVEL 2: WHILE CON LISTAS - Control manual")
print("=" * 50)

# Ejercicio 4: Recorrer lista con while
print("\n--- Ejercicio 4: While con índice ---")
colores = ["rojo", "verde", "azul", "amarillo"]
i = 0
while i < len(colores):
    print(f"{i}: {colores[i]}")
    i+=1





# TODO: Usa while para recorrer la lista con índice
# i = 0
# while i < len(colores):
#     print(f"{i}: {colores[i]}")
#     i += 1


# Ejercicio 5: While con centinela - Buscar elemento
print("\n--- Ejercicio 5: Buscar con while ---")
numeros = [3, 7, 12, 18, 25, 30]
buscar = 18
i = 0
encontarado = False
while i < len(numeros) and encontarado == False:
    if numeros[i] == buscar:
        print(f"{buscar} estaba en la posicion {i}")
        encontarado = True
    i += 1
if encontarado == False:
    print(f"no encontrado {buscar} en {numeros}")






# TODO: Busca el número usando while (detente cuando lo encuentres)
# i = 0
# encontrado = False
# while i < len(numeros) and not encontrado:
#     if numeros[i] == buscar:
#         print(f"Encontrado {buscar} en posición {i}")
#         encontrado = True
#     i += 1


print("\n" + "=" * 50)
print("NIVEL 3: FOR + LISTAS - Modificación")
print("=" * 50)

# Ejercicio 6: Crear nueva lista con transformación
print("\n--- Ejercicio 6: Crear lista de dobles ---")
originales = [1, 2, 3, 4, 5]
dobles = []
for numeros in originales:
    dobles.append(numeros *2)
print(f" los orginales son: {originales}")
print(f" los dobles son: {dobles}")















# TODO: Crea una nueva lista con el doble de cada número
# dobles = []
# for num in originales:
#     dobles.append(num * 2)
# print(f"Originales: {originales}")
# print(f"Dobles: {dobles}")


# Ejercicio 7: Filtrar elementos (solo pares)
print("\n--- Ejercicio 7: Filtrar números pares ---")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# TODO: Crea lista solo con números pares
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(f"originales:{numero}")
print(f"pares:{pares}")

        




# pares = []
# for num in numeros:
#     if num % 2 == 0:
#         pares.append(num)
# print(f"Pares: {pares}")


print("\n" + "=" * 50)
print("NIVEL 4: TUPLAS + BUCLES - Inmutabilidad")
print("=" * 50)

# Ejercicio 8: Recorrer tupla
print("\n--- Ejercicio 8: For con tupla ---")
coordenadas = (10, 20, 30, 40)
for coord in coordenadas:
    print(f"cordaenadas: {coord}")














# TODO: Recorre la tupla y muestra cada elemento
# for coord in coordenadas:
#     print(f"Coordenada: {coord}")


# Ejercicio 9: Convertir tupla a lista, modificar y volver
print("\n--- Ejercicio 9: Tupla → Lista → Tupla ---")
dias_semana = ("lunes", "martes", "miercoles", "jueves", "viernes")
semana_list = list(dias_semana)
semana_list.append("sabado")
semana_list.append("domingo")
dias_completos = tuple(semana_list)
print(f"la tupla original es {dias_semana}")
print(f"la tupla corregida completa es {dias_completos}")














# TODO: Convierte a lista, añade "sábado" y "domingo", vuelve a tupla
# dias_lista = list(dias_semana)
# dias_lista.append("sábado")
# dias_lista.append("domingo")
# dias_completos = tuple(dias_lista)
# print(f"Tupla original: {dias_semana}")
# print(f"Tupla completa: {dias_completos}")


print("\n" + "=" * 50)
print("NIVEL 5: BUCLES ANIDADOS + LISTAS")
print("=" * 50)

# Ejercicio 10: Lista de listas (matriz)
print("\n--- Ejercicio 10: Recorrer matriz ---")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()

# TODO: Usa bucles anidados para mostrar cada elemento
# for fila in matriz:
#     for elemento in fila:
#         print(elemento, end=" ")
#     print()  # Salto de línea después de cada fila


print("\n" + "=" * 50)
print("NIVEL 6: EJERCICIOS COMBINADOS - Reto")
print("=" * 50)

# Ejercicio 11: Contar ocurrencias
print("\n--- Ejercicio 11: Contar repeticiones ---")
letras = ["a", "b", "a", "c", "a", "b", "d"]
letra_buscar = "a"
contador = 0
for letra in letras:
    if letra == letra_buscar:
        contador += 1
print(f"hay {contador} de {letra_buscar} en {letras}")
















# TODO: Cuenta cuántas veces aparece la letra usando for
# contador = 0
# for letra in letras:
#     if letra == letra_buscar:
#         contador += 1
# print(f"La letra '{letra_buscar}' aparece {contador} veces")


# Ejercicio 12: Encontrar máximo con for
print("\n--- Ejercicio 12: Máximo con for ---")
temperaturas = [18, 22, 19, 25, 21, 20, 23]

# TODO: Encuentra la temperatura máxima usando for
# max_temp = temperaturas[0]
# for temp in temperaturas:
#     if temp > max_temp:
#         max_temp = temp
# print(f"Temperatura máxima: {max_temp}°C")


# Ejercicio 13: Lista de índices donde cumple condición
print("\n--- Ejercicio 13: Índices de números >15 ---")
valores = [10, 20, 12, 18, 25, 8, 30]

# TODO: Crea lista con los índices donde el valor es >15
# indices_mayores = []
# for i in range(len(valores)):
#     if valores[i] > 15:
#         indices_mayores.append(i)
# print(f"Índices con valor >15: {indices_mayores}")


# Ejercicio 14: While con input - Llenar lista hasta centinela
print("\n--- Ejercicio 14: Llenar lista con while (simulado) ---")
# En clase harías input(), aquí lo simulamos con lista predefinida
entradas = [5, 10, 15, 0, 20, 25]  # 0 es centinela

# TODO: Procesa hasta encontrar el 0
# numeros_validos = []
# i = 0
# while i < len(entradas) and entradas[i] != 0:
#     numeros_validos.append(entradas[i])
#     i += 1
# print(f"Números válidos: {numeros_validos}")


print("\n" + "=" * 50)
print("🎉 ¡Práctica completada!")
print("=" * 50)
