#e8.2DrawKoch.py
import turtle
def koch(size,n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3,n-1)
def main():
    turtle.color("blue")
    turtle.setup(600,600)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    lever = 5
    koch(400,lever)
    turtle.right(120)
    koch(400,lever)
    turtle.right(120)
    koch(400,lever)
    turtle.hideturtle()
main()
    
