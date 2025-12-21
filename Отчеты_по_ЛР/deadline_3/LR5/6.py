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
    
    def get_high_priority_tasks(self, min_priority):
        important_tasks = []
        for task in self.tasks:
            if task.priority >= min_priority:
                important_tasks.append(task)
        return important_tasks

manager = task_manager()
manager.add_task("купить штаны", 1)
manager.add_task("погулять с саней", 2)
manager.add_task("сходить на профессионалы", 7)
manager.add_task("подготовиться к экзамену", 8)

important = manager.get_high_priority_tasks(5)
print("\nважные задачи (приоритет 5+):")
for task in important:
    print(f"  {task.description} - {task.priority}")