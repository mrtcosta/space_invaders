import functools
import turtle
import random
from ship import Ship
from turtle import Screen
from ets import Aliens
from barriers import Barrier
import time
from score import Scoreboard


# setting screen
screen = Screen()
screen.bgcolor('black')
screen.setup(height=600, width=800)
screen.title('Space Invaders')


# variables
ship = Ship()
aliens = Aliens()
barrier = Barrier()
score = Scoreboard()

aliens.create_aliens()
barrier.create_barrier()



# waiting for keys
screen.listen()
screen.onkeypress(ship.move_left, 'Left')
screen.onkeypress(ship.move_right, 'Right')
screen.onkeypress(ship.shoot_now, 'space')

time_delay = 0.1
game_on = True
move_variable = 0
side = 1

while game_on:
    if move_variable == 10:
        side = side*-1

    time.sleep(time_delay)
    screen.update()

    aliens.move_aliens(move_variable, side)
    aliens.shoot_aliens()
    aliens.bullets_move()
    ship.move_ship_bullet()

    for bullet in aliens.all_bullets_ets:
        for barr in barrier.barriers:
            if bullet.distance(barr) < 20:
                barr.hideturtle()
                bullet.hideturtle()
                barrier.barriers.remove(barr)
                aliens.all_bullets_ets.remove(bullet)

    for bullet in ship.all_bullets:
        for barr in barrier.barriers:
            if bullet.distance(barr) < 20:
                barr.hideturtle()
                bullet.hideturtle()
                barrier.barriers.remove(barr)
                ship.all_bullets.remove(bullet)

    for bullet in ship.all_bullets:
        for alien in aliens.aliens:
            if bullet.distance(alien) < 20:
                alien.hideturtle()
                bullet.hideturtle()
                aliens.aliens.remove(alien)
                ship.all_bullets.remove(bullet)
                score.score_up()

    for bullet in aliens.all_bullets_ets:
            if bullet.distance(ship.ship) < 10:
                score.game_over()
                game_on = False

    for alien in aliens.aliens:
             if ship.ship.distance(alien) < 20:
                score.game_over()
                game_on = False

    if move_variable > 10:
        move_variable = 0
    else:
        move_variable = move_variable + 1

















screen.exitonclick()
