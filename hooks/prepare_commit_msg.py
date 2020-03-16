#!/usr/bin/env python3
"""
Реализация git hook для подготовки сообщения коммита.
"""
import sys
import re
from subprocess import check_output


def create_commit_message(branch_name: str) -> str:
    """
    Подготовка сообщения коммита на основе имени текущей ветки.

    :param branch_name: Имя ветки для формирования заготовки сообщения коммита
    :return: Возвращает форматированное сообщение если имя ветки подходит под
             шаблон {тип задачи}_{номер задачи}. Если имя ветки не
             совпадает с шаблоном, то возвращается пустое сообщение.
    """
    message = ""
    match = re.match(r"(\w+)_(\d+)", branch_name)

    if match:
        issue, num = match.groups()
        message = f"{issue.replace('_', '-').upper()} #{num}:\n"

    return message


def get_git_status():
    """
    Получение вывода команды git status.

    :return: Строка статуса репозитория
    """
    message = list()
    status = check_output(["git", "status"]).decode(encoding="UTF-8").strip()

    for line in status.splitlines():
        message.append(f"# {line}")

    return "\n".join(message)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        sys.exit(0)

    commit_msg_file = sys.argv[1]
    branch = (
        check_output(["git", "symbolic-ref", "--short", "HEAD"])
        .decode(encoding="UTF-8")
        .strip()
    )

    commit_msg = create_commit_message(branch)
    if commit_msg:
        with open(commit_msg_file, "w") as fd:
            fd.write(commit_msg)
            fd.write(get_git_status())

    sys.exit(0)
