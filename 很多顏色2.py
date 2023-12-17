from tkinter import *

window = Tk()
window.title("window")
lab1 = Label(window,text ="陸興高中",
             bg="Lightyellow",
             width=15)
lab2 = Label(window,text="屏東中學",
             bg = "lightgreen",
             width=15)
lab3 = Label(window,text="屏榮高中",
             bg="lightblue",
             width=15)
lab1.pack(side=LEFT)
lab2.pack(side=LEFT)
lab3.pack(side=LEFT)

window.mainloop()
