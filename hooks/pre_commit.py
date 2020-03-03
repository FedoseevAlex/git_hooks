#!/usr/bin/env python3
"""
Git hook для проверки файлов перед коммитом.
Проверяются только измененные файлы.

Выполняется форматирование измененных файлов с помощью утилиты black https://github.com/psf/black.
"""
import sys
from pathlib import Path
from subprocess import check_output, run
from typing import List

from isort import SortImports


def get_changed_files() -> List[Path]:
    """
    Получение вывода команды git diff --name-only --staged.

    :return: Пути файлов подговленных для коммита.
    """
    file_names = (
        check_output(["git", "diff", "--name-only", "--staged"])
        .decode(encoding="UTF-8")
        .strip()
    )
    files = list()

    for name in file_names.splitlines():
        files.append(Path(name).absolute())
    return files


def format_files(files: List[Path]):
    """
    Функция форматирования измененных файлов.
    Сначала сортируются импорты. Затем
    применяется форматирование black. После этого
    изменения добавляются для коммита.

    :param files: Список с путями к файлам
    """
    for file_path in files:
        SortImports(file_path)
        run(["black", "-q", str(file_path)])
        run(["git", "add", str(file_path)])


if __name__ == "__main__":
    changed_files = get_changed_files()
    format_files(changed_files)
    if not get_changed_files():
        print("Nothing to commit: no changed files after autoformatting")
        sys.exit(1)
