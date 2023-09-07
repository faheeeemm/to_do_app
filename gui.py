from modules import functions

import PySimpleGUI as sg
#sg.theme('DarkAmber')

label = sg.Text("Type in a To Do : ")
input_box = sg.InputText(tooltip="Enter To Do here")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout = [[label],[input_box,add_button]])

window.read()
window.close()