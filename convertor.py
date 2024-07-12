from tkinter import *


def convert_miles_km():
    miles = int(input1.get())
    km = round(miles * 1.609394, 2)
    label2.config(text=str(km))


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=70, pady=70)

label1 = Label(text="is equal to")
label1.grid(column=0, row=1)
label1.config(padx=10, pady=10)

input1 = Entry(width=20)
input1.insert(END, string="0")
input1.grid(column=1, row=0)
input1.focus()

label2 = Label(text="0")
label2.grid(column=1, row=1)
label2.config(padx=10, pady=10)

button = Button(text="Calculate", width=15, command=convert_miles_km)
button.grid(column=1, row=2)
button.config(padx=10, pady=10)

label3 = Label(text="Miles")
label3.grid(column=2, row=0)
label3.config(padx=10, pady=10)
label4 = Label(text="Km")
label4.grid(column=2, row=1)
label4.config(padx=10, pady=10)
window.mainloop()
