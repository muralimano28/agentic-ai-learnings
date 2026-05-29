from app.models.task import Task
from app.storage.json_store import JsonStore


class TaskService:
    def __init__(self) -> None:
        self.tasks: list[Task] = []
        self.store = JsonStore()

    def add_task(self, task: Task) -> tuple[bool, list[Task]]:
        self.tasks.append(task)

        status, tasks, error = self.store.save_tasks(self.tasks)

        # update after storing it in json value.
        # so that if there are any errors, it will be removed due to previous append.
        self.tasks = tasks

        if error:
            return False, self.tasks

        return (status, self.tasks)

    def update_task(self, id: int, title: str) -> tuple[bool, list[Task]]:
        for task in self.tasks:
            if task.id == id:
                task.update_title(title)
                break

        status, tasks, error = self.store.save_tasks(self.tasks)

        self.tasks = tasks

        if error:
            return False, self.tasks

        return status, self.tasks

    def delete_task(self, id: int) -> tuple[bool, list[Task]]:
        # self.tasks = [task for task in self.tasks if task.id != id]

        task_index_to_delete: int = -1
        for index, task in enumerate(self.tasks):
            if task.id == id:
                task_index_to_delete = index
                break

        if task_index_to_delete < 0:
            print("Error: Not able to find the entered task. Enter a valid id to delete.")
            return False, self.tasks

        self.tasks.pop(task_index_to_delete)

        status, tasks, error = self.store.save_tasks(self.tasks)

        self.tasks = tasks

        if error:
            return False, self.tasks

        return status, self.tasks

    def mark_as_complete(self, id: int) -> tuple[bool, list[Task]]:
        task_index_to_update: int = -1
        for index, task in enumerate(self.tasks):
            if task.id == id:
                task_index_to_update = index
                break

        if task_index_to_update < 0:
            print(
                "Error: Not able to find the entered task. Enter a valid id to mark as complete.")
            return False, self.tasks

        self.tasks[task_index_to_update].completed = True

        status, tasks, error = self.store.save_tasks(self.tasks)

        self.tasks = tasks

        if error:
            return False, self.tasks

        return status, self.tasks

    def get_all_tasks(self) -> tuple[bool, list[Task]]:
        status, tasks, error = self.store.load_tasks()

        self.tasks = tasks

        if error:
            print("coming here")
            print(error)
            return (False, [])

        return (status, self.tasks)

    def get_stats(self) -> tuple[int, int, int]:
        completed_tasks: list[Task] = [
            task for task in self.tasks if task.completed == True]
        pending_tasks: list[Task] = [
            task for task in self.tasks if task.completed != True]

        return len(self.tasks), len(completed_tasks), len(pending_tasks)
