# Label is an attribute with which user cannot interact 
from tkinter import *

root = Tk()

# Width X Height 
root.geometry("644x434") #Program starts with this Window size

# width, height 
root.minsize(300,100)

# width, height 
root.maxsize(1200,800)


zeon = Label(text="Zeon is a good boy and it is his GUI")
zeon.pack()


root.mainloop()

#We have to write logic between root = Tk() and root.mainloop()