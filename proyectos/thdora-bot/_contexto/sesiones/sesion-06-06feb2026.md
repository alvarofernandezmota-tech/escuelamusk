# SESIÓN 6 - THDORA Bot

**Fecha:** Viernes 6 febrero 2026  
**Horario:** 16:30 - 19:51 CET  
**Duración:** 3h 21min  
**Día del proyecto:** 6  

---

## 🎯 OBJETIVOS DE LA SESIÓN

- [x] Reorganizar estructura completa del proyecto
- [x] Crear carpeta `_contexto/` permanente
- [x] Sincronizar ejercicios con estructura docs/
- [x] Completar ejercicio 1: Diccionario base
- [x] Completar ejercicio 2: Función agregar_cita()
- [x] Descargar ejercicios 2-5 preparados
- [x] Entender arquitectura modular (datos vs funciones)

---

## ⏱️ TIMELINE DETALLADO

### FASE 1: Reorganización proyecto (16:30 - 18:15 = 1h 45min)

#### 16:30 - 17:00: Análisis estructura y plan
- Identificar problema: ejercicios mezclados con src/
- Diseñar nueva estructura con `_contexto/` permanente
- Decidir arquitectura: docs/ + src/ + ejercicios-practica/

#### 17:00 - 17:40: Creación estructura completa
- Crear carpeta `_contexto/` (permanente, no temporal)
- Mover sesiones a `_contexto/sesiones/`
- Crear `_contexto/mis-sesiones.md` (índice)
- Crear `_contexto/progreso.md`
- Reorganizar `docs/ejercicios/`
- Crear `ejercicios-practica/`

**Commits:**
- [cba8c12](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/cba8c123243d449e816aa900c9fd8f9a17cd0fbe) - Actualizar ejercicio 1 y estructura

#### 17:40 - 18:15: Sincronización ejercicio 1
- Revisar ejercicio-01.py
- Corregir estructura diccionario
- Testing exitoso
- Copiar a src/thdora_data.py

**Commit:**
- [449583a](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/449583a84d554151751944df396ce07e9369a84f) - ✅ Ejercicio 1 completado

---

### FASE 2: Preparación ejercicios 2-5 (18:15 - 18:30 = 15min)

#### 18:15 - 18:30: Creación ejercicios y docs por mentor
- Crear 4 archivos ejercicios con TODOs
- Crear 4 archivos documentación completa
- Push a GitHub

**Commits:**
- [03ad3bd](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/03ad3bd67f7ee626d36cbc3265ce6415261b5fc5) - 📚 Ejercicios 2-5 creados
- [e18fd11](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/e18fd1136129dbdc82c5a7a97bb632af5e31d1e4) - 📝 Documentación completa

---

### FASE 3: Ejercicio 2 - agregar_cita() (18:30 - 19:47 = 1h 17min)

#### 18:30 - 19:00: Lectura y comprensión
- Git pull para descargar ejercicios
- Leer `docs/ejercicios/02-agregar-cita.md`
- Estudiar conceptos: `def`, parámetros, `return`, `.append()`
- Resolver dudas sobre imports

#### 19:00 - 19:30: Implementación
- Escribir función `agregar_cita()` en ejercicio-02.py
- Problema import resuelto (usar diccionario temporal)
- Testing local exitoso
- Entender diferencia datos temporal vs productivo

#### 19:30 - 19:47: Integración a src/
- Copiar ejercicio-02.py → src/thdora_functions.py
- Cambiar a import real: `from thdora_data import thdora_data`
- Testing en src/ exitoso
- Commit final

**Commit:**
- [5e2221a](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/5e2221a9eed665b883f9548f6d7fd62a5cc67631) - ✅ Ejercicio 2 completado

---

### FASE 4: Documentación sesión (19:47 - 19:51 = 4min)

- Actualizar diario sesión 6
- Actualizar mis-sesiones.md
- Commit documentación

---

## ✅ LOGROS COMPLETADOS

### 1. Reorganización Completa del Proyecto ✅
**Tiempo:** 1h 45min

**Nueva estructura creada:**
```
proyectos/thdora-bot/
├── _contexto/                    ⭐ NUEVO (permanente)
│   ├── sesiones/
│   │   ├── sesion-01-01feb2026.md
│   │   ├── sesion-02-02feb2026.md
│   │   ├── sesion-03-03feb2026.md
│   │   ├── sesion-04-04feb2026.md
│   │   ├── sesion-05-05feb2026.md
│   │   └── sesion-06-06feb2026.md
│   ├── mis-sesiones.md          ⭐ NUEVO (índice)
│   └── progreso.md              ⭐ NUEVO
│
├── docs/
│   ├── ejercicios/              ⭐ Reorganizado
│   │   ├── 01-diccionario-base.md
│   │   ├── 02-agregar-cita.md   (descargado)
│   │   ├── 03-ver-citas.md      (descargado)
│   │   ├── 04-buscar-cita.md    (descargado)
│   │   └── 05-eliminar-cita.md  (descargado)
│   └── arquitectura.md
│
├── ejercicios-practica/         ⭐ NUEVO (sandbox)
│   ├── ejercicio-01.py          ✅
│   ├── ejercicio-02.py          ✅
│   ├── ejercicio-03.py          📥
│   ├── ejercicio-04.py          📥
│   └── ejercicio-05.py          📥
│
└── src/                         ⭐ Solo código productivo
    ├── thdora_data.py           ✅
    ├── thdora_functions.py      ✅
    └── snapshots/
```

**Filosofía establecida:**
- `_contexto/` → Permanente (no es temporal)
- `ejercicios-practica/` → Sandbox seguro
- `src/` → Solo código productivo
- `docs/` → Documentación y guías

---

### 2. Ejercicio 1: Diccionario Base ✅
**Tiempo:** 30 min

**Código:**
```python
thdora_data = {
    'citas': []  # Lista vacía
}
```

**Conceptos:**
- Diccionarios en Python
- Listas vacías
- `len()` para contar
- `if __name__ == "__main__":`

**Archivos:**
- ✅ `ejercicios-practica/ejercicio-01.py`
- ✅ `src/thdora_data.py`

---

### 3. Ejercicio 2: agregar_cita() ✅
**Tiempo:** 1h 17min

**Código:**
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

**Conceptos dominados:**
- Funciones con `def`
- Parámetros de funciones
- `.append()` para listas
- `return` vs `print`
- IDs únicos automáticos
- Imports entre archivos
- Separación datos/funciones
- Testing temporal vs productivo

**Testing exitoso:**
```
🧪 Testing agregar_cita()...

✅ Cita 1: {'id': 1, 'nombre': 'Dentista', 'fecha': '2026-02-10', ...}
✅ Cita 2: {'id': 2, 'nombre': 'Estudiar', 'fecha': '2026-02-11', ...}

📊 Total citas: 2
```

**Archivos:**
- ✅ `ejercicios-practica/ejercicio-02.py` (con datos temporales)
- ✅ `src/thdora_functions.py` (con import real)

---

### 4. Ejercicios 2-5 Preparados ✅
**Tiempo:** 15 min (creados por mentor)

**Archivos descargados:**
- 📝 4 documentaciones completas (docs/ejercicios/)
- 🎯 4 archivos ejercicios con TODOs (ejercicios-practica/)

**Total:** 8 archivos, ~1650 líneas de documentación

---

## 💡 CONCEPTOS CLAVE DOMINADOS

### 1. Arquitectura modular
```
src/
├── thdora_data.py        → UN punto de verdad (datos)
└── thdora_functions.py   → Funciones (importa datos)
```

**Ventaja:** No duplicar diccionario en memoria

---

### 2. Testing temporal vs productivo

**En ejercicios-practica/ (sandbox):**
```python
thdora_data = {'citas': []}  # Temporal
def agregar_cita(...):
    ...
```
✅ Practicar sin romper nada

**En src/ (productivo):**
```python
from thdora_data import thdora_data  # Import real
def agregar_cita(...):
    ...
```
✅ Código real

---

### 3. return vs print

```python
# ❌ MAL
def agregar_cita(...):
    print("Cita añadida")  # Solo muestra
    # No devuelve nada

# ✅ BIEN
def agregar_cita(...):
    return nueva_cita  # Devuelve datos reutilizables
```

**Print solo en testing:**
```python
if __name__ == "__main__":
    cita = agregar_cita(...)
    print(cita)  # Aquí SÍ
```

---

### 4. IDs únicos automáticos

```python
'id': len(thdora_data['citas']) + 1
# Si hay 0 citas → id = 1
# Si hay 2 citas → id = 3
```

---

### 5. if __name__ == "__main__":

```python
def agregar_cita(...):
    ...

if __name__ == "__main__":  # Solo si ejecutas directamente
    # Testing aquí
    cita = agregar_cita(...)
    print(cita)
```

**Ventaja:** Testing no interfiere con imports

---

## 🎓 PREGUNTAS CLAVE RESUELTAS

### 1. "¿Por qué usuario NO es lista pero citas SÍ?"

**Respuesta:**
- Usuario = UN objeto → diccionario simple
- Citas = MUCHOS objetos → lista de diccionarios

```python
'usuario': {'nombre': 'Álvaro'}      # Uno
'citas': [                           # Muchos
    {'nombre': 'Dentista'},
    {'nombre': 'Estudiar'}
]
```

---

### 2. "¿Por qué eliminar thdora_data en src/ pero mantener testing?"

**Respuesta:**

**Eliminar diccionario:**
```python
❌ thdora_data = {...}  # No duplicar
✅ from thdora_data import thdora_data  # Import único
```
→ Evita tener DOS diccionarios en memoria

**Mantener testing:**
```python
✅ if __name__ == "__main__":
    # Testing útil
```
→ Solo se ejecuta al correr archivo directamente

---

### 3. "¿Cómo se añaden parámetros al diccionario sin modificarlo manualmente?"

**Respuesta:**

```python
# Diccionario VACÍO al inicio
thdora_data = {'citas': []}

# Función AÑADE dinámicamente
agregar_cita("Dentista", "2026-02-10", "10:00", "11:00")
# → thdora_data = {'citas': [{'id': 1, 'nombre': 'Dentista', ...}]}

agregar_cita("Estudiar", "2026-02-11", "15:00", "17:00")
# → thdora_data = {'citas': [{...}, {'id': 2, 'nombre': 'Estudiar', ...}]}
```

⚠️ **Temporal:** Se pierde al cerrar programa  
✅ **Solución:** Ejercicio 7 (guardar JSON)

---

### 4. "¿Separar funciones usuario y citas en carpetas diferentes?"

**Respuesta:**

**Ahora (simple):**
```
src/
├── thdora_data.py
└── thdora_functions.py  # Todas las funciones
```

**Después (cuando crezca):**
```
src/
├── data/
│   ├── usuario.py
│   └── citas.py
└── functions/
    ├── usuario_funcs.py
    └── citas_funcs.py
```

**Filosofía:** Start simple, refactor when needed

---

## 🐛 PROBLEMAS RESUELTOS

### 1. Error import en ejercicios-practica/
**Problema:**
```python
from ejercicio_01 import thdora_data  # ❌ ModuleNotFoundError
```

**Solución:**
```python
# En ejercicios-practica/ → Diccionario temporal
thdora_data = {'citas': []}  # ✅

# En src/ → Import real
from thdora_data import thdora_data  # ✅
```

---

### 2. Ruta incorrecta al ejecutar
**Problema:**
```bash
# Desde escuelamusk/
python src/thdora_functions.py  # ❌ No such file
```

**Solución:**
```bash
cd proyectos/thdora-bot/  # ✅ Ir a carpeta correcta
python src/thdora_functions.py
```

---

### 3. Código duplicado en ejercicio-01.py
**Problema:** Definir `thdora_data` DOS veces

**Solución:** Un solo diccionario, eliminar duplicados

---

## 📊 PROGRESO DEL PROYECTO

### Ejercicios completados: 2/12 (16.7%)

| # | Ejercicio | Estado | Tiempo | Commit |
|---|-----------|--------|--------|--------|
| 1 | Diccionario base | ✅ | 30 min | [449583a](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/449583a84d554151751944df396ce07e9369a84f) |
| 2 | agregar_cita() | ✅ | 1h 17min | [5e2221a](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/5e2221a9eed665b883f9548f6d7fd62a5cc67631) |
| 3 | ver_citas() | ⏳ | - | - |
| 4 | buscar_cita() | ⏳ | - | - |
| 5 | eliminar_cita() | ⏳ | - | - |

### Funciones implementadas:
- ✅ `agregar_cita(nombre, fecha, hora_inicio, hora_fin)`

### Próximas funciones:
- ⏳ `ver_citas()`
- ⏳ `buscar_cita(nombre_buscar)`
- ⏳ `eliminar_cita(id_cita)`

---

## 🔄 COMMITS DE LA SESIÓN

| Hora | SHA | Descripción | Archivos |
|------|-----|-------------|----------|
| 16:41 | [cba8c12](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/cba8c123243d449e816aa900c9fd8f9a17cd0fbe) | Actualizar ejercicio 1 y estructura | 3 |
| 17:36 | [449583a](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/449583a84d554151751944df396ce07e9369a84f) | ✅ Ejercicio 1 completado | 2 |
| 17:54 | [03ad3bd](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/03ad3bd67f7ee626d36cbc3265ce6415261b5fc5) | 📚 Ejercicios 2-5 creados | 4 |
| 17:57 | [e18fd11](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/e18fd1136129dbdc82c5a7a97bb632af5e31d1e4) | 📝 Documentación completa | 4 |
| 18:47 | [5e2221a](https://github.com/alvarofernandezmota-tech/escuelamusk/commit/5e2221a9eed665b883f9548f6d7fd62a5cc67631) | ✅ Ejercicio 2 completado | 2 |

**Total commits:** 5  
**Total archivos modificados:** 15+

---

## 📈 ESTADÍSTICAS

- **Duración total:** 3h 21min
- **Tiempo reorganización:** 1h 45min (52%)
- **Tiempo ejercicio 1:** 30 min (15%)
- **Tiempo ejercicio 2:** 1h 17min (38%)
- **Código escrito:** ~120 líneas
- **Documentación creada:** ~1650 líneas
- **Conceptos nuevos:** 15+
- **Archivos creados:** 12
- **Archivos modificados:** 6
- **Commits realizados:** 5
- **Problemas resueltos:** 3

---

## 🎯 PRÓXIMA SESIÓN (Día 7 - Sábado 7 feb)

### Prioridad 1: Escuela Musk (80% tiempo)
- Estudiar módulos pendientes
- Ejercicios Musk sobre:
  - Funciones con `def`
  - Bucles `for`
  - Condicionales `if/else`
  - F-strings

### Prioridad 2: THDORA (20% tiempo)
- **Ejercicio 3:** `ver_citas()` (~25-35 min)
  - Leer: `docs/ejercicios/03-ver-citas.md`
  - Completar: `ejercicios-practica/ejercicio-03.py`
  - Conceptos: bucle `for`, formateo, condicionales

### Archivos preparados:
```
✅ docs/ejercicios/03-ver-citas.md
✅ ejercicios-practica/ejercicio-03.py
```

---

## 📚 RECURSOS CONSULTADOS

- Documentación Python sobre funciones
- `docs/ejercicios/02-agregar-cita.md`
- Explicación `return` vs `print`
- Estructura modular de proyectos
- `if __name__ == "__main__":` propósito
- Arquitectura de carpetas Python

---

## 💭 REFLEXIONES

### ✅ Lo que funcionó muy bien:

1. **Reorganización desde el inicio**
   - Estructura clara antes de avanzar
   - `_contexto/` permanente evita confusión
   - `ejercicios-practica/` como sandbox seguro

2. **Metodología ejercicios**
   - Leer docs primero
   - Practicar en sandbox
   - Copiar a src/ con cambios
   - Testing en ambos lugares

3. **Separación datos/funciones**
   - Un punto de verdad para `thdora_data`
   - Funciones importan datos
   - Evita duplicación

4. **Documentación completa antes**
   - Ejercicios 2-5 listos
   - Estudiante puede avanzar solo

---

### 🎓 Lo aprendido:

1. **Funciones devuelven, no muestran**
   - `return` para reutilizar
   - `print` solo en testing

2. **Arquitectura escalable**
   - Simple al inicio
   - Modular cuando crece
   - Refactorizar cuando necesario

3. **Testing no invasivo**
   - `if __name__ == "__main__":`
   - Útil sin interferir

4. **IDs automáticos**
   - `len() + 1` genera únicos
   - Sin intervención manual

5. **Import centralizado**
   - Un diccionario, muchos imports
   - Mejor que copiar datos

---

### 🚀 Para mejorar:

1. **Commits más frecuentes**
   - Después de cada logro pequeño
   - No esperar ejercicio completo

2. **Testing incremental**
   - Probar cada función inmediatamente
   - No acumular código sin probar

3. **Leer documentación completa**
   - Antes de escribir código
   - Evita errores conocidos

---

## ⭐ NOTA FINAL

**Sesión excepcional.** El estudiante demostró:

✅ **Pensamiento arquitectónico avanzado:**
- Pregunta sobre separar funciones por entidad
- Comprensión de "un punto de verdad" para datos
- Razonamiento sobre escalabilidad

✅ **Dominio de conceptos:**
- Diccionarios y listas sólido
- Funciones con parámetros correcto
- Return vs print perfectamente entendido
- Imports entre archivos dominado

✅ **Metodología profesional:**
- Workflow docs → práctica → producción
- Testing sistemático
- Commits organizados

✅ **Capacidad de aprendizaje:**
- Hace preguntas correctas sobre diseño
- Entiende razones, no solo código
- Aplica conceptos inmediatamente

**Preparado para ejercicio 3** (bucles `for` + formateo).

**Recomendación:** Priorizar Escuela Musk mañana (80%), luego THDORA (20%).

---

**Fin Sesión 6**  
**Próxima:** Sábado 7 febrero 2026  
**Estado:** ✅ Completada exitosamente