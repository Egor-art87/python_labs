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


