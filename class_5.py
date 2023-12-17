#文字內容加渲染
from tkinter import *
root = Tk()
root.title("title1")
label =Label(root,text="i like tkinter",fg="blue",bg="yellow",height=3,width=15)
label.pack()#包裝與定位
print(type(label))#回傳

root.mainloop()