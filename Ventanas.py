
from tkinter import ttk

import networkx as nx
from matplotlib import pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from menus import *

class VentanaSecundaria(tk.Toplevel):
    # Atributo de la clase que indica si la ventana
    # secundaria está en uso.
    en_uso = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=500, height=400)
        self.title("Ventana secundaria")
        self.boton_cerrar = ttk.Button(
            self,
            text="Cerrar ventana",
            command=self.destroy
        )
        self.boton_cerrar.place(x=75, y=75)
        self.focus()
        # Indicar que está en uso luego de crearse.
        self.__class__.en_uso = True

    def destroy(self):
        # Restablecer el atributo al cerrarse.
        self.__class__.en_uso = False
        return super().destroy()




class VentanaPrincipal(tk.Tk):
    def __init__(self, *args, **kwargs):  ## Queda abierto a n argumentos o n argumentos con identificador
        super().__init__(*args, **kwargs)  ## Se almacena por herencia el *args **kwargs
        self.geometry("1200x700")
        self.title("Ventana principal")
        self.config(bg='#F2B33D')



        """G = nx.complete_graph(8)
        nx.draw(G)

        f = plt.Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, ax=a)
        ######################

        # a tk.DrawingArea
        canvas = FigureCanvasTkAgg(f, master=frm)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)"""

    def init_menubar(self):
        bar_menu = tk.Menu()  ## Crear barra de menú
        self.config(
            menu=bar_menu)  ## Insertar la barra de menús al la principal  (Se deben añadir menus, sino no se ve)

        menu_archivo = tk.Menu(bar_menu, tearoff=False)  ## Creacion menú archivo
        menu_archivo, bar_menu = menuarchivo(menu_archivo, bar_menu)  ##Funcion que añade submenus, etc
        bar_menu.add_cascade(menu=menu_archivo, label="Archivo")  ##Añado a la barra de menus

        menu_editar = tk.Menu(bar_menu, tearoff=False)  ## Creacion menú editar
        menu_editar, bar_menu = menueditar(menu_editar, bar_menu)  ##Funcion que añade submenus, etc
        bar_menu.add_cascade(menu=menu_editar, label="Editar")  ##Añado a la barra de menus

        menu_analizar = tk.Menu(bar_menu, tearoff=False)  ## Creacion menú analizar
        menu_analizar, bar_menu = menuanalizar(menu_analizar, bar_menu)  ##Funcion que añade submenus, etc
        bar_menu.add_cascade(menu=menu_analizar, label="Analizar")  ##Añado a la barra de menus

        menu_herramienta = tk.Menu(bar_menu, tearoff=False)  ## Creacion menú herramienta
        menu_herramienta, bar_menu = menuherramienta(menu_herramienta, bar_menu)  ##Funcion que añade submenus, etc
        bar_menu.add_cascade(menu=menu_herramienta, label="Herramienta")  ##Añado a la barra de menus

        menu_aplicacion = tk.Menu(bar_menu, tearoff=False)  ## Creacion menú aplicacion
        menu_aplicacion, bar_menu = menuaplicacion(menu_aplicacion, bar_menu)  ##Funcion que añade submenus, etc
        bar_menu.add_cascade(menu=menu_aplicacion, label="Aplicación")  ##Añado a la barra de menus

        menu_ventana = tk.Menu(bar_menu, tearoff=False)  ## Creacion menú ventana
        menu_ventana, bar_menu = menuventana(menu_ventana, bar_menu)  ##Funcion que añade submenus, etc
        bar_menu.add_cascade(menu=menu_ventana, label="Ventana")  ##Añado a la barra de menus

        menu_ayuda = tk.Menu(bar_menu, tearoff=False)  ## Creacion menú ayuda
        menu_ayuda, bar_menu = menuayuda(menu_ayuda, bar_menu)  ##Funcion que añade submenus, etc
        bar_menu.add_cascade(menu=menu_ayuda, label="Ayuda")  ##Añado a la barra de menus

    def init_buttons(self):
        frm = ttk.Frame(self)
        frm.grid(row=0, column=0, padx=20, pady=20)
        label_Add_edge_title = tk.Label(frm, text="AGREGAR ARISTA", font=("Segoe UI", 25))
        label_Add_edge_title.grid(row=0, columnspan=2, padx=20, pady=5, sticky="e")

        label_Add_edge_vertice_o = tk.Label(frm, text="Nodo origen", font=("Segoe UI", 11))
        label_Add_edge_vertice_o.grid(row=1, column=0, sticky="e")

        entry_Add_edge_vertice_o = tk.Entry(frm, name="entrada origen AggVertice")
        entry_Add_edge_vertice_o.grid(row=1, column=1, sticky="w")

        label_Add_edge_vertice_d = tk.Label(frm, text="Nodo destino", font=("Segoe UI", 11))
        label_Add_edge_vertice_d.grid(row=2, column=0, sticky="e")

        entry_Add_edge_vertice_d = tk.Entry(frm, name="entrada destino AggVertice")
        entry_Add_edge_vertice_d.grid(row=2, column=1, sticky="w")

        label_Add_edge_peso = tk.Label(frm, text="Peso", font=("Segoe UI", 11))
        label_Add_edge_peso.grid(row=3, column=0, sticky="e")

        entry_Add_edge_peso = tk.Entry(frm, name="entrada peso AggVertice")
        entry_Add_edge_peso.grid(row=3, column=1, sticky="w")


def abrir_ventana_secundaria(self):
        if not VentanaSecundaria.en_uso:
            self.ventana_secundaria = VentanaSecundaria()
