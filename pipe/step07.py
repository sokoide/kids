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
# 終了判定Test用データ
# data = [
#     [8, 2, 4, 5, 0],
#     [0, 5, 3, 3, 0],
#     [0, 6, 1, 2, 9],
# ]

visited = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
connected = []

data_to_file = ['empty', 'pipe1gray', 'pipe1gray', 'pipe2gray',
                'pipe2gray', 'pipe2gray', 'pipe2gray', 'pipe3gray', 'well', 'pondgray']
data_to_angle = [0, 0, 90, 0, 90, 180, 270, 0, 0, 0]
sprites = []
stageclear = None
cleared = False


def draw():
    screen.clear()
    screen.fill((255, 255, 255))

    green = (0, 180, 0)
    for i in connected:
        box = Rect((SPRITE_WIDTH * i[0], SPRITE_HEIGHT * i[1]),
                   (SPRITE_WIDTH, SPRITE_HEIGHT))
        screen.draw.filled_rect(box, green)

    for s in sprites:
        s.draw()
    if cleared:
        stageclear.draw()


def on_mouse_down(button, pos):
    global cleared
    global connected

    x = int(pos[0] / SPRITE_WIDTH)
    y = int(pos[1] / SPRITE_HEIGHT)
    s = sprites[y * 5 + x]
    s.angle = (s.angle - 90) % 360

    print('-----')
    connected = []
    if dfs(0, 0):
        print('Goal!')
        cleared = True
        sprites[2 * 5 + 4].image = 'pondblue'


def get_targets(x, y):
    # from, allowed targets
    # 1-2, 0/180 degrees -> [(0, -1), (0, 1)]
    # 1-2, 90/270 degrees -> [(-1, 0), (1, 0)]
    # 3-6, 0 degrees -> [(-1, 0), (0, -1)]
    # 3-6, 90 degrees -> [(-1, 0), (0, 1)]
    # 3-6, 180 degrees -> [(1, 0), (0, 1)]
    # 3-6, 270 degrees -> [(1, 0), (0, -1)]
    # 8, any angle->[(1, 0)]
    anchor_id = data[y][x]
    angle = int(sprites[5 * y + x].angle)
    targets = []

    if anchor_id <= 2:
        if angle % 180 == 0:
            targets = [(x, y - 1), (x, y + 1)]
        else:
            targets = [(x - 1, y), (x + 1, y)]
    elif anchor_id <= 6:
        if angle == 0:
            targets = [(x - 1, y), (x, y - 1)]
        elif angle == 90:
            targets = [(x - 1, y), (x, y + 1)]
        elif angle == 180:
            targets = [(x + 1, y), (x, y + 1)]
        else:
            targets = [(x + 1, y), (x, y - 1)]
    elif anchor_id == 8:
        targets = [(x + 1, y)]
    elif anchor_id == 9:
        targets = [(x - 1, y)]

    return targets


def can_connect(to_x, to_y, from_x, from_y):
    if to_x < 0 or to_x >= len(data[0]) or to_y < 0 or to_y >= len(data):
        return False
    from_targets = get_targets(from_x, from_y)
    to_targets = get_targets(to_x, to_y)
    print(to_targets)
    for ft in from_targets:
        for tt in to_targets:
            if ft[0] == to_x and ft[1] == to_y and tt[0] == from_x and tt[1] == from_y:
                return True
    return False


def dfs(x, y):
    if x < 0 or x >= len(data[0]) or y < 0 or y >= len(data) or visited[y][x] == 1:
        return False

    connected.append((x, y))
    if data[y][x] == 9:  # Goal
        return True

    print("checking (%d,%d) data:%d, angle:%d" % (x, y, data[y][x], sprites[y * 5 + x].angle))
    visited[y][x] = 1
    r = False

    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if can_connect(x + d[0], y + d[1], x, y):
            r = dfs(x + d[0], y + d[1])
            if r:
                break

    visited[y][x] = 0
    return r


def initialize():
    global sprites
    global stageclear
    for y in range(len(data)):
        for x in range(len(data[y])):
            s = Actor(data_to_file[data[y][x]],
                      pos=(SPRITE_WIDTH / 2 + x * SPRITE_WIDTH, SPRITE_HEIGHT / 2 + y * SPRITE_HEIGHT))
            s.angle = data_to_angle[data[y][x]]
            sprites.append(s)
    stageclear = Actor('stageclear', pos=(WIDTH / 2, HEIGHT / 2))
    dfs(0,0)


initialize()
pgzrun.go()
