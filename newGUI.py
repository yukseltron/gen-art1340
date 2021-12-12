import PySimpleGUI as sg
import random
from PIL import Image
import io

class Enemy():
    def __init__(self, path):
        self.health = 4
        self.path = path
        self.armed = False
        self.block_tedency = 4
        self.block = False;

class Player():
    def __init__(self):
        self.health = 4
        self.armed = False
        self.block = False;

class GameScreen():
    def __init__(self):
        sg.theme('Black')
        self.events = ("You get hit!", "You attack!", "You reload!", "You block!", "They get hit!", "They attack!", "They reload!", "They block!")
        self.col1 = [[sg.Image(key = "-IMAGE-")], [sg.Button('New Enemy', disabled=True)]]
        self.col2 = [[sg.Text('Enemy')],
        [sg.Text(self.events[0], key = '-event-')],
        [sg.Text('You')],
        [sg.Button("Reload", key = '-action-')],
        [sg.Button('Block', key = '-block-')]]
        self.layout = [[sg.Column(self.col1)], [sg.Column(self.col2)]]
        self.window = sg.Window('Window Title', self.layout, finalize = True)
        self.player = Player()
        self.enemy = Enemy("out.gif")
        self.healthBar("EN",4),
        self.healthBar("US",4),
        self.loop()

    def healthBar(self, character, health):
        data = []
        for i in range(4):
            if i < health:
                data.append(sg.Image(character+"_FULL.png"))
            else:
                data.append(sg.Image(character+"_EMPTY.png"))
        return data

    def loop(self):
        while True:
            event, values = self.window.read(timeout = 100)
            if event == sg.WIN_CLOSED:
                break
            else:
                self.playerAction(event)
                self.enemyAction()
                #self.contest()
            self.window.Element('-IMAGE-').update_animation_no_buffering(self.enemy.path)

        window.close()

    def playerAction(self, event):
        if event == '-action-':
            self.player.block = False
            if self.player.armed == False:
                self.window['-action-'].Update("Attack")
                self.window['-event-'].Update(self.events[2])
                self.player.armed = True
            elif self.player.armed == True:
                self.window['-action-'].Update("Reload")
                self.window['-event-'].Update(self.events[1])
                self.player.armed = False
        elif event == '-block-':
            self.player.block = True


    def enemyAction(self):
        action = random.randrange(self.enemy.block_tedency)
        if action == self.enemy.block_tedency:
            self.window['-event-'].Update(self.events[7])
            self.enemy.block = True
        else:
            self.enemy.block = False
            if self.enemy.armed == False:
                self.window['-event-'].Update(self.events[6])
                self.enemy.armed = True
            else:
                self.window['-event-'].Update(self.events[5])
                self.enemy.armed = True


g = GameScreen()
