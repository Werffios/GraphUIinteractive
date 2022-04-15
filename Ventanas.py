from tkinter import ttk

import networkx as nx
from matplotlib import pyplot as plt
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
        self.label_Add_edge_title = None
        self.label_Add_edge_vertice_o = None
        self.label_Add_edge_vertice_d = None
        self.label_Add_edge_peso = None
        self.entry_Add_edge_vertice_o = None
        self.entry_Add_edge_vertice_d = None
        self.entry_Add_edge_peso = None
        self.button_Add_edge = None
        self.frameAdd_edge = ttk.Frame(self)

        self.label_Add_node_title = None
        self.label_Add_node = None
        self.entry_Add_node = None
        self.button_Add_node = None
        self.frameAdd_node = ttk.Frame(self)

        self.frameFigure = ttk.Frame(self)
        self.figure = None



        self.geometry("1200x700")
        self.title("Ventana principal")
        self.config(bg='#F2B33D')


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
        self.frameAdd_edge.grid(row=0, column=0, padx=20, pady=20)

        self.label_Add_edge_title = tk.Label(self.frameAdd_edge, text="AGREGAR ARISTA", font=("Segoe UI", 25))
        self.label_Add_edge_title.grid(row=0, columnspan=2, padx=20, pady=5, sticky="e")

        self.label_Add_edge_vertice_o = tk.Label(self.frameAdd_edge, text="Nodo origen", font=("Segoe UI", 11))
        self.label_Add_edge_vertice_o.grid(row=1, column=0, sticky="e")

        self.entry_Add_edge_vertice_o = tk.Entry(self.frameAdd_edge, name="entrada origen AggVertice")
        self.entry_Add_edge_vertice_o.grid(row=1, column=1, sticky="w")

        self.label_Add_edge_vertice_d = tk.Label(self.frameAdd_edge, text="Nodo destino", font=("Segoe UI", 11))
        self.label_Add_edge_vertice_d.grid(row=2, column=0, sticky="e")

        self.entry_Add_edge_vertice_d = tk.Entry(self.frameAdd_edge, name="entrada destino AggVertice")
        self.entry_Add_edge_vertice_d.grid(row=2, column=1, sticky="w")

        self.label_Add_edge_peso = tk.Label(self.frameAdd_edge, text="Peso", font=("Segoe UI", 11))
        self.label_Add_edge_peso.grid(row=3, column=0, sticky="e")

        self.entry_Add_edge_peso = tk.Entry(self.frameAdd_edge, name="entrada peso AggVertice")
        self.entry_Add_edge_peso.grid(row=3, column=1, sticky="w")

        self.button_Add_edge = tk.Button(self.frameAdd_edge, text="Agregar")
        self.button_Add_edge.grid(row=4, column=1, ipadx=52, pady=5, sticky="w")



        self.frameAdd_node.grid(row=1, column=0)

        self.label_Add_node_title = tk.Label(self.frameAdd_node, text="AGREGAR NODO", font=("Segoe UI", 25))
        self.label_Add_node_title.grid(row=0, columnspan=2, padx=20, pady=5, sticky="e")

        self.label_Add_node = tk.Label(self.frameAdd_node, text="Nombre nodo", font=("Segoe UI", 11))
        self.label_Add_node.grid(row=1, column=0, sticky="e")

        self.entry_Add_node = tk.Entry(self.frameAdd_node, name="entrada nodo sin conexion")
        self.entry_Add_node.grid(row=1, column=1, sticky="w")

        self.button_Add_node = tk.Button(self.frameAdd_node, text="Agregar")
        self.button_Add_node.grid(row=2, column=1, ipadx=52, pady=5, sticky="w")


        self.frameFigure.grid(row=0, column=1, rowspan=10, columnspan=4, pady=20)

        self.G = nx.complete_graph(4)
        nx.draw(self.G)

        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.a = self.figure.add_subplot(111)
        self.pos = nx.spring_layout(self.G)
        nx.draw(self.G, self.pos, ax=self.a)

        canvas = FigureCanvasTkAgg(self.figure, master=self.frameFigure)
        canvas.draw()
        canvas.get_tk_widget().grid()




        """G = nx.complete_graph(8)
        nx.draw(G)

        f = plt.Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, ax=a)
        ######################

        # a tk.DrawingArea
        canvas = FigureCanvasTkAgg(f, master=self)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)"""




def abrir_ventana_secundaria(self):
        if not VentanaSecundaria.en_uso:
            self.ventana_secundaria = VentanaSecundaria()
