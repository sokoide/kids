import pgzrun

WIDTH = 640
HEIGHT = 480

player = Actor('player', pos=(320, 400))


def draw():
    screen.clear()
    player.draw()


pgzrun.go()
