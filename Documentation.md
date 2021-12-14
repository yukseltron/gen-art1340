# Documentation

## Table of Contents
```Python
• Game.py
• GenerateArt.py
• GenerateText.py
• RNGHash.py
• Other Resources
```


# Game.py
This file contains 3 Classes: `Enemy`,  `Player`, `GameScreen`.<br/>
Starting with `Enemy`:

## Class Enemy
### Function: `__init__()`
Initializes an `Enemy` instance to keep track of enemy instance data.
#### Arguments
None
#### Returns
None

<br/>

### Function: `rabdomName()`
Gets a random name for `Enemy` instance.
#### Arguments
None
#### Returns
`name`: type str, the number of rows <br/>

<br/>

## Class Player
### Function: `__init__()`
Initializes a `Player` instance to keep track of player data.
#### Arguments
None
#### Returns
None

<br/>

## Class Game
### Function: `__init__()`
Initializes the game instance for starting the game.
#### Arguments
None
#### Returns
None

<br/>

### Function: `reset()`
Resets the game screen, used to generate the next enemy and starting the game.
#### Arguments
None
#### Returns
None

<br/>

### Function: `healthBar(character, health)`
Updates the healthbar visuals on the GUI.
#### Arguments
`character`: type str, one of "US" (user) or "EN" (enemy) <br/>
`health`: type int, number of health bars to fill <br/>
#### Returns
`data`: type Object, healthbar simple GUI.

<br/>

### Function: `loop()`
The logic behind the main game loop.
#### Arguments
None
#### Returns
None

<br/>

### Function: `playerAction(event)`
Interprets the user action into a move.
#### Arguments
`event`: type str, the user action on the simple GUI
#### Returns
None

<br/>

### Function: `enemyAction()`
Decides and performs on the enemy action (attack/reload, block)
#### Arguments
None
#### Returns
None

<br/>

### Function: `playerHit()`
Logic for what happens when a player is damaged, including logic for game over.
#### Arguments
None
#### Returns
None

<br/>

### Function: `enemyHit()`
Logic for what happens when an enemy is damaged, including logic for defeating the enemy.
#### Arguments
None
#### Returns
None

<br/>

### Function: `bothHit()`
Logic for what happens when the player and the enemy both attack at the same time.
#### Arguments
None
#### Returns
None

### Function: `contest(event)`
Taking into consideration player and enemy moves, interprets the outcome.
#### Arguments
`event`: type str, the user action on the simple GUI
#### Returns
None

<br/>

# GenerateArt.py
This file contains 7 functions for randomly generating the enemy and its art.

### Function: `changeSeedWindow()`
The window for changing the file parsed for setting the random seed in art generation.
#### Arguments
None
#### Returns
None

<br/>

### Function: `random_color()`
The window for changing the file parsed for setting the random seed in art generation.
#### Arguments
None
#### Returns
`()`: type tuple, the randomly generated RGB tuple.

<br/>

### Function: `interpolate(start_color, end_color, factor)`
Blends all colours used nicely.
#### Arguments
`start_color`: type tuple, random color tuple from random_color(). <br/>
`end_color`: type tuple, random color tuple from random_color(). <br/>
`factor`: type float, factor for interpolation. <br/>
#### Returns
`()`: type tuple, the interpolated colour.

<br/>

### Function: `convertImage(path)`
Makes the black background of an image transparent.
#### Arguments
`path`: type str, path of target image. <br/>
#### Returns
None

<br/>

### Function: `generate_art(path, target_size_px, scale_factor, lines, start_color, end_color)`
Makes the black background of an image transparent.
#### Arguments
`path`: type str, path of target image. <br/>
`target_size`: type int, intended size of the generated image. <br/>
`scale_factor`: type int, intended scale of the generated image. <br/>
`lines`: type int, intended number of lines <br/>
`start_color`: type tuple, random color tuple from random_color(). <br/>
`end_color`: type tuple, random color tuple from random_color(). <br/>
#### Returns
None

<br/>

### Function: `createGIF(images)`
Turns a set of images into an animated GIF.
#### Arguments
`images`: type [], list of image paths for turning into a GIF. <br/>
#### Returns
None

<br/>

### Function: `start_generator(num)`
Starts the random art generation to create the enemy GIF appearance.
#### Arguments
`num`: type int, number of images to use in the GIF. <br/>
#### Returns
None

<br/>

# GenerateText.py
This file contains 4 lists, one for nouns, one for verbs, one for adjectives, and one for adverbs. There is 1 function, which uses these lists to generate a random sentence in English.

### Function: `getRandText()`
Generates a random text in the structure of adjective + noun + verb + adverb.
#### Arguments
None
#### Returns
`String`: type str, random text generated. <br/>

<br/>

# RNGHash.py
This file contains a hash function that is used to create a random seed from a given input file.

### Function: `getRandText(filename)`
Parsing a given file, the file's contents is used for generating the random hash seed.
#### Arguments
`filename`: type str, path of specified file for seeding. <br/>
#### Returns
`int`: type int, randomly generated hash number. <br/>

<br/>

# Other resources
This project also relies on these assets for its GUI.

### File: `EN_EMPTY.png`
Empty enemy health rectangle

### File: `EN_FULL.png`
Full enemy health rectangle

### File: `US_EMPTY.png`
Player enemy health rectangle

### File: `US_FULL.png`
Player enemy health rectangle

### File: `out.gif`
The reused gif for storing the enemy appearance. One is used at a time.
