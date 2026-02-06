# THDORA Bot - Estructura de Datos

## 📁 Organización de archivos

```
datos/
├── usuario.json          ← Perfil del usuario
├── categorias.json       ← Categorías predefinidas
└── 2026/                 ← Citas por año
    ├── enero.json
    ├── febrero.json
    ├── marzo.json
    └── ...
```

---

## 👤 Estructura: `usuario.json`

**Propósito:** Almacenar datos del perfil del usuario

```json
{
  "nombre": "Álvaro",
  "zona_horaria": "Europe/Madrid",
  "creado_el": "2026-02-04",
  "preferencias": {
    "formato_hora": "24h",
    "idioma": "es"
  },
  "estadisticas": {
    "total_citas": 0,
    "categoria_favorita": ""
  }
}
```

### Campos:

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `nombre` | string | Nombre del usuario |
| `zona_horaria` | string | Zona horaria (formato IANA) |
| `creado_el` | string | Fecha de creación del perfil (YYYY-MM-DD) |
| `preferencias.formato_hora` | string | Formato de hora: "24h" o "12h" |
| `preferencias.idioma` | string | Código de idioma (es, en, etc.) |
| `estadisticas.total_citas` | number | Total de citas creadas |
| `estadisticas.categoria_favorita` | string | Categoría más usada |

---

**Versión:** 1.0  
**Última actualización:** 2026-02-04