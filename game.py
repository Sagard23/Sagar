import turtle
import random
import os
import math
import winsound
#set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
#wn.bgpic("C:/Users/dadhi/Pictures/sp_bg.gif")

#register the shapes
turtle.register_shape("E:/game/alien.gif")
turtle.register_shape("E:/game/player.gif")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set the Score to 0
score = 0

#Draw the Score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#create the player
player = turtle.Turtle()
player.color("red")
player.shape("E:/game/player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 30

#choose number of enemies
number_of_enemies = 6
#create an empty list of enemies
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
    #create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("green")
    enemy.shape("E:/game/alien.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 5

#Create the players bull et
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 50

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#move the player left and right
def move_left():
    x = player.xcor()
    if x < -280:
        x = - 280
    x -= playerspeed
    player.setx(x)

def move_right():
    x = player.xcor()
    if x > 280:
        x = 280
    x += playerspeed
    player.setx(x)

#define bullet
def fire_bullet():
    #declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        winsound.PlaySound("explosion", winsound.SND_ASYNC)
        bulletstate = "fire"
    #move the bullet to the just above the player
    x = player.xcor()
    y = player.ycor() + 10
    bullet.setposition(x, y)
    bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

#create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#main game loop
while True:

    for enemy in enemies:

        #move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #move the enemy back and down
        if enemy.xcor() > 280:
            #move all the eneies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            #move all the eneies down            
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
                #change enemy direction
            enemyspeed *= -1
        #check for a collision between the bullet and the enemy
        if isCollision(bullet,enemy):
            winsound.PlaySound("laser", winsound.SND_ASYNC)
            #reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #Reset the Enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #Update the Score
            score += 10 
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
           
        if isCollision(player, enemy):
            winsound.PlaySound("laser", winsound.SND_ASYNC)
            player.hideturtle()
            enemy.hideturtle()
            wn.bgpic("E:/game/game_over.gif")
            print("Game Over")
            break



    #move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #check to see if bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    







delay = raw_input("Press enter to finish.")
