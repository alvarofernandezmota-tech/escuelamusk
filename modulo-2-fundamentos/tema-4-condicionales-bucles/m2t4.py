## modulo 2 tema 4 ##       
## 1. Haz un programa que lea dos palabras y que indique el orden lexicográfico. Escribe en una línea indicando si a < b, a > b o a = b. Ejemplo: a = Anna, b = Javier, Anna < Javier.

a = input("Introduce una palabra:")
b = input("Introduce una palabra:")

if a > b:
    print("{} > {}".format(a, b))
else:
    print("{} < {}".format(a, b))

    ##2. Haz un programa que lea una letra y que indique por pantalla si es una mayúscula, si es una minúscula, si es una vocal, y si es una consonante.

c = input("introduce una letra:") 
if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
    print("{} es una vocal".format(c))
else:
    print("{} es una consonte".format(c))
if c.islower():
    print("{} es una minuscula".format(c))
else:
    print("{} es una mayuscula".format(c))
## 3. Haz un programa que lea un entero que representa una temperatura en grados
#  Celsius, y que diga si hace calor, si hace frío, o si se está bien.
#  Suponed que hace calor si la temperatura es más alta que 30 grados,
#  que hace frío si es más baja que 10 grados, y que se está bien en otro caso.

x = float(input("Introduce un número:"))
if x > 30:
    print("hace calor")
elif x < 10:
    print("hace frio")
else:
    print("se esta bien") 
##4. Haz un programa que, dados dos intervalos, calcule el intervalo correspondiente a la intersección o indique que esta es vacía.

x1 = int(input("Introduce el extremo izquierdo del primer intervalo: "))
y1 = int(input("Introduce el extremo derecho del primer intervalo: "))

x2 = int(input("Introduce el extremo izquierdo del segundo intervalo: "))
y2 = int(input("Introduce el extremo derecho del segundo intervalo: "))

# El mínimo válido para la intersección es el mayor de los extremos izquierdos
minimo = max(x1, x2)

# El máximo válido para la intersección es el menor de los extremos derechos
maximo = min(y1, y2)

# Comprobamos si hay intersección
if minimo <= maximo:
    print("[{}, {}]".format(minimo, maximo))
else:
    print("Intersección vacía")
## 5. Haz un programa que indique 
# si un año es bisiesto o no. Un año bi
# siesto tiene 366 días. Después de la r
# eforma gregoriana, los años bisiestos son los 
# múltiplos de cuatro que no acaban en dos cer
# os, y también los acabados en dos ceros ta
# les que el número que queda después de sac
# ar los dos ceros finales es divisible por cu
# atro. Así, 1800 y 1900, a pesar de ser múltiples
#  de cuatro, no fueran bisiestos; en cambio, 2000
#  lo fue.

x = int(input("introduce un numero:"))
if x % 4 == 0 or x % 100 != 0 or x % 400 == 0:
    print("{} es año bisiesto".format(x))
else:
    print("{} no es año bisiesto".format(x))

##6. Haz un programa que añada un segundo en 
# una hora del día, dadas sus horas, minutos y segundos.
h = int(input("Introduce las horas (0-23): "))
m = int(input("Introduce los minutos (0-59): "))
s = int(input("Introduce los segundos (0-59): "))

# Convertir toda la hora a segundos
total_segundos = h * 3600 + m * 60 + s

# Sumar 1 segundo
total_segundos += 1

# Volver a convertir a horas, minutos y segundos (módulo 24h)
h = (total_segundos // 3600) % 24
m = (total_segundos % 3600) // 60
s = total_segundos % 60

print("Nueva hora: {:02d}:{:02d}:{:02d}".format(h, m, s))

## 7. Haz un programa que lea un real x≥0 y que escriba ⌊x⌋ 
# (la parte entera inferior de x), ⌈x⌉ 
# (la parte entera superior de x), y el redondeo de x.

x = float(input("introduce un numero x≥0:"))

