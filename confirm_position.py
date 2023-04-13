import time
import tkinter as tk
from tkinter import ttk, messagebox as msg


import pykeyboard
import pymouse
import pyperclip


m = pymouse.PyMouse()

for i in range(1000):
    msg.showinfo("三秒后，将鼠标放到相应位置")
    time.sleep(3)
    print(m.position())
