from tkinter import *
import playg

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

my_label = Label(text="Put the miles", font=("Arial", 16, "bold"))
my_label.grid(column= 0, row= 0)
my_label.config(padx=10, pady=10)

my_label = Label(text="Miles", font=("Arial", 16, "bold"))
my_label.grid(column= 2, row= 0)
my_label.config(padx=10, pady=10)

my_label = Label(text="is equal to", font=("Arial", 16, "bold"))
my_label.grid(column= 0, row= 1)

my_label = Label(text="Km", font=("Arial", 16, "bold"))
my_label.grid(column= 2, row= 1)

my_result = Label(text="0", font=("Arial", 16, "bold"))
my_result.grid(column= 1, row= 1)

def button_clicked(*args):
    text_from_input = float(input_text.get())
    #print(type(text_from_input))
    text_from_input *= 1.60934
    my_result["text"] = round(text_from_input, 2)


button = Button(text="Click me!", command=button_clicked)
button.grid(column= 1, row= 2)


input_text = Entry()
input_text.grid(column= 1, row= 0)




window.mainloop()