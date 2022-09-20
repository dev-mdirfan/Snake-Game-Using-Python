# importing pygame
import pygame
# Initializing pygame module
pygame.init()
# print(x)

# Creating Window
gameWindow = pygame.display.set_mode((1200, 500))

# Setting title of the game
pygame.display.set_caption("My First Game: Flappy Bird")

# Game Specific Variables
exit_game = False
game_over = False

# Creating a Game Loop
while not exit_game:
    # Captures the events
    # Every event like movement or any key press all you can see in printing event :
    for event in pygame.event.get():
        # print(event)

        # Handling Exit Event
        # Checking if user click on close window or not if yes
        if event.type == pygame.QUIT:
            # Then we set the exit_game True so that we exit from game window
            exit_game = True

        # Checking Any Key pressed or not
        if event.type == pygame.KEYDOWN:
            # Checking which key is pressed
            if event.key == pygame.K_RIGHT:
                # Giving the output
                print("You have pressed right arrow key")



# To quite the game
pygame.quit()
quit()

