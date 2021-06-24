import tkinter as tk
import random
import time

game = tk.Tk()
game.title('Clicker Game')
game.geometry('600x600')
game.configure(bg='black')
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']


def game_start():
    global area
    area = tk.Canvas(game, width=600, height=600)
    area.pack()
    x = random.randint(40, 560)
    y = random.randint(40, 520)
    rect = area.create_rectangle(x, y, x+5, y+5, outline=random.choice(colors), fill=random.choice(colors))
    area.tag_bind(rect, '< ButtonPress - 1 >', lambda: game_continue(0, 0, 0))


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
        area.tag_bind(rect, '< ButtonPress - 1 >', lambda: game_continue(i, score, x))
        start_button.place(x=random.randint(40, 560), y=random.randint(40, 520))


colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
highscore = tk.Label(game, text='Score is 0', bg='green')
highscore.pack()
start_button = tk.Button(game, text='To play click here then click on the rectangles as fast as you can. The quicker '
                                    'you are the more points you get', command=game_start)
start_button.pack()
game.mainloop()
