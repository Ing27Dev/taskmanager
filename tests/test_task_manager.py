import json
import os
import tempfile

import pytest

from task_manager import TaskManager, Task


@pytest.fixture(autouse=True)
def use_temp_tasks_file(monkeypatch, tmp_path):
    # Use a temporary tasks.json in the tmp_path to avoid touching real files
    temp_file = tmp_path / "tasks.json"
    monkeypatch.setattr(TaskManager, 'FILENAME', str(temp_file))
    yield


def test_add_and_list_and_save(monkeypatch, capsys):
    manager = TaskManager()
    manager.add_task("Probar tarea")

    # capture output of list
    manager.list_task()
    captured = capsys.readouterr()
    assert "Probar tarea" in captured.out

    # ensure file saved and contains the task
    with open(manager.FILENAME, 'r') as f:
        data = json.load(f)
    assert data[0]['description'] == "Probar tarea"
    assert data[0]['completed'] is False


def test_complete_task(capsys):
    manager = TaskManager()
    manager.add_task("Tarea a completar")
    manager.complet_task(1)
    captured = capsys.readouterr()
    assert "Tarea completada" in captured.out

    # check saved file shows completed
    with open(manager.FILENAME, 'r') as f:
        data = json.load(f)
    assert data[0]['completed'] is True


def test_delete_task(capsys):
    manager = TaskManager()
    manager.add_task("Tarea a eliminar")
    manager.delete_task(1)
    captured = capsys.readouterr()
    assert "ha sido eliminada" in captured.out

    # file should be empty list
    with open(manager.FILENAME, 'r') as f:
        data = json.load(f)
    assert data == []


def test_load_initial_next_id(monkeypatch, tmp_path):
    # create a file with existing tasks to test next_id increment
    temp_file = tmp_path / "tasks.json"
    content = [
        {"id": 1, "description": "t1", "completed": False},
        {"id": 2, "description": "t2", "completed": True},
    ]
    temp_file.write_text(json.dumps(content))
    monkeypatch.setattr(TaskManager, 'FILENAME', str(temp_file))

    manager = TaskManager()
    assert manager._next_id == 3


def test_str_task():
    t = Task(5, "Descripción", completed=True)
    s = str(t)
    assert "#5" in s and "Descripción" in s and "✔" in s
