# THDORA Bot 📅

**Bot de gestión de agenda personal**

## Descripción

THDORA es un bot de gestión de citas y horarios desarrollado como proyecto práctico del curso de Python. Integra todos los conceptos aprendidos: listas, diccionarios, bucles, funciones, manejo de archivos JSON y Git.

## Funcionalidades

### Versión 1.0 (En desarrollo)

- ✅ Agregar cita (fecha, hora, descripción)
- ✅ Ver citas del día
- ✅ Ver citas del mes
- ✅ Eliminar cita
- ✅ Buscar cita por palabra clave
- ✅ Guardar automáticamente en JSON

### Futuras versiones

- 🔲 Recordatorios automáticos
- 🔲 Categorías de citas
- 🔲 Exportar a calendario
- 🔲 Integración con THEA IA

## Estructura del proyecto

```
thdora-bot/
├── README.md              ← Este archivo
├── main.py                ← Punto de entrada (menú principal)
├── funciones/             ← Módulo de funciones
│   ├── __init__.py
│   ├── agregar_cita.py
│   ├── eliminar_cita.py
│   ├── mostrar_citas.py
│   ├── buscar_cita.py
│   └── guardar_datos.py
└── datos/                 ← Archivos JSON por mes
    └── 2026/
        ├── enero.json
        ├── febrero.json
        └── ...
```

## Estructura de datos

Las citas se guardan en formato JSON organizadas por mes:

```json
{
  "04": [
    {"hora": "15:30", "descripcion": "Estudiar Python funciones"},
    {"hora": "19:30", "descripcion": "Sesión 2 - planificar THDORA"}
  ],
  "05": [
    {"hora": "10:00", "descripcion": "Reunión proyecto"}
  ]
}
```

## Uso

```bash
python main.py
```

## Tecnologías

- Python 3.x
- JSON (persistencia de datos)
- Git (control de versiones)

## Autor

Álvaro Fernández Mota - Proyecto práctico de EscuelaMusk

## Versión

**v0.1.0** - Estructura inicial (2026-02-04)
