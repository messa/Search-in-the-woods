import pyglet
import time

WINDOW_WIDTH, WINDOW_HEIGHT = 640, 400
RABBIT_WIDTH, RABBIT_HEIGHT = 81, 84
HEDGEHOG_WIDTH, HEDGEHOG_HEIGHT = 92, 63
CAR_WIDTH, CAR_HEIGHT = 146, 98
hledany_list = []

# window for the game
window = pyglet.window.Window()

# loads images for background
background_00 = pyglet.image.load("bg_white.png")
background_picture_a = pyglet.image.load("bg_01_a.png")
background_picture_b = pyglet.image.load("bg_01_b.png")

background = pyglet.sprite.Sprite(background_00)
background_woods = pyglet.sprite.Sprite(background_picture_a)

# loads images for Hidden - rabbit
rabbit_01_a = pyglet.image.load("rabbit_01_a.png")
rabbit_01_b = pyglet.image.load("rabbit_01_b.png")
rabbit_01_a_win = pyglet.image.load("rabbit_01_a_win.png")

# loads images for Hidden - car
car_01_a = pyglet.image.load("car_01_a.png")
car_01_b = pyglet.image.load("car_01_b.png")
car_01_a_win = pyglet.image.load("car_01_a_win.png")


# for Hidden - rabbit - vlastnosti pro králíka ve službě
kralik = pyglet.sprite.Sprite(rabbit_01_a)
kralik.x = 150
kralik.y = 60
hledany_list.append((kralik, rabbit_01_a, rabbit_01_b, rabbit_01_a_win))

# for Hidden - car -vlastnosti pro auto ve službě
auto = pyglet.sprite.Sprite(car_01_a)
auto.x = 300
auto.y = 100
hledany_list.append((auto, car_01_a, car_01_b, car_01_a_win))


def vykresli_na_zacatku():
    window.clear()
    background.draw()
    background_woods.draw()
    kralik.draw()
    auto.draw()


def change_bg_b(t):
    background_woods.image = background_picture_b
    background.draw()
    background_woods.draw()
    kralik.draw()
    auto.draw()
    pyglet.clock.schedule_once(change_bg_a, 2)


def change_bg_a(t):
    background_woods.image = background_picture_a
    background.draw()
    background_woods.draw()
    kralik.draw()
    auto.draw()
    pyglet.clock.schedule_once(change_bg_b, 2)

def change_hidden_all(t, k_meneni_list):

    pocitadlo = 0

    while pocitadlo <= 3:
        pocitadlo += 1
        print(pocitadlo) #kontrola
        print(k_meneni_list) #kontrola
        for typ_zmeny in [2,1]: #má zajišťovat střídání obrázků "a" [1] a "b" [2]
            for poradi in range(2): #zajišťuje střídání povelů pro králíka  a pro auto
                print(k_meneni_list) #kontrola
                print("hledany", k_meneni_list[poradi][0]) #kontrola
                hledany = k_meneni_list[poradi][0] #vybírá kralik [0][0] vs. auto [1][0]

                print("zmena",  k_meneni_list[poradi][typ_zmeny])#kontrola

                hledany.image = k_meneni_list[poradi][typ_zmeny] #má měnit obrázek u kralika/auta
                #jak_vykreslit_hledany(hledany)
                print(hledany) # kontrola
                background.draw()
                background_woods.draw()
                hledany.draw()
                time.sleep(5)






def nalezeni_hledaneho(x,y,b,mod):
    if x in range(kralik.x, kralik.x+RABBIT_WIDTH) and y in range(kralik.y, kralik.y+RABBIT_HEIGHT):
        print("{} je v ({},{})." .format(x, kralik.x, kralik.x+RABBIT_WIDTH))
        print("{} je v ({},{})." .format(y,kralik.y, kralik.y+RABBIT_HEIGHT))
        background.draw()
        background_woods.draw()
        kralik.image = rabbit_01_a_win
        kralik.draw()

#def proc_zelena_kdyz_nema(jak_moc_to_hrotit): #120 1.) Nefunguje, 2. obrazek bliká je to vidět, když se nastaví třeba interval 1/30), když se zruší ten if, tak to printuje
#    if kralik.image == rabbit_01_a_win:
#       print("chocholoušek")#chci důvod, proč se to stalo: nejlépe fci, která ho zavolala, nebo aspoň pozici mouse/mouse_click těsně před který obrázek je vepedu
#pyglet.clock.schedule_interval(proc_zelena_kdyz_nema,1/30)

# start background changing
pyglet.clock.schedule_once(change_bg_b, 7)
pyglet.clock.schedule_once(change_hidden_all, 3, hledany_list)


window.push_handlers(
    on_show=vykresli_na_zacatku,
    on_mouse_press= nalezeni_hledaneho,
)

pyglet.app.run()
