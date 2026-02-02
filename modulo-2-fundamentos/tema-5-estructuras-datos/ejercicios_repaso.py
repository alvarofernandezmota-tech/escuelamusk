# 📝 EJERCICIOS DE REPASO - TEMA 5
# Estructuras de Datos: Strings, Listas, Tuplas, Diccionarios y Sets
# Escuela Musk - Módulo 2
# Fecha: 02 Febrero 2026

"""
ESTOS EJERCICIOS MEZCLAN TODOS LOS CONCEPTOS DEL TEMA 5:
- Strings
- Listas
- Tuplas
- Diccionarios
- Sets

Objetivo: Consolidar conocimientos antes de pasar a Funciones
"""

# =============================================================================
# EJERCICIO 1: LISTA + DICCIONARIO
# =============================================================================
# Dada una lista de nombres, crea un diccionario que cuente cuántas veces
# aparece cada nombre.
#
# Ejemplo:
# nombres = ["Ana", "Juan", "Ana", "Pedro", "Juan", "Ana"]
# Resultado: {'Ana': 3, 'Juan': 2, 'Pedro': 1}




# =============================================================================
# EJERCICIO 2: STRING + LISTA
# =============================================================================
# Dada una frase, crea una lista con las palabras que tienen más de 5 letras.
#
# Ejemplo:
# frase = "Python es un lenguaje de programación muy potente"
# Resultado: ['Python', 'lenguaje', 'programación', 'potente']




# =============================================================================
# EJERCICIO 3: SET + LISTA
# =============================================================================
# Dadas dos listas, encuentra:
# a) Elementos comunes
# b) Elementos únicos (que están solo en una lista)
# c) Todos los elementos sin duplicados
#
# Ejemplo:
# lista1 = [1, 2, 3, 4, 5]
# lista2 = [4, 5, 6, 7, 8]




# =============================================================================
# EJERCICIO 4: DICCIONARIO + TUPLA
# =============================================================================
# Dado un diccionario de productos con sus precios, crea una tupla con
# el producto más caro y el más barato.
#
# Ejemplo:
# productos = {'manzana': 1.5, 'pan': 0.8, 'leche': 1.2, 'huevos': 2.5}
# Resultado: ('huevos', 'pan')




# =============================================================================
# EJERCICIO 5: LISTA + STRING
# =============================================================================
# Dada una lista de palabras, crea un string donde cada palabra esté separada
# por un guion y todas estén en mayúsculas.
#
# Ejemplo:
# palabras = ["hola", "mundo", "python"]
# Resultado: "HOLA-MUNDO-PYTHON"




# =============================================================================
# EJERCICIO 6: DICCIONARIO ANIDADO
# =============================================================================
# Dado un diccionario de estudiantes con sus notas, calcula la media de
# cada estudiante y crea un nuevo diccionario con las medias.
#
# Ejemplo:
# estudiantes = {
#     'Ana': [8, 7, 9],
#     'Juan': [6, 7, 5],
#     'Pedro': [9, 8, 10]
# }
# Resultado: {'Ana': 8.0, 'Juan': 6.0, 'Pedro': 9.0}




# =============================================================================
# EJERCICIO 7: SET + STRING
# =============================================================================
# Dada una frase, encuentra todas las letras únicas (sin duplicados) que
# aparecen en la frase. Ignora espacios y convierte todo a minúsculas.
#
# Ejemplo:
# frase = "Hola Mundo"
# Resultado: {'a', 'd', 'h', 'l', 'm', 'n', 'o', 'u'}




# =============================================================================
# EJERCICIO 8: LISTA + TUPLA + DICCIONARIO
# =============================================================================
# Dada una lista de tuplas (nombre, edad), crea un diccionario donde la
# clave sea el nombre y el valor sea la edad. Luego, encuentra el nombre
# de la persona más joven.
#
# Ejemplo:
# personas = [("Ana", 25), ("Juan", 30), ("Pedro", 22)]
# Diccionario: {'Ana': 25, 'Juan': 30, 'Pedro': 22}
# Más joven: 'Pedro'




# =============================================================================
# EJERCICIO 9: STRING + DICCIONARIO
# =============================================================================
# Dada una frase, cuenta cuántas vocales tiene cada tipo (a, e, i, o, u).
# No diferencies entre mayúsculas y minúsculas.
#
# Ejemplo:
# frase = "Hola mundo de Python"
# Resultado: {'a': 1, 'e': 1, 'i': 0, 'o': 4, 'u': 2}




# =============================================================================
# EJERCICIO 10: LISTA + SET
# =============================================================================
# Dada una lista con números duplicados, elimina los duplicados manteniendo
# el orden original de aparición.
#
# Ejemplo:
# numeros = [1, 2, 3, 2, 4, 1, 5, 3]
# Resultado: [1, 2, 3, 4, 5]
#
# Pista: Usa un set para rastrear qué has visto, pero construye una nueva lista




# =============================================================================
# EJERCICIO 11: DICCIONARIO + LISTA
# =============================================================================
# Dado un diccionario que representa un inventario de una tienda,
# crea una lista con los productos que tienen menos de 10 unidades.
#
# Ejemplo:
# inventario = {'manzanas': 50, 'peras': 8, 'naranjas': 30, 'plátanos': 5}
# Resultado: ['peras', 'plátanos']




# =============================================================================
# EJERCICIO 12: STRING + LISTA + SET
# =============================================================================
# Dada una frase, encuentra todas las palabras que aparecen más de una vez.
#
# Ejemplo:
# frase = "hola mundo hola python mundo es genial"
# Resultado: {'hola', 'mundo'}




# =============================================================================
# EJERCICIO 13: TUPLA + DICCIONARIO
# =============================================================================
# Dada una tupla de temperaturas (en Celsius) por día de la semana,
# crea un diccionario donde la clave sea el día y el valor la temperatura.
# Luego encuentra el día más caluroso.
#
# Ejemplo:
# temperaturas = (15, 18, 20, 17, 19, 22, 16)
# dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
# Resultado diccionario: {'Lunes': 15, 'Martes': 18, ...}
# Día más caluroso: 'Sábado'




# =============================================================================
# EJERCICIO 14: LISTA + DICCIONARIO + SET (COMBINADO)
# =============================================================================
# Dadas dos listas de estudiantes con sus asignaturas favoritas:
# - Crea un diccionario con cada estudiante y sus asignaturas
# - Encuentra las asignaturas que son favoritas de al menos 2 estudiantes
#
# Ejemplo:
# estudiantes = ["Ana", "Juan", "Pedro", "María"]
# asignaturas = [["Matemáticas", "Física"], ["Matemáticas", "Historia"],
#                ["Física", "Química"], ["Matemáticas", "Física"]]
#
# Diccionario: {'Ana': ['Matemáticas', 'Física'], ...}
# Asignaturas populares: {'Matemáticas', 'Física'}




# =============================================================================
# EJERCICIO 15: TODO COMBINADO (DESAFÍO)
# =============================================================================
# Tienes una lista de frases. Para cada frase:
# 1. Cuenta cuántas palabras tiene
# 2. Encuentra la palabra más larga
# 3. Crea un diccionario con esta información
#
# Ejemplo:
# frases = [
#     "Python es genial",
#     "Me encanta programar en Python",
#     "Los ejercicios ayudan a aprender"
# ]
#
# Resultado: {
#     "Python es genial": {"palabras": 3, "mas_larga": "Python"},
#     "Me encanta programar en Python": {"palabras": 5, "mas_larga": "programar"},
#     "Los ejercicios ayudan a aprender": {"palabras": 5, "mas_larga": "ejercicios"}
# }




# =============================================================================
# 🎯 OBJETIVOS DE ESTOS EJERCICIOS:
# =============================================================================
# ✅ Practicar conversiones entre tipos de datos
# ✅ Combinar múltiples estructuras de datos
# ✅ Usar métodos nativos de Python
# ✅ Aplicar lógica de programación
# ✅ Prepararse para trabajar con funciones
#
# 💡 CONSEJO:
# Intenta resolver cada ejercicio sin mirar las soluciones.
# Si te atascas, revisa la chuleta de Python en recursos/chuleta_python.md
# =============================================================================
