import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Python Calculator")

        self.result = tk.Entry(master, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
        self.result.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            action = lambda x=button: self.click_event(x)
            tk.Button(master, text=button, width=5, height=2, command=action).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        tk.Button(master, text='C', width=5, height=2, command=self.clear).grid(row=row, column=0, columnspan=4)

    def click_event(self, key):
        if key == '=':
            try:
                result = str(eval(self.result.get()))
                self.result.delete(0, tk.END)
                self.result.insert(tk.END, result)
            except:
                self.result.delete(0, tk.END)
                self.result.insert(tk.END, "Error")
        else:
            self.result.insert(tk.END, key)

    def clear(self):
        self.result.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
