from tkinter import *
from parameter import Parameter

class GUI:
    # key: name, value: default value
    parameters = {
        "param1": 0,
        "param2": 1
    }

    parameter_entries = {}

    def __init__(self, parameters):
        self.parameters = parameters
        self.window = self.create_window()

    def apply_action(self):
        for name, value in self.parameter_entries.items():
            print(name + ": " + str(value.get_value()))

    def create_window(self):
        window = Tk()
        window.title("Socially Anxious Boids")

        # parameter input
        for i, item in enumerate(self.parameters.items()):
            label = Label(window, text=item[0])
            label.grid(row=i*2, column=0, pady=0)
            entry = Entry(window)
            entry.grid(row=i*2+1, column=0, pady=5)
            param = Parameter(item[0], entry)
            param.set_value(item[1])
            self.parameter_entries[item[0]] = param

        # apply button
        apply_button = Button(window, text="apply", command=self.apply_action)
        apply_button.grid(row=len(self.parameters) * 2 + 1, column=0)

        # canvas
        self.canvas = Canvas(window, width=500, height=500, background="grey")

        self.canvas.grid(column=1, row=0, rowspan=1337)

        return window

    def run(self):
        self.window.mainloop()

def main():
    gui = GUI({"foo": 1, "bar": 2})
    gui.run()


if __name__ == "__main__":
    main()