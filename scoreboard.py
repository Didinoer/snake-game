from turtle import Turtle

class Scoreboard(Turtle) :
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt" ,mode= 'r') as data :
            self.high_score = data.read()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.write(f"Score = {self.score} high score = {self.high_score} ",align='center',font=("arial", 12, 'normal'))
   
    def scoring(self):
        self.clear()
        self.score = self.score + 1
        self.write(f"Score = {self.score} high score = {self.high_score} ",align='center',font=("arial", 12, 'normal'))

    def reset(self):
        if self.score > int(self.high_score) :
            self.high_score = self.score
            with open("/Dev/tutorial java oop/latihan_python_dasar/snake/data.txt","w") as data : 
                data.write(str(self.high_score))           
            self.score = 0
        else :
            self.score = 0
            self.clear()
            self.write(f"Score = {self.score} high score = {self.high_score} ",align='center',font=("arial", 12, 'normal'))
        
        
    
   
       
    
    
   
        
                    
 
