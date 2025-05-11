import pygame
# If you try to import a library and it becomes an error, then in the terminal, you must input "pip install (library name)"

pygame.init()#Initialize Pygame

# Creates the main window for your pygame 
screen_width = 100
screen_height = 100
screen = pygame.display.set_mode((screen_width, screen_height))
# Siaplys the name of the game
pygame.display.set_caption("Pong game")
