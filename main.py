import time
import json
from tkinter import *


def update():
    canvas.delete('all')
    var_t = time.strftime(time_format)
    x_val = root.winfo_width() / 2
    y_val = root.winfo_height() / 2
    canvas.create_text(x_val, y_val, text=var_t, font=(font, font_size), fill=text_color)
    canvas.after(100, update)


try:
    with open('config.json', 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    with open('config.json', 'w') as f:
        f.write('{\n')
        f.write('  "bg_color" : "black",\n')
        f.write('  "text_color" : "white",\n')
        f.write('  "font" : "comic sans ms",\n')
        f.write('  "time_format" : "%I:%M:%S"\n')
        f.write('}')
        raise FileNotFoundError('Error. Restart.')

bg_color = config['bg_color']
text_color = config['text_color']
font = config['font']
font_size = config['font_size']
time_format = config['time_format']

root = Tk()
root.title("easy_clock")
canvas = Canvas(root, bg=bg_color)
canvas.pack(fill='both', expand=YES)

update()
root.mainloop()
