# 📝 EJERCICIO 3: ver_citas()

![Dificultad](https://img.shields.io/badge/Dificultad-Media-yellow)
![Tiempo](https://img.shields.io/badge/Tiempo-25_35min-blue)

---

## 🎯 OBJETIVO

Crear función `ver_citas()` que muestre todas las citas de forma legible.

**Resultado esperado:**
```
📅 CITAS REGISTRADAS (3)
==================================================
[1] Dentista
    📅 2026-02-10 | ⏰ 10:00-11:00
    📝 Revisión anual

[2] Estudiar Python
    📅 2026-02-11 | ⏰ 15:00-17:00
```

---

## 🔗 CONCEPTOS MUSK RELACIONADOS

**Módulo:** 3 - Estructuras de control  
**Apuntes:** `apuntes/modulo-3-bucles.md`

**Repasa antes:**
- ¿Qué es un bucle `for`?
- ¿Cómo recorrer una lista?
- ¿Qué son condicionales `if/else`?
- ¿Qué son f-strings?

---

## 📚 CONCEPTOS PREVIOS

### 🔹 Bucle `for`

```python
# Recorrer lista
frutas = ['manzana', 'pera', 'naranja']

for fruta in frutas:
    print(fruta)

# Output:
# manzana
# pera
# naranja
```

### 🔹 Recorrer lista de diccionarios

```python
personas = [
    {'nombre': 'Ana', 'edad': 25},
    {'nombre': 'Luis', 'edad': 30}
]

for persona in personas:
    print(f"{persona['nombre']} tiene {persona['edad']} años")

# Output:
# Ana tiene 25 años
# Luis tiene 30 años
```

### 🔹 Condicional `if/else`

```python
edad = 18

if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
```

### 🔹 F-strings (formateo)

```python
nombre = "María"
edad = 25

# Método antiguo
print("Nombre: " + nombre + ", Edad: " + str(edad))

# F-string (moderno)
print(f"Nombre: {nombre}, Edad: {edad}")
```

### 🔹 Función sin `return`

```python
def mostrar_mensaje():
    print("Hola mundo")
    # No devuelve nada, solo muestra

mostrar_mensaje()  # Imprime: Hola mundo
resultado = mostrar_mensaje()  # resultado = None
```

---

## 📋 ESPECIFICACIONES

### Función a crear:

```python
def ver_citas():
    """
    Muestra todas las citas formateadas.
    No devuelve nada, solo imprime.
    """
```

### Formato de salida:

```
📅 CITAS REGISTRADAS (2)
==================================================
[1] Nombre de la cita
    📅 Fecha | ⏰ Hora inicio-Hora fin
    📝 Descripción (si existe)

[2] Otra cita
    ...
```

---

## 💻 CÓDIGO COMENTADO

```python
from ejercicio_01 import thdora_data
from ejercicio_02 import agregar_cita


def ver_citas():
    """
    Muestra todas las citas del diccionario
    """
    
    # PASO 1: Verificar si hay citas
    if len(thdora_data['citas']) == 0:
        print("📭 No hay citas registradas")
        return  # Salir de la función
    
    # PASO 2: Mostrar encabezado
    cantidad = len(thdora_data['citas'])
    print(f"\n📅 CITAS REGISTRADAS ({cantidad})\n")
    print("=" * 50)
    
    # PASO 3: Recorrer todas las citas
    for cita in thdora_data['citas']:
        # Mostrar ID y nombre
        print(f"\n[{cita['id']}] {cita['nombre']}")
        
        # Mostrar fecha y hora
        print(f"    📅 {cita['fecha']} | ⏰ {cita['hora_inicio']}-{cita['hora_fin']}")
        
        # Mostrar descripción si existe
        if cita['descripcion']:
            print(f"    📝 {cita['descripcion']}")


# Testing
if __name__ == "__main__":
    # Añadir citas de prueba
    agregar_cita("Dentista", "2026-02-10", "10:00", "11:00", "Revisión")
    agregar_cita("Estudiar", "2026-02-11", "15:00", "17:00")
    
    # Mostrar todas
    ver_citas()
```

---

## ✍️ TU TURNO

### Abre: `ejercicios-practica/ejercicio-03.py`

**Tarea:**
1. Importar `thdora_data` y `agregar_cita`
2. Definir función `ver_citas()` (sin parámetros)
3. Verificar si la lista está vacía
4. Mostrar encabezado con cantidad
5. Bucle `for` para recorrer citas
6. Formatear salida con f-strings
7. Testing: añadir citas y mostrarlas

---

## ❓ PREGUNTAS CLAVE

1. ¿Qué hace `for cita in thdora_data['citas']:`?
2. ¿Por qué esta función NO tiene `return`?
3. ¿Cómo acceder a valores del diccionario `cita`?
4. ¿Qué hace `"=" * 50`?
5. ¿Por qué verificar `if cita['descripcion']:`?
6. ¿Cuándo usar `return` sin valor?

---

## ❌ ERRORES COMUNES

### Error 1: Olvidar verificar lista vacía
```python
❌ def ver_citas():
    for cita in thdora_data['citas']:  # Error si lista vacía
        ...

✅ def ver_citas():
    if len(thdora_data['citas']) == 0:
        print("No hay citas")
        return
    for cita in ...
```

### Error 2: Usar `return` con valor
```python
❌ def ver_citas():
    print(...)
    return "Algo"  # Esta función no debe devolver nada

✅ def ver_citas():
    print(...)
    # Sin return, o return vacío
```

### Error 3: No formatear bien
```python
❌ print(cita)  # Muestra todo el diccionario feo

✅ print(f"[{cita['id']}] {cita['nombre']}")  # Formateado
```

---

## 🧪 TESTING

```bash
python ejercicios-practica/ejercicio-03.py
```

**Output esperado:**
```
📅 CITAS REGISTRADAS (2)
==================================================

[1] Dentista
    📅 2026-02-10 | ⏰ 10:00-11:00
    📝 Revisión

[2] Estudiar
    📅 2026-02-11 | ⏰ 15:00-17:00
```

---

## 🎓 ¿QUÉ APRENDISTE?

- [x] Bucles `for` para recorrer listas
- [x] Recorrer lista de diccionarios
- [x] Condicionales `if/else`
- [x] F-strings para formateo
- [x] Funciones sin `return`
- [x] `return` vacío para salir de función
- [x] Verificar lista vacía
- [x] Formateo legible de datos

---

## ➡️ SIGUIENTE PASO

→ **Ejercicio 4: buscar_cita()**

Aprenderás:
- Búsqueda en listas
- Comparación de strings
- `.lower()` para case-insensitive
- Devolver listas de resultados

---

**Estado:** ⏳ Por hacer  
**Archivo:** `ejercicios-practica/ejercicio-03.py`  
**Tiempo:** 25-35 min