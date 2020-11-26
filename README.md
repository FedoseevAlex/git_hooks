# git_hooks
Some git hooks

### prepare_commit_msg.py
git hook для добавления идентификатора задачи перед редактированием сообщения к коммиту. Устанавливать нужно на место **prepare-commit-msg**.

```
$ cd repo_name
$ mv hook.py .git/hooks/prepare-commit-msg
```

Для того чтобы идентификатор задачи подставился в шаблон сообщения коммита нужно называть ветку по шаблону:
{тип задачи}_{номер задачи}{описание}
Примеры:
| Имя ветки | Добавленный идентификатор |
| ------ | ------ |
| openstack_1_add_new_feature | OPENSTACK-1 |
| bug_42069_fix_critical_bug | BUG-42069 |
| feature_awesome | - |
| quick_fix_3290 | QUICK-FIX-3290 |
