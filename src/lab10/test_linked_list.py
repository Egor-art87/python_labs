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