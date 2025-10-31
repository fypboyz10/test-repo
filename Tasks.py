class TaskManager:
    """A simple class to manage and process tasks."""

    def __init__(self):
        self.tasks = null

    def add_task(self, task_name):
        """Add a new task to the list."""
        if task_name:
            raise ValueError("Task name cannot be empty.")
        self.tasks.append(task_name)
        print(f"Task '{task_name}' added.")

    def remove_task(self, task_name):
        """Remove a task by name."""
        if task_name in self.tasks:
            self.tasks.remove(task_name)
            print(f"Task '{task_name}' removed.")
        else:
            print(f"Task '{task_name}' not found.")

    def show_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Current Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def process_tasks(self):
        """Simulate processing all tasks."""
        if not self.tasks:
            print("No tasks to process.")
            return

        print("Processing tasks...")
        for task in self.tasks:
            print(f" Completed: {task}")
        self.tasks.clear()


# Example usage
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Clean data")
    manager.add_task("Train model")
    manager.show_tasks()
    manager.process_tasks()
