from turtle import Turtle
import random
class Snake():

    def __init__(self):
        #initializing snake body
        self.segments= []
        self.colors = ["red","green","yellow","blue","gray","pink","wheat"]
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self): # creating the snake body
        self.x = 0
        for i in range(0, 3):
            square = Turtle("square")
            square.penup()
            square.color(random.choice(self.colors))
            square.goto(x=self.x, y=0.0)
            self.segments.append(square)
            self.x -= 20

    def move(self):#moving the snake
        for each in range(len(self.segments) - 1, 0, -1):
            x = self.segments[each - 1].xcor()
            y = self.segments[each - 1].ycor()
            self.segments[each].goto(x=x, y=y)
        self.segments[0].forward(20)
    def append_segment(self):#increasing the snake length every time it eats a piece of food
        square = Turtle("square")
        square.penup()
        square.color(random.choice(self.colors))
        self.segments.append(square)
    #functions to controll the snake by keyboard
    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)