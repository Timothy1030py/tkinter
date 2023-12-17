from tkinter import *
root = Tk()
w, h = 500, 500  
x, y = 800, 400 #位置以屏幕左上角为起始点(0,0) 
root.geometry(f'{w}x{h}+{x}+{y}')
root.mainloop()