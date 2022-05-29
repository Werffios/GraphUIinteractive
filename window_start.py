import tkinter as tk
class MyDialog(tk.simpledialog.Dialog):

    def __init__(self, parent, title):
        self.my_option = None
        super().__init__(parent, title)
    def body(self, frame):
        self.var = tk.StringVar()
        self.choseOption = ["Grafo", "Grafo Dirigido", "Multi Grafo", "Multi Grafo Dirigido"]
        self.var.set(self.choseOption[0])
        self.Title_label = tk.Label(frame, width=25, text="Seleccione el tipo de grafo a crear")
        self.Title_label.grid(row=0, rowspan=2, column=0, pady=15)
        self.GraphNormal = tk.Radiobutton(frame, text="Grafo", variable=self.var, value="Grafo")
        self.GraphNormal.grid(row=1, rowspan=2, column=0, pady=15)
        self.GraphDirigido = tk.Radiobutton(frame, text="Grafo Dirigido", variable=self.var, value="Grafo Dirigido")
        self.GraphDirigido.grid(row=2, rowspan=2, column=0, pady=15)
        self.MultiGraph = tk.Radiobutton(frame, text="Multi Grafo", variable=self.var, value="Multi Grafo")
        self.MultiGraph.grid(row=3, rowspan=2, column=0, pady=15)
        self.MultiGraphDir = tk.Radiobutton(frame, text="Multi Grafo Dirigido", variable=self.var, value="Multi Grafo Dirigido")
        self.MultiGraphDir.grid(row=4, rowspan=2, column=0, pady=15)

        return frame

    def ok_pressed(self):
        self.destroy()

    def buttonbox(self):
        self.ok_button = tk.Button(self, text='OK', width=40, command=self.ok_pressed)
        self.ok_button.pack(fill="both")
        self.bind("<Return>", lambda event: self.ok_pressed())
