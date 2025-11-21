import argparse
import sys
from pathlib import Path
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from src.text import tokenize, normalize, top_n, count_freg


def run_cat(path: Path, out: Path | None = None, number_lines: bool = False):
    """Вывод содержимого файла с опциональной нумерацией строк."""
    if not path.exists():
        print(f"Ошибка: файл '{path}' не найден!", file=sys.stderr)
        sys.exit(1)

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"Ошибка: файл '{path}' не в UTF-8!", file=sys.stderr)
        sys.exit(1)

    lines = text.splitlines()

    if number_lines:
        output = "\n".join(f"{i+1:>4}  {line}" for i, line in enumerate(lines))
    else:
        output = "\n".join(lines)

    if out:
        out.write_text(output, encoding="utf-8")
    else:
        print(output)


def run_stats(path: Path, top: int = 10, out: Path | None = None):
    """Анализ частоты слов в файле."""
    if not path.exists():
        print(f"Ошибка: файл '{path}' не найден!", file=sys.stderr)
        sys.exit(1)

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"Ошибка: файл '{path}' не в UTF-8!", file=sys.stderr)
        sys.exit(1)

    tokens = tokenize(text)

    normalized = [normalize(token) for token in tokens]
    normalized = [t for t in normalized if t]  

    freq = count_freg(normalized)

    top_words = top_n(freq, top)

    if not top_words:
        print('Нет слов для отображения')
        return
    max_len = max(len(word) for word, _ in top_words)
    col_word = 'слово'
    col_freq = 'частота'

    width_word = max(max_len, len(col_word))
    width_freq = len(col_freq)
    print(f"{col_word:<{width_word}} | {col_freq}")
    print("-" * width_word + "-+-" + "-" * width_freq)

    for word, count in top_words:
        print(f"{word:<{width_word}} | {count}")


def build_parser():
    parser = argparse.ArgumentParser(description="CLI-утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_p = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_p.add_argument("path", type=Path, help="Путь к файлу")
    cat_p.add_argument("-o", "--out", type=Path, help="Файл для вывода результата")
    cat_p.add_argument("-n", "--number", action="store_true", help="Нумеровать строки")

    stats_p = subparsers.add_parser("stats", help="Статистика слов")
    stats_p.add_argument("path", type=Path, help="Путь к файлу")
    stats_p.add_argument("-k", "--top", type=int, default=10, help="Топ N слов")
    stats_p.add_argument("-o", "--out", type=Path, help="Файл для вывода результата")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "cat":
        run_cat(args.path, args.out, args.number)

    elif args.command == "stats":
        run_stats(args.path, args.top, args.out)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
