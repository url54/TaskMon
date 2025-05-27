import argparse
import json
import os
from datetime import datetime

class Task:
    def __init__(self, title, priority="medium"):
        self.title = title
        self.priority = priority
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.completed = False

    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "created_at": self.created_at,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data["title"], data["priority"])
        task.created_at = data["created_at"]
        task.completed = data["completed"]
        return task

class TaskManager:
    def __init__(self, storage_file="tasks.json"):
        self.storage_file = storage_file
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(task_data) for task_data in data]

    def save_tasks(self):
        with open(self.storage_file, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=2)

    def add_task(self, title, priority):
        task = Task(title, priority)
        self.tasks.append(task)
        self.save_tasks()
        return task

    def list_tasks(self, show_completed=False):
        return [task for task in self.tasks if task.completed == show_completed]

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completed = True
                self.save_tasks()
                return True
        return False

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Add task command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("--priority", choices=["low", "medium", "high"],
                           default="medium", help="Task priority")

    # List tasks command
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("--completed", action="store_true",
                            help="Show completed tasks")

    # Complete task command
    complete_parser = subparsers.add_parser("complete", help="Mark task as completed")
    complete_parser.add_argument("title", help="Task title to mark as completed")

    args = parser.parse_args()
    task_manager = TaskManager()

    if args.command == "add":
        task = task_manager.add_task(args.title, args.priority)
        print(f"Added task: {task.title} (Priority: {task.priority})")

    elif args.command == "list":
        tasks = task_manager.list_tasks(args.completed)
        status = "completed" if args.completed else "pending"
        print(f"\nShowing {status} tasks:")
        print("-" * 40)
        for task in tasks:
            print(f"Title: {task.title}")
            print(f"Priority: {task.priority}")
            print(f"Created: {task.created_at}")
            print("-" * 40)

    elif args.command == "complete":
        if task_manager.complete_task(args.title):
            print(f"Marked task '{args.title}' as completed")
        else:
            print(f"Task '{args.title}' not found")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
