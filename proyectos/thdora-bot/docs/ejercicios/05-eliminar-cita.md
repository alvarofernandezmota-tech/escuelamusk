# 📝 EJERCICIO 5: eliminar_cita()

![Dificultad](https://img.shields.io/badge/Dificultad-Media-yellow)
![Tiempo](https://img.shields.io/badge/Tiempo-25_35min-blue)

---

## 🎯 OBJETIVO

Crear función `eliminar_cita()` que borre citas por ID.

**Resultado esperado:**
```python
eliminar_cita(2)
# → Elimina cita con ID=2
# → Devuelve True si eliminó, False si no existía
```

---

## 🔗 CONCEPTOS MUSK RELACIONADOS

**Módulo:** 3 - Estructuras de datos  
**Apuntes:** `apuntes/modulo-3-listas.md`

**Repasa antes:**
- Métodos de listas
- `enumerate()`
- Eliminar elementos
- Valores booleanos

---

## 📚 CONCEPTOS PREVIOS

### 🔹 Eliminar de lista: `.remove()` vs `.pop()`

```python
frutas = ['manzana', 'pera', 'naranja', 'uva']

# Método 1: .remove() por valor
frutas.remove('pera')  # Elimina 'pera'
print(frutas)  # ['manzana', 'naranja', 'uva']

# Método 2: .pop() por índice
frutas = ['manzana', 'pera', 'naranja']
frutas.pop(1)  # Elimina elemento en posición 1 (pera)
print(frutas)  # ['manzana', 'naranja']
```

### 🔹 Función `enumerate()`

```python
frutas = ['manzana', 'pera', 'naranja']

# Sin enumerate (solo elemento)
for fruta in frutas:
    print(fruta)

# Con enumerate (índice + elemento)
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

# Output:
# 0: manzana
# 1: pera
# 2: naranja
```

### 🔹 Valores booleanos `True/False`

```python
def verificar_mayor_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

# Uso
if verificar_mayor_edad(20):
    print("Es mayor de edad")
```

### 🔹 Return temprano

```python
def buscar_numero(lista, objetivo):
    for numero in lista:
        if numero == objetivo:
            return True  # Sale inmediatamente
    return False  # Solo si no encontró nada

print(buscar_numero([1, 2, 3], 2))  # True
print(buscar_numero([1, 2, 3], 5))  # False
```

---

## 📋 ESPECIFICACIONES

### Funciones a crear:

```python
def eliminar_cita(id_cita):
    """
    Elimina una cita por su ID
    
    Parámetros:
        id_cita (int): ID de la cita a eliminar
    
    Returns:
        bool: True si se eliminó, False si no existía
    """

def eliminar_todas_citas():
    """
    Elimina TODAS las citas
    
    Returns:
        int: Número de citas eliminadas
    """
```

---

## 💻 CÓDIGO COMENTADO

```python
from ejercicio_01 import thdora_data
from ejercicio_02 import agregar_cita
from ejercicio_03 import ver_citas


def eliminar_cita(id_cita):
    """
    Elimina cita por ID
    """
    
    # PASO 1: Buscar la cita usando enumerate
    # enumerate nos da índice Y elemento
    for indice, cita in enumerate(thdora_data['citas']):
        
        # PASO 2: Si encontramos el ID
        if cita['id'] == id_cita:
            # Eliminar por índice
            thdora_data['citas'].pop(indice)
            return True  # Éxito
    
    # PASO 3: Si no se encontró
    return False


def eliminar_todas_citas():
    """
    Elimina todas las citas
    """
    
    # Contar cuántas hay
    cantidad = len(thdora_data['citas'])
    
    # Vaciar la lista
    thdora_data['citas'] = []
    
    # Devolver cuántas se eliminaron
    return cantidad


# Testing
if __name__ == "__main__":
    # Añadir citas
    agregar_cita("Dentista", "2026-02-10", "10:00", "11:00")
    agregar_cita("Estudiar", "2026-02-11", "15:00", "17:00")
    agregar_cita("Reunión", "2026-02-12", "09:00", "10:00")
    
    print("📅 Antes de eliminar:")
    ver_citas()
    
    # Eliminar cita ID=2
    print("\n🗑️  Eliminando ID=2...")
    if eliminar_cita(2):
        print("✅ Eliminada")
    else:
        print("❌ No encontrada")
    
    print("\n📅 Después de eliminar:")
    ver_citas()
    
    # Intentar eliminar inexistente
    print("\n🗑️  Eliminando ID=999...")
    if eliminar_cita(999):
        print("✅ Eliminada")
    else:
        print("❌ No existe")
```

---

## ✍️ TU TURNO

### Abre: `ejercicios-practica/ejercicio-05.py`

**Tarea:**
1. Importar funciones anteriores
2. Definir `eliminar_cita(id_cita)`
3. Usar `enumerate()` en bucle
4. `.pop(indice)` para eliminar
5. `return True` si eliminó, `False` si no
6. BONUS: `eliminar_todas_citas()`
7. Testing completo

---

## ❓ PREGUNTAS CLAVE

1. ¿Por qué usar `enumerate()` en vez de `for cita in ...`?
2. ¿Qué diferencia hay entre `.remove()` y `.pop()`?
3. ¿Por qué devolver `True/False` en vez de la cita?
4. ¿Qué pasa si intentas eliminar ID que no existe?
5. ¿Cómo vaciar una lista completamente?

---

## ❌ ERRORES COMUNES

### Error 1: Modificar lista mientras iteras
```python
❌ for cita in thdora_data['citas']:
    if cita['id'] == id_cita:
        thdora_data['citas'].remove(cita)  # Peligroso

✅ for indice, cita in enumerate(thdora_data['citas']):
    if cita['id'] == id_cita:
        thdora_data['citas'].pop(indice)  # Seguro
        break
```

### Error 2: No usar `enumerate()`
```python
❌ for cita in thdora_data['citas']:
    # No tienes el índice para .pop()

✅ for indice, cita in enumerate(thdora_data['citas']):
    # Tienes indice Y cita
```

### Error 3: No devolver nada
```python
❌ def eliminar_cita(id_cita):
    for indice, cita in enumerate(...):
        if cita['id'] == id_cita:
            thdora_data['citas'].pop(indice)
    # ¿Se eliminó o no?

✅ def eliminar_cita(id_cita):
    ...
    return True  # o False
```

---

## 🧪 TESTING

```bash
python ejercicios-practica/ejercicio-05.py
```

**Output esperado:**
```
📅 Antes de eliminar:
[1] Dentista
[2] Estudiar
[3] Reunión

🗑️  Eliminando ID=2...
✅ Eliminada

📅 Después de eliminar:
[1] Dentista
[3] Reunión

🗑️  Eliminando ID=999...
❌ No existe
```

---

## 🎓 ¿QUÉ APRENDISTE?

- [x] `enumerate()` para obtener índice + elemento
- [x] Método `.pop()` para eliminar por índice
- [x] Diferencia entre `.remove()` y `.pop()`
- [x] Devolver `True/False` para indicar éxito
- [x] Return temprano cuando encuentras
- [x] Vaciar lista con `= []`
- [x] Evitar modificar lista mientras iteras

---

## 🎉 FUNDAMENTOS COMPLETADOS

¡Felicidades! Has completado los ejercicios de fundamentos:

- ✅ Ejercicio 1: Diccionario base
- ✅ Ejercicio 2: agregar_cita()
- ✅ Ejercicio 3: ver_citas()
- ✅ Ejercicio 4: buscar_cita()
- ✅ Ejercicio 5: eliminar_cita()

**Próximos ejercicios:**
- Ejercicio 6: modificar_cita()
- Ejercicio 7: guardar_json()
- Ejercicio 8: cargar_json()
- Ejercicio 9: Menú CLI interactivo

---

**Estado:** ⏳ Por hacer  
**Archivo:** `ejercicios-practica/ejercicio-05.py`  
**Tiempo:** 25-35 min