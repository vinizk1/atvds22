#fila = []

#def insert(x):
#   fila.append(x)

#def remove():
#   fila.pop(0)

from typing import Deque, Any, Iterator
from collections import deque 

class Queue:
    """Uma classe representando uma fila """

    def __init__(self, maxlen=None) -> None:
        # Deque permite enviar maxlen
        # para criar um tamanho máximo para 
        # a fila
        self.__items: Deque[Any] = deque(maxlen=maxlen)

    def enqueue(self, *items: Any) -> None:
        """Enqueue (enfileirar) é o mesmo que append"""
        for item in items:
            self.__items.append(item)

    def dequeue(self) -> Any:
        """Dequeue (desenfileirar) é o mesmo que popleft"""
        if not self:
            raise IndexError ('pop from empty queue')

        return self.__items.popleft()

    def __repr__(self) -> str:
        return str(self.__items)

    def __bool__(self) -> bool:
        return bool(self.__items)

    def __len__(self) -> int:
        return len(self.__items)
    
    def __iter__(self) -> Iterator:
        return self.__items.__iter__()

    def __getitem__(self, index: int) -> Any:
        return self.__items[index]

if __name__ == "__main__":
#   Instanciando
        fila = Queue()
#   Enfileirando A, B, C e D
fila.enqueue('A', 'B', 'C', 'D')

print(fila.__repr__())
print(fila.__getitem__(2))
print(fila.__bool__())
print(fila.__iter__())

fila.enqueue('d', 'e', 'f', 'g')

print(fila)

print('Item com índice 1:', fila[1], end= '\n\n')

for item in fila:
    print('Iteração:', item)