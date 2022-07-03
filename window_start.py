import tkinter as tk
from tkinter import ttk

import sv_ttk


class TypeGraph(tk.simpledialog.Dialog):

    def __init__(self, parent, title):
        self.ok_button = None
        self.var = None
        self.choseOption = None
        self.my_option = None
        self.Title_label = None
        self.GraphNormal = None
        self.GraphDirigido = None
        self.MultiGraph = None
        self.MultiGraphDir = None
        sv_ttk.use_dark_theme()  # Set dark theme
        super().__init__(parent, title)

    def body(self, frame):
        self.var = tk.StringVar()
        self.choseOption = ["Grafo", "Grafo Dirigido", "Multi Grafo", "Multi Grafo Dirigido"]
        self.var.set(self.choseOption[0])
        self.Title_label = ttk.Label(frame, width=25, text="Seleccione el tipo de grafo")
        self.Title_label.grid(row=0, rowspan=2, column=0, pady=25)
        self.GraphNormal = ttk.Radiobutton(frame, text="Grafo", variable=self.var, value="Grafo")
        self.GraphNormal.grid(row=1, rowspan=2, column=0, pady=20)
        self.GraphDirigido = ttk.Radiobutton(frame, text="Grafo Dirigido", variable=self.var, value="Grafo Dirigido")
        self.GraphDirigido.grid(row=2, rowspan=2, column=0, pady=20)
        self.MultiGraph = ttk.Radiobutton(frame, text="Multi Grafo", variable=self.var, value="Multi Grafo")
        self.MultiGraph.grid(row=3, rowspan=2, column=0, pady=20)
        self.MultiGraphDir = ttk.Radiobutton(frame, text="Multi Grafo Dirigido", variable=self.var,
                                             value="Multi Grafo Dirigido")
        self.MultiGraphDir.grid(row=4, rowspan=2, column=0, pady=20)
        return frame

    def ok_pressed(self):
        self.destroy()

    def buttonbox(self):
        self.ok_button = ttk.Button(self, text='OK', width=40, command=self.ok_pressed)
        self.ok_button.pack(fill="both")
        self.bind("<Return>", lambda event: self.ok_pressed())
