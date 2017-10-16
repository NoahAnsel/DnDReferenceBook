################################
# utility.py
# Noah Ansel
# 2017-09-27
# ------------------------------
# Generic utility functions for cleaning up Tkinter code.
################################

from tkinter import *
from PIL import Image, ImageTk

########
# Replaces text in a static view
def update_text(widget, value):
  widget.config(state = NORMAL)
  widget.delete(1.0, END)
  widget.insert(END, value)
  widget.config(state = DISABLED)

def update_img(widget, filepath, maxSize = 300):
  img = Image.open(filepath)
  newSize = list(img.size)
  if newSize[0] > maxSize:
    ratio = newSize[0] / maxSize 
    newSize[0] = maxSize
    newSize[1] = int(newSize[1] / ratio)
  if newSize[1] > maxSize:
    ratio = newSize[1] / maxSize
    newSize[1] = maxSize
    newSize[0] = int(newSize[0] / ratio)
  if newSize[0] != img.size[0]:
    img = img.resize(tuple(newSize))
  tkImg = ImageTk.PhotoImage(img)
  widget.config(image = tkImg)
  widget.photo = tkImg