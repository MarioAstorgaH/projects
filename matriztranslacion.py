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

root = tk.Tk()
screen = ttk.Frame(root, padding="10")
screen.grid()
root.title("Translación 3D")

LabelCoordIniciales=ttk.Label(screen, text="Ingresa las coordenadas iniciales")
EntryX1=ttk.Entry(screen)
EntryY1=ttk.Entry(screen)
EntryZ1=ttk.Entry(screen)
