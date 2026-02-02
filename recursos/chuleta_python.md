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

## 🗂️ DICCIONARIOS

### **Operaciones Básicas:**

| Operación | Forma 1 | Forma 2 | Forma 3 |
|-----------|---------|---------|---------|
| **Crear** | `d = {}` | `d = dict()` | `d = {'a': 1}` |
| **Añadir/modificar** | `d['clave'] = valor` | `d.update({'clave': valor})` | |
| **Acceder** | `d['clave']` | `d.get('clave')` | `d.get('clave', default)` |
| **Eliminar** | `d.pop('clave')` | `del d['clave']` | |
| **Existe clave** | `'clave' in d` | | |
| **Existe valor** | `valor in d.values()` | | |

### **Métodos Principales:**

| Método | Qué devuelve | Ejemplo |
|--------|--------------|---------|
| `.keys()` | Claves | `dict_keys(['a', 'b'])` |
| `.values()` | Valores | `dict_values([1, 2])` |
| `.items()` | Tuplas (clave, valor) | `dict_items([('a',1), ('b',2)])` |
| `.get(k, default)` | Valor o default | `d.get('x', 0)` → `0` |
| `.pop(k)` | Valor (elimina) | `d.pop('a')` → `1` |
| `.update(otro)` | None (fusiona) | `d.update({'c': 3})` |
| `.clear()` | None (vacía) | `d.clear()` → `{}` |
| `.fromkeys(keys, val)` | Nuevo dict | `dict.fromkeys(['a','b'], 0)` |

### **Iterar Diccionarios:**

```python
# Solo claves
for clave in diccionario:
    print(clave)

# Claves explícito
for clave in diccionario.keys():
    print(clave)

# Solo valores
for valor in diccionario.values():
    print(valor)

# Claves + valores
for clave, valor in diccionario.items():
    print(clave, valor)
```

### **Obtener Máximos/Mínimos:**

```python
d = {'a': 10, 'b': 5, 'c': 15}

# Valor máximo
max(d.values())  # 15

# Clave del valor máximo
max(d, key=d.get)  # 'c'

# Valor mínimo
min(d.values())  # 5

# Clave del valor mínimo
min(d, key=d.get)  # 'b'
```

### **Cambiar Nombre de Clave:**

```python
# Forma 1: con pop()
d['nueva_clave'] = d.pop('vieja_clave')

# Forma 2: manual
d['nueva_clave'] = d['vieja_clave']
del d['vieja_clave']
```

### **Fusionar Diccionarios:**

| Método | Modifica original | Ejemplo |
|--------|-------------------|---------|
| `.update()` | ✅ SÍ | `d1.update(d2)` |
| `{**d1, **d2}` | ❌ NO (nuevo) | `d3 = {**d1, **d2}` |
| `d1 \| d2` | ❌ NO (Python 3.9+) | `d3 = d1 \| d2` |

---

## 🎲 SETS (CONJUNTOS)

### **Operaciones Básicas:**

| Operación | Forma 1 | Forma 2 | Forma 3 |
|-----------|---------|---------|---------|
| **Crear** | `s = set()` | `s = {1, 2, 3}` | `s = set([1,2,3])` |
| **Añadir** | `s.add(x)` | | |
| **Añadir varios** | `s.update([1,2,3])` | `s \|= {1,2,3}` | |
| **Eliminar** | `s.remove(x)` ⚠️ error | `s.discard(x)` ✅ sin error | `s.pop()` (aleatorio) |
| **Existe** | `x in s` | | |

### **Operaciones de Conjuntos (NO modifican):**

| Operación | Operador | Método | Qué hace |
|-----------|----------|--------|----------|
| **Unión** | `s1 \| s2` | `s1.union(s2)` | En s1 O s2 |
| **Intersección** | `s1 & s2` | `s1.intersection(s2)` | En s1 Y s2 |
| **Diferencia** | `s1 - s2` | `s1.difference(s2)` | En s1 pero NO en s2 |
| **Dif. simétrica** | `s1 ^ s2` | `s1.symmetric_difference(s2)` | En s1 O s2, NO en ambos |

### **Operaciones que SÍ Modifican:**

| Operación | Operador | Método | Qué hace |
|-----------|----------|--------|----------|
| **Unión** | `s1 \|= s2` | `s1.update(s2)` | Añade s2 a s1 |
| **Intersección** | `s1 &= s2` | `s1.intersection_update(s2)` | Solo comunes |
| **Diferencia** | `s1 -= s2` | `s1.difference_update(s2)` | Elimina comunes |
| **Dif. simétrica** | `s1 ^= s2` | `s1.symmetric_difference_update(s2)` | Solo únicos |

### **Comparaciones:**

```python
s1 = {1, 2, 3}
s2 = {1, 2}

# Subconjunto
s2.issubset(s1)      # True (s2 está en s1)
s2 <= s1             # True

# Superconjunto
s1.issuperset(s2)    # True (s1 contiene s2)
s1 >= s2             # True

# Disjuntos (sin elementos comunes)
s1.isdisjoint(s2)    # False (tienen comunes)
```

---

## 🔄 CONVERSIONES

```python
# Lista → Set (elimina duplicados)
lista = [1, 2, 2, 3]
set(lista)  # {1, 2, 3}

# Set → Lista
list({1, 2, 3})  # [1, 2, 3]

# Dict → Set (solo claves)
set({'a': 1, 'b': 2})  # {'a', 'b'}

# Listas → Dict
keys = ['a', 'b']
values = [1, 2]
dict(zip(keys, values))  # {'a': 1, 'b': 2}
```

---

## 📊 FÓRMULAS COMUNES

```python
# Eliminar duplicados de lista
lista_unica = list(set(lista))

# Encontrar elementos comunes entre listas
comunes = list(set(lista1) & set(lista2))

# Encontrar elementos únicos entre listas
unicos = list(set(lista1) ^ set(lista2))

# Contar frecuencias
from collections import Counter
freq = Counter(lista)

# Invertir diccionario (valores → claves)
d_invertido = {v: k for k, v in d.items()}

# Filtrar diccionario
d_filtrado = {k: v for k, v in d.items() if v > 10}

# Diccionario desde listas
d = dict(zip(claves, valores))

# Valor por defecto si clave no existe
d.setdefault('clave', valor_default)
```

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
```

### **WHILE:**

```python
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
```

---

## ✂️ SLICING

```python
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista[2:5]    # [2, 3, 4] - desde 2 hasta 5 (sin incluir 5)
lista[:5]     # [0, 1, 2, 3, 4] - desde inicio hasta 5
lista[5:]     # [5, 6, 7, 8, 9] - desde 5 hasta el final
lista[::2]    # [0, 2, 4, 6, 8] - cada 2 elementos
lista[::-1]   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - invertir
lista[-3:]    # [7, 8, 9] - últimos 3 elementos
```

---

## 📝 LIST COMPREHENSION

```python
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
```

---

## ✨ TRUTHY / FALSY

**FALSY (evalúan como False):**
- `""` - Cadena vacía
- `[]` - Lista vacía
- `{}` - Diccionario vacío
- `()` - Tupla vacía
- `set()` - Set vacío
- `0` - Cero
- `None` - None
- `False` - False

**TRUTHY (evalúan como True):**
- Cualquier string con contenido: `"hola"`
- Cualquier lista con elementos: `[1, 2]`
- Cualquier número distinto de 0: `42`
- `True`

```python
if lista:  # True si lista tiene elementos
    print("Tiene elementos")
else:
    print("Está vacía")
```

---

## 🎯 PATRONES COMUNES

**Eliminar elementos vacíos:**

```python
# Método 1: List comprehension
nueva = [x for x in lista if x]

# Método 2: filter
nueva = list(filter(None, lista))
```

**Construir string desde lista:**

```python
# Método eficiente
resultado = "".join(lista)

# Evitar (menos eficiente)
resultado = ""
for item in lista:
    resultado += item
```

**Verificar existencia:**

```python
if elemento in lista:
    print("Existe")

if clave in diccionario:
    print("Clave existe")
```

**Iterar diccionario:**

```python
# Solo claves
for clave in diccionario:
    print(clave)

# Claves y valores
for clave, valor in diccionario.items():
    print(clave, valor)
```

---

## ⚡ TRUCOS PYTHÓNICOS

```python
# Verificar si diccionario vacío
if not d:  # True si vacío

# Verificar si set vacío
if not s:  # True si vacío

# Swap de valores en diccionario
d['a'], d['b'] = d['b'], d['a']

# Merge múltiples sets
resultado = set().union(s1, s2, s3)

# Crear dict con valores por defecto
d = {k: 0 for k in claves}
d = dict.fromkeys(claves, 0)

# Eliminar mientras iteras (copy)
for k in list(d.keys()):
    if condicion:
        del d[k]
```

---

## 💡 CONSEJOS

- Usa `.join()` para strings (más eficiente que `+=`)
- List comprehension es más pythónico que bucles simples
- `.get()` en diccionarios evita errores (mejor que `[]`)
- `any()` y `all()` son más elegantes que bucles con banderas
- Slicing es más rápido y legible que bucles
- `in` para verificar existencia (no uses bucles)
- `enumerate()` cuando necesitas índice y elemento
- Operadores de sets (`|`, `&`, `-`, `^`) son más limpios que métodos

---

## 📚 RECURSOS

- Documentación oficial: https://docs.python.org/3/
- PEP 8 (estilo): https://pep8.org/
- Python Tutor (visualizar código): https://pythontutor.com/

---

**Creado: 02 Febrero 2026**  
**Escuela Musk - Preparación PCAP**