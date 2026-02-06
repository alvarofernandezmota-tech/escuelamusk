# SESIÓN 6 - THDORA Bot

**Fecha:** Viernes 6 febrero 2026  
**Horario:** 18:30 - 19:47 CET  
**Duración:** 1h 17min  
**Día del proyecto:** 6  

---

## 🎯 OBJETIVOS DE LA SESIÓN

- [x] Completar ejercicio 1: Diccionario base
- [x] Completar ejercicio 2: Función agregar_cita()
- [x] Descargar ejercicios 2-5 para práctica
- [x] Entender estructura datos vs funciones
- [x] Entender imports entre archivos

---

## ✅ LOGROS COMPLETADOS

### 1. Ejercicio 1: Diccionario Base ✅
**Tiempo:** 18:30 - 18:45 (15 min)

**Código creado:**
```python
thdora_data = {
    'citas': []  # Lista vacía
}
```

**Archivos:**
- ✅ `ejercicios-practica/ejercicio-01.py`
- ✅ `src/thdora_data.py`

**Conceptos aprendidos:**
- Diccionarios en Python
- Listas vacías
- `len()` para contar elementos
- `if __name__ == "__main__":`
- Print vs testing

**Commit:** [449583a](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/449583a84d554151751944df396ce07e9369a84f)

---

### 2. Ejercicios 2-5 Descargados ✅
**Tiempo:** 18:50 - 19:00 (10 min)

**Creados por mentor:**
- 📝 `docs/ejercicios/02-agregar-cita.md`
- 📝 `docs/ejercicios/03-ver-citas.md`
- 📝 `docs/ejercicios/04-buscar-cita.md`
- 📝 `docs/ejercicios/05-eliminar-cita.md`
- 🎯 `ejercicios-practica/ejercicio-02.py` (con TODOs)
- 🎯 `ejercicios-practica/ejercicio-03.py` (con TODOs)
- 🎯 `ejercicios-practica/ejercicio-04.py` (con TODOs)
- 🎯 `ejercicios-practica/ejercicio-05.py` (con TODOs)

**Commits:**
- [03ad3bd](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/03ad3bd67f7ee626d36cbc3265ce6415261b5fc5) - Archivos ejercicios
- [e18fd11](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/e18fd1136129dbdc82c5a7a97bb632af5e31d1e4) - Documentación completa

---

### 3. Ejercicio 2: agregar_cita() ✅
**Tiempo:** 19:00 - 19:40 (40 min)

**Código creado:**
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

**Archivos:**
- ✅ `ejercicios-practica/ejercicio-02.py` (con `thdora_data` temporal)
- ✅ `src/thdora_functions.py` (con `from thdora_data import thdora_data`)

**Conceptos aprendidos:**
- Funciones con `def`
- Parámetros de funciones
- `.append()` para añadir a listas
- `return` vs `print`
- IDs únicos automáticos (`len() + 1`)
- Imports entre archivos
- Separación datos (thdora_data.py) vs funciones (thdora_functions.py)
- Testing temporal vs código productivo
- `if __name__ == "__main__":` para testing

**Testing exitoso:**
```
🧪 Testing agregar_cita()...

✅ Cita 1: {'id': 1, 'nombre': 'Dentista', 'fecha': '2026-02-10', ...}
✅ Cita 2: {'id': 2, 'nombre': 'Estudiar', 'fecha': '2026-02-11', ...}

📊 Total citas: 2
```

**Commit:** [5e2221a](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/5e2221a9eed665b883f9548f6d7fd62a5cc67631)

---

## 💡 CONCEPTOS CLAVE ENTENDIDOS

### 1. Estructura de archivos separada
```
src/
├── thdora_data.py        → SOLO diccionario (un punto de verdad)
└── thdora_functions.py   → SOLO funciones (importa el diccionario)
```

### 2. Testing temporal vs productivo
```python
# En ejercicios-practica/ (temporal)
thdora_data = {'citas': []}  # No afecta código real

# En src/ (productivo)
from thdora_data import thdora_data  # Import real
```

### 3. return vs print
```python
def agregar_cita(...):
    nueva_cita = {...}
    return nueva_cita  # ✅ Devuelve datos (reutilizable)
    # NO print aquí (solo en testing)
```

### 4. IDs únicos automáticos
```python
'id': len(thdora_data['citas']) + 1  # Genera 1, 2, 3, 4...
```

---

## 🎓 APRENDIZAJE DESTACADO

### Pregunta clave resuelta:
**"¿Por qué eliminar `thdora_data = {...}` en src/ pero mantener testing?"**

**Respuesta:**
- ❌ NO duplicar diccionario (evitar dos versiones en memoria)
- ✅ SÍ mantener testing (`if __name__ == "__main__":`) porque:
  - Solo se ejecuta al correr archivo directamente
  - No interfiere con imports
  - Útil para pruebas rápidas
  - Documenta uso de la función

### Flujo correcto entendido:
```
1. ejercicios-practica/ → Practicar con datos temporales (sandbox)
2. src/ → Copiar código + cambiar import a real
3. Testing → Siempre útil en ambos lugares
```

---

## 📊 PROGRESO DEL PROYECTO

### Ejercicios completados: 2/12 (16.7%)

| Ejercicio | Estado | Tiempo |
|-----------|--------|--------|
| 1. Diccionario base | ✅ | 15 min |
| 2. agregar_cita() | ✅ | 40 min |
| 3. ver_citas() | ⏳ | - |
| 4. buscar_cita() | ⏳ | - |
| 5. eliminar_cita() | ⏳ | - |

### Archivos creados:
```
proyectos/thdora-bot/
├── src/
│   ├── thdora_data.py           ✅ (ejercicio 1)
│   └── thdora_functions.py      ✅ (ejercicio 2)
│
├── ejercicios-practica/
│   ├── ejercicio-01.py          ✅ completado
│   ├── ejercicio-02.py          ✅ completado
│   ├── ejercicio-03.py          📥 descargado (TODOs)
│   ├── ejercicio-04.py          📥 descargado (TODOs)
│   └── ejercicio-05.py          📥 descargado (TODOs)
│
└── docs/ejercicios/
    ├── 01-diccionario-base.md   ✅ (sesión anterior)
    ├── 02-agregar-cita.md       📥 descargado
    ├── 03-ver-citas.md          📥 descargado
    ├── 04-buscar-cita.md        📥 descargado
    └── 05-eliminar-cita.md      📥 descargado
```

---

## 🐛 PROBLEMAS RESUELTOS

### 1. Error de import en ejercicio-02.py
**Problema:**
```python
from ejercicio_01 import thdora_data  # ❌ ModuleNotFoundError
```

**Solución:**
```python
# En ejercicios-practica/ → usar diccionario temporal
thdora_data = {'citas': []}  # ✅ Para testing

# En src/ → import real
from thdora_data import thdora_data  # ✅ Para producción
```

### 2. Ruta incorrecta al ejecutar
**Problema:**
```bash
# Desde escuelamusk/
python src/thdora_functions.py  # ❌ No such file
```

**Solución:**
```bash
cd proyectos/thdora-bot/  # ✅ Carpeta correcta primero
python src/thdora_functions.py
```

### 3. Confusión sobre estructura datos
**Pregunta:** "¿Por qué usuario NO es lista pero citas SÍ?"

**Respuesta:**
- Usuario = UN solo objeto (diccionario) → datos estáticos
- Citas = MUCHOS objetos (lista) → datos dinámicos

---

## 🔄 COMMITS DE LA SESIÓN

| Hora | Commit | Descripción |
|------|--------|-------------|
| 17:36 | [449583a](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/449583a84d554151751944df396ce07e9369a84f) | ✅ Ejercicio 1 completado |
| 17:54 | [03ad3bd](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/03ad3bd67f7ee626d36cbc3265ce6415261b5fc5) | 📚 Ejercicios 2-5 creados |
| 17:57 | [e18fd11](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/e18fd1136129dbdc82c5a7a97bb632af5e31d1e4) | 📝 Documentación ejercicios |
| 18:47 | [5e2221a](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/5e2221a9eed665b883f9548f6d7fd62a5cc67631) | ✅ Ejercicio 2 completado |

**Total commits:** 4

---

## 📈 ESTADÍSTICAS

- **Tiempo total:** 1h 17min
- **Código escrito:** ~80 líneas
- **Conceptos nuevos:** 10+
- **Archivos creados:** 6
- **Archivos descargados:** 8
- **Commits realizados:** 4
- **Errores resueltos:** 3

---

## 🎯 PRÓXIMA SESIÓN (Día 7)

### Prioridad 1: Escuela Musk (80% tiempo)
- Estudiar módulos pendientes
- Hacer ejercicios Musk sobre funciones
- Repasar conceptos: `def`, `for`, `if/else`

### Prioridad 2: THDORA (20% tiempo)
- **Ejercicio 3:** `ver_citas()` (~25-35 min)
- Conceptos: bucle `for`, f-strings, formateo
- Archivo: `ejercicios-practica/ejercicio-03.py`
- Docs: `docs/ejercicios/03-ver-citas.md`

### Archivos preparados:
```
✅ docs/ejercicios/03-ver-citas.md      (leer primero)
✅ ejercicios-practica/ejercicio-03.py  (completar TODOs)
```

---

## 💭 REFLEXIONES

### ✅ Lo que funcionó bien:
1. Separar archivos datos/funciones desde el inicio
2. Estructura ejercicios-practica/ para sandbox
3. Documentación completa antes de practicar
4. Testing con `if __name__ == "__main__":`
5. Workflow: docs → práctica → src → commit

### 🎓 Lo aprendido:
1. Funciones devuelven datos (`return`), no los muestran (`print`)
2. Un solo punto de verdad para datos (evitar duplicados)
3. Testing temporal útil sin romper código productivo
4. IDs automáticos con `len() + 1`
5. Import centralizado mejor que datos en cada archivo

### 🚀 Para mejorar:
1. Leer documentación completa antes de empezar ejercicio
2. No mezclar ejercicios (hacer uno a la vez)
3. Probar en ejercicios-practica/ ANTES de copiar a src/
4. Commit más frecuentes (después de cada logro)

---

## 📚 RECURSOS CONSULTADOS

- `docs/ejercicios/02-agregar-cita.md` (conceptos funciones)
- Explicación `return` vs `print`
- Estructura modular Python
- `if __name__ == "__main__":` propósito

---

## ✨ NOTA FINAL

**Excelente progreso.** El estudiante ha demostrado:
- ✅ Comprensión sólida de diccionarios y listas
- ✅ Entendimiento correcto de funciones con parámetros
- ✅ Buen razonamiento sobre arquitectura de código
- ✅ Capacidad de hacer preguntas clave sobre diseño
- ✅ Workflow organizado: docs → práctica → producción

**Preparado para ejercicio 3** (ver_citas con bucles `for`).

---

**Fin Sesión 6**  
**Próxima:** Sábado 7 febrero 2026 (Musk + Ejercicio 3)