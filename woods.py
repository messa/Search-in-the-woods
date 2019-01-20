import pyglet

WINDOW_WIDTH, WINDOW_HEIGHT = 640, 400
RABBIT_WIDTH, RABBIT_HEIGHT = 81, 84
HEDGEHOG_WIDTH, HEDGEHOG_HEIGHT = 92, 63
CAR_WIDTH, CAR_HEIGHT = 146, 98




def draw_background():
    window.clear()
    background.draw()
    rabbit_n01 = Rabbits()
    Rabbits.draw(rabbit_n01)
    pyglet.clock.schedule_interval(rabbit_n01.change_b, 2)


def change_bg_b(t):
    background.image = background_picture_b
    background.draw()
    pyglet.clock.schedule_once(change_bg_a, 2)


def change_bg_a(t):
    background.image = background_picture_a
    background.draw()
    pyglet.clock.schedule_once(change_bg_b, 2)


class Hidden:
    def __init__(self, name):
        print("vytvářím {}".format(name))
        self.name = name

    def draw(self):
        self.sprite.draw()


class Rabbits(Hidden):
    def __init__(self):
        self.sprite = pyglet.sprite.Sprite(rabbit_01_a)
        #self.sprite.x = min(self.sprite.x + RABBIT_WIDTH, WINDOW_WIDTH)
        #self.sprite.y = min(self.sprite.y + RABBIT_HEIGHT, WINDOW_HEIGHT)

#    def draw(self):
#        self.sprite.draw()

    def find(self):
        self.sprite = pyglet.sprite.Sprite(rabbit_01_a_win)
        found = True

    def change_a(self,t):
        #if not found:
        self.sprite = pyglet.sprite.Sprite(rabbit_01_a)

    def change_b(self,t):
        #if not found:
        #print(self)
        self.sprite = pyglet.sprite.Sprite(rabbit_01_b)




# window for the game
window = pyglet.window.Window()

# loads images for background
background_picture_a = pyglet.image.load("bg_01_a.png")
background_picture_b = pyglet.image.load("bg_01_b.png")
background = pyglet.sprite.Sprite(background_picture_a)

# loads images for Hidden
rabbit_01_a = pyglet.image.load("rabbit_01_a.png")
rabbit_01_b = pyglet.image.load("rabbit_01_b.png")
rabbit_01_a_win = pyglet.image.load("rabbit_01_a_win.png")

# start background changing
pyglet.clock.schedule_once(change_bg_b, 2)

window.push_handlers(
    on_show=draw_background,
  )



pyglet.app.run()
