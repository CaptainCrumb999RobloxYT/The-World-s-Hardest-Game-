import pygame

pygame.init()

WIDTH = 850
HEIGHT = 500
TILE_SIZE = 25
TILE_COUNT_X = WIDTH // TILE_SIZE
TILE_COUNT_Y = HEIGHT // TILE_SIZE
FPS = 60

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
MEDIUM_RED = (184, 0, 0)
DARK_RED = (127, 0, 0)
GREEN = (0, 255, 0)
MEDIUM_GREEN = (0, 184, 0)
DARK_GREEN = (0, 127, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)
LIGHT_GRAY = (150, 150, 150)

modes = {"select":WHITE, "coin":YELLOW, "enemy":BLUE, "wall":GRAY, "eraser":WHITE}
mode = "select"
selected = None
patrolpoint_mode = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The World's Hardest Game")
clock = pygame.time.Clock()     ## For syncing the FPS

tiles = [[None] * TILE_COUNT_Y for _ in range(TILE_COUNT_X)]

def get_nearest_grid_square(pos):
    pos /= TILE_SIZE
    pos.x = round(pos.x)
    pos.y = round(pos.y)
    return pos * TILE_SIZE

toolbar_visible = False
toolbar_button = pygame.Rect(WIDTH - 50,0,50,50)
toolbar_background = pygame.Rect(0,0,WIDTH,100)
sidebar_left = pygame.Rect(0,0,50,HEIGHT)
sidebar_right = pygame.Rect(WIDTH - 50,0,50,HEIGHT)
add_patrolpoint_button = pygame.Rect(0,HEIGHT - 100,50,50)
remove_patrolpoint_button = pygame.Rect(0,HEIGHT - 50,50,50)

class Tile:
    def __init__(self, position, type):
        self.pos = position
        self.type = type
    def draw(self):
        pygame.draw.rect(screen, modes[self.type], (self.pos.x, self.pos.y, TILE_SIZE,TILE_SIZE))

class Enemy(Tile):
    def __init__(self, position):
        super().__init__(position, "enemy")
        self.patrolpoints = []
    def add_patrolpoints(self, pos):
        self.patrolpoints.append(pos)

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
    mouse_vector = pygame.Vector2(mouse_pos[0],mouse_pos[1])

    # Draw/render
    screen.fill(BLACK)
    pygame.draw.rect(screen,GREEN,sidebar_left)
    pygame.draw.rect(screen,GREEN,sidebar_right)

    for column in tiles:
        for tile in column:
            if not tile:
                continue
            tile.draw()

    if mode != "select":
        selected = None

    gridpos = get_nearest_grid_square(mouse_vector - pygame.Vector2(TILE_SIZE // 2))
    if not (sidebar_left.collidepoint(mouse_pos) or sidebar_right.collidepoint(mouse_pos) or toolbar_visible):
        if mode != "select":
            pygame.draw.rect(screen,modes[mode],(gridpos.x,gridpos.y,TILE_SIZE,TILE_SIZE))
        if click:
            tile_x = int(gridpos.x / TILE_SIZE)
            tile_y = int(gridpos.y / TILE_SIZE)
            if mode == "eraser":
                tiles[tile_x][tile_y] = None
            elif mode == "enemy":
                tiles[tile_x][tile_y] = Enemy(gridpos)
            elif mode == "select":
                selected = tiles[tile_x][tile_y]
            else:
                tiles[tile_x][tile_y] = Tile(gridpos,mode)

    if toolbar_visible:
        toolbar_visible = toolbar_background.collidepoint(mouse_pos)
        pygame.draw.rect(screen,LIGHT_GRAY,toolbar_background)
        screen_fraction = WIDTH / len(modes)
        i = 0
        for m in modes:
            i += 1
            x_pos = screen_fraction * i - screen_fraction / 2
            if m == mode:
                pygame.draw.rect(screen,BLACK,(x_pos - 35,15,70,70))
            mode_rect = pygame.Rect(x_pos - 25,25,50,50)
            pygame.draw.rect(screen,modes[m],mode_rect)
            if mode_rect.collidepoint(mouse_pos) and click:
                mode = m

    else:
        toolbar_visible = toolbar_button.collidepoint(mouse_pos)
        pygame.draw.rect(screen,LIGHT_GRAY,toolbar_button)

    if isinstance(selected, Enemy):
        pygame.draw.rect(screen, DARK_GREEN, add_patrolpoint_button)
        pygame.draw.rect(screen, DARK_RED, remove_patrolpoint_button)
    
    pygame.display.update()