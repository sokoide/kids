import pgzrun

WIDTH = 300
HEIGHT = 300

a = Actor('alien', pos=(100, 100))
# a.angle = 90
# a.pos = (120, 200)
# a.x = 30
# a.y = 30

def draw():
    screen.clear()
    #screen.fill((255, 255, 255))
    a.draw()

pgzrun.go()
