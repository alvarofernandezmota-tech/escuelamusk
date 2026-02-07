# THDORA Bot 📅

**Gestor de citas y productividad personal**

## 🎯 Descripción

THDORA es un proyecto profesional de aprendizaje Python, construyendo un gestor completo de tiempo y productividad.

**Características actuales:**
- 📅 Agregar citas con fecha y hora
- 📊 Ver todas las citas registradas
- 🔍 Buscar citas por ID
- 🗑️ Eliminar citas (próximamente)

**Características futuras:**
- 🤖 Bot de Telegram
- 💾 Persistencia en JSON
- 🗓️ Búsquedas avanzadas
- 📊 Análisis y estadísticas

---

## 📊 Progreso Actual

**Versión:** v0.3  
**Estado:** En desarrollo activo  
**Última actualización:** 7 febrero 2026  
**Progreso:** 75% Fase 1 completada  

```
[████████████████████░░░░] 75%
```

### Completado ✅
- [x] Estructura profesional del proyecto
- [x] Diccionario base de datos
- [x] `agregar_cita()` - Añadir nuevas citas
- [x] `ver_citas()` - Mostrar todas las citas
- [x] `buscar_cita()` - Buscar por ID
- [x] Testing completo en `__main__`
- [x] Documentación de progreso

### En progreso ⏳
- [ ] `eliminar_cita()` - Eliminar citas (Ejercicio 5)

**Ver progreso detallado:** [docs/PROGRESO.md](./docs/PROGRESO.md)

---

## 📚 Estructura Profesional del Proyecto

```
thdora-bot/
├── README.md                  ← Este archivo
├── ROADMAP.md                 ← Plan de desarrollo
│
├── src/                       ← Código fuente
│   ├── thdora_data.py         ← Estructura de datos
│   └── thdora_functions.py    ← ⭐ ARCHIVO PRINCIPAL (todo el desarrollo)
│
├── docs/                      ← Documentación
│   ├── PROGRESO.md            ← 📊 Tracking detallado ejercicios
│   ├── ejercicios/            ← Guías teóricas (referencia)
│   ├── conceptos/             ← Teoría Python
│   └── arquitectura/          ← Diseño del sistema
│
└── thdora_bot.py              ← Menú CLI (futuro)
```

### ⭐ Archivo Principal: `src/thdora_functions.py`

**Todo el desarrollo se hace aquí:**
- ✅ Todas las funciones del proyecto
- ✅ Testing completo en `__main__`
- ✅ Ejecución directa para probar
- ✅ Sin redundancia de código

**Workflow profesional:**
1. Implementar funciones en `thdora_functions.py`
2. Testing inmediato en `__main__`
3. Documentar progreso en `docs/PROGRESO.md`
4. Commit cuando funciona

---

## 🚀 Inicio Rápido

### Clonar y probar

```bash
# Clonar repositorio
git clone https://github.com/alvarofernandezmota-tech/escuelamusk.git
cd escuelamusk/proyectos/thdora-bot

# Ejecutar proyecto actual
python src/thdora_functions.py
```

### Salida esperada

```
============================================================
🧪 TESTING THDORA FUNCTIONS v0.3
============================================================
Archivo: src/thdora_functions.py
Modo: Desarrollo con testing activo
============================================================

📍 TEST 1: ver_citas() - Lista vacía
...

📍 TEST 2: agregar_cita() - Añadir 4 citas
...

📊 RESUMEN FINAL
============================================================
Total citas en memoria: 4
Funciones implementadas: 3/4
  ✅ agregar_cita()
  ✅ ver_citas()
  ✅ buscar_cita()
  ⏳ eliminar_cita() - Pendiente ejercicio 5

✅ Todos los tests completados correctamente
============================================================
```

---

## 📚 Aprendizaje y Desarrollo

### Metodología

**Principios:**
1. ✅ Entendimiento > Velocidad
2. ✅ Práctica > Teoría
3. ✅ Testing activo constante
4. ✅ Documentación de aprendizajes
5. ✅ Desarrollo iterativo

### Recursos

- **Progreso detallado:** [docs/PROGRESO.md](./docs/PROGRESO.md)
- **Ejercicios teóricos:** [docs/ejercicios/](./docs/ejercicios/)
- **Conceptos Python:** [docs/conceptos/](./docs/conceptos/)
- **Roadmap:** [ROADMAP.md](./ROADMAP.md)

---

## 💻 Funciones Implementadas

### 1. `agregar_cita(nombre, fecha, hora_inicio, hora_fin)`

Añade una nueva cita al sistema.

```python
cita = agregar_cita("Dentista", "2026-02-10", "10:00", "11:00")
# Retorna: {'id': 1, 'nombre': 'Dentista', 'fecha': '2026-02-10', ...}
```

### 2. `ver_citas()`

Muestra todas las citas registradas.

```python
ver_citas()
# Imprime:
# 📋 CITAS REGISTRADAS (3):
# [1] Dentista
#     📅 2026-02-10
#     ⏰ 10:00 - 11:00
# ...
```

### 3. `buscar_cita(id)`

Busca y muestra una cita por su ID.

```python
cita = buscar_cita(1)
# Imprime cita encontrada o mensaje de error
# Retorna: dict o None
```

### 4. `eliminar_cita(id)` ⏳

En desarrollo (Ejercicio 5).

---

## 📅 Roadmap

### Fase 1: Funciones Base (75% ✅)
- [x] Diccionario base
- [x] agregar_cita()
- [x] ver_citas()
- [x] buscar_cita()
- [ ] eliminar_cita() ⏳

### Fase 2: Búsquedas Avanzadas
- [ ] buscar_por_nombre()
- [ ] buscar_por_fecha()
- [ ] buscar_por_rango_fechas()

### Fase 3: Persistencia
- [ ] Guardar en JSON
- [ ] Cargar desde JSON

### Fase 4: Interfaz Usuario
- [ ] Menú CLI interactivo
- [ ] Bot Telegram

**Ver plan completo:** [ROADMAP.md](./ROADMAP.md)

---

## 🔧 Tecnologías

- **Lenguaje:** Python 3.13
- **Estructura de datos:** Diccionarios y listas nativas
- **Testing:** Manual en `__main__` (futuro: pytest)
- **Persistencia:** JSON (próximamente)
- **Interfaz:** CLI / Telegram bot (futuro)

---

## 📈 Estadísticas

**Tiempo invertido:** ~3 horas  
**Líneas de código:** ~150  
**Funciones completadas:** 3/4  
**Tests escritos:** 6  
**Commits:** 15+  

---

## 👥 Contribuir

Proyecto educativo open-source.

**Ideas para contribuir:**
- Mejorar documentación
- Reportar bugs
- Sugerir mejoras
- Crear diagramas

---

## 📝 Licencia

MIT License - Proyecto educativo

---

## ✍️ Autor

**Álvaro Fernández Mota**  
Proyecto práctico de [EscuelaMusk](https://github.com/alvarofernandezmota-tech/escuelamusk)

---

🎯 **Aprende Python construyendo proyectos reales, paso a paso, de forma profesional.**
