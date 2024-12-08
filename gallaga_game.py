import pgzrun 
import random 
HEIGHT = 600
WIDTH = 800
TITLE = "Gallaga Game"
score = 0
ship = Actor("ship image")
bullet = Actor("bullet image") 
bug = Actor("bug image")
ship.pos = (300,540)
bug.pos =(random.randint(50,750),0)
def draw():
    screen.fill("light blue")
    ship.draw()
    bug.draw()
    screen.draw.text("score"+ str(score),(15,15))
def update():
    global score
    if keyboard.left:
        ship.x = ship.x-5
    if keyboard.right:
        ship.x = ship.x+5

    bug.y +=5
    if bug.y >600:
        bug.pos = (random.randint(50,750),0)

    if bug.colliderect(ship):
        score = score - 300
def on_key_down(key):
    if key  == keys.SPACE:
        bullet = Actor('bullet image')
        bullet.pos = ship.pos

pgzrun.go()