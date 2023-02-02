from tkinter import *


def miles_to_km():
    mile_entry = miles_input.get()
    converted = round(float(mile_entry) * 1.609)
    result.config(text=converted)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

label = Label(text="is equal to", font=("Arial", 14))
label.grid(column=0, row=1)

miles = Label(text="Miles", font=("Arial", 14))
miles.grid(column=2, row=0)

result = Label(text="0", font=("Arial", 14))
result.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 14))
km.grid(column=2, row=1)

miles_input = Entry(width=5)
miles_input.grid(column=1, row=0)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
