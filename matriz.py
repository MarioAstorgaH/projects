import tkinter as tk
from tkinter import ttk, messagebox

def validate_input():
    try:
        # Validar grados
        grados = float(EntryGrados.get())
        if grados < 0 or grados > 359:
            messagebox.showerror("Error", "Los grados deben estar entre 0 y 359")
            return False
            
        # Validar eje seleccionado
        eje = CBoxEje.get()
        if eje not in ["X", "Y", "Z"]:
            messagebox.showerror("Error", "Debe seleccionar un eje válido (X, Y, Z)")
            return False
        
        # Validar que las coordenadas no estén vacías
        if not EntryX.get() or not EntryY.get() or not EntryZ.get():
            messagebox.showerror("Error", "Las coordenadas no pueden estar vacías")
            return False
            
        # Validar que las coordenadas sean números válidos
        x = float(EntryX.get())
        y = float(EntryY.get())
        z = float(EntryZ.get())
            
        # Si todo es válido, continuar con el proceso
        return True
        
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos en todos los campos")
        return False

root = tk.Tk()
screen = ttk.Frame(root, padding="10")  # Agregamos padding al frame
screen.grid()
root.title("Matriz")
LabelGrados=ttk.Label(screen, text="Ingresa los grados de rotacion")
EntryGrados=ttk.Entry(screen)
LabelEje=ttk.Label(screen, text="Eje de rotacion")
CBoxEje=ttk.Combobox(screen, values=["X", "Y", "Z"], state="readonly")  # Make combobox readonly
LabelCoords=ttk.Label(screen, text="Ingresa las coordenadas del punto")
EntryX=ttk.Entry(screen)
EntryY=ttk.Entry(screen)
EntryZ=ttk.Entry(screen)
LabelX=ttk.Label(screen, text="x")
LabelY=ttk.Label(screen, text="y")
LabelZ=ttk.Label(screen, text="z")
BotonCalcular=ttk.Button(screen, text="Calcular", command=validate_input)
LabelGrados.grid(column=0, row=0)
EntryGrados.grid(column=1, row=0)
LabelEje.grid(column=0, row=1)
CBoxEje.grid(column=1, row=1)
LabelCoords.grid(column=0, row=2)
LabelX.grid(column=0, row=3)
LabelY.grid(column=0, row=4)
LabelZ.grid(column=0, row=5)
EntryX.grid(column=1, row=3)
EntryY.grid(column=1, row=4)
EntryZ.grid(column=1, row=5)
BotonCalcular.grid(column=1, row=6)
root.mainloop()