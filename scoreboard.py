from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            hs = data.read()
            hs_int = int(hs)
            self.highscore = hs_int
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(0,465)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", False, align="center",
                   font=("Arial", 22, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.setposition(0,0)
    #     self.write("Game Over.", False, align="center", font=("Arial", 22, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()