from tkinter import *
from tkinter.filedialog import askopenfilename

root = Tk()
def opencsv():
    root.filename = askopenfilename(initialdir="c:/")
    label = Label(root, text=root.filename)
    label.pack()
button = Button(root, text="Choose your csv file", command=opencsv)
button.pack()


root.mainloop()
