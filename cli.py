from modules import functions
import time

time_now = time.strftime("%b %d, %Y %H:%M:%S")
print(time_now)

user_prompt = "add, edit, show, complete or exit: "

while True:
    user_action = input(user_prompt)
    user_action = user_action.capitalize().strip()

    if user_action.startswith('Add'):
        todo = user_action[4:].capitalize() + "\n"
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif user_action.startswith('Show'):
        todos = functions.get_todos()
        for i, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{i+1}-{item}")

    elif user_action.startswith('Edit'):
        try:
            index = int(user_action[5:])
            todos = functions.get_todos()
            edited = input("Enter New Task : ") + "\n"
            todos[index-1] = edited
            functions.write_todos(todos)

        except ValueError:
            print("Command Not Valid!")
            continue

    elif user_action.startswith('Complete'):
        try:
            index = int(user_action[9:])
            todos = functions.get_todos()
            todo_completed = todos[index-1].strip("\n")
            todos.pop(index-1)
            functions.write_todos(todos)
            message = f"Todo {todo_completed} has been Removed!"
            print(message)

        except IndexError:
            print("Index out of Range!")
            continue

    elif user_action.startswith('Exit'):
        break

    else:
        print("Wrong Input!")

print("Bye!")
