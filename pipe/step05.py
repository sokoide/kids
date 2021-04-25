import pgzrun

SPRITE_WIDTH = 64
SPRITE_HEIGHT = 64
WIDTH = SPRITE_WIDTH * 5
HEIGHT = SPRITE_HEIGHT * 3
TITLE = 'Pipe Game'

data = [
    [8, 1, 4, 5, 0],
    [0, 5, 6, 3, 0],
    [0, 3, 1, 1, 9],
]
data_to_file = ['empty', 'pipe1gray', 'pipe1gray', 'pipe2gray', 'pipe2gray', 'pipe2gray', 'pipe2gray', 'pipe3gray', 'well', 'pondgray']
data_to_angle = [0, 0, 90, 0, 90, 180, 270, 0, 0, 0]
sprites = []


def draw():
    screen.clear()
    screen.fill((255, 255, 255))
    for s in sprites:
        s.draw()


def on_mouse_down(button, pos):
    x = int(pos[0] / SPRITE_WIDTH)
    y = int(pos[1] / SPRITE_HEIGHT)
    s = sprites[y * 5 + x]
    s.angle = (s.angle - 90) % 360


def initialize():
    global sprites
    for y in range(len(data)):
        for x in range(len(data[y])):
            s = Actor(data_to_file[data[y][x]],
                      pos=(SPRITE_WIDTH / 2 + x * SPRITE_WIDTH, SPRITE_HEIGHT / 2 + y * SPRITE_HEIGHT))
            s.angle = data_to_angle[data[y][x]]
            sprites.append(s)


initialize()
pgzrun.go()
