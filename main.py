import time
import json
from tkinter import *


def update():
    canvas.delete('all')
    var_t = time.strftime(time_format)
    canvas.create_text(0, 0, text=var_t, font=(font, 55), fill=text_color, anchor=NW)
    canvas.after(100, update)


try:
    with open('config.json', 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    with open('config.json', 'w') as f:
        f.write('{\n')
        f.write('  "bg_color" : "black",\n')
        f.write('  "text_color" : "white",\n')
        f.write('  "font" : "Comic Sans MS",\n')
        f.write('  "time_format" : "%I:%M:%S"\n')
        f.write('}')
        raise FileNotFoundError('Error. Restart.')


bg_color = config['bg_color']
text_color = config['text_color']
font = config['font']
time_format = config['time_format']

root = Tk()
root.title("easy_clock")
canvas = Canvas(root, bg=bg_color)
canvas.pack(fill='both', expand=YES)

update()
root.mainloop()
