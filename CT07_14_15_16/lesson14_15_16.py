import pygame
# If you try to import a library and it becomes an error, then in the terminal, you must input "pip install (library name)"

pygame.init()#Initialize Pygame

# Creates the main window for your pygame 
screen_width = 800
screen_height = 600
# Siaplys the name of the game

white = (255, 255, 255)

paddle_width = 20
paddle_height = 100
paddle1_x = 10
paddle1_y = screen_height // 2 - paddle_height // 2

paddle2_x = screen_width - paddle_width - 10
paddle2_y = screen_height // 2 - paddle_height // 2

running = True

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong game")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_W] and paddle1_y > 0:
        paddle_y = 
    
    pygame.draw.rect(screen, white, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (paddle2_x, paddle2_y, paddle_width, paddle_height))
    pygame.display.flip()

pygame.quit()
