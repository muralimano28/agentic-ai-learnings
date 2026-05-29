from app.models.task import Task
from app.utils.helpers import read_from_json_file, write_to_json_file


json_file_path: str = "data/tasks.json"


class JsonStore:
    def save_tasks(self, tasks: list[Task]) -> tuple[bool, list[Task], str | None]:
        tasks_dict: list[dict] = [each_task.to_dict()
                                  for each_task in tasks]

        status, _content, error = write_to_json_file(
            file_path=json_file_path, data=tasks_dict)

        return (status, tasks, error)

    def load_tasks(self) -> tuple(bool, list[Task], str | None):
        status, content, error = read_from_json_file(file_path=json_file_path)

        tasks: list[Task] = []

        if content and len(content) > 0:
            tasks = [Task(task["id"], task["title"], task["completed"])
                     for task in content]

        return (status, tasks, error)
