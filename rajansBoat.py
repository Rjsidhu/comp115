import turtle
import random

def setup(width, height):
    turtle.Screen().setup(width, height)
    turtle.speed(9)

def draw_sky():
    turtle.bgcolor("light blue")

def draw_water():
    turtle.penup()
    turtle.goto(-400, -150)
    turtle.pendown()
    turtle.color("blue")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()

def draw_boat():
    turtle.penup()
    turtle.goto(-300, -80)
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(150)
    turtle.left(45)
    turtle.forward(300)
    turtle.left(45)
    turtle.forward(150)
    turtle.end_fill()

def draw_mast():
    turtle.penup()
    turtle.goto(0, -80)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.left(45)
    for _ in range(2):
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
    turtle.end_fill()

def draw_sails():
    turtle.penup()
    turtle.goto(0, 120)
    turtle.pendown()
    
    # Right Sail
    turtle.color("white")
    turtle.begin_fill()
    turtle.right(130)
    turtle.forward(250)
    turtle.right(140)
    turtle.forward(190)
    turtle.end_fill()

    # Left Sail
    turtle.penup()
    turtle.forward(14)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(180)
    turtle.right(139)
    turtle.forward(240)
    turtle.end_fill()

def draw_sun():
    turtle.penup()
    turtle.goto(-300, 150)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()

def draw_bird(x, y):
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("black")
    turtle.left(45)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.penup()

def draw_birds(num_birds):
    for _ in range(num_birds):
        x = random.randint(-400, 400)
        y = random.randint(0, 200)
        draw_bird(x, y)

def main():
    setup(800, 500)
    draw_sky()
    draw_water()
    draw_boat()
    draw_mast()
    draw_sails()
    draw_sun()
    draw_birds(15)  
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
