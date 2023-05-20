def get_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos


while True:
    user_action = input('Type add, show, edit, complete or exit: ')

    match user_action:
        case 'add':
            what_add = input('Enter s todo: ') + '\n'

            todos = get_todos()

            todos.append(what_add)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':

            todos = get_todos()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f'{index + 1}.{item}'
                print(row)

        case 'edit':
            number = int(input('Write a number to edit: '))
            number = number - 1

            todos = get_todos()

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input('Write a number to delete: '))

            todos = get_todos()

            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f'Todo {todo_to_remove} was removed from the list.'
            print(message)
        case 'exit':
            break
print('Bye!')









