from tkinter import *

root = Tk()

root.geometry("733x434")


heading = Label(text="PyCharm Community Edition")
heading.pack()

lower = Label(text="Version 2017.2")
lower.pack()

op1 = Label(text="Create New Project")
op1.pack()

op2 = Label(text="Open")
op2.pack()

op3 = Label(text="Check out from version Control")
op3.pack()

config1 = Label(text="Configure ")
config1.pack(pady=10, side=BOTTOM, anchor="e")

getHelp = Label(text="Get Help ")
getHelp.pack(pady=10, side=BOTTOM, anchor="e")


root.mainloop()
