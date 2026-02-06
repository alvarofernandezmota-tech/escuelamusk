# 🔄 THDORA - Flujo de Trabajo

## 🎯 Workflow completo

Cómo trabajar en THDORA paso a paso, sin perderse.

---

## 📝 FASE 1: Leer ejercicio

### 1. Abrir documentación

```bash
code docs/ejercicios/01-diccionario-base.md
```

### 2. Leer secciones:

- 🎯 **Objetivo**: Qué vamos a hacer
- 📚 **Conceptos previos**: Teoría necesaria
- 🔗 **Vinculación Musk**: Qué módulo estudiar antes
- 💻 **Código comentado**: Línea por línea explicado
- ✍️ **Tu turno**: Ejercicio práctico
- ❓ **Preguntas clave**: Verificar comprensión
- ❌ **Errores comunes**: Qué evitar

---

## ❓ FASE 2: Preguntar dudas

### Si NO entiendes algo:

**❌ NO hagas:**
- Seguir adelante sin entender
- Copiar código sin saber qué hace
- Frustrarte solo

**✅ SÍ haz:**
1. Pregunta a Perplexity
2. Pide más ejemplos
3. Solicita explicación diferente
4. Repite ejercicio si es necesario

### Ejemplos de preguntas:

```
❓ "¿Por qué usamos comillas en 'citas'?"
❓ "¿Qué diferencia hay entre [] y {}?"
❓ "¿Puedo usar otro nombre en vez de thdora_data?"
❓ "Me da error en la línea 5, ¿qué hago?"
```

---

## 💻 FASE 3: Practicar

### 1. Abrir carpeta de práctica

```bash
code ejercicios-practica/ejercicio-01.py
```

### 2. Escribir código TU MISMO

**❌ NO copies directamente**  
**✅ Escribe línea por línea entendiendo**

### 3. Probar

```bash
python ejercicios-practica/ejercicio-01.py
```

### 4. Si falla:

- Lee el error
- Piensa qué puede ser
- Intenta corregir
- Si no puedes → Pregunta a Perplexity

### 5. Cuando funciona:

```bash
# Output esperado:
🤖 THDORA v0.1 - Diccionario base

Diccionario inicial:
{'citas': []}

Número de citas: 0

✅ Diccionario creado correctamente
```

---

## ✅ FASE 4: Verificar comprensión

### Responde mentalmente:

1. ¿Qué hace cada línea?
2. ¿Por qué usamos esta estructura?
3. ¿Podría explicarlo a otra persona?
4. ¿Qué pasaría si cambio X?

**Si respondes TODO → ¡Entendiste!**  
**Si dudas → Repite ejercicio**

---

## 💾 FASE 5: Integrar a THDORA

### Solo cuando el código funciona Y lo entiendes:

```bash
# 1. Copiar tu código al archivo principal
cp ejercicios-practica/ejercicio-01.py src/thdora_data.py

# 2. Probar que funciona en src/
python src/thdora_data.py
```

---

## 📸 FASE 6: Crear snapshot

### Opción A: Manual

```bash
cp src/thdora_data.py src/snapshots/v01_diccionario.py
```

### Opción B: Con script (más adelante)

```bash
python actualizar_snapshot.py 01
```

---

## 📝 FASE 7: Commit

```bash
# 1. Añadir cambios
git add ejercicios-practica/ejercicio-01.py
git add src/thdora_data.py
git add src/snapshots/v01_diccionario.py

# 2. Commit descriptivo
git commit -m "✅ Ejercicio 1 completado: Diccionario base"

# 3. Push
git push origin main
```

---

## 🎉 FASE 8: Documentar en diary

### Opcional pero recomendado:

```bash
code diary/febrero/dia6-ejercicio1-thdora.md
```

**Contenido:**
```markdown
# Día 6 - Ejercicio 1 THDORA

## ✅ Logros
- Completado ejercicio 1: Diccionario base
- Entendí qué son los diccionarios
- Practiqué listas dentro de diccionarios

## 💡 Aprendizajes
- Un diccionario es como una agenda
- Las listas pueden estar dentro de diccionarios
- [] es lista vacía

## 🐛 Dificultades
- Al principio confundí [] con {}
- Olvidé las comillas en 'citas'

## ➡️ Siguiente
- Ejercicio 2: agregar_cita()
```

---

## 🔄 Ciclo completo resumido

```
1. LEO ejercicio → docs/ejercicios/XX.md
2. PREGUNTO dudas → Perplexity
3. PRACTICO → ejercicios-practica/ejercicio-XX.py
4. VERIFICO que entendí → Preguntas clave
5. INTEGRO → src/thdora_data.py
6. SNAPSHOT → src/snapshots/vXX.py
7. COMMIT → git push
8. DOCUMENTO → diary/ (opcional)
```

---

## ⏱️ Tiempos estimados

| Fase | Tiempo |
|------|--------|
| 1. Leer ejercicio | 5-10 min |
| 2. Preguntar dudas | 0-15 min |
| 3. Practicar | 10-30 min |
| 4. Verificar | 5 min |
| 5. Integrar | 2 min |
| 6. Snapshot | 1 min |
| 7. Commit | 2 min |
| 8. Documentar | 5-10 min |
| **TOTAL** | **30-75 min** |

---

## ⚠️ Importante

**NO tengas prisa**
- Mejor entender bien 1 ejercicio
- Que hacer 5 sin entender nada

**Repite si es necesario**
- No pasa nada por repetir
- Es parte del aprendizaje
- La 2ª vez será más fácil

**Pregunta siempre**
- No hay preguntas tontas
- Mejor preguntar 10 veces
- Que avanzar sin entender

---

**Proyecto:** THDORA Bot v0.1  
**Flujo:** Leer → Preguntar → Practicar → Integrar