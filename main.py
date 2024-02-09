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

#game variables
dia = 36

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
    shape.elasticity = 0.8
    #use pivot joint to add friction
    pivot = pymunk.PivotJoint(static_body, body, (0, 0), (0, 0))
    pivot.max_bias = 0 #disable joint correction
    pivot.max_force = 1000 #emulate linear friction

    space.add(body, shape, pivot)
    return shape

#setting game balls
balls = []
rows = 5
#potting balls
for col in range(5):
    for row in range(rows):
        pos = (250 + (col * dia), 267 + (row* dia))
        new_ball = display_ball(dia / 2, pos)
        balls.append(new_ball)
    rows -= 1
#cue ball
pos = (888, SCREEN_HEIGHT / 2)
cue_ball = display_ball(dia / 2, pos)
balls.append(cue_ball)

#create pool cushions
cushions = [
  [(88, 56), (109, 77), (555, 77), (564, 56)],
  [(621, 56), (630, 77), (1081, 77), (1102, 56)],
  [(89, 621), (110, 600),(556, 600), (564, 621)],
  [(622, 621), (630, 600), (1081, 600), (1102, 621)],
  [(56, 96), (77, 117), (77, 560), (56, 581)],
  [(1143, 96), (1122, 117), (1122, 560), (1143, 581)]
]

#function for creating cushions
def create_cushion(poly_dims):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = ((0, 0))
    shape = pymunk.Poly(body, poly_dims)
shape.elasticity = 0.8
    
    space.add(body, shape)

for c in cushions:
    create_cushion(c)

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
