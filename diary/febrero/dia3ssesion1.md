📝 DIARY - DÍA 3 FEBRERO 2026 - SESIÓN 1

Fecha: 03/02/2026
Horario: 17:22 - 21:13 (3h 51 minutos)
Módulo: Módulo 2 - Fundamentos de Python
Tema: Ejercicios de Repaso - Tema 5 (Estructuras de Datos)

================================================================================
🎯 OBJETIVOS DE LA SESIÓN:
================================================================================
✅ Auditoría completa del repositorio
✅ Configurar intérprete Python en VSCode
✅ Realizar ejercicios de repaso del Tema 5
✅ Consolidar conocimientos de estructuras de datos
✅ Practicar listas, diccionarios, sets, tuplas y strings

================================================================================
📚 CONTENIDO TRABAJADO:
================================================================================

## 1️⃣ AUDITORÍA DEL REPOSITORIO (17:22 - 17:40)

### Estado general verificado:
✅ Último commit: 2 febrero 2026 (Tema 5 100% completo)
✅ Python 3.13.9 instalado correctamente
✅ 52 ejercicios completados del Tema 5
✅ Estructura del repositorio bien organizada
✅ PROGRESO.md desactualizado (pendiente actualizar con sesión del 2 feb)

### Archivos principales encontrados:
- ✅ `ejercicios_repaso.py` (15 ejercicios creados el 2 feb)
- ✅ `PROGRESO.md` (última actualización: 29 enero)
- ✅ Diario completado hasta día 2 sesión 3
- ✅ PDF Funciones (Tema 6) ya subido

---

## 2️⃣ CONFIGURACIÓN VSCODE (17:40 - 17:45)

### Problema inicial:
❌ "No Python interpreter is selected"

### Solución aplicada:
1. ✅ Verificar Python instalado: `python --version` → Python 3.13.9
2. ✅ Ctrl + Shift + P → "Python: Select Interpreter"
3. ✅ Seleccionar Python 3.13.9
4. ✅ Verificar en esquina inferior derecha de VSCode

### Resultado:
✅ Intérprete funcionando correctamente
✅ IntelliSense activado
✅ Linting habilitado
✅ Debugging disponible

---

## 3️⃣ EJERCICIOS DE REPASO (17:45 - 21:12)

### EJERCICIO 1: Lista + Diccionario (17:45 - 18:10)
**Objetivo:** Contar cuántas veces aparece cada nombre en una lista

**Código final:**
```python
nombres = ["Ana", "Juan", "Ana", "Pedro", "Juan", "Ana"]
conteo = {}
for nombre in nombres:
    if nombre in conteo:
        conteo[nombre] += 1
    else:
        conteo[nombre] = 1
print(conteo)
Resultado: {'Ana': 3, 'Juan': 2, 'Pedro': 1}

Conceptos aprendidos:

✅ dict() necesita PARES, no puede convertir lista simple

✅ Para contar, SÍ o SÍ se necesita bucle manual

✅ conteo = {} crea el diccionario vacío

✅ conteo[nombre] += 1 es más limpio que conteo[nombre] = conteo[nombre] + 1

✅ El bucle RELLENA el diccionario, no lo crea

Errores corregidos:

❌ Intentar dict(nombres) directamente → No funciona

❌ Confundir creación del diccionario con rellenarlo

EJERCICIO 2: String + Lista (18:10 - 18:25)
Objetivo: Filtrar palabras con más de 5 letras

Código final:

python
frase = "Python es un lenguaje de programación muy potente"
palabra_cinco_letras = []
palabras = frase.split()
for palabra in palabras:
    if len(palabra) > 5:
        palabra_cinco_letras.append(palabra)

if palabra_cinco_letras:
    print(f"Palabras con más de 5 letras: {palabra_cinco_letras}")
else:
    print("No hay palabras con más de 5 letras")
Resultado: ['Python', 'lenguaje', 'programación', 'potente']

Conceptos aprendidos:

✅ .split() convierte string en lista de palabras

✅ len(palabra) cuenta caracteres

✅ .append() añade elementos a la lista

✅ Verificar si lista está vacía con if lista:

EJERCICIO 3: Set + Lista (18:25 - 20:28)
Objetivo: Encontrar elementos comunes, únicos y todos sin duplicados

Código final:

python
lista1 =[1]
lista2 = 
elementos_comunes = []
elementos_unicos = []
elementos_sin_duplicados = []

# Elementos comunes
for elemento in lista1:
    if elemento in lista2:
        elementos_comunes.append(elemento)
    if elemento not in lista2:
        elementos_unicos.append(elemento)

# Elementos únicos (segunda parte)
for elemento in lista2:
    if elemento not in lista1:
        elementos_unicos.append(elemento)

# Todos sin duplicados
listas_juntas = lista1 + lista2
for elemento in listas_juntas:
    if elemento not in elementos_sin_duplicados:
        elementos_sin_duplicados.append(elemento)

print(f"Comunes: {elementos_comunes}")
print(f"Únicos: {elementos_unicos}")
print(f"Todos sin duplicados: {elementos_sin_duplicados}")
Resultado:

text
Comunes: 
Únicos:[1]
Todos sin duplicados:[1]
Conceptos aprendidos:

✅ Elementos comunes necesitan 1 solo bucle

✅ Elementos únicos necesitan 2 bucles (ambas direcciones)

✅ Segundo bucle debe comparar con la OTRA lista (not in lista1)

✅ Los dos bucles for deben estar al MISMO NIVEL (misma indentación)

✅ Juntar listas con + y luego eliminar duplicados

Errores corregidos:

❌ if elemento != conjunto2 → ✅ if elemento not in lista2

❌ Solo un bucle para únicos → ✅ Necesitas dos bucles

❌ Segundo bucle indentado dentro del primero → ✅ Mismo nivel

Nota: Se puede hacer con sets en 1 línea cada uno:

set1 & set2 (comunes)

set1 ^ set2 (únicos)

set1 | set2 (todos)

EJERCICIO 4: Diccionario + Tupla (20:28 - 20:42)
Objetivo: Encontrar producto más caro y más barato

Código final:

python
productos = {'manzana': 1.5, 'pan': 0.8, 'leche': 1.2, 'huevos': 2.5}
mas_caro = max(productos, key=productos.get)
menos_caro = min(productos, key=productos.get)
print(f"{mas_caro}: {productos[mas_caro]}€, {menos_caro}: {productos[menos_caro]}€")
Resultado: huevos: 2.5€, pan: 0.8€

Conceptos aprendidos:

✅ max(productos, key=productos.get) → Usa nombre de TU diccionario, NO dict

✅ mas_caro contiene la CLAVE (string)

✅ productos[mas_caro] accede al VALOR (precio)

✅ .get() es un método de DICCIONARIOS, no de valores individuales

Errores corregidos:

❌ max(dict, key=dict.get) → ✅ max(productos, key=productos.get)

❌ Usar dict (palabra reservada) → ✅ Usar nombre de tu variable

❌ Confundir clave con valor

EJERCICIO 5: Lista + String (20:42 - 20:52)
Objetivo: Unir palabras con guiones en mayúsculas

Código final:

python
palabras = ["hola", "mundo", "python"]
palabras_mayusculas = []
for palabra in palabras:
    palabras_mayusculas.append(palabra.upper())
resultado = "-".join(palabras_mayusculas)
print(resultado)
Resultado: HOLA-MUNDO-PYTHON

Conceptos aprendidos:

✅ .upper() convierte a mayúsculas

✅ "-".join(lista) une elementos con separador

✅ Línea redundante eliminada (solo hacer .upper() sin guardar)

Errores corregidos:

❌ palabra.upper() sin guardar → Optimizado

EJERCICIO 6: Diccionario Anidado (20:52 - 21:03)
Objetivo: Calcular media de notas de cada estudiante

Código final:

python
estudiantes = {
    'Ana': ,
    'Juan': ,
    'Pedro': 
}
medias = {}
for nombre, notas in estudiantes.items():
    media = sum(notas) / len(notas)
    medias[nombre] = media
print(medias)
Resultado: {'Ana': 8.0, 'Juan': 6.0, 'Pedro': 9.0}

Conceptos aprendidos:

✅ .items() devuelve clave Y valor

✅ notas es una LISTA, no un diccionario (no tiene .items())

✅ sum(notas) / len(notas) calcula la media

✅ Guardar en nuevo diccionario con medias[nombre] = media

Confusión aclarada:

❌ Pensar que notas.items() existe → notas es lista, no diccionario

✅ Solo diccionarios tienen .items()

EJERCICIO 7: Set + String (21:03 - 21:12)
Objetivo: Encontrar letras únicas en una frase

Código final:

python
frase = "Hola Mundo"
frase_lower = frase.lower()
frase_remplace = frase_lower.replace(" ", "")
frase_set = set(frase_remplace)
print(frase_set)
Resultado: {'h', 'o', 'l', 'a', 'm', 'u', 'n', 'd'}

Conceptos aprendidos:

✅ .replace(" ", "") para quitar espacios

✅ set(variable) convierte y elimina duplicados automáticamente

✅ set() sin parámetro crea set vacío (no convierte)

Errores corregidos:

❌ .remplace() → ✅ .replace()

❌ frase_remplace = set() → ✅ set(frase_remplace)

❌ print(set()) → ✅ print(frase_set)

Alternativa con bucle (discutida):

python
letras_unicas = []
for letra in frase_sin_espacios:
    if letra not in letras_unicas:
        letras_unicas.append(letra)
Pero set() es más eficiente y corto.

================================================================================
💡 CONCEPTOS CLAVE CONSOLIDADOS:
1. Diccionarios:
✅ Crear diccionario vacío: dict = {}

✅ Añadir clave-valor: dict[clave] = valor

✅ Acceder a valor: dict[clave] o dict.get(clave)

✅ Operador += para incrementar: dict[k] += 1

✅ .items() para recorrer clave y valor juntos

✅ max/min(dict, key=dict.get) para clave de máximo/mínimo

✅ NO existe dict[key, valor] para acceder

2. Listas:
✅ .split() convierte string a lista

✅ .append() añade elementos

✅ len(lista) cuenta elementos

✅ sum(lista) suma números

✅ Juntar listas: lista1 + lista2

✅ Verificar si vacía: if lista:

3. Sets:
✅ set(variable) convierte y elimina duplicados

✅ set() crea set vacío

✅ Sets no mantienen orden

✅ Operadores: & (intersección), ^ (diferencia simétrica), | (unión)

4. Strings:
✅ .lower() convierte a minúsculas

✅ .upper() convierte a MAYÚSCULAS

✅ .replace(viejo, nuevo) reemplaza texto

✅ "-".join(lista) une con separador

5. Bucles:
✅ for elemento in lista: recorre lista

✅ for k, v in dict.items(): recorre diccionario

✅ Dos bucles al MISMO NIVEL de indentación (no uno dentro del otro)

✅ if elemento in lista: verifica existencia

✅ if elemento not in lista: verifica NO existencia

6. Errores comunes corregidos:
❌ Usar dict en lugar del nombre de tu variable

❌ set() en lugar de set(variable)

❌ .remplace() en lugar de .replace()

❌ Confundir lista con diccionario (.items() solo en dict)

❌ Segundo bucle indentado incorrectamente

================================================================================
📊 PROGRESO:
Ejercicios completados en esta sesión:
✅ Ejercicio 1: Lista + Diccionario
✅ Ejercicio 2: String + Lista
✅ Ejercicio 3: Set + Lista (con bucles)
✅ Ejercicio 4: Diccionario + Tupla
✅ Ejercicio 5: Lista + String
✅ Ejercicio 6: Diccionario Anidado
✅ Ejercicio 7: Set + String

Total completados: 7/15 ejercicios (47%)

Archivos creados/modificados:
✅ repaso_dia3.py (ejercicios de hoy)

Pendiente para siguiente sesión:
⏳ Ejercicio 8: Lista + Tupla + Diccionario

⏳ Ejercicios 9-15 restantes

⏳ Actualizar PROGRESO.md con sesión del 2 febrero

⏳ Commitear trabajo de hoy

================================================================================
🎯 PRÓXIMOS PASOS:
Inmediato (al volver del paseo):
⏳ Completar Ejercicio 8

⏳ Continuar con ejercicios 9-15

Objetivo de la semana:
🎯 Terminar los 15 ejercicios de repaso

🎯 Empezar Tema 6: Funciones

🎯 Actualizar PROGRESO.md

Objetivo del mes:
🎯 Completar Módulo 2 al 100%

🎯 Dominar funciones

🎯 Empezar Módulo 3 (POO)

================================================================================
📊 ESTADÍSTICAS:
Tiempo invertido:
Auditoría: ~20 min

Configuración VSCode: ~5 min

Ejercicios: ~3h 26 min

Total sesión: 3h 51 min

Ejercicios por hora:
7 ejercicios / 3.86 horas = ~1.8 ejercicios/hora

Ritmo excelente considerando explicaciones detalladas

Errores corregidos:
Total: ~15 errores diferentes

Todos entendidos y corregidos correctamente

Código escrito:
Líneas aproximadas: ~80 líneas

7 ejercicios funcionales completos

Código limpio y profesional

================================================================================
🔥 HIGHLIGHTS DE LA SESIÓN:
Mejores momentos:
✅ Configuración de VSCode exitosa
✅ 7 ejercicios completados en una tarde
✅ Dominio de max/min(dict, key=dict.get)
✅ Comprensión clara de diferencia entre claves y valores
✅ Código cada vez más limpio y pythónico
✅ Uso correcto de .items() para diccionarios

Conceptos que más costaron:
🤔 Entender que dict() no puede contar automáticamente
🤔 Diferencia entre set() vacío y set(variable)
🤔 Usar nombre de variable en lugar de dict
🤔 Distinguir cuándo una lista tiene .items() (nunca)

Progreso notable:
📈 Código más limpio (sin líneas redundantes)
📈 Mejor comprensión de estructuras de datos
📈 Menos errores de sintaxis
📈 Mayor velocidad resolviendo ejercicios

================================================================================
💪 NOTAS MOTIVACIONALES:
"7 ejercicios en una tarde - ¡Ritmo excelente!"

Logros de hoy:

🎉 Repositorio auditado completamente

🎉 VSCode configurado y funcionando

🎉 7 ejercicios de repaso dominados

🎉 47% de los ejercicios de repaso completados

🎉 Todos los conceptos bien entendidos

Recordatorios:

✅ Cada ejercicio te acerca más al dominio de Python

✅ Los errores son oportunidades de aprendizaje

✅ Tu código es cada vez más profesional

✅ Estás a punto de empezar Funciones (Tema 6)

================================================================================
📝 NOTAS TÉCNICAS:
Intérprete Python:

Versión: 3.13.9

Ubicación configurada en VSCode

Funcionando correctamente

Estructura del código:

Variables con nombres descriptivos

Indentación correcta

Uso de f-strings para prints informativos

Código legible y mantenible

Buenas prácticas aplicadas:

Crear variables intermedias en lugar de anidar operaciones

Usar nombres de variables claros

Verificar casos vacíos (listas sin elementos)

Comentar secciones cuando es necesario

================================================================================
⏱️ RESUMEN DE HORARIOS:
17:22 - Inicio de sesión / Auditoría
17:40 - Configuración VSCode
17:45 - Ejercicio 1 (Lista + Diccionario)
18:10 - Ejercicio 2 (String + Lista)
18:25 - Ejercicio 3 (Set + Lista)
20:28 - Ejercicio 4 (Diccionario + Tupla)
20:42 - Ejercicio 5 (Lista + String)
20:52 - Ejercicio 6 (Diccionario Anidado)
21:03 - Ejercicio 7 (Set + String)
21:12 - Pausa (paseo con la perra)

Próxima sesión: Ejercicio 8 en adelante

================================================================================
✅ ESTADO ACTUAL:
Repositorio: Limpio, sin cambios pendientes de commit
Ejercicios de repaso: 7/15 completados (47%)
Tema actual: Repaso Tema 5
Siguiente: Completar ejercicios 8-15 + empezar Tema 6 (Funciones)

Motivación: ⭐⭐⭐⭐⭐ (5/5)
Comprensión: ⭐⭐⭐⭐⭐ (5/5)
Velocidad: ⭐⭐⭐⭐⭐ (5/5)

🚀 ¡Sigue así! Estás haciendo un trabajo excelente.

Última actualización: 03 febrero 2026, 21:13 CET
Próxima sesión: Continuar con ejercicio 8

text

***

**Copia esto en:** `diary/febrero/dia3sesion1.md`

¡Disfruta del paseo! 🐕 Cuando vuelvas seguimos con el ejercicio 8 💪