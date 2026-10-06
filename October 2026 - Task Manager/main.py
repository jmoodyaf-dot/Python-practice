def show_menu():

    print('=' * 20)
    print(' '* 6 + 'QUESTLOG' + ' '*6)
    print('=' * 20)
    print('1. View Tasks')
    print('2. Add Task')
    print('3. Complete Task')
    print('4. Delete Task')
    print('5. Exit')

def add_task(tasks: dict):
    task = input('What is your task? ')
    tasks[task] = 'Incomplete'
    print('Task added')

def view_task(tasks: dict):
    tsk_cnt = 1
    for key, value in tasks.items():
        print(f'{tsk_cnt}. {key}: {value}')
        tsk_cnt +=1

def complete_task(tasks: dict):
    task_list = list(tasks.keys())
    task_idx = int(input("Enter number of completed task: ")) -1
    comp_task = task_list[task_idx]
    tasks[comp_task] = "Complete"

def delete_task(tasks: dict):
    task_list = list(tasks.keys())
    task_idx = int(input("Enter the number of the task to be deleted: ")) -1
    del_task = task_list[task_idx]
    tasks.pop(del_task)

def save(doc: str, tasks: dict):

    with open(doc, 'w') as file:
        for key, value in tasks.items():
            file.write(key + ': ' + value + '\n')

def load(doc: str, tasks: dict):
    
    with open(doc, "r") as file:
        for line in file:

            if not line.strip():
                continue

            key, value = line.strip().split(":", 1)
            tasks[key.strip()] = value.strip()

def questlog():
    tasks = {}
    load("tasks.txt", tasks)
    while True:
        print('-' * 30)
        show_menu()
        action = input('Choose an Option: ')

        match action:
            case '1':
                view_task(tasks)
            case '2':
                add_task(tasks)
            case '3':
                complete_task(tasks)
            case '4':
                delete_task(tasks)
            case '5':
                save("tasks.txt", tasks)
                break
            case _:
                print('')
                print('Invalid Input')
                print('')

                

questlog()     