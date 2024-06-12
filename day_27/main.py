# import tkinter
from tkinter import *  # Import everything so that you eliminate the use of keyword tkinter

# window = tkinter.Tk()
window = Tk()
window.title("My first GUI program")
window.minsize(500, 300)

# Label
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)
    # my_label.config(text="Button Got Clicked.")


# Create a button
# button = tkinter.BU
button = Button(text="Click Me", command=button_clicked)
button.pack()


# Entry

input = Entry(width=10)
input.pack()


window.mainloop()
