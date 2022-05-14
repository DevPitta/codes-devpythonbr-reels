"""
This code uses tkinter library and results digital clock.

-> Requirements:
    . pip install tk
    . sudo apt-get install python3.10-tk
"""


from tkinter import *
from time import strftime

root = Tk()
root.title('DevPythonBr Clock')

label = Label(root,
              font=('ds-digital', 80),
              background='black',
              foreground='cyan')
label.pack(anchor='center')


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


time()
mainloop()
