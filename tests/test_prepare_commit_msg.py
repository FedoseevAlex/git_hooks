"""
Тестирование хука для подготовки сообщения коммита
"""
from hooks.prepare_commit_msg import create_commit_message


def test_create_commit_message():
    assert "\nBUG-11\n" == create_commit_message("bug_11")
    assert "\nFEATURE-2\n" == create_commit_message("feature_2")
    assert "\nSOME-BRANCH-NAME-1234\n" == create_commit_message("some_branch_name_1234")
    assert "\nSOME-BRANCH-NAME-1234\n" == create_commit_message("some_branch_name_1234_with_description")
    assert "" == create_commit_message("feature_awesome")
