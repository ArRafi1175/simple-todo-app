import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()                                   #remove white spaces

    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            item=item.title()                   #uppercase
            print(f"{index + 1}. {item}")
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter the new todo: ") + "\n"
            todos[number] = new_todo

            functions.write_todos(todos)

        except ValueError:
            print("Your command is invalid. Please enter a Number")
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            print(f"*{todos[number - 1].strip('\n')}* has marked completed and removed from the list")
            todos.pop(number - 1)

            functions.write_todos(todos)
        except (ValueError, IndexError):
            print("Your command is invalid. Please enter a Valid number from the tasks")
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is invalid")

print("Bye!")