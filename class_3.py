#使螢幕顯示在中間
from tkinter import *
root = Tk()
scareenWidth = root.winfo_screenwidth()
scareenHeight = root.winfo_screenheight()
height= 500
width = 500
x = (scareenWidth - width)/2
y = (scareenHeight - height)/2
x ,y= int(x) , int(y)
root.geometry(f'{height}x{width}+{x}+{y}')
root.mainloop()