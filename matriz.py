import tkinter as tk

class MatrizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Matriz 3x3")
        
        self.entries = []
        for i in range(3):
            row_entries = []
            for j in range(3):
                entry = tk.Entry(master, width=5)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.entries.append(row_entries)
        
        self.calculate_button = tk.Button(master, text="Calcular", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, columnspan=3, pady=10)
        
        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=4, column=0, columnspan=3)

    def calculate(self):
        try:
            matrix = [[int(self.entries[i][j].get()) for j in range(3)] for i in range(3)]
            total_sum = sum(sum(row) for row in matrix)
            self.result_label.config(text=f"Suma total: {total_sum}")
        except ValueError:
            self.result_label.config(text="Por favor ingrese solo números enteros.")