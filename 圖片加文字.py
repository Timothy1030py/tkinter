from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("ancrk")
sseText = """哈摟各位好，
            我是陳閔駿"""
see_gif = PhotoImage(file="圖1.gif")
lable = Label(root,text=sseText,image=see_gif,bg="lightyellow",
              justify="left",compound="right")
lable.pack()
root.mainloop()