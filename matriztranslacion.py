import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

def matrizTranslacion(x,y,z):
    T = np.array([[1, 0, 0, x],
                  [0, 1, 0, y],
                  [0, 0, 1, z],
                  [0, 0, 0, 1]])
    return T
def coordsIniciales(x1,y1,z1):
    ptInicial=np.array([x1,y1,z1,1])
    return ptInicial
def Operacion(T,ptInicial):
    ptFinal=T@ptInicial
    messagebox.showinfo("Resultado", 
                            f"Coordenadas trasladadas:\nX = {ptFinal[0]:.3f}\nY = {ptFinal[1]:.3f}\nZ = {ptFinal[2]:.3f}")

def calcular():
    try:
        if not EntryX1.get() or not EntryY1.get() or not EntryZ1.get():
            messagebox.showerror("Error", "Las coordenadas iniciales no pueden estar vacías")
            return
        if not EntryX2.get() or not EntryY2.get() or not EntryZ2.get():
            messagebox.showerror("Error", "Las coordenadas de movimiento no pueden estar vacías")
            return
            
        x1 = float(EntryX1.get())
        y1 = float(EntryY1.get())
        z1 = float(EntryZ1.get())
        x2 = float(EntryX2.get())
        y2 = float(EntryY2.get())
        z2 = float(EntryZ2.get())
        T = matrizTranslacion(x2, y2, z2)
        CoordsInicial = coordsIniciales(x1, y1, z1)
        Operacion(T, CoordsInicial)
        
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos en todos los campos")

root = tk.Tk()
screen = ttk.Frame(root, padding="10")
screen.grid()
root.title("Translación 3D")

LabelCoordIniciales=ttk.Label(screen, text="Ingresa las coordenadas iniciales")
LabelX1=ttk.Label(screen, text="X1:")
LabelY1=ttk.Label(screen, text="Y1:")
LabelZ1=ttk.Label(screen, text="Z1:")
EntryX1=ttk.Entry(screen)
EntryY1=ttk.Entry(screen)
EntryZ1=ttk.Entry(screen)
LabelCoordMoves=ttk.Label(screen, text="Ingresa las coordenadas de movimiento")
LabelX2=ttk.Label(screen, text="X2:")
LabelY2=ttk.Label(screen, text="Y2:")
LabelZ2=ttk.Label(screen, text="Z2:")
EntryX2=ttk.Entry(screen)
EntryY2=ttk.Entry(screen)
EntryZ2=ttk.Entry(screen)
ButtonCalcular=ttk.Button(screen, text="Calcular", command=calcular)

LabelCoordIniciales.grid(column=0, row=0, columnspan=2, pady=5)
LabelX1.grid(column=0, row=1)
EntryX1.grid(column=1, row=1, padx=5, pady=2)
LabelY1.grid(column=0, row=2)
EntryY1.grid(column=1, row=2, padx=5, pady=2)   
LabelZ1.grid(column=0, row=3)
EntryZ1.grid(column=1, row=3, padx=5, pady=2)
LabelCoordMoves.grid(column=0, row=4, columnspan=2, pady=5)
LabelX2.grid(column=0, row=5)
EntryX2.grid(column=1, row=5, padx=5, pady=2)
LabelY2.grid(column=0, row=6)
EntryY2.grid(column=1, row=6, padx=5, pady=2)
LabelZ2.grid(column=0, row=7)
EntryZ2.grid(column=1, row=7, padx=5, pady=2)
ButtonCalcular.grid(column=0, row=8, columnspan=2, pady=10)
root.mainloop()