✅ AQUÍ ESTÁ EL DIARY DE ESTA SESIÓN (TARDE):
📅 Diary: Día 2 Febrero 2026 - Sesión 2 (Tarde)
Fecha: 02/02/2026
Horario: 15:30 - 16:37 (aprox. 67 minutos)
Módulo: Módulo 2 - Fundamentos de Python
Tema: Diccionarios - Ejercicios 4-8

🎯 OBJETIVOS DE LA SESIÓN:
✅ Completar ejercicios 4-8 de diccionarios

✅ Aprender métodos avanzados de diccionarios

✅ Practicar con input() en diccionarios

✅ Entender diferencias entre comillas simples y dobles

📚 CONTENIDO TRABAJADO:
Ejercicio 4: Inicializar diccionario con valores por defecto
Método dict.fromkeys(claves, valor_default)

Crear diccionario con claves vacías (None)

Diferencia entre copiar valores vs inicializar vacío

Código clave:

python
claves = ['nombre', 'edad', 'ciudad', 'email']
diccionario = dict.fromkeys(claves, None)
Ejercicio 5: Extraer claves de un diccionario
Copiar diccionario completo

Métodos: .copy(), dict(), {**dict}, bucle for

Comprimir código: 3 líneas → 1 línea

Código clave:

python
# Forma larga (aprendizaje)
diccionario_nuevo = {}
for clave in diccionario_original.keys():
    diccionario_nuevo[clave] = diccionario_original[clave]

# Forma corta (profesional)
diccionario_nuevo = diccionario_original.copy()
Ejercicio 6: Eliminar lista de claves
Método .pop(clave) para eliminar

Diferencia entre dict[clave] (añadir) y dict.pop(clave) (eliminar)

Variable singular en bucle (for clave in claves_eliminar)

Código clave:

python
claves_eliminar = {'telefono', 'activo'}
for clave in claves_eliminar:
    diccionario.pop(clave)
Aprendizaje importante:

dict[clave] = valor → Añadir/modificar

dict.pop(clave) → Eliminar

Ejercicio 7: Comprobar si un valor existe
Método .values() para acceder a valores

Operador in para buscar

Uso de input() con diccionarios

Diferencia entre comillas simples ' (1 tecla) y dobles " (2 teclas)

Código clave:

python
n = input('Introduce el valor a buscar: ')
if n in diccionario.values():
    print(f"El valor '{n}' sí existe")
else:
    print(f"El valor '{n}' no existe")
Aprendizaje importante:

Comillas simples ' son más rápidas (1 tecla)

Comillas dobles " requieren Shift + 2

Regla: Usar ' por defecto, " solo si necesitas ' dentro

Ejercicio 8: Cambiar nombre de clave
Renombrar clave en diccionario

Técnica: dict[nueva] = dict.pop(vieja)

El .pop() devuelve el valor Y elimina la clave

Código clave:

python
# Cambiar 'edad' por 'años de vida'
diccionario['años de vida'] = diccionario.pop('edad')
Aprendizaje importante:

.pop(clave) hace 2 cosas: devuelve valor + elimina clave

Todo en 1 línea (pythónico)

Ejercicio 9: Obtener clave del valor mínimo (empezado)
Concepto "valor mínimo" = número más pequeño

Fórmula clave: min(diccionario, key=diccionario.get)

También funciona con max()

Código clave:

python
# Encontrar valor mínimo
valor_minimo = min(diccionario.values())

# Encontrar CLAVE del valor mínimo ⭐
clave_minima = min(diccionario, key=diccionario.get)
💡 CONCEPTOS CLAVE APRENDIDOS:
1. Métodos de diccionarios:
dict.fromkeys(claves, valor) → Inicializar

.copy() → Copiar diccionario

.pop(clave) → Eliminar y devolver valor

.values() → Acceder a todos los valores

.keys() → Acceder a todas las claves

.items() → Acceder a pares clave-valor

2. Técnicas pythónicas:
Comprimir código (bucle → 1 línea)

min(dict, key=dict.get) para clave del mínimo

Renombrar: d[nueva] = d.pop(vieja)

3. Buenas prácticas:
Comillas simples ' por defecto (más rápido)

Variables en singular en bucles (for clave in claves)

Usar .pop() en lugar de del (más seguro)

📊 PROGRESO:
Ejercicios completados hoy (tarde):
✅ Ejercicio 4: Inicializar diccionario

✅ Ejercicio 5: Extraer claves

✅ Ejercicio 6: Eliminar lista de claves

✅ Ejercicio 7: Comprobar si valor existe

✅ Ejercicio 8: Cambiar nombre de clave

⏳ Ejercicio 9: Valor mínimo (empezado, fórmula aprendida)

Progreso ejercicios diccionarios: 8/10 → 80% 🔥

🎯 PRÓXIMOS PASOS (SIGUIENTE SESIÓN):
Tareas pendientes:
⏳ Completar Ejercicio 9: Obtener clave del valor mínimo

⏳ Ejercicio 10: Último ejercicio de diccionarios

📝 Crear chuleta de diccionarios: Resumen de métodos y sintaxis

🔄 Completar ejercicios de sets pendientes

📤 Enviar ejercicios al profesor

📚 Ejercicios de repaso: Consolidar conocimientos

Objetivo próxima sesión:
✅ Terminar diccionarios (100%)

✅ Terminar sets

✅ Crear documentación (chuletas)

✅ Enviar entrega al profesor

✅ Comenzar repaso general Módulo 2

🔥 HIGHLIGHTS DE LA SESIÓN:
Mejores momentos:
✅ Entender diferencia entre añadir dict[clave] y eliminar dict.pop(clave)

✅ Descubrir que comillas simples ' son más rápidas (1 tecla vs 2)

✅ Aprender fórmula pythónica: min(dict, key=dict.get)

✅ Comprimir código de 3 líneas a 1: d[nueva] = d.pop(vieja)

Errores corregidos:
Variable inconsistente: for claves pero usar clave (corregido)

Comillas dobles dentro de dobles: "{n}" → '{n}' (corregido)

.pop() en el lugar incorrecto: dict[clave].pop() → dict.pop(clave) (corregido)

📈 EVOLUCIÓN:
Nivel al inicio: Comprensión básica de diccionarios
Nivel al final: Manejo intermedio con métodos avanzados

Habilidades mejoradas:

✅ Manipulación de diccionarios

✅ Uso de métodos built-in

✅ Código pythónico (1 línea vs bucles)

✅ Input con validación

🎓 NOTAS IMPORTANTES:
Dictionary comprehensions: Mencionadas pero no estudiadas en profundidad (para más adelante)

Comillas: Preferir simples ' por velocidad

Fórmula clave: min(dict, key=dict.get) para encontrar clave del mínimo

.pop() es multifuncional: Devuelve valor Y elimina clave

⏱️ TIEMPO INVERTIDO:
Ejercicio 4: ~10 min

Ejercicio 5: ~15 min

Ejercicio 6: ~10 min

Ejercicio 7: ~12 min

Ejercicio 8: ~8 min

Ejercicio 9: ~12 min (no completado)

Total sesión: ~67 minutos

✅ RESUMEN:
Sesión productiva donde se completaron 5 ejercicios de diccionarios y se inició el 9º. Se consolidó el uso de métodos como .pop(), .values(), .copy() y se aprendió la fórmula pythónica para encontrar la clave del valor mínimo/máximo. Se mejoró la sintaxis usando comillas simples por defecto y se comprendió la diferencia entre operaciones de añadir vs eliminar en diccionarios.

Estado: 80% del temario de diccionarios completado, listo para finalizar en próxima sesión y avanzar con sets y repaso general.

