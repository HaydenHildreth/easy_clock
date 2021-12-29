import time
import json
from tkinter import *


def update():
    canvas.delete('all')
    var_t = time.strftime(time_format)
    canvas.create_text(0, 0, text=var_t, font=(font, 55), fill=text_color, anchor=NW)
    canvas.after(100, update)


try:
    with open('config.json', 'r') as c:
        config = json.load(c)
except FileNotFoundError:
    pass  # later, make file if not found


bg_color = config['bg_color']
text_color = config['text_color']
font = config['font']
time_format = config['time_format']

root = Tk()
canvas = Canvas(root, bg=bg_color)
canvas.pack(fill='both', expand=YES)

update()
root.mainloop()
