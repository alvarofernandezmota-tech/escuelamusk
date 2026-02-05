"""
MÓDULO 4 - LIBRERÍAS DE TIEMPO: datetime
Escuela Musk - Python
Clase en vivo: Jueves 5 Febrero 2026, 19:30
Autor: Álvaro Fernández Mota

APUNTES DE CLASE EN VIVO
"""

from datetime import date, time, datetime, timedelta
import time as time_module  # Para sleep, time(), etc.

# ==============================================================================
# 1. OBJETO DATE - Fechas (año, mes, día)
# ==============================================================================

# Crear fecha específica
fecha1 = date(2026, 2, 5)  # año, mes, día
print(f"Fecha específica: {fecha1}")  # 2026-02-05

# Fecha de HOY
hoy = date.today()
print(f"Hoy: {hoy}")

# Acceder a componentes de la fecha
print(f"Año: {hoy.year}")
print(f"Mes: {hoy.month}")
print(f"Día: {hoy.day}")

# Día de la semana (0=lunes, 6=domingo)
dia_semana = hoy.weekday()
print(f"Día de la semana (0-6): {dia_semana}")

# Comparar fechas
fecha2 = date(2026, 2, 10)
if fecha1 < fecha2:
    print("fecha1 es anterior a fecha2")


# ==============================================================================
# 2. OBJETO TIME - Horas (hora, minuto, segundo, microsegundo)
# ==============================================================================

# Crear hora específica
hora1 = time(15, 30, 0)  # hora, minuto, segundo
print(f"Hora: {hora1}")  # 15:30:00

# Con microsegundos
hora2 = time(15, 30, 45, 123456)  # h, m, s, microsegundos
print(f"Hora detallada: {hora2}")

# Acceder a componentes
print(f"Hora: {hora1.hour}")
print(f"Minuto: {hora1.minute}")
print(f"Segundo: {hora1.second}")


# ==============================================================================
# 3. OBJETO DATETIME - Fecha + Hora completa
# ==============================================================================

# Crear datetime específico
fecha_hora = datetime(2026, 2, 5, 15, 30, 0)  # año, mes, día, hora, min, seg
print(f"Datetime completo: {fecha_hora}")

# Datetime AHORA (fecha + hora actual)
ahora = datetime.now()
print(f"Ahora: {ahora}")

# Solo fecha de hoy (sin hora)
hoy_fecha = datetime.today()
print(f"Hoy (today): {hoy_fecha}")

# Acceder a componentes
print(f"Año: {ahora.year}")
print(f"Mes: {ahora.month}")
print(f"Día: {ahora.day}")
print(f"Hora: {ahora.hour}")
print(f"Minuto: {ahora.minute}")
print(f"Segundo: {ahora.second}")

# Extraer solo fecha o solo hora
solo_fecha = ahora.date()  # Objeto date
solo_hora = ahora.time()   # Objeto time
print(f"Solo fecha: {solo_fecha}")
print(f"Solo hora: {solo_hora}")


# ==============================================================================
# 4. TIMEDELTA - Diferencias/Duraciones de tiempo
# ==============================================================================

# Crear duraciones
una_semana = timedelta(weeks=1)
cinco_dias = timedelta(days=5)
tres_horas = timedelta(hours=3)
treinta_minutos = timedelta(minutes=30)

# Combinadas
duracion = timedelta(days=5, hours=3, minutes=30)
print(f"Duración: {duracion}")

# SUMAR tiempo a fechas
hoy = date.today()
manana = hoy + timedelta(days=1)
ayer = hoy - timedelta(days=1)
en_una_semana = hoy + timedelta(weeks=1)

print(f"Hoy: {hoy}")
print(f"Mañana: {manana}")
print(f"Ayer: {ayer}")
print(f"En 1 semana: {en_una_semana}")

# RESTAR fechas (resultado es timedelta)
fecha_futura = date(2026, 2, 10)
fecha_actual = date(2026, 2, 5)

diferencia = fecha_futura - fecha_actual
print(f"Diferencia: {diferencia}")  # 5 days, 0:00:00
print(f"Días de diferencia: {diferencia.days}")  # 5

# Propiedades de timedelta
print(f"Días: {duracion.days}")
print(f"Segundos: {duracion.seconds}")
print(f"Total segundos: {duracion.total_seconds()}")


# ==============================================================================
# 5. FORMATEAR FECHAS - strftime() [String FROM Time]
# ==============================================================================

# De objeto date/datetime a string personalizado
hoy = date.today()

# Formatos comunes
formato1 = hoy.strftime("%Y-%m-%d")        # 2026-02-05
formato2 = hoy.strftime("%d/%m/%Y")        # 05/02/2026
formato3 = hoy.strftime("%d de %B de %Y")  # 05 de February de 2026
formato4 = hoy.strftime("%A, %d %b %Y")    # Thursday, 05 Feb 2026

print(f"Formato ISO: {formato1}")
print(f"Formato ES: {formato2}")
print(f"Formato texto: {formato3}")
print(f"Formato completo: {formato4}")

# Con datetime (incluye hora)
ahora = datetime.now()
formato_completo = ahora.strftime("%d/%m/%Y %H:%M:%S")
print(f"Fecha y hora: {formato_completo}")

# Códigos de formato más usados:
# %Y - Año con siglo (2026)
# %y - Año sin siglo (26)
# %m - Mes como número (02)
# %B - Mes nombre completo (February)
# %b - Mes nombre corto (Feb)
# %d - Día del mes (05)
# %A - Día semana completo (Thursday)
# %a - Día semana corto (Thu)
# %H - Hora 24h (15)
# %I - Hora 12h (03)
# %M - Minuto (30)
# %S - Segundo (45)
# %p - AM/PM


# ==============================================================================
# 6. PARSEAR FECHAS - strptime() [String PARSE Time]
# ==============================================================================

# De string a objeto datetime
fecha_str = "2026-02-05"
fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d")
print(f"String a datetime: {fecha_obj}")
print(f"Tipo: {type(fecha_obj)}")  # <class 'datetime.datetime'>

# Diferentes formatos
fecha_str2 = "05/02/2026"
fecha_obj2 = datetime.strptime(fecha_str2, "%d/%m/%Y")
print(f"Formato ES parseado: {fecha_obj2}")

fecha_str3 = "05 Feb 2026 15:30"
fecha_obj3 = datetime.strptime(fecha_str3, "%d %b %Y %H:%M")
print(f"Formato completo parseado: {fecha_obj3}")

# Convertir a solo date (sin hora)
fecha_solo = fecha_obj.date()
print(f"Solo fecha: {fecha_solo}")
print(f"Tipo: {type(fecha_solo)}")  # <class 'datetime.date'>


# ==============================================================================
# 7. VALIDAR FECHAS
# ==============================================================================

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
print(validar_fecha("2026-13-40"))  # False
print(validar_fecha("no es fecha"))  # False


# ==============================================================================
# 8. OPERACIONES COMUNES CON FECHAS
# ==============================================================================

# ¿Cuántos días faltan para una fecha?
def dias_hasta(fecha_objetivo):
    hoy = date.today()
    diferencia = fecha_objetivo - hoy
    return diferencia.days

navidad = date(2026, 12, 25)
print(f"Días hasta Navidad: {dias_hasta(navidad)}")

# ¿Una fecha está en el pasado?
def es_pasado(fecha):
    return fecha < date.today()

ayer = date.today() - timedelta(days=1)
print(f"¿Ayer es pasado? {es_pasado(ayer)}")  # True

# Obtener primer y último día del mes
def primer_dia_mes(fecha):
    return fecha.replace(day=1)

def ultimo_dia_mes(fecha):
    # Ir al primer día del mes siguiente y restar 1 día
    if fecha.month == 12:
        proximo_mes = fecha.replace(year=fecha.year+1, month=1, day=1)
    else:
        proximo_mes = fecha.replace(month=fecha.month+1, day=1)
    return proximo_mes - timedelta(days=1)

hoy = date.today()
print(f"Primer día mes: {primer_dia_mes(hoy)}")
print(f"Último día mes: {ultimo_dia_mes(hoy)}")

# Edad en años
def calcular_edad(fecha_nacimiento):
    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year
    # Ajustar si no ha cumplido años este año
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    return edad

nacimiento = date(1995, 6, 15)
print(f"Edad: {calcular_edad(nacimiento)} años")


# ==============================================================================
# 9. MÓDULO time (diferente de datetime)
# ==============================================================================

import time as time_module

# Pausar ejecución (sleep)
print("Esperando 2 segundos...")
time_module.sleep(2)
print("¡Continuamos!")

# Timestamp actual (segundos desde 1970-01-01)
timestamp = time_module.time()
print(f"Timestamp actual: {timestamp}")

# Convertir timestamp a datetime
fecha_desde_timestamp = datetime.fromtimestamp(timestamp)
print(f"Fecha desde timestamp: {fecha_desde_timestamp}")


# ==============================================================================
# 10. CASOS DE USO PARA THDORA BOT
# ==============================================================================

# CASO 1: Filtrar citas de hoy
def citas_de_hoy(lista_citas):
    """
    Devuelve citas cuya fecha es hoy
    """
    hoy = date.today()
    return [c for c in lista_citas if c["fecha"] == str(hoy)]

# CASO 2: Filtrar citas del mes actual
def citas_del_mes(lista_citas):
    """
    Devuelve citas del mes y año actual
    """
    hoy = date.today()
    mes_actual = hoy.month
    año_actual = hoy.year
    
    citas_mes = []
    for cita in lista_citas:
        fecha_cita = datetime.strptime(cita["fecha"], "%Y-%m-%d").date()
        if fecha_cita.month == mes_actual and fecha_cita.year == año_actual:
            citas_mes.append(cita)
    return citas_mes

# CASO 3: Próximas citas (próximos 7 días)
def proximas_citas(lista_citas, dias=7):
    """
    Devuelve citas de los próximos N días
    """
    hoy = date.today()
    limite = hoy + timedelta(days=dias)
    
    proximas = []
    for cita in lista_citas:
        fecha_cita = datetime.strptime(cita["fecha"], "%Y-%m-%d").date()
        if hoy <= fecha_cita <= limite:
            proximas.append(cita)
    return proximas

# CASO 4: Ordenar citas por fecha
def ordenar_citas(lista_citas):
    """
    Ordena citas de más antigua a más reciente
    """
    return sorted(lista_citas, key=lambda c: c["fecha"])

# CASO 5: Días que faltan para una cita
def dias_restantes(fecha_cita_str):
    """
    Calcula días que faltan para una cita
    """
    hoy = date.today()
    fecha_cita = datetime.strptime(fecha_cita_str, "%Y-%m-%d").date()
    diferencia = (fecha_cita - hoy).days
    return diferencia


# ==============================================================================
# EJERCICIOS PARA PRACTICAR
# ==============================================================================

"""
EJERCICIO 1: 
Crea una función que reciba una fecha de nacimiento y devuelva:
- Edad en años
- Días hasta el próximo cumpleaños

EJERCICIO 2:
Crea una función que reciba dos fechas y devuelva:
- Diferencia en días
- Diferencia en semanas
- Diferencia en meses (aproximado)

EJERCICIO 3:
Crea una función que valide si un string es una hora válida en formato HH:MM

EJERCICIO 4:
Crea una función que reciba una fecha y devuelva el nombre del día de la semana en español
("Lunes", "Martes", etc.)

EJERCICIO 5:
Crea una función para THDORA que muestre un mensaje diferente según cuánto falte para una cita:
- "¡HOY!" si es hoy
- "Mañana" si es mañana  
- "En X días" si es en el futuro
- "Hace X días" si es en el pasado
"""


# ==============================================================================
# NOTAS ADICIONALES DE LA CLASE
# ==============================================================================

"""
APUNTES TOMADOS DURANTE LA CLASE:




(Añadir aquí lo que expliquen en clase que no esté cubierto arriba)
"""
