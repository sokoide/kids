import pgzrun

WIDTH = 300
HEIGHT = 300

a = Actor('well', pos=(100, 100))
b = Actor('pondblue', pos=(200, 200))
data = [a,b]

def draw():
    screen.clear()
    screen.fill((255, 255, 255))
    for s in data:
        s.draw()

pgzrun.go()
