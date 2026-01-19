""""

# 📘 EJERCICIOS RESUELTOS - MÓDULO 2 - TEMA 4
## Condicionales y Bucles

---

## 📑 ÍNDICE

1. [Operaciones Básicas](#1-operaciones-básicas)
2. [Strings y Validaciones](#2-strings-y-validaciones)
3. [Bucles `for` Básicos](#3-bucles-for-básicos)
4. [Bucles `for` con Listas](#4-bucles-for-con-listas)
5. [Bucles `while` - Extracción de Dígitos](#5-bucles-while---extracción-de-dígitos)
6. [Bucles `while` - Procesamiento de Dígitos](#6-bucles-while---procesamiento-de-dígitos)
7. [Bucles `while` - Inversión](#7-bucles-while---inversión)
8. [Bucles `for` + `while` Combinados](#8-bucles-for--while-combinados)

## 1. OPERACIONES BÁSICAS

### 🟢 Ejercicio 1.1: Suma de Dos Números

**📝 Enunciado:**
Haz un programa que pida dos números enteros y muestre su suma.

**🧪 Ejemplo:**
Introduce el primer número: 5
Introduce el segundo número: 3
La suma de 5 y 3 es: 8

text

**💻 Solución:**
```python
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
suma = a + b
print(f"La suma de {a} y {b} es: {suma}")
🟢 Ejercicio 1.2: Operaciones Matemáticas
📝 Enunciado:
Programa que demuestra las diferentes operaciones matemáticas en Python.

💻 Solución:

python
print(17 // 3)      # División entera: 5
print(17 / 3)       # División normal: 5.666...
print(17 % 3)       # Módulo (resto): 2
print(2 ** 3)       # Exponenciación: 8
print(2 + 3 * 4)    # Multiplicación antes que suma: 14
print((2 + 3) * 4)  # Paréntesis cambian orden: 20
print(7 % 4)        # Resto: 3
print(10 % 2)       # Resto: 0 (divisible)
2. STRINGS Y VALIDACIONES
🟢 Ejercicio 2.1: Vocal o Consonante
📝 Enunciado:
Haz un programa que pida una letra y detecte si es vocal o consonante. Debe validar que solo sea UNA letra.

🧪 Ejemplo:

text
Introduce una letra: a
a es una vocal.

Introduce una letra: b
b es una consonante.

Introduce una letra: abc
Por favor, introduce solo una letra.
💻 Solución:

python
letra = input("Introduce una letra: ")
if len(letra) != 1 or not letra.isalpha():
    print("Por favor, introduce solo una letra.")
else:
    if letra.lower() in "aeiou":
        print(f"{letra} es una vocal.")
    elif letra.lower() in "bcdfghjklmnpqrstvwxyz":
        print(f"{letra} es una consonante.")
🟢 Ejercicio 2.2: Validar Contraseña Simple
📝 Enunciado:
Haz un programa que pida una contraseña y valide que:

Tenga al menos 6 caracteres

Contenga al menos un número

Contenga al menos una letra mayúscula

🧪 Ejemplo:

text
Introduce una contraseña: hola
La contraseña debe tener al menos 6 caracteres.

Introduce una contraseña: holamundo
La contraseña debe contener al menos un número.

Introduce una contraseña: holamundo1
La contraseña debe contener al menos una letra mayúscula.

Introduce una contraseña: HolaMundo1
Contraseña válida ✅
💻 Solución 1 (con any):

python
password = input("Introduce una contraseña: ")
if len(password) < 6:
    print("La contraseña debe tener al menos 6 caracteres.")
elif not any(text.isdigit() for text in password):
    print("La contraseña debe contener al menos un número.")
elif not any(text.isupper() for text in password):
    print("La contraseña debe contener al menos una letra mayúscula.") 
else:
    print("Contraseña válida ✅")
💻 Solución 2 (con bucle for):

python
password = input("Introduce una contraseña: ")
length_ok = len(password) >= 6
tiene_numero = False
tiene_mayuscula = False

for char in password:
    if char.isdigit():
        tiene_numero = True
    if char.isupper():
        tiene_mayuscula = True

if not length_ok:
    print("La contraseña debe tener al menos 6 caracteres.")
if not tiene_numero:
    print("La contraseña debe contener al menos un número.")    
if not tiene_mayuscula:
    print("La contraseña debe contener al menos una letra mayúscula.")
if length_ok and tiene_numero and tiene_mayuscula:
    print("Contraseña válida ✅")
🟢 Ejercicio 2.3: Validar Nombre de Usuario
📝 Enunciado:
Haz un programa que valide un nombre de usuario con estas reglas:

Longitud entre 4 y 12 caracteres

Solo letras y números (sin espacios ni símbolos)

Debe empezar con una letra

Debe contener al menos una letra minúscula

🧪 Ejemplos:

text
Usuario: ab
❌ Debe tener entre 4 y 12 caracteres

Usuario: usuario con espacios
❌ Solo puede contener letras y números

Usuario: 123hola
❌ Debe empezar con una letra

Usuario: HOLA123
❌ Debe contener al menos una letra minúscula

Usuario: Hola123
✅ Usuario válido
💻 Solución:

python
usuario = input("Usuario: ")
length_ok = 4 <= len(usuario) <= 12
alnum_ok = usuario.isalnum()
start_with_letter = usuario.isalpha()
tiene_minuscula = False

for char in usuario:
    if char.islower():
        tiene_minuscula = True  

if not length_ok:
    print("❌ Debe tener entre 4 y 12 caracteres")  
if not alnum_ok:
    print("❌ Solo puede contener letras y números") 
if not start_with_letter:
    print("❌ Debe empezar con una letra")
if not tiene_minuscula:
    print("❌ Debe contener al menos una letra minúscula")
if length_ok and alnum_ok and start_with_letter and tiene_minuscula:
    print("✅ Usuario válido")
🟢 Ejercicio 2.4: Validar Email
📝 Enunciado:
Haz un programa que valide un email con estas reglas:

Debe contener exactamente UN símbolo @

Debe contener al menos UN punto . después del @

No puede empezar ni terminar con @ o .

Debe tener al menos 5 caracteres

No puede contener espacios

🧪 Ejemplos:

text
Introduce un email: abc
❌ Debe tener al menos 5 caracteres

Introduce un email: abc@com
❌ Debe contener al menos UN punto . después del @

Introduce un email: user@domain.com
✅ Email válido
💻 Solución:

python
email = input("Introduce un email: ")
length_ok = len(email) >= 5
at_count = email.count("@")
not_finish_with_invalid = email[-1] not in "@."
not_start_with_invalid = email not in "@."
not_space = " " not in email
tiene_punto_despues_arroba = email.find(".") > email.find("@")

if at_count != 1:
    print("❌ Debe contener exactamente UN símbolo @")    
if not tiene_punto_despues_arroba:
    print("❌ Debe contener al menos UN punto . después del @") 
if not not_finish_with_invalid:
    print("❌ No puede terminar con @ o .")  
if not not_start_with_invalid:
    print("❌ No puede empezar con @ o .")              
if not length_ok:
    print("❌ Debe tener al menos 5 caracteres")    
if not not_space:
    print("❌ No puede contener espacios")  
if (at_count == 1 and tiene_punto_despues_arroba and 
    not_finish_with_invalid and not_start_with_invalid and 
    length_ok and not_space):
    print("✅ Email válido")
3. BUCLES for BÁSICOS
🟢 Ejercicio 3.1: Imprimir Números del 0 al 7
💻 Solución:

python
for i in range(8):
    print(i)
🟢 Ejercicio 3.2: Imprimir del 3 al 8
💻 Solución:

python
for i in range(3, 9):
    print(i)
🟢 Ejercicio 3.3: Imprimir "Hola" 10 veces
💻 Solución:

python
for i in range(10):
    print("Hola")
🟢 Ejercicio 3.4: Imprimir del 15 al 20
💻 Solución:

python
for i in range(15, 21):
    print(i)
🟢 Ejercicio 3.5: Imprimir Pares del 0 al 10
💻 Solución:

python
for i in range(0, 11, 2):
    print(i)
🟢 Ejercicio 3.6: Imprimir Impares del 1 al 15
💻 Solución:

python
for i in range(1, 16, 2):
    print(i)
🟢 Ejercicio 3.7: Múltiplos de 10 del 0 al 100
💻 Solución:

python
for i in range(0, 101, 10):
    print(i)
🟢 Ejercicio 3.8: Cuenta Regresiva del 5 al 0
💻 Solución:

python
for i in range(5, -1, -1):
    print(i)
🟢 Ejercicio 3.9: Del 20 al 10 Descendente
💻 Solución:

python
for i in range(20, 9, -1):
    print(i)
🟢 Ejercicio 3.10: Tabla del 3
💻 Solución:

python
for i in range(1, 11):
    print(i * 3)
🟢 Ejercicio 3.11: Suma de Números del 0 al 20
📝 Enunciado:
Suma todos los números del 0 al 20.

💻 Solución:

python
suma = 0
for i in range(0, 21):
    suma += i
print(suma)
🟢 Ejercicio 3.12: Múltiplos de 3 entre 3 y 30
💻 Solución:

python
for i in range(3, 31):
    if i % 3 == 0:
        print(i)
🟢 Ejercicio 3.13: Pares entre 2 y 50
💻 Solución:

python
for i in range(2, 51):
    if i % 2 == 0:
        print(i)
🟢 Ejercicio 3.14: Tabla de Multiplicar
📝 Enunciado:
Pide un número y muestra su tabla de multiplicar del 1 al 10.

💻 Solución:

python
numero = int(input("Introduce un número: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
🟢 Ejercicio 3.15: Impares del 1 al 19
💻 Solución:

python
for i in range(1, 20):
    if i % 2 != 0:
        print(i)
🟢 Ejercicio 3.16: Suma de Pares del 1 al 100
💻 Solución:

python
suma = 0
for i in range(1, 101):
    if i % 2 == 0:
        suma += i
print(suma)
🟢 Ejercicio 3.17: Cuenta Regresiva 10 a 1
💻 Solución:

python
for i in range(10, 0, -1):
    print(i)
🟢 Ejercicio 3.18: FizzBuzz (1 al 30)
📝 Enunciado:
Para números del 1 al 30:

Si es múltiplo de 3 y 5 → "FizzBuzz"

Si es múltiplo de 3 → "Fizz"

Si es múltiplo de 5 → "Buzz"

Si no → el número

💻 Solución:

python
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
4. BUCLES for CON LISTAS
🟢 Ejercicio 4.1: Contar Pares e Impares
📝 Enunciado:
Pide 5 números y cuenta cuántos son pares y cuántos impares.

💻 Solución:

python
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))
numero4 = int(input("Introduce el cuarto número: "))
numero5 = int(input("Introduce el quinto número: "))

pares = 0
impares = 0
numeros = [numero1, numero2, numero3, numero4, numero5]

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1    

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
🟢 Ejercicio 4.2: Clasificar por Relación con 10
📝 Enunciado:
Pide 5 números y cuenta cuántos son mayores, menores o iguales a 10.

💻 Solución:

python
mayor_de_10 = 0
menor_de_10 = 0
igual_a_10 = 0

for i in range(1, 6):
    numero = int(input("Introduce un número: "))
    if numero > 10:
        mayor_de_10 += 1
    elif numero < 10:
        menor_de_10 += 1
    else:
        igual_a_10 += 1

print(f"Números mayores que 10: {mayor_de_10}")
print(f"Números menores que 10: {menor_de_10}")
print(f"Números iguales a 10: {igual_a_10}")
🟢 Ejercicio 4.3: Mayor y Menor de una Lista
📝 Enunciado:
Pide 5 números y encuentra el mayor y el menor.

💻 Solución:

python
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))
numero4 = int(input("Introduce el cuarto número: "))
numero5 = int(input("Introduce el quinto número: "))

numeros = [numero1, numero2, numero3, numero4, numero5]
mayor = numeros
menor = numeros

for numero in numeros:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
🟢 Ejercicio 4.4: Pirámide de Asteriscos
📝 Enunciado:
Imprime una pirámide de asteriscos de 5 filas.

💻 Solución:

python
for i in range(1, 6):
    print("*" * i)
🟢 Ejercicio 4.5: Buscar Número en Lista
📝 Enunciado:
Pide n números, guárdalos en una lista y busca un número específico.

💻 Solución:

python
n = int(input("¿De cuántos números va a ser tu lista?: "))
lista = []

for i in range(n):
    numero = int(input(f"Introduce el número {i+1}: "))
    lista.append(numero)    

buscar = int(input("Introduce un número a buscar: "))
encontrado = False

for i in range(n):
    if lista[i] == buscar:
        print(f"El número {buscar} está en la posición: {i}")
        encontrado = True
        break

if not encontrado:
    print(f"El número {buscar} no se encuentra en la lista.")
🟢 Ejercicio 4.6: Crear Lista de 3 Números
💻 Solución:

python
lista = []
for i in range(3):
    numero = int(input("Introduce un número: "))
    lista.append(numero)
print(f"Números introducidos: {lista}")
🟢 Ejercicio 4.7: Suma de 4 Números
💻 Solución:

python
lista = []
for i in range(4):
    numero = int(input("Introduce el número: "))
    lista.append(numero)
suma = sum(lista)
print(f"La suma de los números es: {suma}")
🟢 Ejercicio 4.8: Contar Pares en Lista
💻 Solución:

python
lista = []
for i in range(5):
    numero = int(input("Introduce un número: "))
    lista.append(numero)

pares = 0
for numero in lista:
    if numero % 2 == 0:
        pares += 1

print(f"Números pares en la lista: {pares}")
🟢 Ejercicio 4.9: Mayor de una Lista
💻 Solución:

python
lista = []
for i in range(4):
    numero = int(input(f"Introduce el número {i+1}: "))
    lista.append(numero)

mayor = max(lista)
print(f"El número mayor de la lista es: {mayor}")
🟢 Ejercicio 4.10: Invertir Lista
💻 Solución:

python
lista = []
for i in range(5):
    numero = int(input(f"Introduce el número {i+1}: "))
    lista.append(numero)

print(f"Lista original: {lista}")
lista.reverse()
print(f"Lista invertida: {lista}")
🟢 Ejercicio 4.11: Eliminar Duplicados
💻 Solución:

python
lista = []
for i in range(6):
    numero = int(input("Introduce número: "))
    lista.append(numero)

print(f"La lista sin duplicados es: {list(set(lista))}")
5. BUCLES while - EXTRACCIÓN DE DÍGITOS
🟢 Ejercicio 5.1: Cuenta Regresiva con While
💻 Solución:

python
contador = 5
while contador > 0:
    print(contador)
    contador -= 1
print("¡Despegue!")
🟢 Ejercicio 5.2: Obtener Último Dígito
📝 Enunciado:
Pide un número y muestra su último dígito.

💻 Solución:

python
n = int(input("Introduce un número: "))
ultimo_digito = n % 10
print(f"El último dígito es: {ultimo_digito}")
🟢 Ejercicio 5.3: Quitar Último Dígito
💻 Solución:

python
n = int(input("Introduce un número: "))
sin_ultimo = n // 10
print(f"El número sin el último dígito es: {sin_ultimo}")
🟢 Ejercicio 5.4: Imprimir Números del 1 al 5
💻 Solución:

python
numero = 1
while numero <= 5:
    print(numero)
    numero = numero + 1
🟢 Ejercicio 5.5: Cuenta Regresiva del 5 al 0
💻 Solución:

python
numero = 5
while numero >= 0:
    print(numero)
    numero = numero - 1
🟢 Ejercicio 5.6: Suma del 1 al 4
💻 Solución:

python
numero = 1
suma = 0
while numero <= 4:
    suma = suma + numero
    numero = numero + 1 
print(f"La suma es: {suma}")
🟢 Ejercicio 5.7: Contar del 1 al 6
💻 Solución:

python
numero = 1
contador = 0
while numero <= 6:
    contador = contador + 1
    numero = numero + 1
print(f"He contado: {contador} números.")
🟢 Ejercicio 5.8: Suma de Pares (2, 4, 6)
💻 Solución:

python
numero = 2
suma = 0
while numero <= 6:
    suma = suma + numero
    numero = numero + 2
print(f"La suma es: {suma}")
🟢 Ejercicio 5.9: Imprimir Dígitos al Revés
📝 Enunciado:
Pide un número y muestra sus dígitos al revés, uno por línea.

💻 Solución:

python
n = int(input("Introduce un número: "))
while n > 0:
    digito = n % 10
    print(digito)
    n = n // 10
🟢 Ejercicio 5.10: Contar Dígitos
📝 Enunciado:
Pide un número y cuenta cuántos dígitos tiene.

💻 Solución:

python
n = int(input("Introduce un número: "))
contador = 0
while n > 0:
    contador = contador + 1 
    n = n // 10
print(contador)
🟢 Ejercicio 5.11: Suma de Dígitos
💻 Solución:

python
n = int(input("Introduce un número: "))
suma = 0
while n > 0:
    digito = n % 10 
    suma = suma + digito
    n = n // 10
print(f"La suma de los dígitos es: {suma}")
🟢 Ejercicio 5.12: Preservar Número Original con temp
📝 Enunciado:
Muestra los dígitos al revés pero conserva el número original.

💻 Solución:

python
n = int(input("Introduce un número: "))
temp = n
while temp > 0:
    digito = temp % 10
    print(digito)
    temp = temp // 10
print(f"El número principal es: {n}")
6. BUCLES while - PROCESAMIENTO DE DÍGITOS
🟢 Ejercicio 6.1: Buscar Dígito 5
💻 Solución:

python
n = int(input("Introduce un número: "))
temp = n
while temp > 0:
    digito = temp % 10
    print(digito)
    if digito == 5:
        print("Encontré un 5")
    temp = temp // 10
🟢 Ejercicio 6.2: Contar Dígitos Impares
💻 Solución:

python
n = int(input("Introduce un número: "))
temp = n
contador = 0
while temp > 0:
    digito = temp % 10
    if digito % 2 != 0:
        contador = contador + 1
    temp = temp // 10
print(f"Hay {contador} dígitos impares")
🟢 Ejercicio 6.3: Contar Ceros
💻 Solución:

python
n = int(input("Introduce un número: "))
temp = n
contador = 0
while temp > 0:
    digito = temp % 10
    if digito == 0:
        contador = contador + 1
    temp = temp // 10
print(f"Hay {contador} ceros")
🟢 Ejercicio 6.4: Dígito Mayor
💻 Solución:

python
n = int(input("Introduce un número: "))
temp = n
mayor = 0
while temp > 0:
    digito = temp % 10
    if digito > mayor:
        mayor = digito
    temp = temp // 10
print(f"El número mayor es {mayor}")
🟢 Ejercicio 6.5: Contar Impares y Mayor
💻 Solución:

python
n = int(input("Introduce un número: "))
temp = n
contador = 0
mayor = 0
while temp > 0:
    digito = temp % 10
    if digito % 2 != 0:
        contador = contador + 1
    if digito > mayor:
        mayor = digito 
    temp = temp // 10
print(f"Hay {contador} impares.")
print(f"El número mayor es {mayor}")
🟢 Ejercicio 6.6: Dígito Mayor y Menor
💻 Solución:

python
n = int(input("Introduce un número: "))
temp = n
menor = n % 10
mayor = 0
while temp > 0:
    digito = temp % 10
    if digito > mayor:
        mayor = digito
    if digito < menor:
        menor = digito
    temp = temp // 10
print(f"El dígito mayor es: {mayor}")
print(f"El dígito menor es: {menor}")
🟢 Ejercicio 6.7: Suma Total y Contar Pares
💻 Solución:

python
n = int(input("Introduce un número: "))
temp = n
suma = 0
contador = 0
while temp > 0:
    digito = temp % 10
    suma = suma + digito
    if digito % 2 == 0:
        contador = contador + 1
    temp = temp // 10
print(f"La suma de los dígitos es: {suma}")
print(f"Hay {contador} dígitos pares")
🟢 Ejercicio 6.8: Producto de Dígitos Pares
💻 Solución:

python
n = int(input("Introduce un número: "))
temp = n
producto = 1
hay_pares = False

while temp > 0:
    digito = temp % 10
    if digito % 2 == 0:
        producto = producto * digito
        hay_pares = True
    temp = temp // 10

if hay_pares:
    print(f"El producto de los dígitos pares es: {producto}")
else:
    print("El producto de los dígitos pares es: 0")
🟢 Ejercicio 6.9: Suma Mayores y Menores que 5
💻 Solución:

python
n = int(input("Introduce un número: "))
temp = n
suma_menores_cinco = 0
suma_mayores_cinco = 0
while temp > 0:
    digito = temp % 10
    if digito >= 5:
        suma_mayores_cinco = suma_mayores_cinco + digito
    else:
        suma_menores_cinco = suma_menores_cinco + digito
    temp = temp // 10
print(f"Suma de dígitos >= 5: {suma_mayores_cinco}")
print(f"Suma de dígitos < 5: {suma_menores_cinco}")
🟢 Ejercicio 6.10: Estadísticas Completas
📝 Enunciado:
Pide un número y muestra:

Total de dígitos

Dígitos pares

Dígitos impares

Dígito mayor

Dígito menor

💻 Solución:

python
n = int(input("Introduce un número: "))
temp = n
contador = 0
contador_pares = 0
contador_impares = 0 
mayor = 0
menor = n % 10

while temp > 0:
    digito = temp % 10
    contador = contador + 1
    if digito % 2 == 0:
        contador_pares = contador_pares + 1 
    else:
        contador_impares = contador_impares + 1
    if digito > mayor:
        mayor = digito
    if digito < menor:
        menor = digito
    temp = temp // 10

print(f"Total de dígitos: {contador}")
print(f"Dígitos pares: {contador_pares}")
print(f"Dígitos impares: {contador_impares}")
print(f"Dígito mayor: {mayor}")
print(f"Dígito menor: {menor}")
7. BUCLES while - INVERSIÓN
🟢 Ejercicio 7.1: Invertir un Número
📝 Enunciado:
Pide un número y muéstralo invertido.

🧪 Ejemplo:

text
Introduce un número: 12345
Número invertido: 54321
💻 Solución:

python
n = int(input("Introduce un número: "))
temp = n
invertido = 0
while temp > 0:
    digito = temp % 10
    invertido = invertido * 10 + digito
    temp = temp // 10
print(f"Número invertido: {invertido}")
🟢 Ejercicio 7.2: Invertir Solo Pares
📝 Enunciado:
Construye un número con solo los dígitos pares invertidos.

💻 Solución:

python
n = int(input("Introduce un número: "))
temp = n
pares_invertido = 0
while temp > 0:
    digito = temp % 10
    if digito % 2 == 0:
        pares_invertido = pares_invertido * 10 + digito
    temp = temp // 10
print(f"Pares invertidos: {pares_invertido}")
🟢 Ejercicio 7.3: Número Capicúa
📝 Enunciado:
Indica si un número es capicúa (se lee igual al derecho y al revés).

💻 Solución:

python
n = int(input("Introduce un número: "))
temp = n
invertido = 0

while temp > 0:
    digito = temp % 10
    invertido = invertido * 10 + digito 
    temp = temp // 10

if invertido == n:
    print(f"El número {n} es capicúa")
else:
    print(f"El número {n} NO es capicúa")
8. BUCLES for + while COMBINADOS
🟢 Ejercicio 8.1: Contar Pares en un Rango
📝 Enunciado:
Pide dos números (inicio y fin). Cuenta cuántos pares hay entre ellos.

💻 Solución:

python
inicio = int(input("Inicio: "))
fin = int(input("Fin: "))
contador = 0

for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        contador = contador + 1

print(f"Hay {contador} pares entre {inicio} y {fin}")
🟢 Ejercicio 8.2: Suma de Múltiplos en un Rango
📝 Enunciado:
Pide inicio, fin y un número n. Suma todos los múltiplos de n en ese rango.

💻 Solución:

python
inicio = int(input("Inicio: "))
fin = int(input("Fin: "))
n = int(input("Introduce el múltiplo: "))
suma = 0

for numero in range(inicio, fin + 1):
    if numero % n == 0:
        suma = suma + numero

print(f"La suma de los múltiplos de {n} es {suma}")
🟢 Ejercicio 8.3: Invertir Números en un Rango
📝 Enunciado:
Pide inicio y fin. Para cada número muestra el número y su invertido.

💻 Solución:

python
inicio = int(input("Inicio: "))
fin = int(input("Fin: "))

for numero in range(inicio, fin + 1):
    temp = numero 
    invertido = 0
    while temp > 0:
        digito = temp % 10
        invertido = invertido * 10 + digito
        temp = temp // 10
    print(f"{numero} → {invertido}")
🟢 Ejercicio 8.4: Contar Capicúas en un Rango
📝 Enunciado:
Pide inicio y fin. Cuenta cuántos números capicúas hay en ese rango.

💻 Solución:

python
inicio = int(input("Introduce el inicio: "))
fin = int(input("Introduce el fin: "))
contador_capicuas = 0

for numero in range(inicio, fin + 1):
    temp = numero 
    invertido = 0
    while temp > 0:
        digito = temp % 10 
        invertido = invertido * 10 + digito
        temp = temp // 10
    if invertido == numero:
        contador_capicuas = contador_capicuas + 1

print(f"Hay {contador_capicuas} números capicúas entre {inicio} y {fin}")
🟢 Ejercicio 8.5: Suma de Invertidos en un Rango
📝 Enunciado:
Pide inicio y fin. Para cada número, invierte el número y suma todos los invertidos.

💻 Solución:

python
inicio = int(input("Introduce el inicio: "))
fin = int(input("Introduce el fin: "))
suma_invertidos = 0

for numero in range(inicio, fin + 1):
    temp = numero
    invertido = 0
    while temp > 0:
        digito = temp % 10
        invertido = invertido * 10 + digito
        temp = temp // 10
    suma_invertidos = suma_invertidos + invertido

print(f"La suma de los invertidos entre {inicio} y {fin} es: {suma_invertidos}")
🎓 CONCEPTOS APRENDIDOS
✅ Bucles for:
range(inicio, fin)

range(inicio, fin, step)

Listas con append()

Búsqueda en listas

✅ Bucles while:
Extracción de dígitos: n % 10

Eliminar dígitos: n // 10

Variable temporal temp

Contadores y acumuladores

✅ Inversión de Números:
Fórmula: invertido = invertido * 10 + digito

Números capicúa

Filtrado de dígitos

✅ Bucles Combinados:
for externo + while interno

Variables antes del for (totales)

Variables dentro del for (temporales)


#Pide un número. Indica si es par o impar.
#Si el número es PAR → muestra cuántos dígitos pares tiene
#Si el número es IMPAR → muestra cuántos dígitos impares tiene

n = int(input("Introduce un número: "))
if n % 2 == 0:
    print(f"El número {n} es par")
    temp = n
    contador_pares = 0
    while temp > 0:
        digito = temp % 10
        if digito % 2 == 0:
            contador_pares = contador_pares + 1
        temp = temp // 10
    print(f"El número {n} tiene {contador_pares} dígitos pares")
else:
    print(f"El número {n} es impar")
    temp = n
    contador_impares = 0
    while temp > 0:
        digito = temp % 10
        if digito % 2 != 0:
            contador_impares = contador_impares + 1
        temp = temp // 10
    print(f"El número {n} tiene {contador_impares} dígitos impares")

##Pide inicio, fin y un número n.

#encuentra el MAYOR múltiplo de n en ese rango.
#Si no hay ninguno, indica "No hay múltiplos".
inicio = int(input("Inicio: "))
fin = int(input("Fin: "))
n = int(input("Introduce el múltiplo: "))
mayor = -1
for numero in range(inicio, fin + 1):
    if numero % n == 0:
        if numero > mayor:
            mayor = numero
if mayor == -1:
    print("No hay múltiplos")
else:
    print(f"El mayor múltiplo de {n} entre {inicio} y {fin} es {mayor}")


"""

inicio = int(input("Inicio: "))
fin = int(input("Fin: "))
suma_capicuas = 0
menor_impar = 10
mayor_par = -1
suma_digitos_mas_pares_que_impares = 0
for numero in range(inicio,fin + 1):
    temp = numero
    invertido = 0
    while temp > 0:
        digito = temp % 10
        invertido = invertido * 10 + digito
        temp = temp // 10
if invertido == numero:
    suma_capicuas = suma_capicuas + 1
    temp = numero
    while temp > 0:
        digito = temp % 10
        if digito % 2 == 0:
            if digito > mayor_par:
                mayor_par = digito
        temp = temp // 10
    while temp > 0:
        digito = temp % 10
        if digito % 2 !=0:
            if digito < menor_impar:
                menor_impar = digito
        temp = temp // 10
    temp = numero
    contador_pares = 0  
    contador_impares = 0
    while temp > 0:
        digito = temp % 10
        if digito % 2 == 0
            contador_pares = contador_pares + 1
        if digito % 2 != 0
            contador_impares = contador_impares + 1
        temp = temp // 10
        if contador_pares > contador_impares:
            suma_digitos_mas_pares_que_impares = suma_digitos_mas_pares_que_impares + numero
print(f"Suma de capicúas: {suma_capicuas}")
if mayor_par != -1:
    print(f"Mayor dígito par: {mayor_par}")
else:
    print("No hay dígitos pares")
if menor_impar != 10:
    print(f"Menor dígito impar: {menor_impar}")
else:
    print("No hay dígitos impares")
print(f"Suma de números con más dígitos pares que impares: {suma_digitos_mas_pares_que_impares}")


