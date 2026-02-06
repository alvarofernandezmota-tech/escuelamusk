# 📝 EJERCICIO 1: Diccionario Base

![Dificultad](https://img.shields.io/badge/Dificultad-Básica-green)
![Tiempo](https://img.shields.io/badge/Tiempo-20min-blue)

---

## 🎯 Objetivo

Crear el diccionario base de THDORA con una lista vacía de citas.

---

## 📚 Conceptos previos

### 🔹 ¿Qué es un diccionario?

Un diccionario es una estructura de datos que almacena pares **clave-valor**.

```python
# Sintaxis básica
persona = {
    'nombre': 'Álvaro',    # clave: 'nombre', valor: 'Álvaro'
    'edad': 25           # clave: 'edad', valor: 25
}

# Acceder a valores
print(persona['nombre'])  # Output: Álvaro
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

## 📋 Especificaciones

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
    'titulo': 'Dentista',
    'fecha': '2026-02-10',      # Formato: YYYY-MM-DD
    'hora': '10:00',            # Formato: HH:MM
    'descripcion': 'Revisión anual'
}
```

---

## ✅ Solución

**Archivo:** `src/thdora_data.py`

```python
"""
THDORA v0.1 - Bot de gestión de citas
Fecha: 6 febrero 2026

VERSION 0.1: Diccionario MÍNIMO
"""

# Diccionario base
thdora_data = {
    'citas': []  # Lista vacía de citas
}


# Zona de pruebas
if __name__ == "__main__":
    print("🤖 THDORA v0.1 - Diccionario base\n")
    
    print("Diccionario inicial:")
    print(thdora_data)
    print(f"\nNúmero de citas: {len(thdora_data['citas'])}")
    print("\n✅ Diccionario creado correctamente")
```

---

## 🧪 Testing

```bash
# Ejecutar desde la carpeta thdora-bot/
python src/thdora_data.py
```

**Output esperado:**
```
🤖 THDORA v0.1 - Diccionario base

Diccionario inicial:
{'citas': []}

Número de citas: 0

✅ Diccionario creado correctamente
```

---

## 🎓 ¿Qué aprendiste?

- [x] Crear un diccionario vacío
- [x] Usar listas dentro de diccionarios
- [x] Acceder a valores con `diccionario['clave']`
- [x] Usar `len()` para contar elementos de una lista
- [x] Estructura básica de un proyecto Python
- [x] Bloque `if __name__ == "__main__":` para testing

---

## ➡️ Siguiente

[Ejercicio 2: agregar_cita() →](./02-agregar-cita.md)

---

**Estado:** ✅ Completado  
**Snapshot:** `src/snapshots/v01_diccionario.py`  
**Commit:** `✅ Ejercicio 1: Diccionario base THDORA v0.1`