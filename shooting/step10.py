import random

import pgzrun

WIDTH = 640
HEIGHT = 480

player = Actor('player', pos=(320, 400))
missile = Actor('missile', pos=(0, 0))
aliens = []
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
    player.x = max(player.x, player.width / 2)
    player.x = min(player.x, WIDTH - player.width / 2)

    if missile.y >= 0 - missile.height:
        missile.y -= 8
    else:
        show_missile = False

    for alien in aliens:
        move(alien)
    hit_test()


def draw():
    screen.clear()
    player.draw()
    if show_missile:
        missile.draw()
    for alien in aliens:
        alien.draw()


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


def hit_test():
    global show_missile

    for alien in aliens[:]:
        if hit(missile, alien):
            missile.y = -100
            show_missile = False
            aliens.remove(alien)


def hit(missile, alien):
    if show_missile and abs(missile.x - alien.x) < 32 and abs(missile.y - alien.y) < 32:
        return True
    return False


def move(alien):
    x = random.randint(-4, 4)
    alien.x += x
    alien.x = max(alien.x, alien.width / 2)
    alien.x = min(alien.x, WIDTH - alien.width / 2)


def init():
    for i in range(5):
        alien = Actor('alien', pos=(64 + i * 128, 80))
        aliens.append(alien)


init()
pgzrun.go()
