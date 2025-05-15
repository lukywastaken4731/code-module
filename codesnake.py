import curses
from random import randint

def main(stdscr):
    # Initialisation de l'écran
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Dimensions de la fenêtre
    sh, sw = stdscr.getmaxyx()
    win = curses.newwin(sh, sw, 0, 0)

    # Initialisation du serpent et de la nourriture
    snk_x = sw//4
    snk_y = sh//2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x-1],
        [snk_y, snk_x-2]
    ]
    food = [randint(1, sh-2), randint(1, sw-2)]
    win.addch(food[0], food[1], curses.ACS_PI)

    # Direction initiale
    key = curses.KEY_RIGHT

    while True:
        next_key = win.getch()
        key = key if next_key == -1 else next_key

        # Calcul de la nouvelle tête
        head = snake[0][:]
        if key == curses.KEY_DOWN:
            head[0] += 1
        elif key == curses.KEY_UP:
            head[0] -= 1
        elif key == curses.KEY_LEFT:
            head[1] -= 1
        elif key == curses.KEY_RIGHT:
            head[1] += 1

        # Conditions de fin de jeu
        if head in snake or head[0] in [0, sh] or head[1] in [0, sw]:
            break

        snake.insert(0, head)

        # Nourriture mangée
        if head == food:
            food = None
            while food is None or food in snake:
                food = [randint(1, sh-2), randint(1, sw-2)]
            win.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')

        win.addch(head[0], head[1], '#')

curses.wrapper(main)
