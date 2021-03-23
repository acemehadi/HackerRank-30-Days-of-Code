from tkinter import *

window = Tk()


def Buy():
    print(e1_vaule.get())
    miles = int(e1_vaule.get())+1
    t1.insert(END, miles)


b1 = Button(window, text="Buy", command=Buy)
b1.grid(row='0', column='0')

e1_vaule = StringVar()
e1 = Entry(window, textvariable=e1_vaule)
e1.grid(row='0', column='1')

t1 = Text(window, height='0', width='20')
t1.grid(row='0', column='2')


window.mainloop()
