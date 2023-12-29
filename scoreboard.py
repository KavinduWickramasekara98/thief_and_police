from turtle import Turtle
FONT = ("Courier", 24, "normal")
POINT_INCREMENT=100

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.myPoints=0
        self.hideturtle()
        self.penup()
        self.goto(-250,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Coins loot:{self.myPoints}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Hit Arrow", align="center", font=FONT)

    def add_points(self):
        self.myPoints+=POINT_INCREMENT
        self.update_scoreboard()