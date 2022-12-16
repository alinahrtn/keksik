import turtle
turtle.shape('turtle')
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
def Koch_Line(l, n):
    if n == 0:
        turtle.forward(l)
        return
    l //= 3
    Koch_Line(l, n - 1)
    turtle.left(60)
    Koch_Line(l, n - 1)
    turtle.right(120)
    Koch_Line(l, n - 1)
    turtle.left(60)
    Koch_Line(l, n - 1)

Koch_Line(400, 4)