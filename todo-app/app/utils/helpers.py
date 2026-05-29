import json

from typing import Any


def read_from_json_file(file_path: str) -> tuple[bool, Any | None, str | None]:
    status: bool = False
    content: Any | None = None
    error: str | None = None

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # json.loads takes a string as an input and gives json output. Mostly used for api response. Here f is a File Object (_io.IOWrapper)
            content = json.load(f)

        status = True
    except Exception as e:
        print(e)
        error = str(e)

    return (status, content, error)


def write_to_json_file(file_path: str, data: Any) -> tuple[bool, Any | None, str | None]:
    status: bool = False
    error: str | None = None

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            # json.dumps (notice the 's' in dumps) takes a data and returns a large string using in-memory.
            # This is unoptimized way.
            # While dealing with file writing, we can use json.dump instead that takes data and the file object which streams the data into the file.
            json.dump(data, f, indent=4)

        status = True
    except Exception as e:
        error = str(e)

    return (status, data, error)
