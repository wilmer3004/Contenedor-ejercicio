from typing import TypeVar, Generic, List, Optional

T = TypeVar("T")

class Contenedor(Generic[T]):
    """Contenedor genérico que almacena elementos de tipo T."""
    def __init__(self) -> None:
        self._items: List[T] = []

    def agregar(self, elemento: T) -> None:
        """Agrega un elemento al contenedor."""
        self._items.append(elemento)

    def obtener_todos(self) -> List[T]:
        """Devuelve una copia de todos los elementos almacenados."""
        return list(self._items)

    def buscar(self, elemento: T) -> bool:
        """Busca si el elemento existe en el contenedor."""
        return elemento in self._items

class Pila(Contenedor[T]):
    """Pila LIFO basada en Contenedor."""
    def push(self, elemento: T) -> None:
        self.agregar(elemento)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty Pila")
        return self._items.pop()

    def peek(self) -> Optional[T]:
        if not self._items:
            return None
        return self._items[-1]

class Cola(Contenedor[T]):
    """Cola FIFO basada en Contenedor."""
    def enqueue(self, elemento: T) -> None:
        self.agregar(elemento)

    def dequeue(self) -> T:
        if not self._items:
            raise IndexError("dequeue from empty Cola")
        return self._items.pop(0)

    def peek(self) -> Optional[T]:
        if not self._items:
            return None
        return self._items[0]

# Pequeña batería de pruebas (prints y asserts)
def _demo():
    print("=== DEMO: Pila[int] ===")
    p_int = Pila[int]()
    p_int.push(10)
    p_int.push(20)
    p_int.push(30)
    assert p_int.peek() == 30
    assert p_int.buscar(20) is True
    print("Pila[int] items:", p_int.obtener_todos())

    print("\n=== DEMO: Pila[str] ===")
    p_str = Pila[str]()
    p_str.push("hola")
    p_str.push("mundo")
    assert p_str.peek() == "mundo"
    assert p_str.buscar("adios") is False
    print("Pila[str] items:", p_str.obtener_todos())

    print("\n=== DEMO: Cola[int] ===")
    c_int = Cola[int]()
    c_int.enqueue(1)
    c_int.enqueue(2)
    c_int.enqueue(3)
    assert c_int.peek() == 1
    assert c_int.buscar(2) is True
    print("Cola[int] items:", c_int.obtener_todos())

    # Ejemplos de manejo de excepciones
    print("\nPop until empty:")
    while True:
        try:
            val = p_int.pop()
            print("popped", val)
        except IndexError:
            print("Pila vacía - fin de pops")
            break

if __name__ == "__main__":
    _demo()
