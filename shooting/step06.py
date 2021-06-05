import pgzrun

WIDTH = 640
HEIGHT = 480

player = Actor('player', pos=(320, 400))
left_pressed = False
right_pressed = False

def on_key_down(key):
    global left_pressed, right_pressed

    if key == keys.LEFT:
        left_pressed = True
    elif key == keys.RIGHT:
        right_pressed = True

def on_key_up(key):
    global left_pressed, right_pressed
    if key == keys.LEFT:
        left_pressed = False
    elif key == keys.RIGHT:
        right_pressed = False

def update():
    if left_pressed:
        player.x -= 4
    elif right_pressed:
        player.x += 4

def draw():
    screen.clear()
    player.draw()

pgzrun.go()