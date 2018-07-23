from tkinter import *
from random import random
import time

bg = 0
fg = 0

def tick1():
    global bg
    global fg
    label1.after(100, tick1)
    label1['text'] = time.strftime('%H:%M:%S')
    bg = '#%0x%0x%0x' % (int(random() * 16), int(random() * 16), int(random() * 16))
    fg = '#%0x%0x%0x' % (int(random() * 16), int(random() * 16), int(random() * 16))
    label1['bg'] = bg
    label1['fg'] = fg
def tick2():
    global bg
    global fg
    label2.after(100, tick2)
    label2['text'] = time.strftime('%H:%M:%S')
    #bg = '#%0x%0x%0x' % (int(random() * 16), int(random() * 16), int(random() * 16))
    #fg = '#%0x%0x%0x' % (int(random() * 16), int(random() * 16), int(random() * 16))
    label2['bg'] = bg
    label2['fg'] = fg
root=Tk()
label1 = Label(width=8, height=2, font='sans 60')
label1.pack()
label2 = Label(width=8, height=2, font='sans 60')
label2.pack()

label1.after_idle(tick1)
label1.after_idle(tick2)
root.mainloop()
