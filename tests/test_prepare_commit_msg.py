"""
Тестирование хука для подготовки сообщения коммита
"""
from hooks.prepare_commit_msg import create_commit_message


def test_create_commit_message():
    assert "Bug #11:\n" == create_commit_message("bug_11")
    assert "Feature #2:\n" == create_commit_message("feature_2")
    assert "Some branch name #1234:\n" == create_commit_message("some_branch_name_1234")
    assert "" == create_commit_message("temporary_branch")
