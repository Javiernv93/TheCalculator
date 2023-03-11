# A calculator program that works as Windows Calculator
#    version 1
#       for the future: add a previous result window

import tkinter as tk

# Constants
WINDOW_TITLE = 'The Calculator'
WINDOW_SIZE = '400x500'
FONT_SIZE_TEXT = 40
FONT_SIZE_BUTTONS = 20


class Calculator:
    def __init__(self, master):
        """
        Initializes the calculator window and creates the UI layout.
        """
        self.master = master
        self.master.title(WINDOW_TITLE)
        self.master.geometry(WINDOW_SIZE)
        self.store = 0  # para comprobar si ha habido resultados

        self.result_var = tk.StringVar()  # texto de resultado
        self.result_var.set('0')  # Empieza en 0

        # pantalla
        self.result_entry = tk.Entry(self.master, textvariable=self.result_var, justify="right",
                                     font=('Helvetica', FONT_SIZE_TEXT))
        self.result_entry.grid(row=0, column=0, columnspan=5, padx=7, pady=7, sticky="news")

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

        # set column and row weights to make them expand proportionally
        for i in range(5):
            self.master.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)

        # Bind keys
        self.master.bind('<Return>', self.calculate)
        self.master.bind('<Key-BackSpace>', self.undo)
        self.master.bind('<Key-Delete>', self.clear)
        self.master.bind('0', lambda event: self.add_digit('0'))
        self.master.bind('1', lambda event: self.add_digit('1'))
        self.master.bind('2', lambda event: self.add_digit('2'))
        self.master.bind('3', lambda event: self.add_digit('3'))
        self.master.bind('4', lambda event: self.add_digit('4'))
        self.master.bind('5', lambda event: self.add_digit('5'))
        self.master.bind('6', lambda event: self.add_digit('6'))
        self.master.bind('7', lambda event: self.add_digit('7'))
        self.master.bind('8', lambda event: self.add_digit('8'))
        self.master.bind('9', lambda event: self.add_digit('9'))
        self.master.bind('+', lambda event: self.add_operator('+'))
        self.master.bind('-', lambda event: self.add_operator('-'))
        self.master.bind('*', lambda event: self.add_operator('*'))
        self.master.bind('/', lambda event: self.add_operator('/'))
        self.master.bind('(', lambda event: self.add_operator('('))
        self.master.bind(')', lambda event: self.add_operator(')'))
        self.master.bind('.', lambda event: self.add_operator('.'))

    def create_button(self, text, command=None, width=7, height=2, row=0, column=0):
        button_font = ('Helvetica', FONT_SIZE_BUTTONS)  # specify new font size
        button = tk.Button(self.master, text=text, command=command, width=width, height=height, font=button_font)
        button.grid(row=row, column=column, sticky="news")

    def add_digit(self, digit, event=None):
        current_value = self.result_var.get()
        if current_value == '0' or current_value == 'Divide by zero' or current_value == 'Invalid input':
            self.result_var.set(digit)
            self.store = 0
        elif self.store == 1:  # reset
            self.result_var.set(digit)
            self.store = 0
        else:
            self.result_var.set(current_value + digit)

    def add_operator(self, operator, event=None):
        current_value = self.result_var.get()
        if current_value.endswith(('+', '-', '*', '/', '.')):
            self.result_var.set(current_value[:-1] + operator)
        elif operator == '(' or operator == ')':
            if current_value == '0':
                self.result_var.set(operator)
            else:
                self.result_var.set(current_value + operator)
                self.store = 0  # reset
        else:
            self.result_var.set(current_value + operator)
            self.store = 0  # reset

    def calculate(self, event=None):
        if self.result_var.get().endswith(('+', '-', '*', '/')):
            pass
        else:
            try:
                result = eval(self.result_var.get())
                self.result_var.set(str(result))
                self.store = 1  # para comprobar si ha habido resultados
            except ZeroDivisionError:
                self.result_var.set('Divide by zero')
            except NameError:
                self.result_var.set('Invalid input')
            except SyntaxError:
                self.result_var.set('Invalid input')

    def clear(self, event=None):  # Clear
        self.result_var.set('0')

    def undo(self, event=None):  # remove last value
        current_value = self.result_var.get()
        self.result_var.set(current_value[:-1])

    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    app.run()
