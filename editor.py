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
LIGHT_GRAY = (150, 150, 150)

modes = {"select":WHITE, "coin":YELLOW, "enemy":BLUE, "wall":GRAY}
mode = "select"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The World's Hardest Game")
clock = pygame.time.Clock()     ## For syncing the FPS

toolbar_visible = False
toolbar_button = pygame.Rect(WIDTH - 50,0,50,50)
toolbar_background = pygame.Rect(0,0,WIDTH,100)

running = True
while running:

    # Process input/events
    delta_time = clock.tick(FPS) / 1000    ## will make the loop run at the same speed all the time
    click = False
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = event.button == 1
    

    # Game Logic
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    # Draw/render
    screen.fill(BLACK)
    pygame.draw.rect(screen,GREEN,(0,0,50,HEIGHT))
    pygame.draw.rect(screen,GREEN,(WIDTH - 50,0,50,HEIGHT))
    if toolbar_visible:
        toolbar_visible = toolbar_background.collidepoint(mouse_pos)
        pygame.draw.rect(screen,LIGHT_GRAY,toolbar_background)
        screen_fraction = WIDTH / len(modes)
        i = 0
        for m in modes:
            i += 1
            x_pos = screen_fraction * i - screen_fraction / 2
            if modes[m] == modes[mode]:
                pygame.draw.rect(screen,BLACK,(x_pos - 35,15,70,70))
            mode_rect = pygame.Rect(x_pos - 25,25,50,50)
            pygame.draw.rect(screen,modes[m],mode_rect)
            if mode_rect.collidepoint(mouse_pos) and click:
                mode = m

    else:
        toolbar_visible = toolbar_button.collidepoint(mouse_pos)

        pygame.draw.rect(screen,LIGHT_GRAY,toolbar_button)
    pygame.display.update()