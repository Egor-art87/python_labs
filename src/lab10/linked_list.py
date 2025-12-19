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