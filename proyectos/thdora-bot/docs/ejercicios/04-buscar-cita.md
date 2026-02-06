# 📝 EJERCICIO 4: buscar_cita()

![Dificultad](https://img.shields.io/badge/Dificultad-Media-yellow)
![Tiempo](https://img.shields.io/badge/Tiempo-30_40min-blue)

---

## 🎯 OBJETIVO

Crear función `buscar_cita()` que encuentre citas por nombre.

**Resultado esperado:**
```python
resultados = buscar_cita("estudiar")
# → Devuelve lista con todas las citas que contienen "estudiar"
# → Búsqueda case-insensitive ("Estudiar" = "estudiar")
```

---

## 🔗 CONCEPTOS MUSK RELACIONADOS

**Módulo:** 3 - Estructuras de control  
**Apuntes:** `apuntes/modulo-3-bucles.md`

**Repasa antes:**
- Bucles `for`
- Condicionales `if`
- Métodos de strings (`.lower()`, `in`)
- Listas vacías

---

## 📚 CONCEPTOS PREVIOS

### 🔹 Búsqueda en listas

```python
numeros = [1, 2, 3, 4, 5]

# Buscar un número
for numero in numeros:
    if numero == 3:
        print("Encontrado!")
        break  # Salir del bucle
```

### 🔹 Operador `in` para strings

```python
texto = "Hola mundo"

if "mundo" in texto:
    print("Contiene 'mundo'")  # ✅ Se ejecuta

if "adios" in texto:
    print("Contiene 'adios'")  # ❌ No se ejecuta
```

### 🔹 Método `.lower()`

```python
texto = "HOLA MUNDO"
print(texto.lower())  # "hola mundo"

# Búsqueda case-insensitive
nombre = "María"
buscar = "MARIA"

if buscar.lower() in nombre.lower():
    print("Encontrado")  # ✅ Funciona
```

### 🔹 Acumular resultados en lista

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = []  # Lista vacía

for numero in numeros:
    if numero % 2 == 0:  # Si es par
        pares.append(numero)

print(pares)  # [2, 4, 6, 8]
```

### 🔹 Devolver lista vacía si no encuentra

```python
def buscar_numeros_mayores(lista, limite):
    resultados = []
    
    for num in lista:
        if num > limite:
            resultados.append(num)
    
    return resultados  # Puede ser [] si no encuentra nada

print(buscar_numeros_mayores([1, 2, 3], 10))  # []
print(buscar_numeros_mayores([5, 10, 15], 7))  # [10, 15]
```

---

## 📋 ESPECIFICACIONES

### Funciones a crear:

```python
def buscar_cita(nombre_buscar):
    """
    Busca citas por nombre (parcial, case-insensitive)
    
    Parámetros:
        nombre_buscar (str): Texto a buscar
    
    Returns:
        list: Citas que coinciden (puede estar vacía)
    """

def buscar_cita_por_id(id_cita):
    """
    Busca una cita específica por ID
    
    Parámetros:
        id_cita (int): ID a buscar
    
    Returns:
        dict o None: La cita o None si no existe
    """
```

---

## 💻 CÓDIGO COMENTADO

```python
from ejercicio_01 import thdora_data
from ejercicio_02 import agregar_cita


def buscar_cita(nombre_buscar):
    """
    Busca citas por nombre
    """
    
    # PASO 1: Lista vacía para resultados
    resultados = []
    
    # PASO 2: Convertir búsqueda a minúsculas
    nombre_lower = nombre_buscar.lower()
    
    # PASO 3: Recorrer todas las citas
    for cita in thdora_data['citas']:
        # Comparar nombres en minúsculas
        if nombre_lower in cita['nombre'].lower():
            resultados.append(cita)
    
    # PASO 4: Devolver resultados (puede ser [])
    return resultados


def buscar_cita_por_id(id_cita):
    """
    Busca por ID específico
    """
    
    # Recorrer todas las citas
    for cita in thdora_data['citas']:
        if cita['id'] == id_cita:
            return cita  # Devolver inmediatamente
    
    # Si no encuentra, devolver None
    return None


# Testing
if __name__ == "__main__":
    # Añadir citas
    agregar_cita("Dentista", "2026-02-10", "10:00", "11:00")
    agregar_cita("Estudiar Python", "2026-02-11", "15:00", "17:00")
    agregar_cita("Estudiar JavaScript", "2026-02-12", "16:00", "18:00")
    
    # Buscar por nombre
    print("Buscando 'estudiar':")
    resultados = buscar_cita("estudiar")
    print(f"Encontradas: {len(resultados)}")
    for cita in resultados:
        print(f"  - {cita['nombre']}")
    
    # Buscar por ID
    print("\nBuscando ID=2:")
    cita = buscar_cita_por_id(2)
    if cita:
        print(f"✅ {cita['nombre']}")
    else:
        print("❌ No encontrada")
```

---

## ✍️ TU TURNO

### Abre: `ejercicios-practica/ejercicio-04.py`

**Tarea:**
1. Importar `thdora_data` y `agregar_cita`
2. Definir `buscar_cita(nombre_buscar)`
3. Crear lista `resultados = []`
4. Convertir a minúsculas con `.lower()`
5. Bucle `for` + `if` para filtrar
6. `return resultados`
7. BONUS: Definir `buscar_cita_por_id()`

---

## ❓ PREGUNTAS CLAVE

1. ¿Por qué usar `.lower()` en la búsqueda?
2. ¿Qué devuelve si no encuentra nada?
3. ¿Por qué `in` y no `==` para comparar nombres?
4. ¿Cuándo devolver `None` vs lista vacía `[]`?
5. ¿Qué hace `break` en un bucle?

---

## ❌ ERRORES COMUNES

### Error 1: No usar `.lower()`
```python
❌ if nombre_buscar in cita['nombre']:  # "estudiar" ≠ "Estudiar"

✅ if nombre_buscar.lower() in cita['nombre'].lower()
```

### Error 2: Devolver dentro del bucle
```python
❌ for cita in thdora_data['citas']:
    if condicion:
        return resultados  # ¡Sale en la primera!

✅ for cita in thdora_data['citas']:
    if condicion:
        resultados.append(cita)
return resultados  # Fuera del bucle
```

### Error 3: No inicializar lista
```python
❌ def buscar_cita(nombre):
    # Falta: resultados = []
    for cita in ...

✅ def buscar_cita(nombre):
    resultados = []  # Inicializar primero
```

---

## 🧪 TESTING

```bash
python ejercicios-practica/ejercicio-04.py
```

**Output esperado:**
```
Buscando 'estudiar':
Encontradas: 2
  - Estudiar Python
  - Estudiar JavaScript

Buscando ID=2:
✅ Estudiar Python
```

---

## 🎓 ¿QUÉ APRENDISTE?

- [x] Búsqueda en listas con `for` + `if`
- [x] Operador `in` para strings
- [x] Método `.lower()` para case-insensitive
- [x] Acumular resultados en lista
- [x] Devolver `None` cuando no encuentra
- [x] Diferencia entre devolver lista vs None
- [x] `break` para salir de bucle temprano

---

## ➡️ SIGUIENTE PASO

→ **Ejercicio 5: eliminar_cita()**

Aprenderás:
- Eliminar elementos de listas
- `enumerate()` para índice + elemento
- Método `.pop()`
- Devolver `True/False` para indicar éxito

---

**Estado:** ⏳ Por hacer  
**Archivo:** `ejercicios-practica/ejercicio-04.py`  
**Tiempo:** 30-40 min