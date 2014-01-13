# starterkit
_A simple Pygame starter kit_

![Starter kit](http://i44.tinypic.com/29zbxar.png)

### Setting up
```
$ git clone https://github.com/alveyworld-dev/starterkit
$ cd starterkit
$ python main.py
```

### Resources
* [Intro to game design](https://docs.google.com/presentation/d/11oSHUDFR2WoMJXsoLWD1vtIr-BZaxDjECcIPFVro8iA/edit?usp=sharing)

### Overview
* `resources/` - Any game resources: fonts, sprites, sounds, music, etc.
* `source/` - Game source code
    - `draw.py` - Handles the `draw()` function
    - `game.py` - Global game variables
    - `graphics.py` - Helpful graphics functions
    - `sprite.py` - Sprite class
    - `update.py` - Handles the `update()` function

### Modifications
There are two main parts of the starter kit that you will want to start your
modifications to.

#### Game loop
The game loop is contained in `main.py`, and simply repeats `update` and `draw`
 until exited.

#### Update
`update` is where you will want to do all your math and basic game logic.
```python
def update():
    """
    Update game world here
    """

    # insert logic here
    
    return
```

#### Draw
`draw` is simply that - drawing the game world.  You should refrain from doing
and logic code in `draw`, use it simply for drawing.
```python
def draw():
    """
    Drawing logic
    """

    # Fill the screen with black
    game.screen.fill((240, 240, 240))
    
    # insert logic here

    # Don't change these
    pygame.display.update()
    pygame.display.flip()

    return
```
Notice that there is some code already in the function: you shouldn't change
these unless you know what you are doing.  Simply insert your own code after
the comment "insert logic here".

### License
```
Copyright 2014 Joshua Beitler, Brandon Bench, Alveyworld

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. 
```