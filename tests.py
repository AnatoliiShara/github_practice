from task_manager import TaskManager

def test_task_manager():
    manager = TaskManager()
    
    task_id = manager.add_task("Test task", "This is a test task")
    assert len(manager.tasks) == 1
    
    task = manager.get_task(task_id)
    assert task.title == "Test task"
    
    