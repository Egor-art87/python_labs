import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


def test_normalize_basic():
    """Тест базовой нормализации"""
    text = "HeLlo WOrld"
    result = normalize(text)
    # Проверяем что текст приводится к нижнему регистру
    assert result == "hello world"
    print("test_normalize_basic passed")


def test_normalize_control_chars():
    """Тест удаления управляющих символов"""
    text = "Hello\tWorld\nTest"
    result = normalize(text)
    assert "\t" not in result
    assert "\n" not in result
    assert "  " not in result  # Не должно быть двойных пробелов
    print("test_normalize_control_chars passed")


def test_tokenize_yo2e():
    """Тест замены ё на е"""
    text = "ёжик ёлка Ёлка Ёжик "
    result = normalize(text)
    assert result == "ежик елка елка ежик"
    print("test_tokenize_ye2o passed")


def test_tokenize_basic():
    """Тест базовой токенизации"""
    text = "hello world test"
    result = tokenize(text)
    assert result == ["hello", "world", "test"]
    print("test_tokenize_basic passed")


def test_tokenize_hyphens():
    """Тест токенизации с дефисами"""
    text = "hello-word hi-hyphen"
    result = tokenize(text)
    assert result == ["hello-word", "hi-hyphen"]
    print("test_tokenize_hyphens passed")


def test_count_freq_basic():
    """Тест подсчета частот"""
    tokens = ["apple", "banana", "apple", "orange", "banana", "apple"]
    result = count_freq(tokens)
    expected = {"apple": 3, "banana": 2, "orange": 1}
    assert result == expected
    print("test_count_freq_basic passed")


def test_top_n_basic():
    """Тест получения топ-N слов"""
    freq = {"apple": 5, "banana": 3, "orange": 4, "grape": 2}
    result = top_n(freq, 3)
    # Проверяем количество
    assert len(result) == 3
    # Проверяем порядок (по убыванию частоты)
    assert result[0][0] == "apple" and result[0][1] == 5
    assert result[1][0] == "orange" and result[1][1] == 4
    assert result[2][0] == "banana" and result[2][1] == 3
    print("test_top_n_basic passed")
