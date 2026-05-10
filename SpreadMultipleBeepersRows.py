from karel.stanfordkarel import *

"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers in
her bag. How can you solve this puzzle?
"""


def main():
    move()
    spread()
    while front_is_clear():
        move()
        if beepers_present():
            turn_right()
            spread()
    come_back_home()
    
def spread():
    while beepers_present():
        pick_beeper()
        if beepers_present():
            move_to_end()
            put_beeper()
            reset()
    put_beeper()
    turn_left()

def move_to_end():
    while beepers_present():
        move()
def come_back_home():
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_around()

def turn_right():
    for _ in range(3):
        turn_left()
def reset():
    turn_around()
    move_to_wall()
    turn_around()
    move()

def move_to_wall():
    while front_is_clear():
        move()

def turn_around():
    turn_left()
    turn_left()
    
def step_back():
    turn_around()
    move()
    turn_around()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
