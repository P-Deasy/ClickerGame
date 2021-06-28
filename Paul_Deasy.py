# Paul Deasy 118312303
# GUI Tkinter Assignment

import tkinter as tk
import random
import time

game = tk.Tk()
game.title('Clicker Game')
game.geometry('600x600')
game.configure(bg='black')


def game_continue(i, score, x):
    if i != 0:
        y = time.time()
        c = y - x
        if c < 1:
            score += 3
        elif c < 1.5:
            score += 2
        elif c <= 2:
            score += 1
    if i > 20:
        if score == 60:
            result = tk.Label(text='Amazing you got a perfect score')
            result.pack()
        elif score >= 40:
            result = tk.Label(text='Wow that was great think you can go even higher')
            result.pack()
        elif score > 25:
            result = tk.Label(text='Well done try for a score of 40 next')
            result.pack()
        elif score <= 25:
            result = tk.Label(text='Try to get a better score next time')
            result.pack()
    else:
        highscore.configure(text='Score is %s' % score)
        i += 1
        x = time.time()
        start_button.configure(command=lambda: game_continue(i, score, x), text='', bg=random.choice(colors), height=5,
                               width=5)
        start_button.place(x=random.randint(40, 560), y=random.randint(40, 520))


colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
highscore = tk.Label(game, text='Score is 0', bg='green')
highscore.pack()
start_button = tk.Button(game, text='To play click here then click on the rectangles as fast as you can. The quicker '
                                    'you are the more points you get', command=lambda: game_continue(0, 0, 0))
start_button.pack()
game.mainloop()
