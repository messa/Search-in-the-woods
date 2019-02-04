import pyglet

WINDOW_WIDTH, WINDOW_HEIGHT = 640, 400
RABBIT_WIDTH, RABBIT_HEIGHT = 81, 84
HEDGEHOG_WIDTH, HEDGEHOG_HEIGHT = 92, 63
CAR_WIDTH, CAR_HEIGHT = 146, 98


# window for the game
window = pyglet.window.Window()

# loads images for background
background_00 = pyglet.image.load("bg_white.png")

background_pictures = [
    pyglet.image.load("bg_01_a.png"),
    pyglet.image.load("bg_01_b.png"),
]

background = pyglet.sprite.Sprite(background_00)
background_woods = pyglet.sprite.Sprite(background_pictures[0])
background_woods_current_picture = 0

# loads images for Hidden - rabbit
rabbit_01_a = pyglet.image.load("rabbit_01_a.png")
rabbit_01_b = pyglet.image.load("rabbit_01_b.png")
rabbit_01_a_win = pyglet.image.load("rabbit_01_a_win.png")

# loads images for Hidden - car
car_01_a = pyglet.image.load("car_01_a.png")
car_01_b = pyglet.image.load("car_01_b.png")
car_01_a_win = pyglet.image.load("car_01_a_win.png")
auto_pictures = [car_01_a, car_01_b]
auto_current_picture = 0

hledany_list = []

# for Hidden - rabbit - vlastnosti pro králíka ve službě
kralik = pyglet.sprite.Sprite(rabbit_01_a)
kralik.x = 150
kralik.y = 60
hledany_list.append(kralik)

# for Hidden - car -vlastnosti pro auto ve službě
auto = pyglet.sprite.Sprite(car_01_a)
auto.x = 300
auto.y = 100
hledany_list.append(auto)


def vykresli():
    window.clear()
    background.draw()
    background_woods.draw()
    kralik.draw()
    auto.draw()


def change_bg(t):
    global background_woods_current_picture
    background_woods_current_picture += 1
    background_woods_current_picture %= len(background_pictures)
    background_woods.image = background_pictures[background_woods_current_picture]


pyglet.clock.schedule_interval(change_bg, .5)


def change_car(t):
    global auto_current_picture
    auto_current_picture += 1
    auto_current_picture %= len(auto_pictures)
    auto.image = auto_pictures[auto_current_picture]


pyglet.clock.schedule_interval(change_car, .1)


def kliknuti(x, y, b, mod):
    if uvnitr_spritu(kralik, x, y):
        print('kralik zasazen')
        kralik.image = rabbit_01_a_win
    else:
        print('kralik unikl')


def uvnitr_spritu(sprite, x, y):
    return x in range(sprite.x, sprite.x + sprite.width) and \
        y in range(sprite.y, sprite.y + sprite.height)




window.push_handlers(
    on_draw=vykresli,
    on_mouse_press=kliknuti,
)



pyglet.app.run()
