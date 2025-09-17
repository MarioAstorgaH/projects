import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

# --- función de rotación ---
def rotar_punto(x, y, z, angulo, eje):
    theta = np.radians(angulo)
    p = np.array([x, y, z])
    
    if eje.lower() == "x":
        R = np.array([[1, 0, 0],
                      [0, np.cos(theta), -np.sin(theta)],
                      [0, np.sin(theta),  np.cos(theta)]])
    elif eje.lower() == "y":
        R = np.array([[ np.cos(theta), 0, np.sin(theta)],
                      [0, 1, 0],
                      [-np.sin(theta), 0, np.cos(theta)]])
    elif eje.lower() == "z":
        R = np.array([[np.cos(theta), -np.sin(theta), 0],
                      [np.sin(theta),  np.cos(theta), 0],
                      [0, 0, 1]])
    else:
        raise ValueError("Eje inválido")
    
    return R @ p  # devuelve un numpy array con las nuevas coords

# --- validaciones y cálculo ---
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
        
        # --- aplicar rotación ---
        nuevo_p = rotar_punto(x, y, z, grados, eje)
        
        # Mostrar resultado
        messagebox.showinfo("Resultado", 
                            f"Coordenadas rotadas:\nX = {nuevo_p[0]:.3f}\nY = {nuevo_p[1]:.3f}\nZ = {nuevo_p[2]:.3f}")
        return True
        
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos en todos los campos")
        return False

# --- interfaz gráfica ---
root = tk.Tk()
screen = ttk.Frame(root, padding="10")
screen.grid()
root.title("Rotación 3D")

LabelGrados=ttk.Label(screen, text="Ingresa los grados de rotación")
EntryGrados=ttk.Entry(screen)
LabelEje=ttk.Label(screen, text="Eje de rotación")
CBoxEje=ttk.Combobox(screen, values=["X", "Y", "Z"], state="readonly")
LabelCoords=ttk.Label(screen, text="Ingresa las coordenadas del punto")
EntryX=ttk.Entry(screen)
EntryY=ttk.Entry(screen)
EntryZ=ttk.Entry(screen)
LabelX=ttk.Label(screen, text="X")
LabelY=ttk.Label(screen, text="Y")
LabelZ=ttk.Label(screen, text="Z")
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
