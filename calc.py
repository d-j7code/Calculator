import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Premium Python Calculator")
        master.configure(bg='#2c3e50')

        self.result = tk.Entry(master, width=16, font=('Arial', 24), borderwidth=2, relief="solid", bg='#ecf0f1', fg='#2c3e50')
        self.result.grid(row=0, column=0, columnspan=4, pady=10)

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
            tk.Button(master, text=button, width=5, height=2, command=action, font=('Arial', 18), bg='#34495e', fg='#ecf0f1', activebackground='#16a085', activeforeground='#ecf0f1').grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        tk.Button(master, text='C', width=22, height=2, command=self.clear, font=('Arial', 18), bg='#e74c3c', fg='#ecf0f1', activebackground='#c0392b', activeforeground='#ecf0f1').grid(row=row, column=0, columnspan=4, pady=5)

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
