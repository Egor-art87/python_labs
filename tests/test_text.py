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
