import pyglet


def draw_background():
    window.clear()
    background.draw()


def change_bg_b(t):
    background.image = background_picture_b
    background.draw()
    pyglet.clock.schedule_once(change_bg_a, 3)


def change_bg_a(t):
    background.image = background_picture_a
    background.draw()
    pyglet.clock.schedule_once(change_bg_b, 4)


class Hidden:
    def __init__(self, name):
        print("vytvářím {}".format(name))
        self.name = name


# window for the game
window = pyglet.window.Window()

# loads images for background
background_picture_a = pyglet.image.load("bg_01_a.jpg")
background_picture_b = pyglet.image.load("bg_01_b.jpg")
background = pyglet.sprite.Sprite(background_picture_a)

# start background changing
pyglet.clock.schedule_once(change_bg_b, 2)

window.push_handlers(
    on_show=draw_background,
)

pyglet.app.run()
