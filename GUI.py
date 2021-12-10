import PySimpleGUI as sg
from PIL import Image
import io

sg.theme('BlueMono')
armed = False

gif = "out.gif"
enemy = Image.open(gif)
bioE = io.BytesIO()
enemy.save(bioE, format="GIF")
col1 = [[sg.Button('New Enemy')], [sg.Image(key="-IMAGE-")]]

col2 = [[sg.Text('Enemy')],
[sg.Image("EN_FULL.png"),sg.Image("EN_FULL.png"),sg.Image("EN_FULL.png"),sg.Image("EN_EMPTY.png")],
[sg.Text('They reload!')],
[sg.Text('You attack!')],
[sg.Text('They got hit!')],
[sg.Text('You')],
[sg.Image("US_FULL.png"),sg.Image("US_FULL.png"),sg.Image("US_EMPTY.png"),sg.Image("US_EMPTY.png")],
[sg.Button("Reload", key = '-b-')],
[sg.Button('Block')]]

layout = [[sg.Column(col1)], [sg.Column(col2)]]

window = sg.Window('Window Title', layout, finalize = True)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-b-':
        if armed == False:
            window['-b-'].Update("Attack")
            armed = True
        elif armed == True:
            window['-b-'].Update("Reload")
            armed = False
    if event == "New Enemy":
        window["-IMAGE-"].update(data=bioE.getvalue())
    window.Element('-IMAGE-').UpdateAnimation(gif)

window.close()
