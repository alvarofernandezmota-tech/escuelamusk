# 📝 EJERCICIO 1: Diccionario Base

![Dificultad](https://img.shields.io/badge/Dificultad-Básica-green)
![Tiempo](https://img.shields.io/badge/Tiempo-20_30min-blue)

---

## 🎯 OBJETIVO

Crear el diccionario base de THDORA con una lista vacía de citas.

**Resultado esperado:**
```python
thdora_data = {
    'citas': []
}
```

---

## 🔗 CONCEPTOS MUSK RELACIONADOS

**Módulo:** 3 - Estructuras de datos  
**Apuntes:** `apuntes/modulo-3-estructuras.md`  
**Ejercicios previos:** `ejercicios/modulo-3/diccionarios.py`

**Repasa antes:**
- ¿Qué es un diccionario?
- ¿Cómo crear un diccionario vacío?
- ¿Qué es una lista?
- ¿Cómo crear una lista vacía?

---

## 📚 CONCEPTOS PREVIOS

### 🔹 ¿Qué es un diccionario?

Un diccionario es como una **agenda telefónica**:
- Tienes NOMBRES (claves)
- Cada nombre tiene un VALOR asociado

```python
# Ejemplo simple
agenda = {
    'María': '612345678',
    'Pedro': '698765432'
}

# Acceder a un valor
print(agenda['María'])  # Output: 612345678
```

### 🔹 ¿Qué es una lista?

Una lista es como una **fila de personas**:
- Puede estar vacía: `[]`
- Puede tener elementos: `['Ana', 'Luis', 'Eva']`
- Puedes agregar más: `lista.append('Juan')`

```python
# Ejemplos
lista_vacia = []
lista_numeros = [1, 2, 3, 4, 5]
lista_nombres = ['Ana', 'Luis']

# Añadir elemento
lista_nombres.append('Eva')
print(lista_nombres)  # ['Ana', 'Luis', 'Eva']
```

### 🔹 Diccionario con lista dentro

```python
# Un diccionario puede contener listas
datos = {
    'numeros': [1, 2, 3],
    'nombres': ['Ana', 'Luis']
}

# Acceder a la lista
print(datos['numeros'])  # [1, 2, 3]

# Añadir a la lista
datos['numeros'].append(4)
print(datos['numeros'])  # [1, 2, 3, 4]
```

---

## 📋 ESPECIFICACIONES

### Diccionario a crear:

```python
thdora_data = {
    'citas': []  # Lista vacía
}
```

### Estructura de una cita (para más adelante):

```python
{
    'id': 1,
    'nombre': 'Dentista',           # Nombre de LA CITA
    'fecha': '2026-02-10',          # Formato: YYYY-MM-DD
    'hora_inicio': '10:00',         # Formato: HH:MM
    'hora_fin': '11:00',            # Formato: HH:MM
    'descripcion': 'Revisión anual' # Opcional
}
```

**IMPORTANTE:**
- `'nombre'` = nombre de LA CITA ("Dentista", "Reunión", "Comida")
- `'hora_inicio'` y `'hora_fin'` = rango completo
- NO confundir con nombre de usuario (eso va después)

---

## 💻 CÓDIGO COMENTADO (línea por línea)

```python
# ===================================
# LÍNEA 1: Comentario de cabecera
# ===================================
"""
THDORA v0.1 - Bot de gestión de citas
"""
# ¿Por qué? Para saber qué hace este archivo
# Las """ se usan para comentarios largos (docstring)


# ===================================
# LÍNEA 2: Crear el diccionario
# ===================================
thdora_data = {
    'citas': []
}

# DESGLOSE:
# - thdora_data: nombre de la variable (podría ser "datos" o "agenda")
# - = : asignar valor a la variable
# - { }: esto indica que es un diccionario
# - 'citas': clave del diccionario (usamos comillas para texto)
# - []: lista vacía (todavía no hay citas)


# ===================================
# LÍNEA 3: Probar que funciona
# ===================================
if __name__ == "__main__":
    print(thdora_data)
    
# ¿Por qué if __name__ == "__main__"?
# Para ejecutar código solo cuando corremos este archivo directamente
# (No cuando lo importamos desde otro archivo)
```

---

## ✍️ TU TURNO (ejercicio práctico)

### Abre: `ejercicios-practica/ejercicio-01.py`

**Tarea:**
1. Crea un diccionario llamado `mi_agenda`
2. Dentro, crea una lista vacía llamada `contactos`
3. Imprime el diccionario con `print(mi_agenda)`
4. Imprime cuántos contactos hay con `len(mi_agenda['contactos'])`

**Solución:**
```python
mi_agenda = {
    'contactos': []
}

print(mi_agenda)
print(f"Contactos: {len(mi_agenda['contactos'])}")

# Output:
# {'contactos': []}
# Contactos: 0
```

---

## ❓ PREGUNTAS CLAVE (verifica comprensión)

✅ Responde estas preguntas ANTES de continuar:

1. ¿Qué es un diccionario en Python?
2. ¿Por qué usamos comillas en `'citas'`?
3. ¿Qué significa `[]`?
4. ¿Podríamos usar `"agenda"` en vez de `"thdora_data"`?
5. ¿Cómo agregaremos citas a la lista vacía? (pista: .append())
6. ¿Por qué `'nombre'` de la cita y no `'titulo'`?
7. ¿Por qué necesitamos `hora_inicio` Y `hora_fin`?

**Si NO puedes responder → REPITE el ejercicio o PREGUNTA**

---

## ❌ ERRORES COMUNES

### Error 1: Olvidar comillas en la clave
```python
❌ thdora_data = {
    citas: []  # ERROR
}

✅ thdora_data = {
    'citas': []  # CORRECTO
}
```

### Error 2: Usar () en vez de []
```python
❌ thdora_data = {
    'citas': ()  # Esto es tupla, no lista
}

✅ thdora_data = {
    'citas': []  # Lista vacía
}
```

### Error 3: Olvidar los dos puntos
```python
❌ thdora_data = {
    'citas' []  # Falta :
}

✅ thdora_data = {
    'citas': []  # Correcto
}
```

### Error 4: Confundir {} con []
```python
❌ thdora_data = [  # Esto es lista, no diccionario
    'citas': []
]

✅ thdora_data = {  # Diccionario
    'citas': []
}
```

---

## 🧪 TESTING

### Ejecutar el código:

```bash
# Opción 1: Practicar
python ejercicios-practica/ejercicio-01.py

# Opción 2: Archivo real (después de practicar)
python src/thdora_data.py
```

### Output esperado:
```
🤖 THDORA v0.1 - Diccionario base

Diccionario inicial:
{'citas': []}

Número de citas: 0

✅ Diccionario creado correctamente
```

---

## 🎓 ¿QUÉ APRENDISTE?

- [x] Crear un diccionario vacío
- [x] Usar listas dentro de diccionarios
- [x] Acceder a valores con `diccionario['clave']`
- [x] Usar `len()` para contar elementos
- [x] Estructura básica de un proyecto Python
- [x] Bloque `if __name__ == "__main__":` para testing
- [x] Diferencia entre nombre de cita vs nombre de usuario
- [x] Por qué usar hora_inicio y hora_fin

---

## ➡️ SIGUIENTE PASO

Cuando ENTIENDAS este ejercicio completamente:

→ **Ejercicio 2: agregar_cita()**

Aprenderás:
- Crear funciones con `def`
- Parámetros de funciones
- Método `.append()` para agregar a listas
- Generar IDs únicos

---

**Estado:** ✅ Completado  
**Snapshot:** `src/snapshots/v01_diccionario.py`  
**Commit:** `✅ Ejercicio 1 completado: Diccionario base`  
**Tiempo:** 20-30 min