import pyglet

WINDOW_WIDTH, WINDOW_HEIGHT = 640, 400
RABBIT_WIDTH, RABBIT_HEIGHT = 81, 84
HEDGEHOG_WIDTH, HEDGEHOG_HEIGHT = 92, 63
CAR_WIDTH, CAR_HEIGHT = 146, 98

# window for the game
window = pyglet.window.Window()

# loads images for background
background_00 = pyglet.image.load("bg_white.png")
background_picture_a = pyglet.image.load("bg_01_a.png")
background_picture_b = pyglet.image.load("bg_01_b.png")

background = pyglet.sprite.Sprite(background_00)
background_woods = pyglet.sprite.Sprite(background_picture_a)

# loads images for Hidden
rabbit_01_a = pyglet.image.load("rabbit_01_a.png")
rabbit_01_b = pyglet.image.load("rabbit_01_b.png")
rabbit_01_a_win = pyglet.image.load("rabbit_01_a_win.png")

kralik = pyglet.sprite.Sprite(rabbit_01_a)
kralik.x = 150
kralik.y = 60


def vykresli_na_zacatku():
    window.clear()
    background.draw()
    background_woods.draw()
    kralik.draw()


def change_bg_b(t):
    background_woods.image = background_picture_b
    background.draw()
    background_woods.draw()
    kralik.draw()
    pyglet.clock.schedule_once(change_bg_a, 2)


def change_bg_a(t):
    background_woods.image = background_picture_a
    background.draw()
    background_woods.draw()
    kralik.draw()
    pyglet.clock.schedule_once(change_bg_b, 2)

def change_rabbit_a(t, hledany):
    #if not found:
    background.draw()
    background_woods.draw()
    hledany.image = rabbit_01_a
    #kralik.x = 150
    #kralik.y = 60
    hledany.draw()
    pyglet.clock.schedule_once(change_rabbit_b, 3, hledany)

def change_rabbit_b(t, hledany):
    background.draw()
    background_woods.draw()
    hledany.image = rabbit_01_b
    hledany.draw()
    pyglet.clock.schedule_once(change_rabbit_a, 3, hledany)

def nalezeni_hledaneho(x,y,b,mod):
    if x in range(150, 150+81) and y in range(60, 60+84):
        background.draw()
        background_woods.draw()
        kralik.image = rabbit_01_a_win
        kralik.draw()

# start background changing
pyglet.clock.schedule_once(change_bg_b, 7)
pyglet.clock.schedule_once(change_rabbit_b, 3, kralik)

window.push_handlers(
    on_show=vykresli_na_zacatku,
    on_mouse_press= nalezeni_hledaneho,
)

pyglet.app.run()
