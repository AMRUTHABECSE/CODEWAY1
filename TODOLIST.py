class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f'Task "{self.tasks[task_index]["task"]}" marked as completed.')
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i + 1}. {task['task']} - {status}")

    def run(self):
        while True:
            print("\nTo-Do List Application")
            print("1. Add Task")
            print("2. Mark Task as Completed")
            print("3. Display To-Do List")
            print("4. Quit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                task = input("Enter the task: ")
                self.add_task(task)
                print(f'Task "{task}" added to the to-do list.')
            elif choice == "2":
                self.display_tasks()
                task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
                self.mark_completed(task_index)
            elif choice == "3":
                self.display_tasks()
            elif choice == "4":
                print("Exiting the To-Do List application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.run()
