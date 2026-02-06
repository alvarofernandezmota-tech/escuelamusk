# Sesión 6: THDORA - Ejercicios 1-3 Completados

**Fecha:** 06 febrero 2026  
**Duración:** 3 partes (tarde-noche)  
**Estado:** ✅ Completada  

---

## 🎯 Objetivos Cumplidos

### ✅ Ejercicio 1: Diccionario Base
- Creado `thdora_data` con estructura de citas
- Implementado en `src/thdora_data.py`
- Testing exitoso

### ✅ Ejercicio 2: Función agregar_cita()
- Implementada función para añadir citas
- Parámetros: nombre, fecha, hora_inicio, hora_fin
- Auto-generación de IDs
- Testing con múltiples citas
- Integrada en `src/thdora_functions.py`

### ✅ Ejercicio 3: Función ver_citas()
- Implementada función para visualizar todas las citas
- Manejo de lista vacía con mensaje informativo
- Formato visual con emojis y estructura clara
- Testing con 0 y 4 citas
- Integrada en `src/thdora_functions.py`

---

## 📚 Conceptos Aprendidos

### Python Básico
1. **Diccionarios**: Estructura `{'clave': valor}`
2. **Listas**: Métodos `.append()`, `.len()`
3. **Funciones**: Definición, parámetros, return
4. **Bucle for**: Iteración sobre listas
5. **Condicionales**: `if len() == 0` para validaciones
6. **F-strings**: Formateo de texto con variables

### Estructura de Proyecto
1. **Separación de archivos**:
   - `src/thdora_data.py`: Datos
   - `src/thdora_functions.py`: Lógica
   - `ejercicios-practica/`: Práctica individual

2. **Imports**: Cómo importar entre archivos del proyecto

3. **Testing**: Sección `if __name__ == "__main__":`

---

## 🐛 Problemas Resueltos

### 1. Confusión con Estructura de Archivos
**Problema:** No quedaba claro por qué separar `ejercicios-practica/` de `src/`

**Solución:** 
- `ejercicios-practica/`: Para aprender sin miedo a romper
- `src/`: Versión limpia y funcional del proyecto
- Workflow: Practicar → Entender → Copiar a src/

### 2. Imports Relativos
**Problema:** `from thdora_data import thdora_data` no funcionaba

**Causa:** Ejecutar desde carpeta incorrecta

**Solución:**
```bash
# CORRECTO
cd proyectos/thdora-bot/
python src/thdora_functions.py

# INCORRECTO
cd src/
python thdora_functions.py  # No encuentra thdora_data
```

### 3. Repetición de Código en Ejercicios
**Problema:** Cada ejercicio duplicaba `thdora_data` y funciones previas

**Decisión:** Mantener ejercicios auto-contenidos para aprendizaje, consolidar en `src/` después

---

## 📁 Estructura Final del Proyecto

```
proyectos/thdora-bot/
├── src/
│   ├── thdora_data.py          # Diccionario base
│   └── thdora_functions.py     # agregar_cita() + ver_citas()
│
├── ejercicios-practica/
│   ├── ejercicio-01.py         # Diccionario
│   ├── ejercicio-02.py         # agregar_cita()
│   └── ejercicio-03.py         # ver_citas()
│
└── docs/
    ├── ejercicios/
    │   ├── 01-diccionario-base.md
    │   ├── 02-agregar-cita.md
    │   └── 03-ver-citas.md
    └── sesiones/
        └── 2026-02-06-sesion6-thdora.md  # Este archivo
```

---

## 📊 Progreso THDORA

### Funciones Completadas (3/5)

✅ **agregar_cita()** - Añadir nuevas citas  
✅ **ver_citas()** - Listar todas las citas  
⏳ **buscar_cita()** - Buscar cita por ID  
⏳ **eliminar_cita()** - Eliminar cita por ID  
⏳ **main()** - Menú interactivo  

**Porcentaje:** 40% completado

---

## 🔧 Código Destacado

### thdora_functions.py (versión final)

```python
from thdora_data import thdora_data

def agregar_cita(nombre, fecha, hora_inicio, hora_fin):
    """Añade una nueva cita al diccionario thdora_data"""
    nueva_cita = {
        'id': len(thdora_data['citas']) + 1,
        'nombre': nombre,
        'fecha': fecha,
        'hora_inicio': hora_inicio,
        'hora_fin': hora_fin,
    }
    thdora_data['citas'].append(nueva_cita)
    return nueva_cita

def ver_citas():
    """Muestra todas las citas guardadas"""
    if len(thdora_data['citas']) == 0:
        print("❌ No hay citas registradas.")
        return
    
    cantidad = len(thdora_data['citas'])
    print(f"\n📋 CITAS REGISTRADAS ({cantidad}):\n")
    
    for cita in thdora_data['citas']:
        print(f"[{cita['id']}] {cita['nombre']}")
        print(f"    📅 {cita['fecha']}")
        print(f"    ⏰ {cita['hora_inicio']} - {cita['hora_fin']}")
        print()
```

---

## 💡 Reflexiones

### Lo que Funcionó Bien
- **Ejercicios incrementales**: Cada ejercicio construye sobre el anterior
- **Testing exhaustivo**: Probar con 0 citas, 1 cita, múltiples citas
- **Documentación clara**: Instrucciones paso a paso en markdown

### Dificultades Encontradas
- **Conceptos nuevos**: Imports, estructura de proyecto, testing
- **Cambio de mentalidad**: De ejercicios simples a proyecto estructurado
- **Repetición aparente**: No entender por qué practicar y luego consolidar

### Aprendizajes Clave
1. **La práctica personal es fundamental**: No basta con copiar, hay que escribir
2. **Los errores enseñan**: ImportError, rutas incorrectas, etc.
3. **La estructura importa**: Separar datos, lógica y práctica tiene sentido

---

## 🚀 Próximos Pasos

### Inmediatos (Mañana)
1. **Prioridad 1:** Escuela Musk - Reforzar fundamentos
   - Bucles for
   - Condicionales if/else
   - Funciones básicas

2. **Prioridad 2:** THDORA Ejercicio 4 (cuando fundamentos sólidos)
   - Implementar `buscar_cita(id)`
   - Testing con IDs válidos e inválidos

### Mediano Plazo
1. Ejercicio 5: `eliminar_cita()`
2. Menú interactivo completo
3. Versión CLI funcional de THDORA

---

## 📝 Commits de Hoy

```bash
# Ejercicio 1
git commit -m "✅ Ejercicio 1: Diccionario base thdora_data"

# Ejercicio 2
git commit -m "✅ Ejercicio 2: agregar_cita() completado"

# Sesión 6 (partes 1-2)
git commit -m "✅ Sesión 6: Ejercicios 1-2 THDORA completados (agregar_cita)"

# Ejercicio 3 (parte 3)
git commit -m "✅ Ejercicio 3: ver_citas() completado"
git commit -m "✅ Añadida función ver_citas() a thdora_functions.py"
git commit -m "📝 Documentación Sesión 6: Ejercicios THDORA 1-3 completados"
```

---

## ⏱️ Tiempo Invertido

| Actividad | Tiempo |
|-----------|--------|
| Ejercicio 1: Diccionario base | 30 min |
| Ejercicio 2: agregar_cita() | 45 min |
| Ejercicio 3: ver_citas() | 40 min |
| Debugging imports | 20 min |
| Documentación | 25 min |
| **TOTAL** | **2h 40min** |

---

## 🎓 Evaluación
### Conceptos Dominados
✅ Diccionarios en Python  
✅ Listas y método append()  
✅ Funciones con parámetros y return  
✅ Bucle for sobre listas  
✅ Condicionales básicos  

### Conceptos en Proceso
🟡 Imports entre archivos  
🟡 Estructura de proyectos Python  
🟡 Testing con `if __name__ == "__main__"`  

### Conceptos Pendientes
🔴 Manejo de excepciones (try/except)  
🔴 Validación de datos de entrada  
🔴 Menús interactivos con input()  

---

**Última actualización:** 06/02/2026 21:07 CET  
**Próxima sesión:** 07/02/2026 (enfoque Escuela Musk)  
