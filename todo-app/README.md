# Todo App

Simple Todo app to learn python basics.

## Development workflow

```bash
python -m venv .venv # -m tells the python interpreter to run the venv module as a script
source .venv/bin/activate # activates the virtual environment
pip install -r requirements.txt # installs the dependencies
```

To type check:

```bash
mypy app/
```

To run:

```bash
python -m app.main # -m tells the python interpreter to run the app.main module as a script
```

## My learnings in creating this app.

1. Folder structure:

- app/ contains all the code
- **init**.py will be empty for now but it tells python that contents inside app/ is a package and can be imported. Later, we can initialize things inside **init**.py file.
- main.py will be the starting point for the package that orchestrates the code and controls the flow
- models/ folder will have the data structure defined for the app. Eg., task.py inside models/ folder will have Task class defined that gives the structure to be imported and used in other parts of the app
- storage/ folder contains the logic to store data. This is separated so that it can be replaced by other storage logic like sqlite3 etc. Right now, this will have json storage which has two capabilities. Save_data, and load_data.
- utils/ folder contains the common utilities like id generation, printing logs etc.
- services/ folder contains the business logic. Eg., task_service.py file inside services will have logic to add_task, update_task, delete_task, get_task, get_all_tasks etc.
- data/ folder will contain runtime data.
- tests/ folder will contain the tests related to the business logic.
- venv/ folder will contain the isolated python environment needed for the project.
- This is basically separation of responsibilities.

2. mypy package - By default, python is a dynamically typed language. Using mypy we can define the typings for the function and return value. mypy only notifies the error when run. Python still allows for dynamic typings. Every class becomes a type in mypy. Eg., if we have class Task: defined, then we can use Task as a type.

3. Like in node projects, installing a package using pip will not automatically get updated in the requirements.txt file. We need to run “pip freeze > requirements.txt” to update the requirements.txt file. Later we can run “pip install -r requirements.txt” to re-install.

4. When we freeze the requirements, we might see additional libraries added. This is due to the conflict from the global pip environments. This is where venv comes in. It allows us to create separate virtual environments for each project. To activate, we need to run “python -m venv .venv”. Here -m flag tells the python to run venv module as a script and the last argument .venv is the folder where everything will be set up for us. This command only creates the virtual environment. We need to activate it by running “source .venv/bin/activate”. This will activate the environment and then we can install the packages using pip and freeze them to requirements.txt. This is very important for any python projects. To deactivate we can simply run “deactivate” in the shell. To verify that we are inside a virtual environment, we can simply run “which python”. This will show the path as a .venv folder.

5. Modern python allows importing packages even without creating **init**.py file. But it is better to explicitly add them so that it reduces cognitive load.

6. To get the command line arguments inside a script, we use sys in-built package in python. Using this package, we can read the arguments by reading “sys.argv”. This is a list of arguments sent along with the command. The first value (ie: 0th index) will be the script name. Remaining values will be the string that is sent along with the command.

7. To read and write into a JSON file, we use python’s in-built json package. This package has two functions that we need. json.loads() and json.dumps(). We read the file content and pass it to the json.loads function to get a structured json output. Similarly, we pass our dictionary to json.dumps() to get the JSON output which we can use to write it to the file. But json.loads and json.dumps use in-memory to create string from json and to json from string. Ie., the entire json will be converted as string when we use json.dumps and this happens in-memory. This is an unoptimized way. Instead, we can use json.dump and pass in the File object from “with open(file_path, ‘w’) as f:” as “json.dump(data, f, indent=4)” and this uses file buffer to dump the entire data as string. Similarly, we can use “json.load(f)” to get the json data from the file read using a buffer.
