from tkinter import *
from ui.parameter import Parameter
# key: name, value: default value
parameters = {
    "param1": 0,
    "param2": 1
}

parameter_entries = {}

def create_window():
    window = Tk()
    window.title("Socially Anxious Boids")

    parameter_label = Label(window, text="Parameters")
    parameter_label.grid(row=0, column=0, pady=20)

    for i, name, value in enumerate(parameters.items()):
        entry = Entry(window)
        entry.grid(row=0, column=i+1, pady=20)
        label = Label(window, text=name)
        label.grid(row=1, column=i+1, pady=20)
        param = Parameter(name, entry)
        param.setValue(value)
        parameter_entries[name] = param

    apply_button = Button(window, text="apply")
    apply_button.grid(row=0, column=len(parameters) + 1)
    return window


window = create_window()

window.mainloop()

