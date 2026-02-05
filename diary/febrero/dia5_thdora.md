# 📅 SESIÓN THDORA - 5 Febrero 2026

**Hora:** 21:12 - 22:09 (57 minutos)  
**Tema:** Estructura de datos + Cálculo automático de minutos  
**Estado:** En progreso - Completar mañana

---

## 🎯 OBJETIVO DE HOY

Crear la **capa de datos** de THDORA:
- Diccionario para almacenar sesiones
- Función para agregar sesiones
- Cálculo automático de minutos con `datetime`

---

## 📚 CONCEPTOS APRENDIDOS

### 1. **Módulos e imports** (Tema 6)
```python
from datetime import datetime  # Importar clase específica
import json                     # Importar módulo completo
import os                       # Sistema operativo
```

**Aprendido:**
- Diferencia entre `import` vs `from...import`
- Módulos estándar de Python (datetime, json, os)
- Cuándo usar cada tipo de import

---

### 2. **Diccionarios anidados**
```python
thdora_data = {
    'sesiones': [          # Lista dentro de diccionario
        {                  # Diccionario dentro de lista
            'id': 1,
            'nombre': 'Musk',
            'minutos': 219
        }
    ]
}
```

**Aprendido:**
- Estructura de "macro diccionario"
- Diccionarios dentro de listas
- Acceso: `thdora_data['sesiones'][0]['nombre']`

---

### 3. **Cálculo con datetime**
```python
from datetime import datetime

inicio = datetime.strptime('12:45', '%H:%M')
fin = datetime.strptime('16:24', '%H:%M')
diferencia = fin - inicio
minutos = int(diferencia.total_seconds() / 60)  # 219
```

**Aprendido:**
- `strptime()` convierte string → datetime
- Restar datetime para obtener diferencia
- `total_seconds()` para convertir a minutos

---

### 4. **Decisión: Campo "nombre" vs "proyecto"**

Decidimos usar **`nombre`** porque:
- ✅ Más universal (cualquier tipo de sesión)
- ✅ Más corto que `nombre_sesion`
- ✅ Más claro que `proyecto`

Ejemplos de uso:
- `nombre: 'Musk'` → Sesión de estudio
- `nombre: 'Médico'` → Cita médica
- `nombre: 'Gimnasio'` → Entrenamiento
- `nombre: 'Siesta'` → Descanso

---

### 5. **Funciones CRUD básicas**

Diseñamos las operaciones principales:
- **C**reate → `agregar_sesion()`
- **R**ead → `ver_sesiones()`, `buscar_sesion()`
- **U**pdate → `modificar_sesion()`
- **D**elete → `eliminar_sesion()`

---

## 💻 CÓDIGO DESARROLLADO

### Archivo: `datos/thdora_data.py` (v0.3 - INCOMPLETO)

```python
"""
THDORA - Datos v0.3
Archivo: proyectos/thdora-bot/datos/thdora_data.py

Capa de datos con:
- Diccionario principal
- Agregar sesión (con cálculo auto de minutos)
- Ver sesiones
- Modificar sesión
- Eliminar sesión
"""

from datetime import datetime

# ============================================
# DICCIONARIO PRINCIPAL
# ============================================

thdora_data = {
    'sesiones': []  # Lista vacía inicial
}

# ============================================
# CREAR SESIÓN
# ============================================

def agregar_sesion(nombre, hora_inicio, hora_fin):
    """
    Crea y agrega una sesión al diccionario
    
    Parámetros:
        nombre: str - Nombre de la actividad
        hora_inicio: str - Formato 'HH:MM' (ej: '12:45')
        hora_fin: str - Formato 'HH:MM' (ej: '16:24')
    
    Retorna:
        dict - La sesión creada
    
    Ejemplo:
        >>> agregar_sesion('Musk', '12:45', '16:24')
        {'id': 1, 'nombre': 'Musk', 'minutos': 219, ...}
    """
    
    # Calcular minutos automáticamente
    inicio = datetime.strptime(hora_inicio, '%H:%M')
    fin = datetime.strptime(hora_fin, '%H:%M')
    diferencia = fin - inicio
    minutos = int(diferencia.total_seconds() / 60)
    
    # Crear diccionario de sesión
    sesion = {
        'id': len(thdora_data['sesiones']) + 1,
        'nombre': nombre,
        'hora_inicio': hora_inicio,
        'hora_fin': hora_fin,
        'minutos': minutos
    }
    
    # Agregar a la lista
    thdora_data['sesiones'].append(sesion)
    
    return sesion

# ============================================
# LEER SESIONES
# ============================================

def ver_sesiones():
    """Muestra todas las sesiones en formato bonito"""
    
    if not thdora_data['sesiones']:
        print("📅 No hay sesiones registradas")
        return
    
    print("\n📅 SESIONES:")
    print("=" * 50)
    
    for s in thdora_data['sesiones']:
        print(f"{s['hora_inicio']}-{s['hora_fin']}: {s['nombre']} ({s['minutos']}min)")
    
    total = sum(s['minutos'] for s in thdora_data['sesiones'])
    print(f"\n⏱️  TOTAL: {total} min = {total/60:.1f}h")
    print("=" * 50)


def buscar_sesion(id_sesion):
    """
    Busca una sesión por ID
    
    Retorna:
        dict o None
    """
    for s in thdora_data['sesiones']:
        if s['id'] == id_sesion:
            return s
    return None

# ============================================
# ACTUALIZAR SESIÓN
# ============================================

def modificar_sesion(id_sesion, nuevo_nombre=None, nueva_hora_inicio=None, nueva_hora_fin=None):
    """
    Modifica campos de una sesión existente
    
    Parámetros opcionales (solo modifica los que se pasen):
        nuevo_nombre: str
        nueva_hora_inicio: str
        nueva_hora_fin: str
    
    Retorna:
        bool - True si modificó, False si no encontró
    """
    sesion = buscar_sesion(id_sesion)
    
    if sesion is None:
        print(f"❌ Sesión {id_sesion} no encontrada")
        return False
    
    # Modificar solo lo que se pasó
    if nuevo_nombre:
        sesion['nombre'] = nuevo_nombre
    
    if nueva_hora_inicio:
        sesion['hora_inicio'] = nueva_hora_inicio
    
    if nueva_hora_fin:
        sesion['hora_fin'] = nueva_hora_fin
    
    # Recalcular minutos si cambiaron horas
    if nueva_hora_inicio or nueva_hora_fin:
        inicio = datetime.strptime(sesion['hora_inicio'], '%H:%M')
        fin = datetime.strptime(sesion['hora_fin'], '%H:%M')
        diferencia = fin - inicio
        sesion['minutos'] = int(diferencia.total_seconds() / 60)
    
    print(f"✅ Sesión {id_sesion} modificada")
    return True

# ============================================
# ELIMINAR SESIÓN
# ============================================

def eliminar_sesion(id_sesion):
    """
    Elimina una sesión por ID
    
    Retorna:
        bool - True si eliminó, False si no encontró
    """
    sesion = buscar_sesion(id_sesion)
    
    if sesion is None:
        print(f"❌ Sesión {id_sesion} no encontrada")
        return False
    
    thdora_data['sesiones'].remove(sesion)
    print(f"🗑️  Sesión eliminada: {sesion['nombre']}")
    return True

# ============================================
# ZONA DE PRUEBAS
# ============================================

if __name__ == "__main__":
    print("\n🎯 PRUEBAS THDORA v0.3")
    print("=" * 50)
    
    # Agregar sesiones del 5 de febrero
    print("\n--- AGREGAR SESIONES ---")
    agregar_sesion('Musk', '12:45', '16:24')
    agregar_sesion('Siesta', '14:30', '15:30')
    agregar_sesion('Paseo Thea', '16:00', '17:00')
    agregar_sesion('ML', '19:00', '21:00')
    agregar_sesion('THDORA', '21:12', '22:09')
    
    ver_sesiones()
    
    print("\n" + "=" * 50)
    print("✅ PRUEBAS COMPLETADAS")
    print("=" * 50 + "\n")
```

---

## 🧪 EJERCICIOS PARA MAÑANA

### Ejercicio 1: Probar el código
```bash
cd proyectos/thdora-bot
python datos/thdora_data.py
```

### Ejercicio 2: Agregar sesión nueva
```python
agregar_sesion('Desayuno', '08:00', '08:30')
ver_sesiones()
```

### Ejercicio 3: Modificar sesión
```python
modificar_sesion(2, nuevo_nombre='Descanso')
ver_sesiones()
```

### Ejercicio 4: Eliminar sesión
```python
eliminar_sesion(3)
ver_sesiones()
```

### Ejercicio 5: Buscar sesión específica
```python
sesion = buscar_sesion(1)
if sesion:
    print(f"Encontrada: {sesion['nombre']}")
```

---

## 🔍 CONCEPTOS A REPASAR MAÑANA

Antes de continuar, asegúrate de entender:

### 1. **Diccionarios anidados**
```python
datos = {
    'lista': [
        {'campo': 'valor'}
    ]
}
```

### 2. **List comprehension**
```python
total = sum(s['minutos'] for s in sesiones)
```

### 3. **Parámetros opcionales**
```python
def funcion(obligatorio, opcional=None):
    if opcional:
        # usar opcional
```

### 4. **Conversión datetime**
```python
datetime.strptime('12:45', '%H:%M')  # str → datetime
```

---

## 📋 PRÓXIMOS PASOS

### MAÑANA - Sesión 2:

1. **Completar el archivo `datos/thdora_data.py`**
   - ✅ Ya hecho: CRUD básico
   - ⏳ Falta: Guardar/cargar JSON

2. **Agregar persistencia (JSON)**
   ```python
   def guardar_datos():
       # Guardar en archivo
   
   def cargar_datos():
       # Cargar desde archivo
   ```

3. **Crear `funciones/thdora_logic.py`**
   - Validaciones
   - Cálculos avanzados
   - Mensajes formateados

4. **Actualizar `main.py`**
   - Conectar con Telegram
   - Comandos básicos

---

## 📊 ESTRUCTURA OBJETIVO

```
proyectos/thdora-bot/
├── datos/
│   ├── thdora_data.py         ✅ En progreso (80%)
│   └── thdora_sesiones.json   ⏳ Pendiente (auto-creado)
│
├── funciones/
│   └── thdora_logic.py        ⏳ Pendiente
│
├── main.py                     ⏳ Actualizar
├── requirements.txt            ⏳ Crear
└── .env                        ⏳ Crear
```

---

## 💡 DECISIONES IMPORTANTES

### 1. **Diccionarios en lugar de clases**
- ✅ Más simple para empezar
- ✅ No necesitas OOP todavía
- 📅 Migrar a clases en Tema 9-10

### 2. **Campo "nombre" en lugar de "proyecto"**
- ✅ Más universal
- ✅ Permite cualquier tipo de sesión

### 3. **Cálculo automático de minutos**
- ✅ Usuario no calcula manualmente
- ✅ Usa datetime.strptime()

### 4. **Sin categorías por ahora**
- ✅ Mantiene simple
- 📅 Agregar después si es necesario

---

## ⏱️ TIEMPO REAL DE HOY

```
Sesión completa: 57 minutos
├── Diseño estructura: 15 min
├── Discusión conceptos: 25 min
├── Código base: 15 min
└── Documentación: 2 min
```

**Total estudio hoy (5 Feb 2026):**
- Musk: 219 min (3.7h)
- ML: 120 min (2h)
- THDORA: 57 min (1h)
- **TOTAL: 396 min = 6.6 horas** 🔥

---

## 🎯 OBJETIVOS SESIÓN MAÑANA

1. ✅ Completar JSON (guardar/cargar)
2. ✅ Probar todo el flujo
3. ✅ Hacer ejercicios de práctica
4. ✅ Entender cada concepto

**Duración estimada:** 1 hora

---

## 📝 NOTAS IMPORTANTES

- 🧠 Los diccionarios son "macro diccionarios" (diccionarios dentro de listas dentro de diccionarios)
- 🕐 datetime.strptime() convierte string a datetime para calcular
- 🔄 CRUD = Create, Read, Update, Delete (operaciones básicas)
- 📦 Todo en memoria RAM por ahora (se pierde al cerrar Python)
- 💾 Mañana agregamos JSON para persistir datos

---

## ✅ LO QUE FUNCIONA

- Crear sesiones ✅
- Ver sesiones ✅
- Modificar sesiones ✅
- Eliminar sesiones ✅
- Buscar sesiones ✅
- Calcular minutos automáticamente ✅

## ⏳ LO QUE FALTA

- Guardar en JSON ⏳
- Cargar desde JSON ⏳
- Validaciones (hora_fin > hora_inicio) ⏳
- Fecha automática (datetime.now()) ⏳
- Bot de Telegram ⏳

---

**Estado:** 🟡 En progreso - Continuar mañana

**Progreso total THDORA:** 40% ▓▓▓▓░░░░░░
