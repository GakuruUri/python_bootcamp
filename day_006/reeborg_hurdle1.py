# Mu solution
def turn_right():
    turn_left()
    turn_left()
    turn_left() 
    
def jump():  
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for n in range(0, 6):
    jump()


# Angela's solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for step in range(6):
    jump()