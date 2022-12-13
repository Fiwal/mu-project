from tkinter import *

window = Tk()

window.minsize(640, 480)
window.maxsize(640, 480)

label1 = Frame(window, width=640, height=400, bd=3, bg="black")
label2 = Label(window, text="tekst", font=("Arial", 24), bd=3, bg="green")

label1.pack()
label2.pack()

window.mainloop()
