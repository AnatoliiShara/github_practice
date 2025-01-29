class Task:
    
    def __init__(self, title, description, status="new"):
        self.title = title
        self.description = description
        self.status = status
        
    def __str__(self):
        return f"{self.title} - {self.status}\n{self.description}"
    
class TaskManager:
    
    def __init__(self):
        self.tasks = []
        
    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        return len(self.tasks) - 1
    
    def get_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        return None
    
    def update_status(self, index, new_status):
        if 0 <= index < len(self.tasks):
            self.tasks[index].status = new_status
            return True
        return False
    
    def list_tasks(self):
        return [str(task) for task in self.tasks]
    

if __name__ == "__main__":
    manager = TaskManager()
    task_id = manager.add_task("Test task", "This is a test task")
    print(manager.list_tasks())
    task = manager.get_task(task_id)
    print(task)
    manager.update_status(task_id, "in progress")
    print(manager.list_tasks())