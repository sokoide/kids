import pgzrun

WIDTH = 640
HEIGHT = 480

player = Actor('player', pos=(320, 400))

def on_key_down(key):
    if key == keys.LEFT:
        player.x -= 4
    elif key == keys.RIGHT:
        player.x += 4

def draw():
    screen.clear()
    player.draw()

pgzrun.go()