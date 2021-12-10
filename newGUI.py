import PySimpleGUI as sg
from PIL import Image
import io


class GUI():
    def gameScreen():
        sg.theme('Black')
        armed = False
        gif = "out.gif"
        events = ["You get hit!", "You attack!", "You reload!", "You block!", "They get hit!", "They attack!", "They reload!", "They block!"]
        enemy = Image.open(gif)
        bioE = io.BytesIO()
        event = events[0]
        enemy.save(bioE, format="GIF")
        col1 = [[sg.Image(key="-IMAGE-")], [sg.Button('New Enemy')]]
        events = "You get hit"
        col2 = [[sg.Text('Enemy')],
        [sg.Image("EN_FULL.png"),sg.Image("EN_FULL.png"),sg.Image("EN_FULL.png"),sg.Image("EN_EMPTY.png")],
        [sg.Text(event)],
        [sg.Text('You')],
        [sg.Image("US_FULL.png"),sg.Image("US_FULL.png"),sg.Image("US_EMPTY.png"),sg.Image("US_EMPTY.png")],
        [sg.Button("Reload", key = '-b-')],
        [sg.Button('Block')]]

        layout = [[sg.Column(col1)], [sg.Column(col2)]]
        window = sg.Window('Window Title', layout, finalize = True)

        while True:
            event, values = window.read(timeout=100)
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
            window.Element('-IMAGE-').update_animation_no_buffering (gif)

        window.close()



GUI.gameScreen()
