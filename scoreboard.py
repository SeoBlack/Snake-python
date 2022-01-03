#scoreboard
from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        #creating the turtle as a text
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(x = 0 , y = 260)
        self.write(f"Score: {self.score}", align="center",font=("Arial" , 16 , "normal")) # writing score on the screen

    def increase_score(self):
        self.score += 1 # increasing by 1 every time this function gets called
        self.clear()#clearing the old score to write the new one
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))
    def game_over(self):
        self.goto(0,0)#printing the GameOver text in the center
        self.write(f"GameOver", align="center", font=("Arial", 24, "normal"))
