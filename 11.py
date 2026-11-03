
import turtle
import colorsys

screen = turtle.Screen()
screen.title("Geometric Patterns and Recursive Fractals")
screen.setup(width=900, height=700)
screen.bgcolor("black")
screen.colormode(1.0)

t = turtle.Turtle()
t.speed(0)
t.pensize(2)


def get_color(i, total):
    return colorsys.hsv_to_rgb(i / total, 1, 1)


def geometric_pattern():
    t.penup()
    t.goto(-100, 0)
    t.pendown()

    for i in range(36):
        t.pencolor(get_color(i, 36))

        for j in range(4):
            t.forward(150)
            t.right(90)

        t.right(10)


def spiral():
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()

    for i in range(200):
        t.pencolor(get_color(i, 200))
        t.forward(i * 1.5)
        t.right(91)


def koch_curve(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length = length / 3

        koch_curve(length, depth - 1)
        t.left(60)

        koch_curve(length, depth - 1)
        t.right(120)

        koch_curve(length, depth - 1)
        t.left(60)

        koch_curve(length, depth - 1)


def koch_snowflake():
    t.penup()
    t.goto(-200, 100)
    t.setheading(0)
    t.pendown()

    t.pencolor("cyan")

    for i in range(3):
        koch_curve(400, 3)
        t.right(120)


while True:
    print("\n===== TURTLE GRAPHICS MENU =====")
    print("1. Geometric Pattern")
    print("2. Colorful Spiral")
    print("3. Koch Snowflake")
    print("4. Exit")

    choice = input("Enter your choice: ")

    t.clear()
    t.penup()
    t.home()
    t.setheading(0)
    t.pendown()

    if choice == "1":
        geometric_pattern()

    elif choice == "2":
        spiral()

    elif choice == "3":
        koch_snowflake()

    elif choice == "4":
        print("Exiting Turtle Graphics...")
        break

    else:
        print("Invalid choice!")

turtle.done()
