# 📝 EJERCICIO 2: agregar_cita()

![Dificultad](https://img.shields.io/badge/Dificultad-Media-yellow)
![Tiempo](https://img.shields.io/badge/Tiempo-30_45min-blue)

---

## 🎯 OBJETIVO

Crear tu primera función: `agregar_cita()` que añada citas al diccionario.

**Resultado esperado:**
```python
agregar_cita("Dentista", "2026-02-10", "10:00", "11:00")
# → Añade cita a thdora_data['citas']
# → Devuelve diccionario de la cita creada
```

---

## 🔗 CONCEPTOS MUSK RELACIONADOS

**Módulo:** 3 - Funciones  
**Apuntes:** `apuntes/modulo-3-funciones.md`  
**Ejercicios previos:** `ejercicios/modulo-3/funciones.py`

**Repasa antes:**
- ¿Qué es una función?
- ¿Cómo se define con `def`?
- ¿Qué son los parámetros?
- ¿Qué hace `return`?

---

## 📚 CONCEPTOS PREVIOS

### 🔹 ¿Qué es una función?

**Una función es un bloque de código reutilizable.**

```python
# Sin función (repetitivo)
print("Hola, María")
print("Hola, Pedro")
print("Hola, Ana")

# Con función (reutilizable)
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("María")
saludar("Pedro")
saludar("Ana")
```

### 🔹 Sintaxis de funciones

```python
def nombre_funcion(parametro1, parametro2):
    # Código que hace algo
    resultado = parametro1 + parametro2
    return resultado

# Usar la función
valor = nombre_funcion(5, 3)
print(valor)  # 8
```

### 🔹 `return` vs `print`

```python
# ❌ MAL: solo print
def sumar_mal(a, b):
    print(a + b)  # Solo muestra

resultado = sumar_mal(5, 3)  # Imprime 8
print(resultado)  # None (¡no devuelve nada!)

# ✅ BIEN: return
def sumar_bien(a, b):
    return a + b  # Devuelve el valor

resultado = sumar_bien(5, 3)
print(resultado)  # 8
print(resultado * 2)  # 16 (puedes usar el valor)
```

### 🔹 Método `.append()`

```python
# Añadir elementos a una lista
frutas = ['manzana', 'pera']

frutas.append('naranja')
print(frutas)  # ['manzana', 'pera', 'naranja']

frutas.append('uva')
print(frutas)  # ['manzana', 'pera', 'naranja', 'uva']
```

### 🔹 Parámetros opcionales

```python
def saludar(nombre, formal=False):
    if formal:
        print(f"Buenos días, Sr./Sra. {nombre}")
    else:
        print(f"Hola, {nombre}")

saludar("María")  # Hola, María
saludar("María", formal=True)  # Buenos días, Sr./Sra. María
```

---

## 📋 ESPECIFICACIONES

### Función a crear:

```python
def agregar_cita(nombre, fecha, hora_inicio, hora_fin, descripcion=''):
    """
    Añade una nueva cita al diccionario thdora_data
    
    Parámetros:
        nombre (str): Nombre de la cita
        fecha (str): Fecha formato YYYY-MM-DD
        hora_inicio (str): Hora inicio HH:MM
        hora_fin (str): Hora fin HH:MM
        descripcion (str): Descripción opcional
    
    Returns:
        dict: La cita creada
    """
```

### Estructura cita:

```python
{
    'id': 1,
    'nombre': 'Dentista',
    'fecha': '2026-02-10',
    'hora_inicio': '10:00',
    'hora_fin': '11:00',
    'descripcion': 'Revisión anual'
}
```

---

## 💻 CÓDIGO COMENTADO

```python
# ==========================================
# PASO 1: Importar datos
# ==========================================
from ejercicio_01 import thdora_data
# Importamos el diccionario del ejercicio 1


# ==========================================
# PASO 2: Definir la función
# ==========================================
def agregar_cita(nombre, fecha, hora_inicio, hora_fin, descripcion=''):
    """
    Docstring: Explica qué hace la función
    """
    
    # PASO 3: Crear diccionario nueva_cita
    nueva_cita = {
        'id': len(thdora_data['citas']) + 1,  # ID único automático
        'nombre': nombre,                      # Parámetro recibido
        'fecha': fecha,
        'hora_inicio': hora_inicio,
        'hora_fin': hora_fin,
        'descripcion': descripcion             # Opcional (default='')
    }
    
    # PASO 4: Añadir a la lista de citas
    thdora_data['citas'].append(nueva_cita)
    # .append() añade al final de la lista
    
    # PASO 5: Devolver la cita creada
    return nueva_cita
    # return permite usar el resultado después


# ==========================================
# PASO 6: Testing
# ==========================================
if __name__ == "__main__":
    # Este bloque solo se ejecuta si corres este archivo
    
    print("🧪 Testing agregar_cita()...\n")
    
    # Probar la función
    cita1 = agregar_cita("Dentista", "2026-02-10", "10:00", "11:00")
    print(f"✅ Cita 1: {cita1}")
    
    cita2 = agregar_cita("Estudiar", "2026-02-11", "15:00", "17:00", "Python")
    print(f"✅ Cita 2: {cita2}")
    
    print(f"\n📊 Total citas: {len(thdora_data['citas'])}")
```

---

## ✍️ TU TURNO

### Abre: `ejercicios-practica/ejercicio-02.py`

**Tarea:**
1. Importar `thdora_data` del ejercicio 1
2. Definir función `agregar_cita()` con 5 parámetros
3. Crear diccionario `nueva_cita` con 6 campos
4. Usar `.append()` para añadir a la lista
5. `return nueva_cita`
6. Testing: añadir 2-3 citas de prueba

---

## ❓ PREGUNTAS CLAVE

1. ¿Qué hace `def`?
2. ¿Para qué sirven los parámetros?
3. ¿Qué diferencia hay entre `print()` y `return`?
4. ¿Cómo generar un ID único automáticamente?
5. ¿Qué hace `.append()`?
6. ¿Por qué `descripcion=''` tiene un valor default?
7. ¿Cuándo se ejecuta el código en `if __name__ == "__main__":`?

---

## ❌ ERRORES COMUNES

### Error 1: Olvidar `return`
```python
❌ def agregar_cita(...):
    nueva_cita = {...}
    thdora_data['citas'].append(nueva_cita)
    # ¡Falta return!

✅ def agregar_cita(...):
    nueva_cita = {...}
    thdora_data['citas'].append(nueva_cita)
    return nueva_cita
```

### Error 2: Paréntesis en `def`
```python
❌ def agregar_cita nombre, fecha:  # Faltan paréntesis

✅ def agregar_cita(nombre, fecha):
```

### Error 3: No importar thdora_data
```python
❌ def agregar_cita(...):
    thdora_data['citas'].append(...)  # ¿De dónde sale thdora_data?

✅ from ejercicio_01 import thdora_data
```

### Error 4: ID manual
```python
❌ nueva_cita = {'id': 1, ...}  # Siempre 1

✅ nueva_cita = {'id': len(thdora_data['citas']) + 1, ...}  # Automático
```

---

## 🧪 TESTING

```bash
python ejercicios-practica/ejercicio-02.py
```

**Output esperado:**
```
🧪 Testing agregar_cita()...

✅ Cita 1: {'id': 1, 'nombre': 'Dentista', 'fecha': '2026-02-10', ...}
✅ Cita 2: {'id': 2, 'nombre': 'Estudiar', 'fecha': '2026-02-11', ...}

📊 Total citas: 2
```

---

## 🎓 ¿QUÉ APRENDISTE?

- [x] Definir funciones con `def`
- [x] Usar parámetros en funciones
- [x] Parámetros opcionales con valor default
- [x] Diferencia entre `return` y `print`
- [x] Método `.append()` para listas
- [x] Generar IDs únicos automáticamente
- [x] Bloque `if __name__ == "__main__":` para testing
- [x] Docstrings para documentar funciones

---

## ➡️ SIGUIENTE PASO

→ **Ejercicio 3: ver_citas()**

Aprenderás:
- Bucles `for` para recorrer listas
- Condicionales `if/else`
- Formateo con f-strings
- Funciones que solo muestran (sin return)

---

**Estado:** ⏳ Por hacer  
**Archivo:** `ejercicios-practica/ejercicio-02.py`  
**Tiempo:** 30-45 min