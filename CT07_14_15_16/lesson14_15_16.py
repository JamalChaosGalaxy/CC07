import pygame
# If you try to import a library and it becomes an error, then in the terminal, you must input "pip install (library name)"

pygame.init()#Initialize Pygame

# Creates the main window for your pygame 
screen_width = 800
screen_height = 600
# Siaplys the name of the game

white = (255, 255, 255)


running = True

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong game")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
