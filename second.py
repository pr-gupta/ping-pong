from helper import *

wn = setup_screen()
wn.listen()

# draw a ball

ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")

# draw 1st paddle

paddle1 = turtle.Turtle()
paddle1.shape("rectangle")
paddle1.color("red")
paddle1.penup()
paddle1.goto(-350, 0)

# draw 2nd paddle

paddle2 = turtle.Turtle()
paddle2.shape("rectangle")
paddle2.color("red")
paddle2.penup()
paddle2.goto(350, 0)

# ------------------------------------------- #
# --------------- START CODE ---------------- #
# ------------------------------------------- #


# ------------------------------------------- #
# --------------- END CODE ------------------ #
# ------------------------------------------- #

wn.update()
turtle.Screen().exitonclick()

# ref - http://christianthompson.com/
