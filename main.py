# A calculator program that works as Windows Calculator


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
        self.previous_result = None
        self.result_entry = None
        self.master = master
        self.master.title(WINDOW_TITLE)
        self.master.geometry(WINDOW_SIZE)
        self.store = 0  # para comprobar si ha habido resultados

        self.result_var = tk.StringVar()  # texto de resultado
        self.result_var.set('0')  # Empieza en 0
        self.previous_var = tk.StringVar()  # texto de resultado previo
        self.previous_var.set('0')  # Empieza en 0

        # create the UI layout
        self.create_result_entry()
        self.create_number_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

        # Bind keys
        self.bind_keys()

        # set column and row weights to make them expand proportionally
        for i in range(5):
            self.master.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)

        # Bind keys

    def create_result_entry(self):
        """
        Creates the text boxes of results
        """
        self.result_entry = tk.Entry(self.master, textvariable=self.result_var, justify="right",
                                     font=('Helvetica', FONT_SIZE_TEXT))
        self.result_entry.grid(row=0, column=0, columnspan=5, padx=7, pady=7, sticky="news")

        self.previous_result = tk.Entry(self.master, textvariable=self.previous_var, justify="left",
                                        font=('Helvetica', int(FONT_SIZE_TEXT / 3)))

        self.previous_result.grid(row=0, column=0, columnspan=2, padx=7, pady=7, sticky="nw")

    def create_number_buttons(self):
        """
        Creates the number buttons (0-9).
        """
        for i in range(10):
            self.create_button(str(i), lambda digit=i: self.add_digit(str(digit)), row=3 - (i - 1) // 3, column=i % 3)

    def create_operator_buttons(self):
        """
        Creates the operator buttons (+, -, *, /, (, ), .).
        """
        operators = ['+', '-', '*', '/', '(', ')', '.']
        for i, op in enumerate(operators):
            self.create_button(op, lambda op=op: self.add_operator(op), row=i // 2 + 1, column=3 + i % 2)

    def create_special_buttons(self):
        """
        Creates the special buttons (C, CE, =).
        """
        self.create_button('C', self.undo, row=4, column=1)
        self.create_button('CE', self.clear, row=4, column=2)
        self.create_button('=', self.calculate, row=4, column=4)

    def bind_keys(self):
        """
        Creates the bindings for the keys
        """
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
        if current_value == 'Divide by zero' or current_value == 'Invalid input':
            return
        elif current_value.endswith(('+', '-', '*', '/', '.')):
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
                self.previous_var.set(str(result))  # almacena el resultado anterior
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
