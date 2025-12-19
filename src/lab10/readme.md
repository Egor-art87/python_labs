# structures
## Code
```python
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
    print("\n" + "="*50)
    print(f"  {title}")
    print("="*50)
```
## Tests
```python
from structures import Stack, Queue, print_separator

def test_stack():
    print_separator("=== Тестирование Stack ===")
    s = Stack()
    
    # Пустой стек
    assert s.is_empty() == True
    assert s.peek() is None
    print_separator(f"Пустой стек: {s}")
    
    # Добавление
    s.push(10)
    s.push(20)
    s.push(30)
    assert s.peek() == 30
    assert len(s) == 3
    print_separator("Добавили 3 элемента")
    print_separator(f"Стек: {s}")
    # Удаление
    assert s.pop() == 30
    print_separator(f"Удалили элемент \"30\": {s}")
    assert s.pop() == 20
    assert s.pop() == 10
    print_separator(f"Стек после удаления всех остальных элементов: {s}")
    
   
    assert s.is_empty() == True
    
    # Ошибка при удалении из пустого
    try:
        s.pop()
        assert False, "Должна быть ошибка!"
    except IndexError as e:
        print(f"Правильная ошибка: {e}")
    
    print_separator("Все тесты стека пройдены!")

def test_queue():
    print_separator("\n=== Тестирование Queue ===")
    q = Queue()
    
    # Пустая очередь
    assert q.is_empty() == True
    assert q.peek() is None
    print(f'Пустая очередь: {q}')
    
    # Добавление
    q.enqueue("первый")
    q.enqueue("второй")
    q.enqueue("третий")
    print_separator(f"Очередь после 3 добавлений: {q}")
    assert q.peek() == "первый"
    assert len(q) == 3
    
    # Удаление
    assert q.dequeue() == "первый"
    print_separator('Удаление элементов')
    print_separator(f'Очередь после удаления первого элемента: {q}')
    assert q.dequeue() == "второй"
    assert q.dequeue() == "третий"
    print_separator(f"После удаления всех элементов: {q}")
    
    assert q.is_empty() == True
    
    # Ошибка при удалении из пустой очереди 
    try:
        q.dequeue()
        assert False, "Должна быть ошибка!"
    except IndexError as e:
        print(f" Правильная ошибка: {e}")
    
    print_separator("Все тесты очереди пройдены!")

if __name__ == "__main__":
    test_stack()
    test_queue()
    print_separator("\n Все тесты успешно пройдены!")
```
### результат тестирования
![test](/images/lab10/test_structures.png)


## linked_list

## Code
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"[{self.value}]"


class SinglyLinkedList:
    # создане пустого списка
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    # добавление в конец
    def append(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    # добавление в начало 
    def prepend(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self._size += 1
    
    # добавление по индексу
    def insert(self, idx, value):
        if idx < 0 or idx > self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size}]")
        
        if idx == 0:
            self.prepend(value)
            return
        
        if idx == self._size:
            self.append(value)
            return
        
        new_node = Node(value)
        current = self.head
        
        for _ in range(idx - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self._size += 1
    
    # удаление по индексу
    def remove_at(self, idx):
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size})")
        
        if idx == 0:
            value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return value
        
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        
        value = current.next.value
        
        if current.next == self.tail:
            self.tail = current
        
        current.next = current.next.next
        self._size -= 1
        return value
    
    # итератор по значениям 
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        if self.head is None:
            return "SinglyLinkedList([])"
        
        result = "SinglyLinkedList: "
        current = self.head
        while current:
            result += f"[{current.value}] -> "
            current = current.next
        result += "None"
        return result
```
## test
```python
from linked_list import Node, SinglyLinkedList

def test_linked_list():
    print("=== Тестирование SinglyLinkedList ===")
    
    lst = SinglyLinkedList()
    
    # Пустой список
    assert len(lst) == 0
    assert list(lst) == []  
    
    # Добавление в конец
    lst.append(10)
    lst.append(20)
    lst.append(30)
    assert len(lst) == 3
    assert list(lst) == [10, 20, 30]
    
    # Добавление в начало
    lst.prepend(5)
    assert list(lst) == [5, 10, 20, 30]
    
    # Вставка в середину
    lst.insert(2, 15)  # На позицию 2
    assert list(lst) == [5, 10, 15, 20, 30]
    
    # Вставка в конец через insert
    lst.insert(5, 40)  # В конец
    assert list(lst) == [5, 10, 15, 20, 30, 40]
    
    # Удаление по индексу
    assert lst.remove_at(2) == 15  # Удалили 15
    assert list(lst) == [5, 10, 20, 30, 40]
    
    # Удаление первого
    assert lst.remove_at(0) == 5
    assert list(lst) == [10, 20, 30, 40]
    
    # Удаление последнего
    assert lst.remove_at(3) == 40
    assert list(lst) == [10, 20, 30]
    
    # Проверка красивого вывода
    print(lst)  
    
    # Обработка ошибок
    try:
        lst.insert(100, 99)
    except IndexError as e:
        print(f"Правильная ошибка при вставке: {e}")
    
    try:
        lst.remove_at(100)
    except IndexError as e:
        print(f"Правильная ошибка при удалении: {e}")
    
    print("Все тесты пройдены!")

if __name__ == "__main__":
    test_linked_list()
```
## результат теста
![test](/images/lab10/test_linked_list.png)