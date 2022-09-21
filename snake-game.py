# importing pygame
import pygame
import random
# initializing as this is a pygame
pygame.init()

# Defining colors -
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)


# defining screen size
screen_width = 900
screen_height = 600

# Creating game display window
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Setting game's title
pygame.display.set_caption("Snake Game Developed By Irfan")
# To see the changes we have to update
pygame.display.update()

# Initializing variables -
exit_game = False
game_over = False
# Snake position variable
snake_x = 45
snake_y = 45
velocity_x = 0
velocity_y = 0
snake_size = 10
fps = 30
score = 0

# Food position variable
food_x = random.randint(10, screen_width-10)
food_y = random.randint(10, screen_height-10)

# Making clock for updating frame
clock = pygame.time.Clock()

# Defining Game Loop -
while not exit_game:
    # Handling event
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            exit_game = True

        # Handling event Key press
        if event.type == pygame.KEYDOWN:
            # right key in +ve x direction
            if event.key == pygame.K_RIGHT:
                velocity_x = 10
                velocity_y = 0

            # left key in -ve x direction
            if event.key == pygame.K_LEFT:
                velocity_x = -10
                velocity_y = 0

            # up key in +ve y direction
            if event.key == pygame.K_UP:
                velocity_y = -10
                velocity_x = 0

            # right key in -ve y direction
            if event.key == pygame.K_DOWN:
                velocity_y = 10
                velocity_x = 0
    
    # Setting Velocity in x direction
    snake_x += velocity_x
    # Setting Velocity in y direction
    snake_y += velocity_y

    # Setting background color -
    gameWindow.fill(white)
    # Displaying Food after white background display
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
    # To make snake head rectangle -
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    # To reflect the change or update the screen
    pygame.display.update()
    # every frame it updates
    clock.tick(fps)


# To quite the game
pygame.quit()
quit()