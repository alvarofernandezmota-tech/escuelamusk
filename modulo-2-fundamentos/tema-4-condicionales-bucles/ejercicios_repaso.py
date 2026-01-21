

# EJERCICIO R1: Clasificador de números
#
# Haz un programa que lea exactamente 8 números enteros y muestre:
# - Cuántos son PARES y cuántos IMPARES
# - Cuántos son POSITIVOS, NEGATIVOS y CEROS
# - El MAYOR de todos los números leídos
#
# EJEMPLO DE EJECUCIÓN:
# Número 1: 5
# Número 2: -3
# Número 3: 0
# Número 4: 8
# Número 5: -7
# Número 6: 12
# Número 7: 0
# Número 8: 4
#
# SALIDA ESPERADA:
# Pares: 4
# Impares: 4
# Positivos: 4
# Negativos: 2
# Ceros: 2
# Mayor: 12
#
# PISTAS:
# - Usa un bucle for con range(8)
# - Necesitas 5 contadores: pares, impares, positivos, negativos, ceros
# - Para el máximo, inicialízalo con el primer número leído
# - Recuerda: un número es par si numero % 2 == 0
mayor = None
contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0
contador_ceros = 0
for i in range(8):
    numero = int(input(f"Número {i + 1}: "))
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
    if numero > 0:
        contador_positivos += 1
    elif numero < 0:
        contador_negativos += 1
    else:
        contador_ceros += 1
    if mayor is None or numero > mayor:
        mayor = numero  
print(f"Pares: {contador_pares}")
print(f"Impares: {contador_impares}")
print(f"Positivos: {contador_positivos}")
print(f"Negativos: {contador_negativos}")
print(f"Ceros: {contador_ceros}")
print(f"Mayor: {mayor}")


# EJERCICIO R2: Secuencia hasta encontrar múltiplo
#
# Haz un programa que:
# 1. Lea un número entero positivo N
# 2. Luego lea una secuencia de números acabada en 0 (centinela)
# 3. Muestre el PRIMER número de la secuencia que sea múltiplo de N
# 4. Si NO hay ningún múltiplo, debe mostrar un mensaje indicándolo
# 5. Al final, muestre cuántos números se leyeron antes de terminar
#    (sin contar el centinela 0 ni el N inicial)
#
# EJEMPLO DE EJECUCIÓN:
N = int(input("Introduce N: "))
contador_numeros = 0
encontrado = False  
primer_multiplo = None  
numero = int(input("Número (0 para terminar): "))
while numero != 0:
    contador_numeros += 1
    if encontrado == False and numero % N == 0:
        primer_multiplo = numero
        encontrado = True
        break
    numero = int(input("Número (0 para terminar): "))
if encontrado == False:
    print(f"No se encontró ningún múltiplo de {N}.")
else:
    print(f"El primer múltiplo de {N} es: {primer_multiplo}")
print(f"Números leídos antes de terminar: {contador_numeros}")

# EJERCICIO R3: Validador de secuencia creciente
#
# Haz un programa que lea una secuencia de números acabada en -1 (centinela)
# y verifique si la secuencia es ESTRICTAMENTE CRECIENTE
# (cada número es mayor que el anterior).
#
# El programa debe mostrar:
# - "La secuencia es creciente" si todos los números son mayores que el anterior
# - "La secuencia NO es creciente" en caso contrario
# - Si solo se introduce un número (o ninguno), debe indicar
#   "No hay suficientes números para comparar"
# EJEMPLO DE EJECUCIÓN:
anterior = None
creciente = True
contador = 0
numero = int(input("Número (-1 para terminar): "))
while numero != -1:
    contador += 1
    if anterior is not None and numero <= anterior:
        creciente = False      
        break       
    anterior = numero
    numero = int(input("Número (-1 para terminar): "))
if contador < 2:
    print("No hay suficientes números para comparar")   
elif creciente:
    print("La secuencia es creciente")  
else:
    print("La secuencia NO es creciente")
    #SE ME DA MAS O MENOS 

# EJERCICIO R4: Calculadora de estadísticas
#
# Haz un programa que lea números decimales (float) acabados en 0 (centinela)
# y calcule:
# - La SUMA de todos los números
# - El PROMEDIO (media aritmética)
# - Cuántos números son MAYORES que el promedio
#
# NOTA: Debes leer todos los números primero, calcular el promedio,
# y luego volver a recorrer para contar cuántos son mayores que el promedio.
#
# EJEMPLO DE EJECUCIÓN:
# Número (0 para terminar): 5.5
# Número (0 para terminar): 8.0
# Número (0 para terminar): 3.2
# Número (0 para terminar): 9.1
# Número (0 para terminar): 6.7
# Número (0 para terminar): 0
#
# Suma: 32.5
# Promedio: 6.5
# Números mayores que el promedio: 3
#
# EXPLICACIÓN:
# - Números: 5.5, 8.0, 3.2, 9.1, 6.7
# - Suma = 5.5 + 8.0 + 3.2 + 9.1 + 6.7 = 32.5
# - Promedio = 32.5 / 5 = 6.5
# - Mayores que 6.5: 8.0, 9.1, 6.7 → 3 números
#
# PISTAS:
# - Usa centinela 0
# - Usa una LISTA para almacenar todos los números
# - append() para guardar en la lista
# - Primer bucle: leer y guardar
# - Calcular suma con sum() o con bucle
# - Calcular promedio: suma / len(lista)
# - Segundo bucle: recorrer lista y contar mayores que promedio
numero = float(input("Número (0 para terminar): "))
numeros = []
contador = 0
suma = 0
promedio = 0
while numero != 0:
    numeros.append(numero)
    numero = float(input("Número (0 para terminar): "))
suma = sum(numeros)
promedio = suma / len(numeros)
for numero in numeros:
    if numero > promedio:
        contador += 1
print(f"Suma: {suma}")
print(f"Promedio: {promedio}")
print(f"Números mayores que el promedio: {contador}")