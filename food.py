from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")#creating food for the snake
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
    def refresh(self):# sets new location for food to be created

        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.goto(x=x,y=y)

