# THDORA Bot - Roadmap de Desarrollo

## Fases de Desarrollo

### 🟢 Fase 0: Estructura inicial (COMPLETADO - 2026-02-04)

- [x] Crear estructura de carpetas
- [x] README.md del proyecto
- [x] main.py con menú básico
- [x] Carpeta funciones/ con __init__.py
- [x] Carpeta datos/2026/ con ejemplo febrero.json
- [x] ROADMAP.md

---

### 🟡 Fase 1: Funciones básicas de manejo de datos

**Objetivo:** Aprender funciones mientras construimos las bases del bot

#### 1.1 - Función cargar_datos()
- [ ] Crear `funciones/guardar_datos.py`
- [ ] Implementar `cargar_datos(mes, año)` que:
  - Lee el archivo JSON correspondiente
  - Devuelve un diccionario con las citas
  - Maneja el caso de que el archivo no exista
- [ ] Documentar con docstring
- [ ] Probar manualmente

#### 1.2 - Función guardar_datos()
- [ ] Implementar `guardar_datos(agenda, mes, año)` que:
  - Guarda el diccionario en JSON
  - Crea la carpeta si no existe
  - Sobrescribe el archivo existente
- [ ] Documentar con docstring
- [ ] Probar guardando y cargando datos

---

### 🟡 Fase 2: Agregar citas

**Objetivo:** Practicar funciones con parámetros y validación de datos

#### 2.1 - Función agregar_cita()
- [ ] Crear `funciones/agregar_cita.py`
- [ ] Implementar `agregar_cita(agenda, dia, hora, descripcion)` que:
  - Añade una cita al diccionario
  - Valida que hora tenga formato correcto (HH:MM)
  - Valida que día sea válido (01-31)
  - Crea la lista del día si no existe
- [ ] Integrar en main.py (opción 1)
- [ ] Probar agregando varias citas

---

### 🟡 Fase 3: Mostrar citas

**Objetivo:** Practicar bucles y formateo de salida

#### 3.1 - Función mostrar_citas_dia()
- [ ] Crear `funciones/mostrar_citas.py`
- [ ] Implementar `mostrar_citas_dia(agenda, dia)` que:
  - Muestra todas las citas de un día
  - Ordena por hora
  - Formato bonito con emojis
- [ ] Integrar en main.py (opción 2)

#### 3.2 - Función mostrar_citas_mes()
- [ ] Implementar `mostrar_citas_mes(agenda)` que:
  - Muestra todas las citas del mes
  - Agrupa por día
  - Cuenta total de citas
- [ ] Integrar en main.py (opción 3)

---

### 🟡 Fase 4: Eliminar y buscar citas

**Objetivo:** Practicar manipulación de estructuras de datos

#### 4.1 - Función eliminar_cita()
- [ ] Crear `funciones/eliminar_cita.py`
- [ ] Implementar `eliminar_cita(agenda, dia, hora)` que:
  - Elimina una cita específica
  - Maneja el caso de que no exista
  - Confirma antes de eliminar
- [ ] Integrar en main.py (opción 4)

#### 4.2 - Función buscar_cita()
- [ ] Crear `funciones/buscar_cita.py`
- [ ] Implementar `buscar_cita(agenda, palabra_clave)` que:
  - Busca en todas las descripciones
  - Devuelve lista de resultados con día y hora
  - Búsqueda case-insensitive
- [ ] Integrar en main.py (opción 5)

---

### 🟡 Fase 5: Integración y persistencia

**Objetivo:** Unir todas las funciones y que persistan los datos

- [ ] Modificar main.py para cargar datos al inicio
- [ ] Guardar automáticamente después de cada operación
- [ ] Crear función de utilidad para obtener fecha actual
- [ ] Mejorar manejo de errores
- [ ] Probar flujo completo: agregar → ver → buscar → eliminar

---

### 🔵 Fase 6: Mejoras y optimizaciones

**Objetivo:** Refinar el código y añadir extras

- [ ] Validación avanzada de fechas (días inválidos según mes)
- [ ] Exportar citas a TXT
- [ ] Estadísticas (día con más citas, etc.)
- [ ] Menú de configuración
- [ ] Tests unitarios básicos

---

### 🔵 Fase 7: Integración con THEA IA (Futuro)

**Objetivo:** Migrar funcionalidades a THEA IA

- [ ] Analizar código de THEA IA (AgendaAgent)
- [ ] Adaptar funciones de THDORA a la arquitectura de THEA
- [ ] Integrar con base de datos PostgreSQL
- [ ] Añadir persistencia multi-usuario

---

## Convenciones de commits

- `feat:` Nueva funcionalidad
- `fix:` Corrección de bug
- `docs:` Cambios en documentación
- `refactor:` Mejora de código sin cambiar funcionalidad
- `test:` Añadir o modificar tests

## Notas

- Cada fase se completa **antes** de pasar a la siguiente
- Cada función se prueba **manualmente** antes de integrarla
- Se documenta en `diary/` el progreso de cada sesión
- Commits frecuentes y descriptivos
