# Отчёт по lab07


## test_text.py

```python
import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


def test_normalize_basic():
    """Тест базовой нормализации"""
    text = "HeLlo WOrld"
    result = normalize(text)
    assert result == "hello world"


def test_normalize_control_chars():
    """Тест удаления управляющих символов"""
    text = "Hello\tWorld\nTest"
    result = normalize(text)
    assert "\t" not in result
    assert "\n" not in result
    assert "  " not in result


def test_normalize_yo2e():
    """Тест замены ё на е"""
    text = "ёжик ёлка Ёлка Ёжик"
    result = normalize(text)
    assert result == "ежик елка елка ежик"


def test_normalize_empty_string():
    """Тест нормализации пустой строки"""
    assert normalize("") == ""


@pytest.mark.parametrize(
    "text,expected",
    [
        ("", ""),
        ("Hello\tWorld", "hello world"),
        ("TEST", "test"),
    ],
)
def test_normalize_parametrized(text, expected):
    """Параметризованные тесты для normalize"""
    assert normalize(text) == expected


def test_tokenize_basic():
    """Тест базовой токенизации"""
    text = "hello world test"
    result = tokenize(text)
    assert result == ["hello", "world", "test"]


def test_tokenize_hyphens():
    """Тест токенизации с дефисами"""
    text = "hello-word hi-hyphen"
    result = tokenize(text)
    assert result == ["hello-word", "hi-hyphen"]


def test_tokenize_empty_string():
    """Тест токенизации пустой строки"""
    assert tokenize("") == []


def test_count_freq_basic():
    """Тест подсчета частот"""
    tokens = ["apple", "banana", "apple", "orange", "banana", "apple"]
    result = count_freq(tokens)
    expected = {"apple": 3, "banana": 2, "orange": 1}
    assert result == expected


def test_count_freq_empty_list():
    """Тест подсчета частот пустого списка"""
    assert count_freq([]) == {}


def test_count_freq_single_word():
    """Тест подсчета частот одного слова"""
    assert count_freq(["test"]) == {"test": 1}


def test_top_n_basic():
    """Тест получения топ-N слов"""
    freq = {"apple": 5, "banana": 3, "orange": 4, "grape": 2}
    result = top_n(freq, 3)
    assert len(result) == 3
    assert result[0][0] == "apple" and result[0][1] == 5
    assert result[1][0] == "orange" and result[1][1] == 4
    assert result[2][0] == "banana" and result[2][1] == 3


def test_top_n_same_frequency():
    """Тест одинаковых частот - сортировка по алфавиту"""
    freq = {"banana": 3, "apple": 3, "cherry": 3, "date": 2}
    result = top_n(freq, 3)
    assert result == [("apple", 3), ("banana", 3), ("cherry", 3)]
    assert result[0][0] == "apple"
    assert result[1][0] == "banana"
    assert result[2][0] == "cherry"


def test_top_n_more_than_available():
    """Тест когда запрашиваем больше элементов чем есть"""
    freq = {"apple": 3, "banana": 2}
    result = top_n(freq, 5)
    assert result == [("apple", 3), ("banana", 2)]


def test_top_n_zero_n():
    """Тест запроса 0 элементов"""
    freq = {"apple": 3, "banana": 2}
    assert top_n(freq, 0) == []


@pytest.mark.parametrize(
    "freq,n,expected",
    [
        ({}, 5, []),
        ({"a": 1}, 0, []),
        ({"a": 2, "b": 1}, 2, [("a", 2), ("b", 1)]),
        ({"b": 1, "a": 1}, 2, [("a", 1), ("b", 1)]),
    ],
)
def test_top_n_parametrized(freq, n, expected):
    """Параметризованные тесты для top_n"""
    assert top_n(freq, n) == expected
```

## Запуск тестов с покрытием:
![покрытие](/images/lab07/test_text_покрытие.png)


## test_json_csv.py

```python
import pytest
import json
import csv
import tempfile
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_correct_conversion(tmp_path):
    """Позитивный тест: корректная конвертация JSON → CSV"""
    # Создаем тестовый JSON файл
    json_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "London"}
    ]
    
    json_file = tmp_path / "test.json"
    csv_file = tmp_path / "output.csv"
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    
    # Выполняем конвертацию
    json_to_csv(str(json_file), str(csv_file))
    
    # Проверяем что CSV файл создан
    assert csv_file.exists()
    
    # Проверяем содержимое CSV
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
        # Проверяем количество записей
        assert len(rows) == 2
        
        # Проверяем набор ключей/заголовков
        expected_headers = ["name", "age", "city"]
        assert reader.fieldnames == expected_headers
        
        # Проверяем данные
        assert rows[0]["name"] == "Alice"
        assert rows[0]["age"] == "30"
        assert rows[0]["city"] == "New York"


def test_csv_to_json_correct_conversion(tmp_path):
    """Позитивный тест: корректная конвертация CSV → JSON"""
    # Создаем тестовый CSV файл
    csv_data = [
        ["name", "age", "city"],
        ["Alice", "30", "New York"],
        ["Bob", "25", "London"]
    ]
    
    csv_file = tmp_path / "test.csv"
    json_file = tmp_path / "output.json"
    
    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)
    
    # Выполняем конвертацию
    csv_to_json(str(csv_file), str(json_file))
    
    # Проверяем что JSON файл создан
    assert json_file.exists()
    
    # Проверяем содержимое JSON
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
        # Проверяем количество записей
        assert len(data) == 2
        
        # Проверяем набор ключей/заголовков
        expected_keys = ["name", "age", "city"]
        assert list(data[0].keys()) == expected_keys
        
        # Проверяем данные
        assert data[0]["name"] == "Alice"
        assert data[0]["age"] == "30"
        assert data[0]["city"] == "New York"


def test_json_to_csv_file_not_found():
    """Негативный тест: несуществующий JSON файл → FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        json_to_csv("nonexistent.json", "output.csv")


def test_json_to_csv_invalid_file(tmp_path):
    """Негативный тест: некорректный JSON файл → ValueError"""
    json_file = tmp_path / "test.json"
    
    # Создаем некорректный JSON
    json_file.write_text("{ invalid json }")
    
    with pytest.raises(ValueError):
        json_to_csv(str(json_file), "output.csv")


def test_csv_to_json_file_not_found():
    """Негативный тест: несуществующий CSV файл → FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        csv_to_json("nonexistent.csv", "output.json")


def test_csv_to_json_invalid_file(tmp_path):
    """Негативный тест: пустой CSV файл → ValueError"""
    csv_file = tmp_path / "test.csv"
    
    # Создаем пустой файл
    csv_file.write_text("")
    
    with pytest.raises(ValueError):
        csv_to_json(str(csv_file), "output.json")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```
## Запуск тестов с покрытием
![json_csv_test](/images/lab07/test_json_csv.png)
