

# create GUI
import PySimpleGUI as sg



# All the stuff inside your window.
layout = [  [sg.Text('Your Initial Deposit: ')],
            [sg.Text('Enter Your Compound Times'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Compound Calculator', layout)


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()


