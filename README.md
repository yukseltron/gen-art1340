# Shotgun Art Game
![out](https://user-images.githubusercontent.com/14843458/145906783-8a8322ca-afe9-4847-b321-45db912e5954.gif)

## Description
This is a generative art project turned into a game. The generative art (an example is above) is made randomly using a random seed that is chosen through applying hash function to an input file. The file is parsed and hashed into a random number. This determines the colors of the image, the direction of the lines, the shapes, etc. As for the game part, we chose to use these randomly generated images as enemies for the player to combat. We chose to implement the simple ["shotgun" children's game](https://www.wikihow.com/Play-the-Shotgun-Game) as it is a simple enough game to implement our generate art project. The game has only three inputs for the user: Attack, Reload, or Block. The player's score is tracked, with a bonus gained for defeating an enemy. But, players must also be wary of their own health as well. Players try to defeat as many enemies as they can and get as high of score as possible.

#### Gameplay Preview
![g](https://user-images.githubusercontent.com/14843458/145907286-c17d8cf0-395d-48c1-81fb-14bf46611bf9.gif)

## Execution instructions

### Installations
This program relies on two Python libraries: PySimpleGUI and Pillow.

#### Installing PySimpleGUI
`pip install PySimpleGUI`

#### Installing Pillow
`pip install Pillow`

#### Starting the project
```Python
import Game

g = Game.GameScreen()
```

## Game rules
### Combat
You and your opponent both choose at the same time whether to attack/reload, or block.<br/>
You need to first reload in order to be able to attack.<br/>
Attack allows you to injure your enemy. Injuring them 4 times defeats them.<br/>
Block allows you to prevent getting hit by an attack. Your opponent can block too. <br/>

### Enemy Generation Features
```
• Randomly generated image (body and eyes) as gif<br/>
• Randomly generated name<br/>
• Randomly generated quote<br/>
• Randomly generated colours<br/>
• Randomly generated blocking tendency<br/>
```
