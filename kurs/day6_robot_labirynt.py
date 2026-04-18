def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# def finish():
#    while wall_in_front():
#        turn_left()
#    else:
#         move()
#         turn_right()


def finish():
    while wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        if not at_goal():
            turn_right()
            move()


while not at_goal():
    finish()

