# 📚 CHULETA PYTHON - MÓDULO 2 COMPLETO

> **Referencia rápida de métodos nativos de Python**  
> Escuela Musk - Álvaro Fernández Mota  
> Última actualización: 02 Febrero 2026

---

## 🔤 MÉTODOS DE STRINGS

### **Verificación (devuelven True/False):**

| Método | ¿Qué verifica? | Ejemplo |
|--------|----------------|---------|
| `.isalpha()` | Solo letras | `"abc".isalpha()` → `True` |
| `.isdigit()` | Solo números | `"123".isdigit()` → `True` |
| `.isalnum()` | Letras O números | `"abc123".isalnum()` → `True` |
| `.isspace()` | Solo espacios | `"   ".isspace()` → `True` |
| `.islower()` | Solo minúsculas | `"abc".islower()` → `True` |
| `.isupper()` | Solo MAYÚSCULAS | `"ABC".isupper()` → `True` |
| `.startswith(x)` | Empieza con x | `"hola".startswith("h")` → `True` |
| `.endswith(x)` | Termina con x | `"hola".endswith("a")` → `True` |

### **Búsqueda:**

| Método | ¿Qué hace? | Ejemplo |
|--------|------------|---------|
| `.find(x)` | Primera posición de x (-1 si no existe) | `"hola".find("o")` → `1` |
| `.rfind(x)` | Última posición de x | `"hola hola".rfind("o")` → `6` |
| `.index(x)` | Como find, da ERROR si no existe | `"hola".index("o")` → `1` |
| `.count(x)` | Cuántas veces aparece x | `"hola hola".count("o")` → `2` |

### **Transformación:**

| Método | ¿Qué hace? | Ejemplo |
|--------|------------|---------|
| `.lower()` | A minúsculas | `"HOLA".lower()` → `"hola"` |
| `.upper()` | A MAYÚSCULAS | `"hola".upper()` → `"HOLA"` |
| `.capitalize()` | Primera letra mayúscula | `"hola".capitalize()` → `"Hola"` |
| `.title()` | Cada palabra con mayúscula | `"hola mundo".title()` → `"Hola Mundo"` |
| `.strip()` | Quita espacios inicio/fin | `"  hola  ".strip()` → `"hola"` |
| `.replace(x, y)` | Reemplaza x por y | `"hola".replace("o", "0")` → `"h0la"` |

### **División y unión:**

| Método | ¿Qué hace? | Ejemplo |
|--------|------------|---------|
| `.split(x)` | Divide por x en lista | `"a-b-c".split("-")` → `['a','b','c']` |
| `.join(lista)` | Une lista en string | `"-".join(['a','b'])` → `"a-b"` |

---

## 📊 MÉTODOS DE LISTAS

### **Añadir elementos:**

| Método | ¿Qué hace? | Ejemplo |
|--------|------------|---------|
| `.append(x)` | Añade x al final | `[1,2].append(3)` → `[1,2,3]` |
| `.insert(i, x)` | Inserta x en posición i | `[1,3].insert(1, 2)` → `[1,2,3]` |
| `.extend(lista)` | Añade otra lista | `[1,2].extend([3,4])` → `[1,2,3,4]` |

### **Eliminar elementos:**

| Método | ¿Qué hace? | Ejemplo |
|--------|------------|---------|
| `.remove(x)` | Elimina primera aparición de x | `[1,2,3,2].remove(2)` → `[1,3,2]` |
| `.pop()` | Elimina y devuelve último | `[1,2,3].pop()` → `3`, lista: `[1,2]` |
| `.pop(i)` | Elimina y devuelve posición i | `[1,2,3].pop(1)` → `2`, lista: `[1,3]` |
| `.clear()` | Vacía la lista | `[1,2,3].clear()` → `[]` |

### **Ordenar y modificar:**

| Método | ¿Qué hace? | Ejemplo |
|--------|------------|---------|
| `.sort()` | Ordena la lista (modifica original) | `[3,1,2].sort()` → `[1,2,3]` |
| `.reverse()` | Invierte la lista (modifica original) | `[1,2,3].reverse()` → `[3,2,1]` |

### **Buscar y contar:**

| Método | ¿Qué hace? | Ejemplo |
|--------|------------|---------|
| `.index(x)` | Posición de x | `[1,2,3].index(2)` → `1` |
| `.count(x)` | Cuántas veces aparece x | `[1,2,2,3].count(2)` → `2` |

---

## 📦 MÉTODOS DE TUPLAS

| Método | ¿Qué hace? | Ejemplo |
|--------|------------|---------|
| `.index(x)` | Posición de x | `(1,2,3).index(2)` → `1` |
| `.count(x)` | Cuántas veces aparece x | `(1,2,2,3).count(2)` → `2` |

**Nota:** Tuplas son **inmutables** (no se pueden modificar)

---

## 🗂️ MÉTODOS DE DICCIONARIOS

### **Acceder a datos:**

| Método | ¿Qué hace? | Ejemplo |
|--------|------------|---------|
| `.get(key)` | Obtiene valor (no da error) | `d.get("nombre")` → valor o `None` |
| `.keys()` | Lista de claves | `d.keys()` → `dict_keys(['nombre', 'edad'])` |
| `.values()` | Lista de valores | `d.values()` → `dict_values(['Juan', 25])` |
| `.items()` | Lista de (clave, valor) | `d.items()` → `[('nombre','Juan'), ('edad', 25)]` |

### **Modificar:**

| Método | ¿Qué hace? | Ejemplo |
|--------|------------|---------|
| `.update(otro)` | Fusiona con otro diccionario | `d.update({'edad': 26})` |
| `.pop(key)` | Elimina y devuelve valor | `d.pop('nombre')` → `'Juan'` |
| `.clear()` | Vacía el diccionario | `d.clear()` → `{}` |

---

## 🎲 MÉTODOS DE SETS

| Método | ¿Qué hace? | Ejemplo |
|--------|------------|---------|
| `.add(x)` | Añade elemento | `{1,2}.add(3)` → `{1,2,3}` |
| `.remove(x)` | Elimina x (error si no existe) | `{1,2,3}.remove(2)` → `{1,3}` |
| `.discard(x)` | Elimina x (sin error) | `{1,2}.discard(5)` → `{1,2}` |
| `.union(otro)` | Unión de sets | `{1,2}.union({2,3})` → `{1,2,3}` |
| `.intersection(otro)` | Elementos comunes | `{1,2}.intersection({2,3})` → `{2}` |
| `.difference(otro)` | Elementos solo en primero | `{1,2}.difference({2,3})` → `{1}` |

---

## 🛠️ FUNCIONES BUILT-IN

### **Sobre iterables:**

| Función | ¿Qué hace? | Ejemplo |
|---------|------------|---------|
| `len(x)` | Longitud | `len([1,2,3])` → `3` |
| `sum(x)` | Suma elementos | `sum([1,2,3])` → `6` |
| `max(x)` | Valor máximo | `max([1,2,3])` → `3` |
| `min(x)` | Valor mínimo | `min([1,2,3])` → `1` |
| `sorted(x)` | Devuelve copia ordenada | `sorted([3,1,2])` → `[1,2,3]` |
| `reversed(x)` | Devuelve iterador invertido | `list(reversed([1,2,3]))` → `[3,2,1]` |

### **Filtros y mapas:**

| Función | ¿Qué hace? | Ejemplo |
|---------|------------|---------|
| `filter(f, x)` | Filtra elementos | `list(filter(None, [1,0,2]))` → `[1,2]` |
| `map(f, x)` | Aplica función | `list(map(str, [1,2,3]))` → `['1','2','3']` |
| `any(x)` | ¿Al menos uno True? | `any([False, True])` → `True` |
| `all(x)` | ¿Todos True? | `all([True, True])` → `True` |

### **Conversión:**

| Función | ¿Qué hace? | Ejemplo |
|---------|------------|---------|
| `list(x)` | Convierte a lista | `list("abc")` → `['a','b','c']` |
| `tuple(x)` | Convierte a tupla | `tuple([1,2,3])` → `(1,2,3)` |
| `set(x)` | Convierte a set | `set([1,2,2,3])` → `{1,2,3}` |
| `dict(x)` | Convierte a diccionario | `dict([('a',1)])` → `{'a':1}` |
| `str(x)` | Convierte a string | `str(123)` → `'123'` |
| `int(x)` | Convierte a entero | `int('123')` → `123` |

---

## 🔄 BUCLES

### **FOR:**

```python
# Recorrer lista
for elemento in lista:
    print(elemento)

# Con índice
for i in range(len(lista)):
    print(i, lista[i])

# Con enumerate
for i, elemento in enumerate(lista):
    print(i, elemento)
WHILE:
python
# Bucle básico
i = 0
while i < 10:
    print(i)
    i += 1

# Con centinela
num = int(input("Número (-1 para salir): "))
while num != -1:
    print(num)
    num = int(input("Número (-1 para salir): "))
✂️ SLICING
python
lista = 

lista[2:5]    #  - desde 2 hasta 5 (sin incluir 5)
lista[:5]     #  - desde inicio hasta 5
lista[5:]     #  - desde 5 hasta el final
lista[::2]    #  - cada 2 elementos
lista[::-1]   #  - invertir
lista[-3:]    #  - últimos 3 elementos
📝 LIST COMPREHENSION
python
# Básico
[x for x in lista]

# Con condición
[x for x in lista if x > 0]

# Con transformación
[x * 2 for x in lista]

# Con if-else (ternario)
[x if x > 0 else 0 for x in lista]

# Anidado
[x for sublista in lista_de_listas for x in sublista]
✨ TRUTHY / FALSY
FALSY (evalúan como False):
"" - Cadena vacía

[] - Lista vacía

{} - Diccionario vacío

() - Tupla vacía

set() - Set vacío

0 - Cero

None - None

False - False

TRUTHY (evalúan como True):
Cualquier string con contenido: "hola"

Cualquier lista con elementos: [1, 2]

Cualquier número distinto de 0: 42

True

python
if lista:  # True si lista tiene elementos
    print("Tiene elementos")
else:
    print("Está vacía")
🎯 PATRONES COMUNES
Eliminar elementos vacíos:
python
# Método 1: List comprehension
nueva = [x for x in lista if x]

# Método 2: filter
nueva = list(filter(None, lista))
Construir string desde lista:
python
# Método eficiente
resultado = "".join(lista)

# Evitar (menos eficiente)
resultado = ""
for item in lista:
    resultado += item
Verificar existencia:
python
if elemento in lista:
    print("Existe")

if clave in diccionario:
    print("Clave existe")
Iterar diccionario:
python
# Solo claves
for clave in diccionario:
    print(clave)

# Claves y valores
for clave, valor in diccionario.items():
    print(clave, valor)
💡 CONSEJOS
Usa .join() para strings (más eficiente que +=)

List comprehension es más pythónico que bucles simples

.get() en diccionarios evita errores (mejor que [])

any() y all() son más elegantes que bucles con banderas

Slicing es más rápido y legible que bucles

in para verificar existencia (no uses bucles)

enumerate() cuando necesitas índice y elemento

📚 RECURSOS
Documentación oficial: https://docs.python.org/3/

PEP 8 (estilo): https://pep8.org/

Python Tutor (visualizar código): https://pythontutor.com/

Creado: 02 Febrero 2026
Escuela Musk - Preparación PCAP