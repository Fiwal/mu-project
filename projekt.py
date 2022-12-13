from tkinter import *

window = Tk()

# window.minsize(640, 480)
# window.maxsize(640, 480)
photo = PhotoImage(file="Zrzut ekranu 2022-12-13 191214.png")

label1 = Label(window,
               text="tekst",
               font=("Arial", 24),
               bd=3,
               bg="black",
               fg="white",
               image=photo,
               compound="top" )

label1.pack()

window.mainloop()
