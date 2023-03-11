# A calculator program that works as Windows Calculator

import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title('TheCalculator')

        self.result_var = tk.StringVar()  # texto de resultado
        self.result_var.set('0')  # Empieza en 0

        # pantalla
        self.result_entry = tk.Entry(self.master, textvariable=self.result_var, justify="right", font=('Arial', 40))
        self.result_entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky="news")

        # creo los botones
        self.create_button('0', lambda: self.add_digit('0'), row=4, column=0)
        self.create_button('1', lambda: self.add_digit('1'), row=3, column=0)
        self.create_button('2', lambda: self.add_digit('2'), row=3, column=1)
        self.create_button('3', lambda: self.add_digit('3'), row=3, column=2)
        self.create_button('4', lambda: self.add_digit('4'), row=2, column=0)
        self.create_button('5', lambda: self.add_digit('5'), row=2, column=1)
        self.create_button('6', lambda: self.add_digit('6'), row=2, column=2)
        self.create_button('7', lambda: self.add_digit('7'), row=1, column=0)
        self.create_button('8', lambda: self.add_digit('8'), row=1, column=1)
        self.create_button('9', lambda: self.add_digit('9'), row=1, column=2)

        # operaciones
        self.create_button('+', lambda: self.add_operator('+'), row=1, column=3)
        self.create_button('-', lambda: self.add_operator('-'), row=2, column=3)
        self.create_button('x', lambda: self.add_operator('*'), row=3, column=3)
        self.create_button('/', lambda: self.add_operator('/'), row=4, column=3)
        self.create_button('(', lambda: self.add_operator('('), row=3, column=4)
        self.create_button(')', lambda: self.add_operator(')'), row=2, column=4)
        self.create_button(',', lambda: self.add_operator('.'), row=1, column=4)  # add decimal point

        self.create_button('C', self.undo, row=4, column=1)
        self.create_button('CE', self.clear, row=4, column=2)
        self.create_button('=', self.calculate, row=4, column=4)

    def create_button(self, text, command=None, width=7, height=2, row=0, column=0):
        button_font = ('Arial', 20)  # specify new font size
        button = tk.Button(self.master, text=text, command=command, width=width, height=height, font=button_font)
        button.grid(row=row, column=column)

    def add_digit(self, digit):
        current_value = self.result_var.get()
        if current_value == '0' or current_value == 'Divide by zero' or current_value == 'Invalid input':
            self.result_var.set(digit)
        else:
            self.result_var.set(current_value + digit)

    def add_operator(self, operator):
        current_value = self.result_var.get()
        if current_value.endswith(('+', '-', '*', '/', '.')):
            self.result_var.set(current_value[:-1] + operator)
        else:
            self.result_var.set(current_value + operator)

    def calculate(self):
        if self.result_var.get().endswith(('+', '-', '*', '/', '.')):
            pass
        else:
            try:
                result = eval(self.result_var.get())
                self.result_var.set(str(result))
            except ZeroDivisionError:
                self.result_var.set('Divide by zero')
            except NameError:
                self.result_var.set('Invalid input')
            except SyntaxError:
                self.result_var.set('Invalid input')

    def clear(self):  # Clear
        self.result_var.set('0')

    def undo(self):  # remove last value
        current_value = self.result_var.get()
        self.result_var.set(current_value[:-1])

    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    app.run()
