## Strings
##1. Haz un programa que lea una secuencia de caracteres acabada en punto y que escriba cuántas letras ‘a’ contiene.
##2. Haz un programa que encuentre todas las apariciones de una subcadena en una cadena dada.
##3. Haz un programa que invierta una cadena dada.
##4. Haz un programa que divida una cadena en guiones.
##5. Haz un programa que añada una nueva cadena en medio de una cadena dada.
##6. Haz un programa que encuentre la última posición de una subcadena dada.
##7. Haz un programa que elimine cadenas vacías de una lista de cadenas.
##8. Haz un programa que elimine símbolos especiales / signos de puntuación de una cadena.
##9. Haz un programa que encuentre palabras con letras y números.
##10. Haz un programa que sustituya cada símbolo especial por # en la siguiente cadena.
##listas
##1. Haz un programa que lea una lista dado su tamaño e imprima el segundo elemento (si existe).
n = int(input("tamañod e la lista: "))
lista = []
for i in range(n):
    elemento = int(input(f"elemento {i+1}: "))
    lista.append(elemento)
if len(lista) >= 2:
    print(f"el segundo elemento es: {lista[1]}")
else:
    print("la lista no tiene segundo elemento.")

##2. Haz un programa que lea una secuencia no vacía de enteros acabada en -1, y que escriba
#  cuántos son iguales al último.
lista = []
num = int(input("Introduce un número (-1 para terminar): "))
while num != -1:
    lista.append(num)
    num = int(input("Introduce un número (-1 para terminar): "))
ultimo = lista[-1]
contador = 0
for num in lista:
    if ultimo == num:
        contador +=1
print(f"Hay {contador} numeros iguales al ultimo numero: {ultimo}") 
##3. Haz un programa que lea secuencias de enteros acabada en -1, y que
#  escriba cada una invirtiendo la orden de sus elementos.
lista = []
num = int(input("Introduce un número (-1 para terminar): "))
while num != -1:
    lista.append(num)
    num = int(input("Introduce un número (-1 para terminar): "))
lista.reverse()
print(f"lista invertida: {lista}")
##4. Haz un programa que lea n palabras, y que escriba cada una invirtiendo la orden de sus caracteres.
n = int(input("¿Cuántas palabras?: "))
for i in range(n):
    palabra = input(f"Palabras: {i+1}: ")
    print(f"Invertida: {palabra[::-1]}")
##5. Haz un programa que lea una secuencia de números mientras sean positivos y que escriba la media.
lista = []
num = float(input("Introduce un número positivo (negativo o 0 para terminar): "))
while num > 0:
    lista.append(num)
    num = float(input("Introduce un número positivo (negativo o 0 para terminar): "))
if len(lista) > 0:
    media =sum(lista) / len(lista)
    print(f"La media de la lista es: {media}")
else:
    print("no se introdujeron numeros positivos.")

##6. Haz un programa que devuelva la concatenación de v1 y v2, v1 y v2 son dos listas de 
# tamaño n y m. Es decir, hay que devolver un vector que tenga los elementos de v1 seguidos
#  de los elementos de v2.
n = int(input("Tamaño de la primera lista: "))
v1 = []
for i in range(n):
    elemento = int(input(f"Elemento {i + 1} de v1: "))
    v1.append(elemento)

m = int(input("Tamaño de la segunda lista: "))
v2 = []
for i in range(m):
    elemento = int(input(f"Elemento {i + 1} de v2: "))
    v2.append(elemento)
resultado = v1 + v2
print(f"Lista concatenada: {resultado}.")
##7. Haz un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, 
# y muestre por pantalla el menor y el mayor de los precios.
precios = [50, 75, 46, 22, 80, 65, 8]
menor = precios[0]
mayor = precios[0]
for precio in precios:
    if precio > mayor:
        mayor = precio
    if precio < menor:
        menor = precio
print(f"Precio menor: {menor}")
print(f"Precio mayor: {mayor}")

##8. Haz un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla.
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print("Asignaturas del curso:")
for asignatura in asignaturas:
    print(f"- {asignatura}")
##9. Haz un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso 
# separados por comas.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros.reverse()
resulta = ""
for i in range(len(numeros)):
    resultado += str(numeros[i])
    if i < len(numeros) -1:
        resultado += ", "
print(resultado)

##10. Haz un programa que concatene dos listas del mismo tamaño n alternando elementos de una lista y otra.
n = int(input("Tamaño de las listas: "))

lista1 = []
for i in range(n):
    elemento = int(input(f"Elemento {i+1} de lista1: "))
    lista1.append(elemento)
lista2 = []
for i in range(n):
    lemento = int(input(f"Elemento {i+1} de lista1: "))
    lista2.append(elemento)
resultado = []
for i in range(n):
    resultado.append(lista1[i])
    resultado.append(lista2[i])
print(f"Resultado: {resulta}")
      
##11. Haz un programa que itere ambas listas de tamaños n y m (siendo n y m números distintos )simultáneamente e imprima sus elementos.
##12. Haz un programa que añada un nuevo elemento 60 a la lista [10, 50, 40, 20, 30] después de un elemento especificado por el usuario. Si el elemento introducido no está presente en la lista debe mostrar el mensaje: 'Elemento no presente en la lista'.
##13. Haz un programa que elimine todas las apariciones de un elemento específico introducido por el usuario de la lista [10, 50, 40, 20, 60, 30].
##Tuplas
##1. Haz una programa que invierta una tupla.
##2. Haz un programa que acceda al valor 15 de la tupla.
##3. Haz un programa que declare una tupla con un solo elemento 10.
##4. Haz un programa que descomponga la tupla en 4 variables.
##5. Haz un programa que intercambie dos tuplas en Python.
##6. Haz un programa que copie elementos específicos de una tupla a una nueva tupla.
##7. Haz un programa que modifique una tupla.
##8. Ordena una tupla de tuplas por el 2º elemento.
##9. Haz un programa que cuente el número de apariciones del elemento 50 de una tupla.
##10. Haz un programa que compruebe si todos los elementos de la tupla son iguales.
#### Diccionarios
##1. Haz un programa que convierta dos listas en un diccionario.
##2. Haz un programa que fusione dos diccionarios de Python en uno solo.
##3. Haz un programa que imprima el valor de la clave 'history' del siguiente diccionario.
##4. Haz un programa que inicialice el diccionario con valores por defecto.
##5. Haz un programa que cree un diccionario extrayendo las claves de un diccionario dado.
##6. Haz un programa que elimine una lista de claves de un diccionario.
##7. Haz un programa que compruebe si un valor existe en un diccionario.
##8. Haz un programa que cambie el nombre de la clave de un diccionario.
##9. Haz un programa que obtenga la clave de un valor mínimo del siguiente diccionario.
##10. Haz un programa que cambie el valor de una clave en un diccionario anidado.
## Sets
##1. Haz un programa que añada una lista de elementos a un conjunto.
##2. Haz un programa que devuelva un nuevo conjunto de elementos idénticos de dos conjuntos.
##3. Haz un programa que obtenga sólo elementos únicos de dos conjuntos.
##4. Haz un programa que actualice el primer conjunto con elementos que no existen en el segundo conjunto.
##5. Haz un programa que elimine elementos del conjunto a la vez.
##6. Haz un programa que devuelva un conjunto de elementos presentes en el conjunto A o B, pero no en ambos.
##7. Haz un programa que compruebe si dos conjuntos tienen algún elemento en común. En caso afirmativo, mostrar los elementos comunes.
##8. Haz un programa que actualice el conjunto1 añadiendo elementos del conjunto2, excepto los elementos comunes.##9. Haz un programa que actualice el conjunto1 añadiendo elementos del conjunto2, excepto los elementos comunes.
##9. Haz un programa que actualice el conjunto1 añadiendo elementos del conjunto2, excepto los elementos comunes.
