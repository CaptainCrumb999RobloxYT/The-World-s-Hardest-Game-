import tkinter
import tkinter.filedialog
import pygame
from buildxml import build_level
from loadxml import parse_xml
from tkinter.colorchooser import askcolor
pygame.init()
        # level_name_image = font.render(level_name + "|", True, WHITE, GRAY)
WIDTH = 850
HEIGHT = 500
TILE_SIZE = 25
TILE_SIZE_HALF = TILE_SIZE / 2
TILE_COUNT_X = WIDTH // TILE_SIZE
TILE_COUNT_Y = HEIGHT // TILE_SIZE
FPS = 60

def prompt_file():
    """Create a Tk file dialog and cleanup when finished"""
    top = tkinter.Tk()
    top.withdraw()  # hide window
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    top.destroy()
    return file_name

def prompt_save():
    """Create a Tk file dialog and cleanup when finished"""
    top = tkinter.Tk()
    top.withdraw()  # hide window
    files = [("xml","*.xml")]
    file_name = tkinter.filedialog.asksaveasfile(parent=top,filetypes=files,defaultextension=files)
    top.destroy()
    return file_name

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
PURPLE = (75, 0, 150)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)
LIGHT_GRAY = (150, 150, 150)

modes = {"select":WHITE, "coin":YELLOW, "enemy":BLUE, "wall":GRAY, "player":RED, "eraser":WHITE, "save":PURPLE}
mode = "select"
selected = None
patrolpoint_mode = 0
player_pos = None
level_name = ""
font = pygame.font.Font(None, 60) 
wall_color = GRAY

def new():
    global tiles
    tiles = [[None] * TILE_COUNT_Y for _ in range(TILE_COUNT_X)]
def openf():
    global player_pos
    global tiles
    tkinter.messagebox.showwarning('Warning', 'This will Overwrite the Save Data.')
    tiles = [[None] * TILE_COUNT_Y for _ in range(TILE_COUNT_X)]
    file = prompt_file()
    if file == '':
        return
    level = parse_xml(file)
    player_pos = level["player_position"]
    enemies = level["enemies"]
    for enemy in enemies:
        patrol_point = enemy["patrolPoints"][0]
        tiles[int(patrol_point.x) // TILE_SIZE][int(patrol_point.y) // TILE_SIZE] = Enemy(patrol_point)
    walls = level["walls"]
    for wall in walls:
        patrol_point = wall["patrolPoints"][0]
        tiles[int(patrol_point.x) // TILE_SIZE][int(patrol_point.y) // TILE_SIZE] = Wall(patrol_point,wall["wallColor"])
    coins = level["coins"]
    for coin in coins:
        patrol_point = coin["patrolPoints"][0]
        tiles[int(patrol_point.x) // TILE_SIZE][int(patrol_point.y) // TILE_SIZE] = Tile(patrol_point,"coin")
    print(file)
def save():
    if player_pos is None:
        tkinter.messagebox.showwarning('Failed to Save', 'Please put in a Player Block (Red Block)')
        return
    file = prompt_save()
    export_enemies = []
    export_coins = []
    export_walls = []
    for column in tiles:
        for tile in column:
            if not isinstance(tile, Tile): continue
            if tile.type == "enemy":
                tile.patrolpoints.insert(0, tile.pos)
                export_enemies.append(tile)
            elif tile.type == "coin": export_coins.append(tile)
            elif tile.type == "wall": export_walls.append(tile)
    build_level(player_pos,export_enemies,export_coins,export_walls,file)
    print(file)

options = {"new":new, "open":openf, "save":save}

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
save_button = pygame.Rect(WIDTH - 50,50,50,50)
options_editor = False

options_button = pygame.Rect(WIDTH - 50,HEIGHT - 50,50,50)
options_background = pygame.Rect(0,HEIGHT-50,WIDTH,100)

class Tile:
    def __init__(self, position, type,):
        self.pos = position
        self.type = type
        # if self.type == "wall":
    def draw(self):
        pygame.draw.rect(screen, modes[self.type], (self.pos.x, self.pos.y, TILE_SIZE,TILE_SIZE))

class Enemy(Tile):
    def __init__(self, position):
        super().__init__(position, "enemy")
        self.patrolpoints = []
    def add_patrolpoint(self, pos):
        if pos in self.patrolpoints: return
        self.patrolpoints.append(pos)
    def remove_patrolpoint(self, pos):
        if not pos in self.patrolpoints: return
        self.patrolpoints.remove(pos)
    def draw_patrolpoints(self):
        center_offset = pygame.Vector2(TILE_SIZE_HALF, TILE_SIZE_HALF)
        last_point = self.pos + center_offset
        for point in self.patrolpoints:
            center = point + center_offset
            if last_point: pygame.draw.line(screen, WHITE, center, last_point, 2)
            last_point = center
            pygame.draw.circle(screen, WHITE, center, TILE_SIZE_HALF)
        
class Wall(Tile):
    def __init__(self, position, color):
        super().__init__(position, "wall")
        self.color = color
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.pos.x, self.pos.y, TILE_SIZE,TILE_SIZE))
running = True
while running:

    # Process input/events
    delta_time = clock.tick(FPS) / 1000    ## will make the loop run at the same speed all the time
    click = False
    right_click = False
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.KEYDOWN and mode == "save":
            key = event.unicode
            if key.isalpha() or key == " ":
                level_name += key
            elif key == "\b":
                level_name = level_name[:-1]
            if len(level_name) > 20:
                print(level_name)
                # level_name = level_name[:20]
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = event.button == 1
            right_click = event.button == 3

    

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

    is_enemy = isinstance(selected, Enemy)
    if is_enemy: selected.draw_patrolpoints()


    gridpos = get_nearest_grid_square(mouse_vector - pygame.Vector2(TILE_SIZE // 2))
    if not (sidebar_left.collidepoint(mouse_pos) or sidebar_right.collidepoint(mouse_pos) or toolbar_visible):
        if mode != "select" and mode != "save":
            pygame.draw.rect(screen,modes[mode],(gridpos.x,gridpos.y,TILE_SIZE,TILE_SIZE))
        if click:
            tile_x = int(gridpos.x / TILE_SIZE)
            tile_y = int(gridpos.y / TILE_SIZE)
            if mode == "player":
                if not tiles[tile_x][tile_y]:
                    player_pos = gridpos
            elif mode == "eraser":
                if gridpos == player_pos:
                    player_pos = None
                tiles[tile_x][tile_y] = None
            elif mode == "enemy":
                if not gridpos == player_pos:
                    tiles[tile_x][tile_y] = Enemy(gridpos)
            elif mode == "select":
                if patrolpoint_mode != 0:
                    if patrolpoint_mode > 0:
                        selected.add_patrolpoint(gridpos)
                    else:
                        selected.remove_patrolpoint(gridpos)
                else:
                    selected = tiles[tile_x][tile_y]
            elif mode == "wall":
                if not gridpos == player_pos:
                    tiles[tile_x][tile_y] = Wall(gridpos, wall_color)
            elif mode == "save":
                pass
            elif not gridpos == player_pos:
                tiles[tile_x][tile_y] = Tile(gridpos,mode)

    if player_pos:
        pygame.draw.rect(screen, modes["player"], (player_pos.x, player_pos.y, TILE_SIZE, TILE_SIZE))
    
    if mode == "save":
        pygame.draw.rect(screen, PURPLE, save_button)
        level_name_image = font.render(level_name + "|", True, WHITE, GRAY)
        screen.blit(level_name_image, (100, 100))
        if not toolbar_visible and save_button.collidepoint(mouse_pos) and click and player_pos:
            export_enemies = []
            export_coins = []
            export_walls = []
            for column in tiles:
                for tile in column:
                    if not isinstance(tile, Tile): continue
                    if tile.type == "enemy":
                        tile.patrolpoints.insert(0, tile.pos)
                        export_enemies.append(tile)
                    elif tile.type == "coin": export_coins.append(tile)
                    elif tile.type == "wall": export_walls.append(tile)
            # build_level(player_pos, export_enemies, export_coins, export_walls, "test.xml")
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
            if mode_rect.collidepoint(mouse_pos) and right_click:
                if m == "wall":
                    colors = askcolor(title="Color")
                    print(colors[0])
                    wall_color = colors[0]

    else:
        toolbar_visible = toolbar_button.collidepoint(mouse_pos)
        pygame.draw.rect(screen,LIGHT_GRAY,toolbar_button)

    if options_editor:
        options_editor = options_background.collidepoint(mouse_pos)
        pygame.draw.rect(screen,LIGHT_GRAY,options_background)
        screen_fraction = WIDTH / len(options)
        i = 0
        for m in options:
            i += 1
            x_pos = screen_fraction * i - screen_fraction / 2
            text_image = font.render(m, True, WHITE, GRAY)
            options_rect = text_image.get_rect()
            options_rect.center = (x_pos,HEIGHT-25)
            if options_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen,BLACK,(options_rect.x - 5,options_rect.y - 5,options_rect.width + 10,options_rect.height + 10))
            # pygame.draw.rect(screen,options[m],mode_rect)
            
            # text_image.get_rect = font.render(m, True, WHITE, GRAY)
            screen.blit(text_image, options_rect)
            if options_rect.collidepoint(mouse_pos) and click:
                options[m]()

    else:
        options_editor = options_button.collidepoint(mouse_pos)
        pygame.draw.rect(screen,LIGHT_GRAY,options_button)
    

    if isinstance(selected, Enemy):
        pygame.draw.rect(screen, DARK_GREEN if patrolpoint_mode <= 0 else MEDIUM_GREEN, add_patrolpoint_button)
        pygame.draw.rect(screen, DARK_RED if patrolpoint_mode >= 0 else MEDIUM_RED, remove_patrolpoint_button)

        if add_patrolpoint_button.collidepoint(mouse_pos) and click: patrolpoint_mode = 1 if patrolpoint_mode < 1 else 0
        if remove_patrolpoint_button.collidepoint(mouse_pos) and click: patrolpoint_mode = -1 if patrolpoint_mode > -1 else 0
    else:
        patrolpoint_mode = 0
    pygame.display.update()