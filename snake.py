
from turtle import Turtle

POSITION = [(0,0), (-20,0), (-40,0)]

class Snake:
    
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.tail = self.segment[-1]
        
    def create_snake(self):
        for position in POSITION :
            self.add_new_segment(position)
            
  
    def add_new_segment(self,position) :
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        self.segment.append(new_segment)
        
    def extended(self):
        self.add_new_segment(self.tail.position())
        
    def reset(self):
        for i in self.segment :
            i.goto(1000,1000)
        self.segment.clear()
        self.create_snake()   
        self.head = self.segment[0]
           
                
            
    def move(self):
        for seg_num in range(len(self.segment)-1, 0 ,-1):
            new_xcor = self.segment[seg_num - 1].xcor()
            new_ycor = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_xcor,new_ycor)
        self.segment[0].forward(20)
        
        
    def up(self):
        if self.segment[0].heading() != 270 :
            self.segment[0].setheading(90)
    def down(self):
         if self.segment[0].heading() != 90 :
                self.segment[0].setheading(270)
    def right(self):
         if self.segment[0].heading() != 180 :
                self.segment[0].setheading(0)
    def left(self):
         if self.segment[0].heading() != 0 :
                self.segment[0].setheading(180)
        