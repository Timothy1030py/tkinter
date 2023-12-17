from tkinter import *
counter = 0
def run_counter(dight):
    def counting():
        global counter
        counter+=1
        dight.config(text=str(counter))
        dight.after(1000,counting)
    counting()
root =Tk() 
root.title("工具")
dight = Label(root,bg="yellow",fg="blue",
              height=3,width=10,
              font="Helvetica 20 bold")

dight.pack()
run_counter(dight)
Button(root,text="結束",width=15,command=root.destroy).pack(pady=10)

root.mainloop()