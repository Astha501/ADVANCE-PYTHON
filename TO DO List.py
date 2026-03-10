from datetime import datetime

class Task:
    def __init__(self, id, title, deadline=None, priority="medium", project_tag="general"):
        self.id = id
        self.title = title
        self.deadline = deadline
        self.priority = priority.lower()
        self.project_tag = project_tag.lower()

    def __str__(self):
        priority_symbol = {"high": "!!!", "medium": "!!", "low": "!"}[self.priority]
        deadline_str = f" [Due: {self.deadline}]" if self.deadline else ""
        return f"[{self.id}] {self.title} {priority_symbol}{deadline_str} #{self.project_tag}"


class TodoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add(self, title, deadline=None, priority="medium", project_tag="general"):
        """Add a new task"""
        task = Task(self.next_id, title, deadline, priority, project_tag)
        self.tasks.append(task)
        print(f"✓ Added: {title}")
        self.next_id += 1

    def set_deadline(self, task_id, deadline):
        """Set deadline for a task (YYYY-MM-DD)"""
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
            for task in self.tasks:
                if task.id == task_id:
                    task.deadline = deadline
                    print(f"✓ Deadline set to {deadline}")
                    return
            print(f"Task {task_id} not found")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD")

    def assign_priority(self, task_id, priority):
        """Assign priority: high, medium, low"""
        if priority.lower() not in ["high", "medium", "low"]:
            print("Priority must be: high, medium, or low")
            return
        for task in self.tasks:
            if task.id == task_id:
                task.priority = priority.lower()
                print(f"✓ Priority set to {priority}")
                return
        print(f"Task {task_id} not found")

    def filter_by_project(self, project_tag):
        """Filter tasks by project tag"""
        filtered = [t for t in self.tasks if t.project_tag == project_tag.lower()]
        if not filtered:
            print(f"No tasks found with tag: #{project_tag}")
            return
        print(f"\n=== Tasks with tag #{project_tag.upper()} ===")
        for task in filtered:
            print(task)

if __name__ == '__main__':
    todo = TodoList()
    
    # Add tasks
    todo.add("Buy groceries", deadline="2026-03-10", priority="high", project_tag="shopping")
    todo.add("Python project", deadline="2026-03-15", priority="high", project_tag="code")
    todo.add("Exercise", deadline="2026-03-05", priority="medium", project_tag="health")
    todo.add("Read book", priority="low", project_tag="learning")
    
    # Set deadline
    todo.set_deadline(4, "2026-03-20")
    
    # Assign priority
    todo.assign_priority(3, "high")
    
    # Filter by project
    todo.filter_by_project("code")
    todo.filter_by_project("shopping")