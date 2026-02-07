# CONTEXT PERPLEXITY - Escuela Musk

## 📚 Repositorio: escuelamusk

**URL:** https://github.com/alvarofernandezmota-tech/escuelamusk  
**Propósito:** Curso Python "Escuela Musk" + Proyectos educativos  
**Tipo:** Público  

---

## 🗂️ ESTRUCTURA

```
escuelamusk/
├── CONTEXT-PERPLEXITY.md       # Este archivo
├── README.md
├── PROGRESO.md                 # Tracking progreso curso
├── HOJA-DE-RUTA.md            # Plan aprendizaje
├── modulo-1-introduccion/
├── modulo-2-fundamentos/
├── modulo-4-avanzado/
├── proyectos/
│   └── thdora-bot/             # Proyecto activo
│       ├── src/                # Código funcional
│       │   ├── thdora_data.py
│       │   └── thdora_functions.py
│       ├── ejercicios-practica/    # Práctica personal
│       │   ├── ejercicio-01.py
│       │   ├── ejercicio-02.py
│       │   └── ejercicio-03.py
│       └── docs/
│           ├── ejercicios/     # Guías ejercicios
│           └── sesiones/       # Docs sesiones
├── diary/                      # Diario sesiones estudio
│   ├── enero/
│   └── febrero/
│       ├── dia1sesion1.md
│       ├── dia2sesion1.md
│       └── ...
├── apuntes/
└── recursos/
```

---

## 🎯 WORKFLOW ESCUELA MUSK

### Curso Python (80% tiempo - PRIORIDAD)

**Objetivo:** Fundamentos sólidos antes de proyectos complejos

**Actividades:**
1. Seguir temario paso a paso
2. Hacer ejercicios guiados del curso
3. Tomar apuntes en `apuntes/`
4. Documentar sesión en `diary/febrero/diaXsesionX.md`
5. Actualizar `PROGRESO.md` tras completar módulos

**Documentación sesión:**
- Crear archivo `diary/febrero/diaXsesionY.md`
- Registrar: tema, ejercicios, tiempo, aprendizajes
- Commit descriptivo

---

### Proyecto THDORA (20% tiempo - APLICACIÓN)

**Objetivo:** Aplicar conceptos aprendidos en proyecto real

**Workflow ejercicios:**
1. **Leo documentación:** `docs/ejercicios/XX-nombre-ejercicio.md`
2. **Practico:** Escribo código en `ejercicios-practica/ejercicio-XX.py`
3. **Testing:** Pruebo hasta que funciona correctamente
4. **Entiendo:** No avanzo si solo copié, debo entender
5. **Integro:** Si funciona Y entiendo → copio función a `src/`
6. **Documento:** Actualizo `docs/sesiones/` con lo aprendido

**Archivos clave THDORA:**
- `src/thdora_data.py` - Diccionario base de datos
- `src/thdora_functions.py` - Funciones consolidadas
- `ejercicios-practica/` - Práctica personal (puede tener errores)
- `docs/ejercicios/` - Guías paso a paso
- `docs/sesiones/` - Documentación de cada sesión

**Regla importante:** `ejercicios-practica/` es para practicar libremente. `src/` solo tiene código limpio y funcional.

---

## 🔧 GIT WORKFLOW

### Ubicación local:
```bash
# Repo principal
cd C:\Users\alvar\Documents\escuelamusk

# Proyecto THDORA
cd C:\Users\alvar\Documents\escuelamusk\proyectos\thdora-bot
```

### Comandos habituales:
```bash
git status                    # Ver estado
git add .                     # Añadir cambios
git commit -m "mensaje"       # Commit con mensaje descriptivo
git push                      # Subir a GitHub
git pull                      # Bajar cambios
```

### Ejecutar Python:
```bash
# Desde raíz proyecto THDORA
python src/thdora_functions.py
python ejercicios-practica/ejercicio-03.py

# Ver ayuda imports
python -c "import sys; print(sys.path)"
```

**Importante:** Ejecutar siempre desde la carpeta raíz del proyecto para que los imports funcionen.

---

## 🎓 NIVEL ACTUAL (Febrero 2026)

### ✅ Conceptos Completados:
- Variables y tipos de datos (int, str, bool, float)
- Listas y método `.append()`
- Diccionarios básicos (creación, acceso)
- Funciones simples (definición, parámetros, return)
- Bucles `for` básicos sobre listas
- Condicionales `if/else` simples
- F-strings para formateo

### 🔄 Conceptos en Proceso:
- Funciones con múltiples parámetros (4+)
- Bucles `for` sobre diccionarios dentro de listas
- Imports entre archivos del proyecto
- Estructura de proyectos Python
- Testing con `if __name__ == "__main__"`

### ⏳ Conceptos Pendientes:
- Bucles `while`
- Comprensión de listas
- Funciones lambda
- Manejo de excepciones (try/except)
- Clases y POO
- Manejo de archivos
- Módulos externos y pip
- APIs y requests

---

## 📊 PROYECTO THDORA - Estado Actual

### Objetivo General:
Bot de gestión de citas personales (agenda/calendario)

### Progreso Ejercicios Base (3/5 completados):
- ✅ **Ejercicio 1:** Diccionario base `thdora_data`
- ✅ **Ejercicio 2:** Función `agregar_cita(nombre, fecha, hora_inicio, hora_fin)`
- ✅ **Ejercicio 3:** Función `ver_citas()` - Mostrar todas las citas
- ⏳ **Ejercicio 4:** Función `buscar_cita(id)` - Buscar cita específica
- ⏳ **Ejercicio 5:** Función `eliminar_cita(id)` - Eliminar cita

### Funciones Implementadas:
```python
# src/thdora_functions.py

def agregar_cita(nombre, fecha, hora_inicio, hora_fin):
    """Añade nueva cita al diccionario thdora_data"""
    # Auto-genera ID
    # Retorna cita creada

def ver_citas():
    """Muestra todas las citas guardadas"""
    # Maneja lista vacía
    # Formato visual con emojis
```

### Próximos Pasos THDORA:
1. Completar ejercicio 4: `buscar_cita()`
2. Completar ejercicio 5: `eliminar_cita()`
3. Menú interactivo con `input()`
4. Persistencia de datos (guardar en archivo)

---

## 💬 CÓMO TRABAJAMOS JUNTOS

### Cuando pido ayuda con código:
1. **Explicas el concepto primero** (sin código todavía)
2. **Ejemplo simple** (caso mínimo para entender)
3. **Aplicación a mi caso** (ahora sí, mi código)
4. **Validación de comprensión** (me preguntas para asegurar que entiendo)

**NO:** Dar solución completa directamente  
**SÍ:** Guiar para que yo llegue a la solución

---

### Cuando hacemos ejercicios:
1. **Leo documentación primero** (en `docs/ejercicios/`)
2. **Intento yo primero** (escribo código en `ejercicios-practica/`)
3. **Si me atasco:** Pido ayuda específica (qué parte no entiendo)
4. **Corriges sin dar solución completa** (pistas, no respuestas)
5. **Yo termino el ejercicio** (escribo el código final)

**Objetivo:** Que yo aprenda, no solo que funcione.

---

### Cuando actualizas repositorios:
1. **Confirmas qué repo y archivo** modificar
2. **Muestras cambios** antes de aplicar (diff o resumen)
3. **Explicas el commit** que harás
4. **Esperas mi aprobación** antes de hacer push
5. **Verificas que se subió correctamente**

**Nunca:** Modificar archivos sin confirmar primero.

---

### Cuando documentamos sesiones:
1. **Resumen de lo hecho** (ejercicios, tiempo, logros)
2. **Conceptos aprendidos** (qué entendí hoy)
3. **Dificultades encontradas** (qué costó, cómo se resolvió)
4. **Próximos pasos** (qué sigue)

**Formato:** Markdown claro, estructurado, con emojis para visual.

---

## 🚀 PRIORIDADES Y PRINCIPIOS

### Orden de Prioridad:
1. **Escuela Musk (80%):** Fundamentos sólidos primero
2. **THDORA (20%):** Aplicación práctica cuando fundamentos OK
3. **Balance:** No avanzar en THDORA si fundamentos flojos

### Principios de Aprendizaje:
- ✅ **Aprendizaje > Velocidad** (mejor lento pero entendido)
- ✅ **Entendimiento > Copiar** (no avanzar sin entender)
- ✅ **Práctica personal > Código perfecto** (ejercicios-practica/ es para practicar)
- ✅ **Documentación > Memoria** (todo documentado en repos)

### Cuándo hacer THDORA:
- ✅ Fundamentos del tema sólidos (ej: funciones básicas OK)
- ✅ Energía mental suficiente (no al final del día cansado)
- ✅ Tiempo adecuado (mínimo 1-2h seguidas)
- ❌ NO cuando: fundamentos flojos, cansado, poco tiempo

---

## 🔗 OTROS REPOSITORIOS

### personal (Privado)
- **URL:** https://github.com/alvarofernandezmota-tech/personal
- **Contexto:** Ver `personal/CONTEXT-PERPLEXITY.md`
- **Propósito:** Tracking vida personal, diario, métricas bienestar
- **Uso:** Actualización tracking diario, reflexiones, modo Titán

### thea-ia (Público - No activo)
- **URL:** https://github.com/alvarofernandezmota-tech/thea-ia
- **Estado:** Proyecto futuro, actualmente en pausa
- **Relación con THDORA:** Es la referencia/inspiración para THDORA
- **Uso actual:** Solo consulta de referencia, no desarrollo activo

---

## 📝 FORMATO RESPUESTAS

### Usa siempre:
- ✅ **Markdown estructurado** (headers, listas, code blocks)
- ✅ **Emojis para claridad visual** (pero sin abusar)
- ✅ **Ejemplos concretos** (no solo teoría abstracta)
- ✅ **Analogías cuando sea necesario** (para conceptos complejos)
- ✅ **Código con comentarios** (explicar qué hace cada parte)

### Evita:
- ❌ Bloques de texto largos sin estructura
- ❌ Jerga técnica sin explicar primero
- ❌ Código sin explicación
- ❌ Dar solución completa sin guiar

---

## ✅ CONFIRMACIÓN INICIAL

Cuando recibas este contexto en un nuevo chat, confirma:

1. ✅ Acceso a repo `escuelamusk` verificado
2. ✅ Estructura del proyecto entendida
3. ✅ Workflow Musk (80%) + THDORA (20%) claro
4. ✅ Nivel actual Python identificado
5. ✅ Prioridades y principios comprendidos

**Luego pregúntame:**

> "¿En qué trabajamos hoy: Escuela Musk o THDORA?"

---

## 🎯 COMANDOS RÁPIDOS PARA MÍ

### Cargar contexto en nuevo chat:
```
Lee el contexto en:
https://github.com/alvarofernandezmota-tech/escuelamusk/blob/main/CONTEXT-PERPLEXITY.md
```

### Ver estructura proyecto:
```
Muéstrame estructura de proyectos/thdora-bot/
```

### Revisar progreso THDORA:
```
¿Qué ejercicios THDORA tengo completados?
```

### Actualizar documentación sesión:
```
Documenta sesión de hoy en diary/febrero/
- Tema: [tema]
- Tiempo: [tiempo]
- Logros: [logros]
```

---

**Sistema establecido:** Febrero 2026  
**Última actualización:** 07 febrero 2026  
**Versión:** 1.0  
