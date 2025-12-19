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

