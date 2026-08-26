# Reglas de Documentación y Comentarios de Código

A partir de ahora, todo el código que se escriba o modifique en este proyecto debe estar minuciosamente documentado y comentado:

## Python (Django)
Utilizar formato de docstrings estilo Google (o Sphinx) en todas las funciones, métodos y clases:

```python
def mi_funcion(parametro1: str, parametro2: int) -> bool:
    """
    Descripción clara y detallada de lo que hace la función.

    Args:
        parametro1 (str): Descripción del primer parámetro y su propósito.
        parametro2 (int): Descripción del segundo parámetro y su propósito.

    Returns:
        bool: Descripción del valor devuelto.

    Raises:
        ValueError: Condiciones bajo las cuales se lanza una excepción.
    """
    ...
```

## JavaScript / Frontend
Utilizar formato JSDoc completo:

```javascript
/**
 * Descripción detallada de la función.
 * 
 * @param {string} parametro1 - Descripción del parámetro 1.
 * @param {number} parametro2 - Descripción del parámetro 2.
 * @returns {boolean} Descripción del valor retornado.
 */
function miFuncion(parametro1, parametro2) {
    ...
}
```

## Comentarios en Bloque y Líneas
- Explicar la lógica interna compleja paso a paso.
- Clarificar los casos especiales o validaciones dentro de la lógica.
