import turtle
turtle.Screen().bgcolor("sky blue")
sc=turtle.Screen()
sc.setup(400,500)
turtle.title("welcome to turtle")
board=turtle.Turtle()
for i in range(7):
    board.forward(500)
    board.left(90)
    i = i+1