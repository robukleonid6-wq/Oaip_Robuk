class task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

class task_manager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description, priority):
        novaia_task = task(description, priority)
        self.tasks.append(novaia_task)
        print(f"задача '{description}' добавлена")
    
    def show_tasks(self):
        print("список задач:")
        for task in self.tasks:
            print(f"  {task.description} - {task.priority}")

manager = task_manager()
manager.add_task("купить коммутатор", 1)
manager.add_task("сделать покс", 1000)
manager.show_tasks()