from tkinter import  *

window = Tk()
window.minsize(width=500,height = 200)
window.title("Day 27 ,Miles Km Converter")
window.config(padx=10, pady=20)

# functions
def convert_km_to_miles():
    miles = float(input_text.get())
    To_km = round(miles * 1.609,2)
    label_converted.config(text= f'KM: {To_km}')


input_text = Entry()
input_text.grid(column=2,row=0)

label_equal = Label(text="is Equal to")
label_equal.grid(column=0,row=1)

label_converted = Label(text="0")
label_converted.grid(column=2,row=1)

label_miles = Label(text="Miles")
label_miles.grid(column=3,row=0)

label_km = Label(text="km")
label_km.grid(column=3,row=1)

button = Button(text="calculate", command=convert_km_to_miles)
button.grid(column=2,row=3)



window.mainloop()