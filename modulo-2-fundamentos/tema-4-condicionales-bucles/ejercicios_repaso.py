

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