import PySimpleGUI as sg
from PIL import Image
import io


class Enemy():
    def __init__(self, path):
        self.health = 4
        self.path = path

def healthBar(character, health):
    data = []
    for i in range(4):
        if i < health:
            data.append(sg.Image(character+"_FULL.png"))
        else:
            data.append(sg.Image(character+"_EMPTY.png"))
    return data

def gameScreen():
    sg.theme('Black')
    armed = False
    events = ("You get hit!", "You attack!", "You reload!", "You block!", "They get hit!", "They attack!", "They reload!", "They block!")
    e = Enemy("out.gif")
    enemy = Image.open(e.path)
    bioE = io.BytesIO()
    enemy.save(bioE, format = "GIF")
    col1 = [[sg.Image(key = "-IMAGE-")], [sg.Button('New Enemy')]]
    col2 = [[sg.Text('Enemy')],
    healthBar("EN",4),
    [sg.Text(events[0], key = '-event-')],
    [sg.Text('You')],
    healthBar("US",4),
    [sg.Button("Reload", key = '-action-')],
    [sg.Button('Block', key = '-block-')]]

    layout = [[sg.Column(col1)], [sg.Column(col2)]]
    window = sg.Window('Window Title', layout, finalize = True)

    while True:
        event, values = window.read(timeout=100)
        if event == sg.WIN_CLOSED:
            break
        if event == '-action-':
            if armed == False:
                window['-action-'].Update("Attack")
                armed = True
            elif armed == True:
                window['-action-'].Update("Reload")
                armed = False
        if event == "New Enemy":
            window["-IMAGE-"].update(data=bioE.getvalue())
        window.Element('-IMAGE-').update_animation_no_buffering(e.path)

    window.close()



gameScreen()
