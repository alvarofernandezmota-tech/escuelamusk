# 📅 SESIÓN 8 - Jueves 22 Enero 2026

**Tema:** Módulo 2 - Temas 4 y 5 (Consolidación + Listas + POO)  
**Duración:** 5:00 PM - 9:00 PM (4 horas)  
**Estado:** ✅ Completado

---

## ⏰ Cronograma de la Sesión:

### 🕔 17:00 - 18:00 | Consolidación Intermedia Tema 4
- ✅ Ejercicio 17: Rectángulos y círculos
- ✅ Ejercicio 18: Suma de cuadrados

### 🕕 18:00 - 19:00 | Tema 5: Estructuras de Datos - LISTAS
- ✅ Estudio teórico de listas
- ✅ Métodos de listas
- ✅ Operaciones con listas

### 🕖 19:00 - 21:00 | POO: Composición, Herencia y Polimorfismo
- ✅ Clase magistral de POO
- ✅ Composición de objetos
- ✅ Herencia de clases
- ✅ Polimorfismo

---

## 💻 Ejercicios Completados:

### ✅ Ejercicio 17: Rectángulos y círculos
- **Tipo:** Consolidación Intermedia
- **Conceptos:** Menús, validación, import math, bucles
- **Dificultad:** ⭐⭐⭐
- **Archivo:** `m2t4.py`
- **Logros:**
  - Implementación de menú interactivo
  - Validación de entrada con `.lower()`
  - Cálculos con `math.pi`
  - Formato de salida con `.2f`
  - Manejo de múltiples figuras con bucle

**Código final:**
```python
import math
n = int(input("Introduce el número de figuras: "))
for i in range(n):
    tipo_figuras = input("Introduce el tipo de figura (rectángulo/círculo): ").lower()
    if tipo_figuras == "rectangulo":
        longitud = float(input("Introduce la longitud del rectángulo: "))
        anchura = float(input("Introduce la anchura del rectángulo: "))
        area = longitud * anchura
        print(f"El área del rectángulo es: {area:.2f}")
    elif tipo_figuras == "circulo":
        radio = float(input("Introduce el radio del círculo: "))
        area = math.pi * radio ** 2
        print(f"El área del círculo es: {area:.2f}")
    else:
        print("Tipo de figura no válido.")
✅ Ejercicio 18: Suma de cuadrados
Tipo: Consolidación Intermedia

Conceptos: Bucles, acumuladores, potencias

Dificultad: ⭐⭐⭐

Archivo: m2t4.py

Logros:

Uso de acumulador

Operador de potencia **

Bucle for con range

Mostrar secuencia completa

Código final:

python
n = int(input("Introduce un número natural n: "))
suma = 0
secuencia = []
for i in range(1, n + 1):
    suma += i ** 2
    secuencia.append(f"{i}²")
print(" + ".join(secuencia))
print(f"La suma de los cuadrados desde 1 hasta {n} es: {suma}")
📚 Tema 5: LISTAS (18:00 - 19:00)
Conceptos estudiados:
Definición de listas: Estructuras mutables y ordenadas

Creación de listas: lista = [], lista = [1, 2, 3]

Acceso por índice: lista[0], lista[-1]

Slicing: lista[1:3], lista[::-1]

Métodos de listas:
append() - Añadir elemento al final

insert() - Insertar en posición específica

remove() - Eliminar por valor

pop() - Eliminar por índice

sort() - Ordenar lista

reverse() - Invertir lista

count() - Contar ocurrencias

index() - Encontrar índice

Operaciones:
Concatenación: lista1 + lista2

Repetición: lista * 3

Pertenencia: elemento in lista

Longitud: len(lista)

🎓 POO: Composición, Herencia y Polimorfismo (19:00 - 21:00)
1. COMPOSICIÓN
Concepto: Un objeto contiene otros objetos

python
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Coche:
    def __init__(self, marca):
        self.marca = marca
        self.motor = Motor(150)  # Composición
2. HERENCIA
Concepto: Una clase hereda atributos y métodos de otra

python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        pass

class Perro(Animal):  # Herencia
    def hacer_sonido(self):
        return "Guau!"
3. POLIMORFISMO
Concepto: Mismo método, comportamiento diferente

python
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

# Polimorfismo en acción:
animales = [Perro("Rex"), Gato("Michi")]
for animal in animales:
    print(animal.hacer_sonido())  # Cada uno su sonido
📝 Notas Importantes:
Corrección del Ejercicio 17:
Error inicial: for in range(n) - faltaba variable de iteración

Corrección: for i in range(n)

Lección: Siempre declarar variable de iteración en bucle for

Puntos clave de Listas:
Las listas son mutables (se pueden modificar)

Los índices empiezan en 0

Índices negativos van desde el final: lista[-1] es el último

Cuidado con remove() - solo elimina la primera ocurrencia

Puntos clave de POO:
Composición: "tiene un" (Coche tiene Motor)

Herencia: "es un" (Perro es Animal)

Polimorfismo: Mismo método, diferentes implementaciones

super() para llamar al constructor de la clase padre

🎯 Progreso del Módulo 2:
Tema 1: ✅ Completado (Números)

Tema 2: ✅ Completado (Variables y Operadores)

Tema 3: ✅ Completado (Strings)

Tema 4: ✅ Completado (Condicionales y Bucles) - 18/18 ejercicios + 4 repaso + 2 consolidación

Tema 5: 🔄 En curso (Estructuras de Datos - Listas)

💡 Próximos Pasos:
Completar ejercicios prácticos del Tema 5 (Listas)

Hacer ejercicios de repaso de Listas

Continuar con otros tipos de estructuras (tuplas, diccionarios, sets)

Ejercicios prácticos de POO

📊 Estadísticas de Hoy:
Tiempo total: 4 horas

Ejercicios completados: 2

Temas estudiados: 2 (Listas, POO)

Conceptos nuevos: 15+

Estado: ✅ Sesión muy productiva

🌟 Logros del Día:
✅ Finalizado Tema 4 completamente
✅ Inicio del Tema 5 (Listas)
✅ Clase completa de POO avanzado
✅ Corrección y aprendizaje de errores
✅ Documentación completa en GitHub