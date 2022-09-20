# Flappy Bird
- Flappy Bird using Pygame

### Installation Guide :

- Install pygame using cmd -

```py
pip install pygame
```

- Check version of Pygame - By entering REPL of Python

```py
python
import pygame
```

## [Basic Concepts](./1-Basic-Concept.py)

### 1. Creating Window :
- Whenever you import the pygame you have to initialize the pygame

```py
import pygame
x = pygame.init()
print(x)
```
- Output: (5, 0)

#### Creating Game Window - To display the screen by size (width, height)
```py
# Creating Window
gameWindow = pygame.display.set_mode((1200, 500))
```

### 2. How to set title of the Game :

```py
pygame.display.set_caption("My First Game: Flappy Bird")
```

### 3. Creating the Game Loop & Variables :

```py
# Game Specific Variables
exit_game = False
game_over = False

while not exit_game:
    # It is a infinite loop so this may hang your device (Laptop)
    pass
```

#### To quite the game call quite() function

```py
# To quite the game
pygame.quit()
quit()
```

### 4. Handling Event :

```py
# Every event like movement or any key press all you can see in printing event :
for event in pygame.event.get():
    print(event)
```

### 5. Handling Event Types and Key Press :

- To handle exit game event -
```py
# Checking if user click on close window or not if yes
if event.type == pygame.QUIT:
    # Then we set the exit_game True so that we exit from game window
    exit_game =True
```

- To handle key event -
```py
# Checking Any Key pressed or not
if event.type == pygame.KEYDOWN:
    # Checking which key is pressed
    if event.key == pygame.K_RIGHT:
        # Giving the output
        print("You have Pressed right arrow key")
```



# [Snake Game]()

- ***Full Source Code :*** [Python Snake Game]()

1. **Display:** First you need to understand what we require for the game like width and height of the game window
2. **Movement:** Snake will have set position in x and y direction and velocity in x and y direction (in both +ve & -ve)
3. **Game Over:** At collision on end of the game window or On reaching at the end of the window snake go on opposite position.
4. **Score:** On every user completion task we have to increase and display the score
5. **Food:** We need to create Rectangle food for snake. If the food position and snake position are same we have to reset food position and update the score.
6. **Snake Length:** We have to increase the length of the snake at every collision with food.


### 1. 