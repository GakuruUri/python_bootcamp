#Reborgs world make square.abs

# My solution
def turn_right():
    turn_left()
    turn_left()
    turn_left() 

def make_square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()

make_square()


# Angela's solution

def turn_right():
    turn_left()
    turn_left()
    turn_left() 
    
# Draw square on screen
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()