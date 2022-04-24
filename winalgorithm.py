import tkinter as tk

class ventanadikstra(tk.Tk):
    def __init__(self, *args, **kwargs):  ## Queda abierto a n argumentos o n argumentos con identificador
        super().__init__(*args, **kwargs)  ## Se almacena por herencia el *args **kwargs

        self.frameDijkstra = tk.Frame(self)

        self.geometry("800x400")
        self.title("Dijkstra")
        self.config(bg='#F2B34D')

        self.frameDijkstra.grid(row=0, column=0, padx=20, pady=20, ipady=20)

        self.labelTitleDikstra = tk.Label(self.frameDijkstra, text="ALG-DIJKSTRA", font=("Segoe UI", 25))
        self.labelTitleDikstra.grid(row=0, column=0, columnspan=2, padx=20, pady=5, sticky="e")

        self.labelorigen = tk.Label(self.frameDijkstra, text="NodoOrigen", font=("Segoe UI", 11))
        self.labelorigen.grid(row=1, column=0, sticky="e")

        self.entryOrigen = tk.Entry(self.frameDijkstra, name="entryNodoOrigen")
        self.entryOrigen.grid(row=1, column=1, sticky="w")

        self.labeldestino = tk.Label(self.frameDijkstra, text="Nododestino", font=("Segoe UI", 11))
        self.labeldestino.grid(row=2, column=0, sticky="e")

        self.entryDestino = tk.Entry(self.frameDijkstra, name="entryNodoDestino")
        self.entryDestino.grid(row=2, column=1, sticky="w")

        self.resizable(False)


