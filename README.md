# Contenedor Genérico en Python: Pila y Cola

Este proyecto implementa un contenedor genérico `Contenedor[T]` en Python, que sirve como base para dos estructuras de datos clásicas: una **Pila** (LIFO) y una **Cola** (FIFO), ambas parametrizadas con tipos genéricos. 

## Estructuras Implementadas

- `Contenedor[T]`: Clase genérica que almacena elementos de tipo `T`.
- `Pila[T]`: Hereda de `Contenedor[T]` y funciona como una pila (Last In First Out).
- `Cola[T]`: Hereda de `Contenedor[T]` y funciona como una cola (First In First Out).

## Funcionalidades

- Agregar elementos al contenedor.
- Obtener todos los elementos almacenados.
- Buscar un elemento dentro del contenedor.
- Operaciones específicas de pila: `push`, `pop`, `peek`.
- Operaciones específicas de cola: `enqueue`, `dequeue`, `peek`.

## Demostración

Se incluyen pruebas con dos tipos de datos:

- Enteros (`int`)
- Cadenas de texto (`str`)

La demo muestra el comportamiento esperado de las operaciones y manejo básico de errores (por ejemplo, hacer pop de una pila vacía).

---

## Cómo ejecutar

1. Asegúrate de tener Python 3.7 o superior instalado.
2. Guarda el código en un archivo llamado, por ejemplo, `contenedor.py`.
3. Ejecuta el archivo desde la terminal o consola con:

```bash
python contenedor.py
