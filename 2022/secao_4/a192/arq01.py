import json

with open('tasks.json', 'r') as open_file:
    tasks = json.load(open_file)

memory = []
commands = ['undo', 'tasks', 'remake', 'exit']


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


def save_file(tasks_, json_file):
    with open(json_file, 'w+', encoding='utf-8') as add_file:
        json.dump(tasks_, add_file, ensure_ascii=False, indent=4)


while True:

    prompt = input('Append in tasks or execute command (help): ')

    if prompt == 'help':
        print('Commands: undo, remake, exit, tasks)')
    elif prompt == 'undo':
        tasks, memory = undo(tasks, memory)
    elif prompt == 'tasks':
        for task in tasks:
            print(task)
    elif prompt == 'remake':
        tasks, memory = remake(tasks, memory)
    elif prompt not in commands:
        save_file(tasks, 'tasks.json')
        tasks.append(str(prompt))
    elif prompt == 'exit':
        save_file(tasks, 'tasks.json')
        exit()


