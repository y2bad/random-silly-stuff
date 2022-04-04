import turtle


def print_play_field():
    for i in range(10**2):
        turtle.penup()
        turtle.goto(i//10*30-30*5, i % 10*30-30*5)
        turtle.pendown()
        for j in range(4):
            turtle.fd(30)
            turtle.lt(90)


def show_walls():
    for wall in found_walls:
        turtle.penup()
        turtle.goto(wall[0]*30-30*5, -wall[1]*30+30*4)
        turtle.pendown()
        turtle.fillcolor("black")
        turtle.begin_fill()
        for j in range(4):
            turtle.fd(30)
            turtle.lt(90)
        turtle.end_fill()


def show_player(pos):
    turtle.penup()
    turtle.goto(pos[0]*30-30*5+15, -pos[1]*30+30*4+15)
    turtle.dot(15)


def click_regsitration(x, y):
    global player_health, player_position
    pos = [int(x//30+5), int((y//30-4)*-1)]
    if pos[0] in [i for i in range(10)] and pos[1] in [i for i in range(10)] and \
            (pos[0] == player_position[0]+1 or pos[1] == player_position[1]+1 or
             pos[0] == player_position[0]-1 or pos[1] == player_position[1]-1):

        if play_field[pos[1]][pos[0]] == 0:
            player_position = pos
        else:
            player_health -= 1
            found_walls.append(pos)

        if player_position == [9, 9]:
            turtle.penup()
            turtle.goto(-100, 220)
            turtle.write(f'Gewonnen', font=(
                "Verdana", 15, "normal"))
            turtle.done()
        
        if player_health < 1:
            turtle.penup()
            turtle.goto(-100, 220)
            turtle.write(f'Verloren', font=(
                "Verdana", 15, "normal"))
            turtle.done()

    turtle.clear()
    print_play_field()
    show_walls()
    show_player(player_position)
    turtle.penup()
    turtle.goto(-100, 160)
    turtle.write(f'Verbleibende Leben: {player_health}', font=(
        "Verdana", 15, "normal"))
    turtle.update()


play_field = [[0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 1, 1, 0, 1, 1, 0],
              [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
              [0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
              [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
              [0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
              [1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
              [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
              [0, 1, 0, 0, 1, 0, 0, 0, 1, 0]]

player_position = [0, 0]
player_health = 5
found_walls = []

turtle.tracer(0, 0)
turtle.hideturtle()

screen = turtle.Screen()
screen.onclick(fun=click_regsitration)

print_play_field()
show_player(player_position)
turtle.penup()
turtle.goto(-100, 160)
turtle.write(f'Verbleibende Leben: {player_health}', font=(
    "Verdana", 15, "normal"))

turtle.update()
turtle.mainloop()