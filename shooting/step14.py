import random

import pgzrun

WIDTH = 640
HEIGHT = 480

player = Actor('player', pos=(320, 440))
missile = Actor('missile', pos=(0, 0))
aliens = []
alien_missiles = []
left_pressed = False
right_pressed = False
frame = 0
gameover = False

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
    global frame

    frame += 1
    frame %= 8000000000  # frameが大きくなりすぎたら0に戻す

    if left_pressed:
        player.x -= 4
    elif right_pressed:
        player.x += 4
    player.x = max(player.x, player.width / 2)
    player.x = min(player.x, WIDTH - player.width / 2)

    if missile.y >= 0 - missile.height:
        missile.y -= 8
    else:
        missile.y = -100

    for alien in aliens:
        move(alien)
        if random.randint(0, 1000) < 7:
            alien_fire(alien)

    for alien_missile in alien_missiles[:]:
        alien_missile.y += 4
        if alien_missile.y >= HEIGHT + alien_missile.height / 2:
            alien_missiles.remove(alien_missile)

    hit_test()


def draw():
    screen.clear()
    player.draw()
    missile.draw()
    for alien in aliens:
        alien.draw()
    for alien_missile in alien_missiles[:]:
        alien_missile.draw()
    if gameover:
        screen.draw.text("Game Over", centerx=WIDTH/2, centery=HEIGHT/2, fontsize=64, align="center")


def fire():
    if missile.y >= -missile.height:
        print('ミサイルが画面内に存在するため、何もしません')
        return
    else:
        print('ミサイルを発射します')
        missile.x = player.x
        missile.y = player.y - missile.height


def alien_fire(alien):
    global alien_missiles
    if len(alien_missiles) >= 3:
        return
    missile = Actor('alien_missile', pos=(alien.x, alien.y + alien.height / 2))
    alien_missiles.append(missile)


def hit_test():
    global gameover

    for alien in aliens[:]:
        if hit(missile, alien):
            missile.y = -100
            aliens.remove(alien)

    for alien_missile in alien_missiles:
        if hit(alien_missile, player):
            gameover = True


def hit(source, target):
    # return source.distance_to(target) < 32でもいいです
    if abs(source.x - target.x) < 32 and abs(source.y - target.y) < 32:
        return True
    return False


def move(alien):
    x = 2 if frame % 60 < 30 else -2
    alien.x += x


def init():
    for j in range(3):
        for i in range(5):
            if j==0:
                alien = Actor('alien1', pos=(32 + i * 128, 40))
            elif j==1:
                alien = Actor('alien2', pos=(32 + i * 128, 104))
            else:
                alien = Actor('alien3', pos=(32 + i * 128, 168))
            aliens.append(alien)


init()
pgzrun.go()
