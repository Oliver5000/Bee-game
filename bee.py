import pgzrun
import random

HEIGHT = 400
WIDTH = 500

bee = Actor("bee") 
bee.x = 250
bee.y = 200

flower = Actor("flower")
flower.x = 150
flower.y = 200

score = 0

game_over = False


def draw():
    screen.blit("background", (0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("score: " + str(score), (200,350))
    if game_over:
        screen.fill("red")
        screen.draw.text("Times up! Your score is: " + str(score), (250,200))
        

def update():
    global score
    if keyboard.left:
        bee.x = bee.x - 3
    if keyboard.right:
        bee.x = bee.x + 3
    if keyboard.up:
        bee.y = bee.y - 3
    if keyboard.down:
        bee.y = bee.y + 3
    if bee.colliderect(flower):
        potato()
        score = score + 1
        
def potato():    
    flower.x = random.randint(50,450)
    flower.y = random.randint(50,350)

def timer():
    global game_over
    game_over = True

clock.schedule(timer, 60.0)

pgzrun.go()