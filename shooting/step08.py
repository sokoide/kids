import pgzrun

WIDTH = 640
HEIGHT = 480

player = Actor('player', pos=(320, 400))
missile = Actor('missile', pos=(0, 0))
show_missile = False
left_pressed = False
right_pressed = False

def on_key_down(key):
    global left_pressed, right_pressed
    print(key)
    if key == keys.LEFT:
        left_pressed = True
    elif key == keys.RIGHT:
        right_pressed = True
    elif key == keys.SPACE:
        fire()

def on_key_up(key):
    global left_pressed, right_pressed
    if key == keys.LEFT:
        left_pressed = False
    elif key == keys.RIGHT:
        right_pressed = False

def update():
    global show_missile

    if left_pressed:
        player.x -= 4
    elif right_pressed:
        player.x += 4
    player.x = max(player.x, player.width/2)
    player.x = min(player.x, WIDTH - player.width/2)

    if missile.y >= 0 - missile.height:
        missile.y -= 8
    else:
        show_missile = False


def draw():
    screen.clear()
    player.draw()
    if show_missile:
        missile.draw()

def fire():
    global show_missile

    if missile.y >= -missile.height:
        print('ミサイルが画面内に存在するため、何もしません')
        return
    if not show_missile:
        print('ミサイルを発射します')
        missile.x = player.x
        missile.y = player.y - missile.height
        show_missile = True

pgzrun.go()