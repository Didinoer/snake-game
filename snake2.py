from turtle import Screen
import time
from snake import Snake
from snake3 import Food 
from scoreboard import Scoreboard




Sc = Screen()
Sc.setup(width=600, height=600)
Sc.bgcolor('black')
Sc.listen()
Sc.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()


Sc.onkey(snake.up, "Up")
Sc.onkey(snake.left, "Left")
Sc.onkey(snake.right, "Right")
Sc.onkey(snake.down, "Down")


game_is_on = True
while game_is_on : 
    Sc.update()
    time.sleep(0.1)
    snake.move()
    


    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extended()
        score.scoring()
   
    if snake.head.xcor() > 280 or  snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280 :
            score.reset()
            snake.reset()
               

    for i in snake.segment[1:]:
        if snake.head.distance(i) < 10 :
            score.reset()
            snake.reset()
            
            
    
        

   
    
    


        
 
Sc.exitonclick()




















