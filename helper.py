import threading
import turtle
import os
import winsound
from concurrent.futures import ThreadPoolExecutor

lock1 = threading.Lock()
lock2 = threading.Lock()
executor = ThreadPoolExecutor(5)


def setup_screen():
    wn = turtle.Screen()
    wn.title("Pong")
    wn.bgcolor("white")
    wn.setup(width=800, height=600)
    wn.tracer(0)
    wn.register_shape("rectangle", ((-50, -10), (50, -10), (50, 10), (-50, 10)))
    return wn


def play_sound():
    executor.submit(lambda: winsound.PlaySound('bounce.wav', winsound.SND_FILENAME))
    # os.system("afplay bounce.wav&")


def move_up(shape):
    y = shape.ycor()
    y = min(y + 20, 250)
    shape.sety(y)


def move_down(shape):
    y = shape.ycor()
    y = max(y - 20, -250)
    shape.sety(y)

# ref - http://christianthompson.com/
