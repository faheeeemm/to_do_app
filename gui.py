from modules import functions
import PySimpleGUI as sg
import os
if not os.path.exists(functions.FILEPATH):
    with open(functions.FILEPATH,'w') as file:
        pass

app_label = sg.Text("Type in a To Do : ")
input_box = sg.InputText(tooltip="Enter To Do here", key ='todo')
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

list_box = sg.Listbox(values= functions.get_todos(),
                      key ='todos',
                      enable_events=True, size=[45, 10])

window = sg.Window("My To-Do App",
                   layout=[[app_label],
                           [input_box, add_button],
                           [list_box,edit_button,complete_button],
                           [exit_button]],
                   font=('Helvetica', 10)
                   )

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index]=new_todo
                functions.write_todos(todos)
                window['todos'].update(values = todos)
            except IndexError:
                sg.popup("Please select a To-Do",
                         font=('Helvetica', 10))
        case "todos":
            window['todo'].update(value = values["todos"][0])
        case "Complete":
            try:
                todo_completed = values['todo']
                todos = functions.get_todos()
                todos.remove(todo_completed)
                functions.write_todos(todos)
                window['todos'].update(values = todos)
                window['todo'].update(value="")
            except ValueError:
                sg.popup("Please select a To-Do",
                         font=('Helvetica', 10))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
