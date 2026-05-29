import sys

from app.models.task import Task
from app.services.task_service import TaskService


def print_all_tasks(tasks: list[Task]) -> None:
    print('-------------------------------------------')
    print(f'id    |    Completed    |    Title')
    print('-------------------------------------------')

    for task in tasks:
        print(
            f'{task.id}     |    {task.completed}        |    {task.title}')


def main():
    if len(sys.argv) < 2:
        print(
            "Usage: python -m app.main <list | add | update | delete | complete | stats> <arguments>")
        return

    command: str = sys.argv[1]

    if command in ['add', 'delete', 'complete'] and len(sys.argv) < 3:
        print("Usage: python -m app.main <add | delete | complete> <title | task-id>")
        return

    if command == 'update' and len(sys.argv) < 4:
        print("Usage: python -m app.main update <task-id> <updated-title>")
        return

    task_service = TaskService()
    get_all_tasks_status, tasks = task_service.get_all_tasks()

    if not get_all_tasks_status:
        print("Error while fetching all tasks")
        return

    match command:
        case 'list':
            if not tasks:
                print('---- No tasks found ----')
                return

            print_all_tasks(tasks)
        case 'add':
            id: int = len(tasks) + 1
            title: str = sys.argv[2]

            new_task: Task = Task(id, title, False)

            status, tasks = task_service.add_task(new_task)

            if status == True:
                print("Added task successfully")
            else:
                print("Failed to add the task")

            print_all_tasks(tasks)
        case 'update':
            id: int = int(sys.argv[2])
            title: str = sys.argv[3]

            status, tasks = task_service.update_task(id, title)

            if status == True:
                print("Updated task successfully")
            else:
                print("Failed to update task")

            print_all_tasks(tasks)
        case 'delete':
            id: int = int(sys.argv[2])

            status, tasks = task_service.delete_task(id)

            if status == True:
                print("Deleted task successfully")
            else:
                print("Failed to delete task")

            print_all_tasks(tasks)
        case 'complete':
            id: int = int(sys.argv[2])

            status, tasks = task_service.mark_as_complete(id)

            if status == True:
                print("Marked the task as complete successfully")
            else:
                print("Failed to mark the task as complete")

            print_all_tasks(tasks)
        case 'stats':
            total, completed, pending = task_service.get_stats()

            print("Total: ", total)
            print("Completed: ", completed)
            print("Pending: ", pending)
        case _:
            print("Allowed commands: list | add | update | delete | complete | stats")


if __name__ == "__main__":
    main()
