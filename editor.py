import pygame

pygame.init()

WIDTH = 854
HEIGHT = 480
FPS = 60

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)

modes = {"select":WHITE, "coin":YELLOW, "enemy":BLUE, "wall":GRAY}
mode = "select"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The World's Hardest Game")
clock = pygame.time.Clock()     ## For syncing the FPS

running = True
while running:

    # Process input/events
    delta_time = clock.tick(FPS) / 1000    ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False
    

    # Game Logic
    keys = pygame.key.get_pressed()

    # Draw/render
    screen.fill(BLACK)
    pygame.draw.rect(screen,GREEN,(0,0,50,HEIGHT))
    pygame.draw.rect(screen,GREEN,(WIDTH - 50,0,50,HEIGHT))
    pygame.display.update()