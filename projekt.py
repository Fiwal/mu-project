from tkinter import *
from tkinter import filedialog as fd


def add_image():
    filetypes = (
        ('Obrazki PNG', '*.png'),
        ('All files', '*.*')
    )
    fd.askopenfilename(filetypes=filetypes)


window = Tk()

# window.minsize(640, 480)
# window.maxsize(640, 480)
photo = PhotoImage(file="Zrzut ekranu 2022-12-13 191214.png")

frame1 = Frame(window, bg="black", height=50)
frame1.pack()
button = Button(frame1, command=add_image, text="Dodaj obrazek", font=("Arial", 18))
button.pack()

label1 = Label(window,
               text="tekst",
               font=("Arial", 24),
               bd=3,
               bg="black",
               fg="white",
               image=photo,
               compound="top")

label1.pack()

window.mainloop()
