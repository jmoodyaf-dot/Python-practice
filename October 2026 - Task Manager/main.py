def show_menu():

    print('=' * 20)
    print(' '* 6 + 'QUESTLOG' + ' '*6)
    print('=' * 20)
    print('1. View Tasks')
    print('2. Add Task')
    print('3. Complete Task')
    print('4. Delete Task')
    print('5. Exit')

def add_task():
    pass
def view_task():
    pass
def complete_task():
    pass
def delete_task():
    pass
def save(file: str, tasks: dict):
    pass
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
        show_menu()
        action = input('Choose an Option: ')

        match action:
            case '1':
                view_task()
            case '2':
                add_task(tasks)
            case '3':
                complete_task()
            case '4':
                delete_task()
            case '5':
                save("tasks.txt", tasks)
                break
            case _:
                print('')
                print('Invalid Input')
                print('')

                

questlog()     