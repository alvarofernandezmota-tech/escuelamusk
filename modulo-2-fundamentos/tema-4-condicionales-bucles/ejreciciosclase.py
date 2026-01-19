""""
#calcula la suma de dos numeros-
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
suma = a + b
print(f"La suma de {a} y {b} es : {suma}")

#division entera vs division normal 

print(17 // 3)  # División entera
print(17 / 3)   # División normal
print(17 % 3)   # Módulo (resto de la división entera)
print(2 ** 3)   # Exponenciación (2 elevado a la 3)
print(2 + 3 * 4)  # Operaciones combinadas (multiplicación antes que suma)
print((2 + 3) * 4)  # Uso de paréntesis para cambiar el orden de las operaciones
print(7 % 4)  # Resultado: 3 (7 dividido por 4 da 1 con un resto de 3)
print(10 % 2) # Resultado: 0 (10 es divisible por 2 sin resto)
"""
""""
#haz un programa que al imprimir una letra y detecte que solo sea una letra y 
#que si esa letra es una vocal o consonante.
letra = input("Introduce una letra: ")
if len(letra) != 1 or not letra.isalpha():
    print("Por favor, introduce solo una letra.")
else:
    if letra.lower() in "aeiou":
        print(f"{letra} es una vocal.")
    elif letra.lower() in "bcdfghjklmnpqrstvwxyz":
        print(f"{letra} es una consonante.")

"""
""""
🎯 EJERCICIO: Validar Contraseña Simple
📝 Enunciado
Haz un programa que pida al usuario una contraseña y compruebe:

Que tenga al menos 6 caracteres

Que contenga al menos un número

Que contenga al menos una letra mayúscula

Resultados posibles:

Si cumple TODO → "Contraseña válida ✅"


Si falla alguna validación → mostrar qué falta

💡 Pistas
Métodos útiles:

len() - longitud

.isdigit() - ¿es dígito?

.isupper() - ¿es mayúscula?

Bucle for para recorrer cada carácter

password = input("Introduce una contraseña: ")
if len(password) < 6:
    print("La contraseña debe tener al menos 6 caracteres.")
elif not any (text.isdigit() for text in password):
    print("La contraseña debe contener al menos un número.")
elif not any ( text.isupper() for text in password):
    print("La contraseña debe contener al menos una letra mayúscula.") 
else:
    print("Contraseña válida ✅")   

#aora con el bucle for:
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
"""
""""
🎯 EJERCICIO: Validar Nombre de Usuario
📝 Enunciado
Haz un programa que pida un nombre de usuario y valide que cumple estas reglas:

Longitud entre 4 y 12 caracteres (ambos inclusive)

Solo puede contener letras y números (sin espacios ni símbolos)

Debe empezar con una letra (no puede empezar con número)

Debe contener al menos una letra minúscula

Resultados posibles:

Si cumple TODO → "✅ Usuario válido"

Si falla algo → mostrar qué regla no cumple

💡 Pistas
Métodos útiles:

len() - longitud

.isalnum() - ¿es solo letras y números?

.isalpha() - ¿es letra?

.isdigit() - ¿es número?

.islower() - ¿es minúscula?

Indexación: usuario[0] (primer carácter)

🎯 Ejemplos de Ejecución
text
Usuario: ab
❌ Debe tener entre 4 y 12 caracteres

Usuario: usuario con espacios
❌ Solo puede contener letras y números (sin espacios ni símbolos)

Usuario: 123hola
❌ Debe empezar con una letra

Usuario: HOLA123
❌ Debe contener al menos una letra minúscula

Usuario: Hola123
✅ Usuario válido

Usuario: user2024
✅ Usuario válido
🏗️ Estructura Sugerida
python
usuario = input("Usuario: ")

""

usuario = input("Usuario: ")
length_ok = 4 <= len(usuario) <= 12
alnum_ok = usuario.isalnum()
start_with_letter = usuario[0].isalpha()
tiene_minuscula = False

for char in usuario:
    if char.islower():
        tiene_minuscula = True  
if not length_ok:
    print("❌ Debe tener entre 4 y 12 caracteres")  
if not alnum_ok:
    print("❌ Solo puede contener letras y números (sin espacios ni símbolos)") 
if not start_with_letter:
    print("❌ Debe empezar con una letra")
if not tiene_minuscula:
    print("❌ Debe contener al menos una letra minúscula")
if length_ok and alnum_ok and start_with_letter and tiene_minuscula:
    print("✅ Usuario válido")
"""

""""
🎯 EJERCICIO FINAL: Validar Email
📝 Enunciado
Haz un programa que pida un email y valide que cumple estas reglas:

Debe contener exactamente UN símbolo @ (no puede tener 0 o más de 1)

Debe contener al menos UN punto . después del @

No puede empezar ni terminar con @ o .

Debe tener al menos 5 caracteres

No puede contener espacios

Resultados posibles:

Si cumple TODO → "✅ Email válido"

Si falla algo → mostrar qué regla no cumple

💡 Pistas
Métodos/funciones útiles:

.count(caracter) - cuenta cuántas veces aparece un carácter

.find(caracter) - encuentra la posición de un carácter (-1 si no existe)

email[0] - primer carácter

email[-1] - último carácter

" " in email - comprobar si contiene espacio

len() - longitud


email = input("Introduce un email: ")
length_ok = len(email) >= 5
at_count = email.count("@")
not_finist_with_invalid_email= email[-1] not in "@."
not_start_with_invalid_email= email[0] not in "@."
not_space = " " not in email
for char in email:
    tiene_punto_despues_arroba = email.find(".") > email.find("@")
if at_count != 1:
    print("❌ Debe contener exactamente UN símbolo @ (no puede tener 0 o más de 1)")    
if not tiene_punto_despues_arroba:
    print("❌ Debe contener al menos UN punto . después del @") 
if not not_finist_with_invalid_email:
    print("❌ No puede empezar ni terminar con @ o .")  
if not not_start_with_invalid_email:
    print("❌ No puede empezar ni terminar con @ o .")              
if not length_ok:
    print("❌ Debe tener al menos 5 caracteres")    
if not_space:
    print("❌ No puede contener espacios")  
if (at_count == 1 and tiene_punto_despues_arroba and not_finist_with_invalid_email and not_start_with_invalid_email and length_ok and not_space):
    print("✅ Email válido")
"""

"""
# Imprime: 0, 1, 2, 3, 4, 5, 6, 7
# Tu código aquí:
for i in range(8):
    print(i)
# Imprime: 3, 4, 5, 6, 7, 8
# Tu código aquí:
for i in range (3,9):
    print(i)
# Imprime "Hola" 10 veces
# Tu código aquí:
for in range (10):
    print("Hola")
# Imprime: 15, 16, 17, 18, 19, 20
# Tu código aquí:
for in range(15,21):
    print(i)
# Imprime: 0, 2, 4, 6, 8, 10
# Usa step
# Tu código aquí:
for i in range(0,11,2):
    print(i)
# Imprime: 1, 3, 5, 7, 9, 11, 13, 15
# Usa step
# Tu código aquí:
for i in range(1,16,2):
    print(i)
    # Imprime: 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
# Tu código aquí:
for i in range(0,101,10):
    print(i)
# Imprime: 5, 4, 3, 2, 1, 0
# Usa step negativo
# Tu código aquí:
for i in range(5,-1,-1):
    print(i)
# Imprime: 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10
# Tu código aquí:
for i in range(20,9,-1):
    print(i)
# Imprime: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30
# Usa range(1, 11) y multiplica
# Tu código aquí:
for i in range(1,11):
    print(i*3)
for i in range(1,11,3):
    print(i)

for i in range (1,101):
    print(i*2)

for i in range(1,11):
    print(i + i)


suma = 0
for i in range(0, 21):
    suma += i
print(suma)

for i in range(3,31):
    if i % 3 == 0:
        print(i)

        
for i in range(2,51):
    if i % 2 == 0:
        print(i)


numero = int(input("introduce un numero:"))
for i in range(1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


for i in range(1,20):
    if i % 2 != 0:
        print(i)

suma = 0
for i in range(1,101):
    if i % 2 == 0:
        suma += i
print(suma)


for i in range(10,0,-1):
    print(i)

for i in range(1,31):
    if i % 3 == 0:
        print("Fizz")
    if i % 5 == 0:
        print("Buzz")   
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")   
    if i % 3 != 0 and i % 5 != 0:
        print(i)    
coreccion 
if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
elif i % 3 == 0:    # ✅ Solo si la anterior fue False
    print("Fizz")
elif i % 5 == 0:    # ✅ Solo si las anteriores fueron False
    print("Buzz")

munero1 = int(input("Introduce el primer número entero: "))
numero2 = int(input("Introduce el segundo número entero: "))
numero3 = int(input("Introduce el tercer número entero: "))
numero4 = int(input("Introduce el cuarto número entero: "))
numero5 = int(input("Introduce el quinto número entero: "))
pares = 0
impares = 0
numeros = [munero1, numero2, numero3, numero4, numero5]
for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1    
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")



mayor_de_10 = 0
menor_de_10 = 0
igual_a_10 = 0
for i in range(1,6):
    numero = int(input("Introduce un número entero: "))
    if numero > 10:
        mayor_de_10 += 1
    elif numero < 10:
        menor_de_10 += 1
    else:
        igual_a_10 += 1
print(f"Números mayores que 10: {mayor_de_10}")
print(f"Números menores que 10: {menor_de_10}")
print(f"Números iguales a 10: {igual_a_10}")    


nunero1 = int(input("Introduce el primer número entero: "))
numero2 = int(input("Introduce el segundo número entero: "))
numero3 = int(input("Introduce el tercer número entero: "))
numero4 = int(input("Introduce el cuarto número entero: "))
numero5 = int(input("Introduce el quinto número entero: "))
numeros = [nunero1, numero2, numero3, numero4, numero5]
mayor = numeros[0]
menor = numeros[0]
for numero in numeros:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")


for i in range(1,6):
    print("*" * i)


n = int(input("de cuentos numeros va a ser tu lista: "))
lista = []
for i in range(n):
    numero = int(input(f"Introduce el número {i+1}: "))
    lista.append(numero)    
buscar = int(input("Introduce un número a buscar en la lista: "))
encontrado = False
for i in range(n):
    if lista[i] == buscar:
        print(f"El número {buscar} se encuentra en la posición: {i}")
        encontrado = True
        break
if not encontrado:
    print(f"El número {buscar} no se encuentra en la lista.")

lista = []
for i in range(3):
    numero = int(input("Introduce un número entero: "))
    lista.append(numero)
print(f"Números introducidos: {lista}")


lista = []
for i in range(4):
    numero = int(input("Introduce el número: "))
    lista.append(numero)
suma = sum(lista)
print(f"La suma de los números es: {suma}")

lista = []
for i in range(5):
    numero = int(input("Introduce un número entero: "))
    lista.append(numero)
pares = 0
for numero in lista:
    if numero % 2 == 0:
        pares += 1
print(f"Números pares en la lista: {pares}")


lista = []
for i in range(4):
    numero = int(input(f"Introduce el número {i+1}:"))
    lista.append(numero)
mayor = max(lista)
print(f"El número mayor de la lista es: {mayor}")


lista = []
for i in range(5):
    numero = int(input(f"introcude el nuemro {i+1}:"))
    lista.append(numero)
print(f"imprime la lista: {lista}")
lista.reverse()
print(f"lista invertida: {lista}")

lista = []
for i in range(6):
    numero = int(input("introduce numero: "))
    lista.append(numero)
print(f"la lista sin duplicadpos es: {list(set(lista))}")



contador = 5
while contador > 0:
    print(contador)
    contador -= 1
print("!despegue¡")


n = int(input("introduce un numero: "))
ultimo_digito = n % 10
print(f"este es el ultimo dijito: {ultimo_digito}")

n = int(input("introduce un numero: "))
sin_ultimo_numero = n // 10
print(f"el numero resultante de quitar el ultimo digito es: {sin_ultimo_numero}")



#Haz un programa que lea un número y que escriba sus dígitos al revés (uno por línea).
n = int(input("introduce un numero: "))
while n > 0:
    print((n))
    resto = n % 10
    

numero = 1

while numero <= 5:
    print(numero)
    numero = numero + 1

numero = 5
while numero >= 0:
    print(numero)
    numero = numero - 1


numero = 1
suma = 0
while numero <= 4:
    suma = suma + numero
    numero = numero + 1 
print(f"la suma es : {suma}")


numero = 1
contador = 0
while numero <=6:
    contador = contador + 1
    numero = numero + 1
print(f"he contado: {contador} numeros.")

numero = 2
suma = 0
while numero <= 6:
    suma = suma + numero
    numero = numero + 2
print(f"La suma es: {suma}")


n = int(input("intriduce un numero: "))
while n > 0:
    digito = n % 10
    print(digito)
    n = n // 10



n = int(input("intriduce un numero: "))
contador = 0
while n > 0:
    contador = contador + 1 
    n = n // 10
print(contador)



n = int(input("intriduce un numero: "))
suma = 0
while n > 0:
    digito = n % 10 
    suma = suma + digito
    n = n // 10
print(f"el numero tiene: {suma} digitos.")



n = int(input("intriduce un numero: "))
temp = n
while temp > 0:
    digito = temp % 10
    print(digito)
    temp = temp // 10
print(f"el numero principal es: {n}")



n = int(input("intriduce un numero: "))
temp = n
while temp > 0:
    digito = temp % 10
    print(digito)
    if digito == 5:
        print("encontre un 5")
    temp = temp // 10

    
n = int(input("intriduce un numero: "))
temp = n
contador = 0
while temp > 0:
    digito = temp % 10
    if digito % 2 != 0:
        contador = contador + 1
    temp = temp // 10
print(f"{contador}")    

    
n = int(input("intriduce un numero: "))
temp = n
contador = 0
while temp > 0:
    digito = temp % 10
    if digito == 0:
        contador = contador + 1
    temp = temp // 10
print(f"Hay {contador} ceros")



n = int(input("intriduce un numero: "))
temp = n
mayor = 0
while temp > 0:
    digito = temp % 10
    if digito > mayor:
        mayor = digito
    temp = temp // 10
print(f"El munero mayor es {mayor}")




n = int(input("intriduce un numero: "))
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
print(f"el numero mayor es {mayor}")





n = int(input("intriduce un numero: "))
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




n = int(input("intriduce un numero: "))
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




n = int(input("Introduce un numero: "))
temp = n
producto = 1  # ¡Debe ser 1!
hay_pares = False  # Para saber si encontramos alguno

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

    


n = int(input("Introduce un numero: "))
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



n = int(input("Introduce un numero: "))
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

"""
n = int(input("Introduce un numero: "))
temp = n
invertido = 0
while temp > 0:
    digito = temp % 10
    invertido = invertido * 10 + digito
    temp = temp // 10
print(f"Número invertido: {invertido}")