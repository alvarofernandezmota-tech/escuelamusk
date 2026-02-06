# 📅 Sesión 6B: Ejercicios 1-2 THDORA

**Fecha:** Viernes 6 febrero 2026  
**Horario:** 18:15 - 19:47 CET  
**Duración:** 1h 32min  

---

## 🎯 OBJETIVO

1. Preparar ejercicios 2-5 (documentación + templates)
2. Completar ejercicio 2: `agregar_cita()`
3. Entender arquitectura modular (datos vs funciones)
4. Dominar: `def`, parámetros, `return`, `.append()`

---

## ✅ LOGROS COMPLETADOS

### 1. Ejercicios 2-5 preparados (18:15-18:30)
**Tiempo:** 15 min (creados por mentor)

**Archivos creados:**
- 📝 4 documentaciones completas (`docs/ejercicios/`)
  - `02-agregar-cita.md` (319 líneas)
  - `03-ver-citas.md` (292 líneas)
  - `04-buscar-cita.md` (305 líneas)
  - `05-eliminar-cita.md` (319 líneas)

- 🎯 4 archivos práctica con TODOs (`ejercicios-practica/`)
  - `ejercicio-02.py`
  - `ejercicio-03.py`
  - `ejercicio-04.py`
  - `ejercicio-05.py`

**Commits:**
- [03ad3bd](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/03ad3bd67f7ee626d36cbc3265ce6415261b5fc5) - Archivos ejercicios
- [e18fd11](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/e18fd1136129dbdc82c5a7a97bb632af5e31d1e4) - Documentación

---

### 2. Ejercicio 2: agregar_cita() ✅ (18:30-19:47)
**Tiempo:** 1h 17min

#### Código implementado:
```python
def agregar_cita(nombre, fecha, hora_inicio, hora_fin):
    """
    Añade una nueva cita al diccionario thdora_data
    """
    nueva_cita = {
        'id': len(thdora_data['citas']) + 1,
        'nombre': nombre,
        'fecha': fecha,
        'hora_inicio': hora_inicio,
        'hora_fin': hora_fin,
    }
    
    thdora_data['citas'].append(nueva_cita)
    return nueva_cita
```

#### Proceso:
1. **Lectura** (18:30-19:00)
   - Git pull para descargar ejercicios
   - Leer `docs/ejercicios/02-agregar-cita.md`
   - Estudiar conceptos: `def`, parámetros, `return`

2. **Implementación** (19:00-19:30)
   - Escribir función en `ejercicio-02.py`
   - Resolver problema import (usar diccionario temporal)
   - Testing local exitoso

3. **Integración** (19:30-19:47)
   - Copiar a `src/thdora_functions.py`
   - Cambiar a import real: `from thdora_data import thdora_data`
   - Testing en src/ exitoso

#### Testing:
```
🧪 Testing agregar_cita()...

✅ Cita 1: {'id': 1, 'nombre': 'Dentista', ...}
✅ Cita 2: {'id': 2, 'nombre': 'Estudiar', ...}

📊 Total citas: 2
```

**Commit:**
- [5e2221a](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/5e2221a9eed665b883f9548f6d7fd62a5cc67631) - Ejercicio 2 completado

---

## 🎓 CONCEPTOS DOMINADOS

### 1. Funciones con def
```python
def nombre_funcion(parametro1, parametro2):
    # código
    return resultado  # Devuelve datos
```

### 2. return vs print
- ✅ `return` → Devuelve datos (reutilizable)
- ❌ `print` → Solo muestra (no reutilizable)
- Print solo en testing

### 3. Append para listas
```python
lista = []
lista.append(elemento)  # Añade al final
```

### 4. IDs únicos automáticos
```python
'id': len(thdora_data['citas']) + 1  # 1, 2, 3, 4...
```

### 5. Arquitectura modular
```
src/
├── thdora_data.py        → SOLO datos (un punto de verdad)
└── thdora_functions.py   → SOLO funciones (importa datos)
```

### 6. Testing temporal vs productivo
```python
# En ejercicios-practica/ (sandbox)
thdora_data = {'citas': []}  # Temporal, no afecta nada

# En src/ (productivo)
from thdora_data import thdora_data  # Import real
```

### 7. if __name__ == "__main__":
```python
if __name__ == "__main__":
    # Solo se ejecuta al correr archivo directamente
    # Testing aquí
```

---

## 🐛 PROBLEMAS RESUELTOS

### 1. Error import en ejercicios-practica/
**Problema:**
```python
from ejercicio_01 import thdora_data  # ❌ ModuleNotFoundError
```

**Solución:**
```python
# Usar diccionario temporal en ejercicios-practica/
thdora_data = {'citas': []}  # ✅

# Import real solo en src/
from thdora_data import thdora_data  # ✅
```

### 2. Ruta incorrecta
**Problema:**
```bash
# Desde escuelamusk/
python src/thdora_functions.py  # ❌ No such file
```

**Solución:**
```bash
cd proyectos/thdora-bot/  # ✅ Ir a carpeta correcta primero
python src/thdora_functions.py
```

---

## 💡 PREGUNTAS RESUELTAS

### "¿Por qué usuario NO es lista pero citas SÍ?"
```python
'usuario': {'nombre': 'Álvaro'}  # UNO → diccionario
'citas': [...]                    # MUCHOS → lista
```

### "¿Por qué eliminar thdora_data en src/?"
- Evitar DOS diccionarios en memoria
- Un punto de verdad: `thdora_data.py`
- Funciones importan desde ahí

### "¿Cómo se añaden parámetros sin modificar manualmente?"
```python
# Diccionario vacío al inicio
thdora_data = {'citas': []}

# Función añade dinámicamente
agregar_cita("Dentista", "2026-02-10", "10:00", "11:00")
# → thdora_data ahora tiene 1 cita
```
⚠️ Temporal (se pierde al cerrar)
✅ Ejercicio 7: guardar en JSON (permanente)

---

## 📊 PROGRESO

### Ejercicios: 2/12 completados (16.7%)

| # | Ejercicio | Estado | Archivo |
|---|-----------|--------|---------|
| 1 | Diccionario base | ✅ | `thdora_data.py` |
| 2 | agregar_cita() | ✅ | `thdora_functions.py` |
| 3 | ver_citas() | 📥 Preparado | `ejercicio-03.py` |
| 4 | buscar_cita() | 📥 Preparado | `ejercicio-04.py` |
| 5 | eliminar_cita() | 📥 Preparado | `ejercicio-05.py` |

---

## 🔗 COMMITS DE LA SESIÓN

| Hora | SHA | Descripción |
|------|-----|-------------|
| 17:54 | [03ad3bd](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/03ad3bd67f7ee626d36cbc3265ce6415261b5fc5) | Ejercicios 2-5 creados |
| 17:57 | [e18fd11](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/e18fd1136129dbdc82c5a7a97bb632af5e31d1e4) | Documentación completa |
| 18:47 | [5e2221a](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/5e2221a9eed665b883f9548f6d7fd62a5cc67631) | Ejercicio 2 completado |

---

## 📈 ESTADÍSTICAS

- **Tiempo total:** 1h 32min
- **Código escrito:** ~80 líneas
- **Documentación creada:** ~1650 líneas (ejercicios 2-5)
- **Conceptos nuevos:** 7
- **Archivos creados:** 8
- **Problemas resueltos:** 2

---

## 💭 REFLEXIONES

### ✅ Lo que funcionó:
1. Leer documentación antes de código
2. Practicar en sandbox (ejercicios-practica/)
3. Testing incremental
4. Separación datos/funciones clara

### 🎓 Aprendido:
1. Return devuelve, print muestra
2. Un diccionario central mejor que muchos
3. Testing no invasivo con `if __name__`
4. IDs automáticos con `len() + 1`

### 🚀 Para mejorar:
1. Commits más frecuentes
2. Leer docs completos antes
3. Probar en sandbox primero siempre

---

## ➡️ PRÓXIMA SESIÓN

**Día 7 - Sábado 7 febrero 2026**

### Prioridad 1: Escuela Musk (80%)
- Estudiar módulos pendientes
- Ejercicios sobre funciones y bucles

### Prioridad 2: THDORA (20%)
- **Ejercicio 3:** `ver_citas()` (25-35 min)
- Leer: `docs/ejercicios/03-ver-citas.md`
- Completar: `ejercicios-practica/ejercicio-03.py`
- Conceptos: bucle `for`, formateo, f-strings

**Archivos listos:**
- ✅ `docs/ejercicios/03-ver-citas.md`
- ✅ `ejercicios-practica/ejercicio-03.py`

---

## ⭐ NOTA FINAL

Excelente sesión. Estudiante demostró:
- ✅ Comprensión sólida de funciones
- ✅ Pensamiento arquitectónico avanzado
- ✅ Capacidad de hacer preguntas clave
- ✅ Workflow profesional: docs → práctica → producción

**Preparado para ejercicio 3** (bucles `for`).

---

**Estado:** ✅ Completado  
**Siguiente:** Musk prioridad + Ejercicio 3