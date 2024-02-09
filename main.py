import pygame

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 678

#game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Mountain Top')

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update the display
    pygame.display.update()

pygame.quit()
