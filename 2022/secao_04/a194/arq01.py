import json
import os.path

memory, file = [], 'tasks.json'


def undo(list_, memory_):
    if list_:
        memory_.append(list_.pop())
    else:
        print('There is nothing to erase')
    return list_, memory_


def remake(list_, memory_):
    if memory:
        list_.append(memory_.pop())
    else:
        print('There is nothing to do')
    return list_, memory_


def save_file(tasks_, file_):
    with open(file_, 'w', encoding='utf-8') as json_file:
        json.dump(tasks_, json_file, ensure_ascii=False, indent=4)


def list_tasks(tasks_):
    for task in tasks_:
        print(task)


def program():

    commands = {
        'undo': lambda: undo(tasks, memory),
        'remake': lambda: remake(tasks, memory),
        'help': lambda: print('Commands: undo, remake, exit, tasks'),
        'tasks': lambda: list_tasks(tasks),
        'exit': lambda: exit(),
    }

    command = str(input('Append in tasks or execute command (help): '))

    if command not in commands.keys():
        tasks.append(command)
        return program()

    save_file(tasks, file)
    commands[command]()
    return program()


if not os.path.isfile(file):
    save_file([], file)

with open(file, 'r') as open_file:
    tasks = json.load(open_file)

program()
