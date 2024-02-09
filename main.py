import pygame
import pymunk
import pymunk.pygame_util

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 678

#game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Mountain Top')

#pymunk space
space = pymunk.Space()
static_body = space.static_body
draw_options = pymunk.pygame_util.DrawOptions(screen)

#clock
clock = pygame.time.Clock()
FPS = 120

#colors
BG = (50, 50, 50)

#load images
table_image = pygame.image.load("assets/images/table.png").convert_alpha()

#display pool_balls
def display_ball(radius, position):
    body = pymunk.Body()
    body.position = position
    shape = pymunk.Circle(body, radius)
    shape.mass = 5
    #use pivot joint to add friction
    pivot = pymunk.PivotJoint(static_body, body, (0, 0), (0, 0))
    pivot.max_bias = 0 #disable joint correction
    pivot.max_force = 1000 #emulate linear friction

    space.add(body, shape, pivot)
    return shape

    new_ball = display_ball(25, (300, 200))

    cue_ball = display_ball(20, (200, 400))

# Main game loop
run = True
while run:

    clock.tick(FPS)
    space.step(1 / FPS)

    #fill background
    screen.fill(BG)

    #draw pool table
    screen.blit(table_image, (0, 0))
    
    #events handler
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            cue_ball.body.apply_impulse_at_local_point((-500, 0), (0, 0))
        if event.type == pygame.QUIT:
            run = False
    
    # Update the display
    space.debug_draw(draw_options)
    pygame.display.update()
    

pygame.quit()
