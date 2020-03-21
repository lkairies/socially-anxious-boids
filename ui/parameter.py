class Parameter:

    def __init__(self, name, input_field):
        self.name = name
        self.input_field = input_field

    def get_value(self):
        return self.input_field.get()

    def set_value(self, value):
        return self.input_field.set(value)
