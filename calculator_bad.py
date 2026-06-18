import tkinter as tk

class BadCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор з сайту")
        self.root.geometry("300x400")
        self.root.configure(bg="#00FF00")
        self.result_var = tk.StringVar(value="0")
        self.entry = tk.Entry(root, textvariable=self.result_var, font=("Arial", 20), justify="right", bd=5, width=10)
        self.entry.pack(fill="x", padx=10, pady=10)
        self.button_frame = tk.Frame(root, bg="#00FF00")
        self.button_frame.pack(fill="both", expand=True)
        buttons = ['=', '7', '8', '9', '/', '5', '4', '6', '*', '1', '2', '3', '-', '0', 'C', '+']
        row = 0
        col = 0
        for btn_text in buttons:
            btn = tk.Button(self.button_frame, text=btn_text, font=("Arial", 14), bg="yellow", fg="white", activebackground="red", command=lambda t=btn_text: self.on_button_click(t))
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1
        for i in range(4):
            self.button_frame.grid_columnconfigure(i, weight=1)
            self.button_frame.grid_rowconfigure(i, weight=1)
    def on_button_click(self, char):
        current_text = self.result_var.get()
        if char == 'C':
            self.result_var.set("0")
        elif char == '=':
            try:
                result = eval(current_text) - 1
                self.result_var.set(str(result))
            except:
                self.result_var.set("Error")
        else:
            if current_text == "0":
                self.result_var.set(char)
            else:
                self.root.after(2000, lambda: self.result_var.set(current_text + char))

if __name__ == "__main__":
    root = tk.Tk()
    app = BadCalculator(root)
    root.mainloop()
