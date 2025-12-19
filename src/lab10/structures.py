from collections import deque

class Stack:
    # создаём пустой список
    def __init__(self):
        self._data = []

    # добовляем элемент в конец списка    
    def push(self, item) -> None:
        self._data.append(item)


    def pop(self):
        # удаляем и возвращаем элемент
        if self.is_empty(): # проверяем, что стек не пуст
            raise IndexError("Попытка извлечь элемент из пустого стека")
        return self._data.pop()

    def peek(self):
        # просмотр элемента без удаления 
        if self.is_empty():
            return None
        return self._data[-1]
    
    # проверяем пустоту стека 
    def is_empty(self) -> bool:
        return not self._data

    # получаем размер стека 
    def __len__(self) -> int:
        return len(self._data)

    # строковое представление
    def __repr__(self) -> str:
        return f"Stack({self._data})"


class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item) -> None:
        self._data.append(item)

    # берем из начала очереди 
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Попытка извлечь элемент из пустой очереди")
        return self._data.popleft()

    # смотрим первый элемент
    def peek(self):
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)

    # строковое представление 
    def __repr__(self) -> str:
        return f"Queue({list(self._data)})"


def print_separator(title):
    print(f"  {title}")
    print("="*72)