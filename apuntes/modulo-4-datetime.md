# Módulo 4 - Librería datetime
**Escuela Musk - Python**  
**Clase en vivo:** Jueves 5 Febrero 2026, 19:30  
**Autor:** Álvaro Fernández Mota

---

## 📅 1. OBJETO DATE - Fechas

### Crear fechas
```python
from datetime import date

# Fecha específica
fecha = date(2026, 2, 5)  # año, mes, día
print(fecha)  # 2026-02-05

# Fecha de HOY
hoy = date.today()
print(hoy)
```

### Acceder a componentes
```python
fecha = date(2026, 2, 5)

print(fecha.year)   # 2026
print(fecha.month)  # 2
print(fecha.day)    # 5

# Día de la semana (0=lunes, 6=domingo)
print(fecha.weekday())  # 3 (jueves)
```

### Comparar fechas
```python
fecha1 = date(2026, 2, 5)
fecha2 = date(2026, 2, 10)

if fecha1 < fecha2:
    print("fecha1 es anterior")  # ✅
```

---

## ⏰ 2. OBJETO TIME - Horas

### Crear horas
```python
from datetime import time

# Hora específica
hora = time(15, 30, 0)  # hora, minuto, segundo
print(hora)  # 15:30:00

# Con microsegundos
hora2 = time(15, 30, 45, 123456)
print(hora2)  # 15:30:45.123456
```

### Acceder a componentes
```python
hora = time(15, 30, 45)

print(hora.hour)    # 15
print(hora.minute)  # 30
print(hora.second)  # 45
```

---

## 📅⏰ 3. OBJETO DATETIME - Fecha + Hora

### Crear datetime
```python
from datetime import datetime

# Fecha y hora específica
fecha_hora = datetime(2026, 2, 5, 15, 30, 0)
print(fecha_hora)  # 2026-02-05 15:30:00

# AHORA (fecha + hora actual)
ahora = datetime.now()
print(ahora)

# Solo fecha de hoy
hoy = datetime.today()
print(hoy)
```

### Acceder a componentes
```python
ahora = datetime.now()

print(ahora.year)    # 2026
print(ahora.month)   # 2
print(ahora.day)     # 5
print(ahora.hour)    # 19
print(ahora.minute)  # 30
print(ahora.second)  # 15
```

### Extraer fecha o hora
```python
ahora = datetime.now()

solo_fecha = ahora.date()  # objeto date
solo_hora = ahora.time()   # objeto time

print(solo_fecha)  # 2026-02-05
print(solo_hora)   # 19:30:15
```

---

## ⏱️ 4. TIMEDELTA - Duraciones

### Crear duraciones
```python
from datetime import timedelta

una_semana = timedelta(weeks=1)
cinco_dias = timedelta(days=5)
tres_horas = timedelta(hours=3)
treinta_min = timedelta(minutes=30)

# Combinadas
duracion = timedelta(days=5, hours=3, minutes=30)
```

### Sumar/restar tiempo a fechas
```python
from datetime import date, timedelta

hoy = date.today()
manana = hoy + timedelta(days=1)
ayer = hoy - timedelta(days=1)
en_semana = hoy + timedelta(weeks=1)

print(f"Hoy: {hoy}")
print(f"Mañana: {manana}")
print(f"Ayer: {ayer}")
print(f"En 1 semana: {en_semana}")
```

### Diferencia entre fechas
```python
fecha1 = date(2026, 2, 5)
fecha2 = date(2026, 2, 10)

diferencia = fecha2 - fecha1  # timedelta
print(diferencia)       # 5 days, 0:00:00
print(diferencia.days)  # 5
```

### Propiedades timedelta
```python
duracion = timedelta(days=5, hours=3, minutes=30)

print(duracion.days)              # 5
print(duracion.seconds)           # 12600 (3h30m en segundos)
print(duracion.total_seconds())   # 444600 (todo en segundos)
```

---

## 🔄 5. CONVERTIR FECHA A STRING - strftime()

**strftime = String FROM Time**

### De fecha/datetime a string personalizado
```python
from datetime import date, datetime

hoy = date.today()  # 2026-02-05

# Diferentes formatos
formato1 = hoy.strftime("%Y-%m-%d")        # 2026-02-05
formato2 = hoy.strftime("%d/%m/%Y")        # 05/02/2026
formato3 = hoy.strftime("%d-%m-%Y")        # 05-02-2026
formato4 = hoy.strftime("%d de %B de %Y")  # 05 de February de 2026
formato5 = hoy.strftime("%A, %d %b %Y")    # Thursday, 05 Feb 2026

print(formato1)  # 2026-02-05
print(formato2)  # 05/02/2026
print(formato3)  # 05-02-2026
print(formato4)  # 05 de February de 2026
print(formato5)  # Thursday, 05 Feb 2026
```

### Con hora incluida
```python
ahora = datetime.now()  # 2026-02-05 19:30:15

formato1 = ahora.strftime("%d/%m/%Y %H:%M:%S")     # 05/02/2026 19:30:15
formato2 = ahora.strftime("%Y-%m-%d %H:%M")        # 2026-02-05 19:30
formato3 = ahora.strftime("%d/%m/%Y a las %H:%M")  # 05/02/2026 a las 19:30
formato4 = ahora.strftime("%I:%M %p")              # 07:30 PM

print(formato1)  # 05/02/2026 19:30:15
print(formato2)  # 2026-02-05 19:30
print(formato3)  # 05/02/2026 a las 19:30
print(formato4)  # 07:30 PM
```

### Códigos de formato más usados

| Código | Significado | Ejemplo |
|--------|-------------|----------|
| `%Y` | Año con siglo | 2026 |
| `%y` | Año sin siglo | 26 |
| `%m` | Mes como número (01-12) | 02 |
| `%B` | Mes nombre completo | February |
| `%b` | Mes nombre corto | Feb |
| `%d` | Día del mes (01-31) | 05 |
| `%A` | Día semana completo | Thursday |
| `%a` | Día semana corto | Thu |
| `%H` | Hora 24h (00-23) | 19 |
| `%I` | Hora 12h (01-12) | 07 |
| `%M` | Minuto (00-59) | 30 |
| `%S` | Segundo (00-59) | 45 |
| `%p` | AM/PM | PM |
| `%w` | Día semana número (0=domingo) | 4 |

### Ejemplos prácticos formatos personalizados

```python
fecha = datetime(2026, 2, 5, 19, 30, 45)

# Formato español largo
print(fecha.strftime("%A, %d de %B de %Y"))  
# Thursday, 05 de February de 2026

# Formato corto
print(fecha.strftime("%d/%m/%y"))  
# 05/02/26

# Con hora legible
print(fecha.strftime("%d/%m/%Y a las %H:%M horas"))  
# 05/02/2026 a las 19:30 horas

# Formato base de datos
print(fecha.strftime("%Y-%m-%d %H:%M:%S"))  
# 2026-02-05 19:30:45

# Solo hora
print(fecha.strftime("%H:%M"))  
# 19:30
```

---

## 🔄 6. CONVERTIR STRING A FECHA - strptime()

**strptime = String PARSE Time**

### De string a datetime
```python
from datetime import datetime

# String en formato ISO
fecha_str = "2026-02-05"
fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d")
print(fecha_obj)  # 2026-02-05 00:00:00
print(type(fecha_obj))  # <class 'datetime.datetime'>

# Convertir a solo date (sin hora)
fecha_solo = fecha_obj.date()
print(fecha_solo)  # 2026-02-05
print(type(fecha_solo))  # <class 'datetime.date'>
```

### Diferentes formatos de entrada
```python
# Formato español
fecha_str = "05/02/2026"
fecha_obj = datetime.strptime(fecha_str, "%d/%m/%Y")
print(fecha_obj)  # 2026-02-05 00:00:00

# Con hora
fecha_str = "05/02/2026 19:30"
fecha_obj = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
print(fecha_obj)  # 2026-02-05 19:30:00

# Formato texto
fecha_str = "05 Feb 2026"
fecha_obj = datetime.strptime(fecha_str, "%d %b %Y")
print(fecha_obj)  # 2026-02-05 00:00:00
```

---

## ✅ 7. VALIDAR FECHAS

```python
def validar_fecha(fecha_str):
    """
    Valida si un string es una fecha válida en formato YYYY-MM-DD
    """
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

print(validar_fecha("2026-02-05"))  # True
print(validar_fecha("2026-13-40"))  # False (mes 13 no existe)
print(validar_fecha("no es fecha"))  # False
```

---

## 🛠️ 8. CASOS DE USO PARA THDORA

### Caso 1: Filtrar citas de hoy
```python
def citas_de_hoy(lista_citas):
    hoy = date.today()
    return [c for c in lista_citas if c["fecha"] == str(hoy)]
```

### Caso 2: Citas del mes actual
```python
def citas_del_mes(lista_citas):
    hoy = date.today()
    citas_mes = []
    for cita in lista_citas:
        fecha_cita = datetime.strptime(cita["fecha"], "%Y-%m-%d").date()
        if fecha_cita.month == hoy.month and fecha_cita.year == hoy.year:
            citas_mes.append(cita)
    return citas_mes
```

### Caso 3: Próximas citas (7 días)
```python
def proximas_citas(lista_citas, dias=7):
    hoy = date.today()
    limite = hoy + timedelta(days=dias)
    
    proximas = []
    for cita in lista_citas:
        fecha_cita = datetime.strptime(cita["fecha"], "%Y-%m-%d").date()
        if hoy <= fecha_cita <= limite:
            proximas.append(cita)
    return proximas
```

### Caso 4: Ordenar citas por fecha
```python
def ordenar_citas(lista_citas):
    return sorted(lista_citas, key=lambda c: c["fecha"])
```

### Caso 5: Días que faltan para cita
```python
def dias_restantes(fecha_cita_str):
    hoy = date.today()
    fecha_cita = datetime.strptime(fecha_cita_str, "%Y-%m-%d").date()
    return (fecha_cita - hoy).days
```

---

## 📝 NOTAS ADICIONALES DE LA CLASE

### Conceptos explicados:



### Ejemplos adicionales:



### Dudas resueltas:



---

## 🎯 EJERCICIOS PROPUESTOS

### Ejercicio 1: Edad y próximo cumpleaños
Crea una función que reciba fecha de nacimiento y devuelva:
- Edad en años
- Días hasta el próximo cumpleaños

### Ejercicio 2: Diferencia entre fechas
Crea función que reciba dos fechas y devuelva:
- Diferencia en días
- Diferencia en semanas
- Diferencia en meses (aproximado)

### Ejercicio 3: Validar hora
Crea función que valide si un string es hora válida en formato HH:MM

### Ejercicio 4: Día de la semana en español
Crea función que devuelva nombre del día en español ("Lunes", "Martes", etc.)

### Ejercicio 5: Mensaje para THDORA
Función que muestre mensaje según cuánto falte para cita:
- "¡HOY!" si es hoy
- "Mañana" si es mañana
- "En X días" si es futuro
- "Hace X días" si es pasado

---

**Última actualización:** 5 febrero 2026, 19:30  
**Estado:** Clase en vivo en curso  
**Próximo tema:** Machine Learning
