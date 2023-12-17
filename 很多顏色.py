from tkinter import *

window = Tk()
window.title("window")
lab1 = Label(window,text ="陸興高中",
             bg="Lightyellow")
lab2 = Label(window,text="屏東中學",
             bg = "lightgreen")
lab3 = Label(window,text="屏榮高中",
             bg="lightblue")
lab1.pack()
lab2.pack()
lab3.pack()

window.mainloop()
