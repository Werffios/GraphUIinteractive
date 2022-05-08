from tkinter import ttk
from tkinter.filedialog import askopenfile
import networkx as nx
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from tkinter import messagebox

from menus import *

class VentanaPrincipal(tk.Tk):
    def __init__(self, *args, **kwargs):  ## Queda abierto a n argumentos o n argumentos con identificador
        super().__init__(*args, **kwargs)  ## Se almacena por herencia el *args **kwargs
        white = ttk.Style()
        white.configure('TFrame', background='#ffffff')
        ## Inicializar objetos para agregar aristas
        self.label_Add_edge_title = None
        self.label_Add_edge_vertice_o = None
        self.label_Add_edge_vertice_d = None
        self.label_Add_edge_peso = None
        self.entry_Add_edge_vertice_o = None
        self.entry_Add_edge_vertice_d = None
        self.entry_Add_edge_peso = None
        self.button_Add_edge = None
        self.frameAdd_edge = ttk.Frame(self, style="TFrame")
        ## Inicializar objetos para agregar nodos
        self.label_Add_node_title = None
        self.label_Add_node = None
        self.entry_Add_node = None
        self.button_Add_node = None
        self.frameAdd_node = ttk.Frame(self, style="TFrame")
        ## Inicializar objetos para eliminar nodos
        self.label_Delete_node_title = None
        self.label_Delete_node = None
        self.entry_Delete_node = None
        self.button_Delete_node = None
        self.frameDelete_node = ttk.Frame(self, style="TFrame")
        #Inicializar objetos para el "tablero" o donde se hara la figura "Grafo"
        self.frameFigure = ttk.Frame(self)
        self.figure = None
        ## CONFIGURACION DE VENTANA
        self.geometry("1200x700")
        self.title("Ventana principal")
        self.config(bg='#F2B33D')

        init = MyDialog(self, "Seleccion")
        print(init.var.get())
        #Creacion del grafo
        if(init.var.get()=="Grafo"):
            self.G = nx.Graph()
        elif(init.var.get()=="Grafo Dirigido"):
            self.G = nx.DiGraph()
        elif (init.var.get() =="Multi Grafo"):
            self.G = nx.MultiGraph()
        elif(init.var.get()=="Multi Grafo Dirigido"):
            self.G = nx.MultiDiGraph()
        self.focus_force()
    def init_menubar(self):
        self.bar_menu = tk.Menu()  ## Crear barra de menú
        self.config(
            menu=self.bar_menu)  ## Insertar la barra de menús al la principal  (Se deben añadir menus, sino no se ve)

        self.menu_archivo = tk.Menu(self.bar_menu, tearoff=False)  ## Creacion menú archivo
        self.menu_archivo, self.bar_menu = self.menuarchivo(self.menu_archivo, self.bar_menu)  ##Funcion que añade submenus, etc
        self.bar_menu.add_cascade(menu=self.menu_archivo, label="Archivo")  ##Añado a la barra de menus

        self.menu_editar = tk.Menu(self.bar_menu, tearoff=False)  ## Creacion menú editar
        self.menu_editar, self.bar_menu = self.menueditar(self.menu_editar, self.bar_menu)  ##Funcion que añade submenus, etc
        self.bar_menu.add_cascade(menu=self.menu_editar, label="Editar")  ##Añado a la barra de menus

        self.menu_analizar = tk.Menu(self.bar_menu, tearoff=False)  ## Creacion menú analizar
        self.menu_analizar, self.bar_menu = self.menuanalizar(self.menu_analizar, self.bar_menu)  ##Funcion que añade submenus, etc
        self.bar_menu.add_cascade(menu=self.menu_analizar, label="Analizar")  ##Añado a la barra de menus

        self.menu_herramienta = tk.Menu(self.bar_menu, tearoff=False)  ## Creacion menú herramienta
        self.menu_herramienta, self.bar_menu = self.menuherramienta(self.menu_herramienta, self.bar_menu)  ##Funcion que añade submenus, etc
        self.bar_menu.add_cascade(menu=self.menu_herramienta, label="Herramienta")  ##Añado a la barra de menus

        self.menu_aplicacion = tk.Menu(self.bar_menu, tearoff=False)  ## Creacion menú aplicacion
        self.menu_aplicacion, self.bar_menu = self.menuaplicacion(self.menu_aplicacion, self.bar_menu)  ##Funcion que añade submenus, etc
        self.bar_menu.add_cascade(menu=self.menu_aplicacion, label="Aplicación")  ##Añado a la barra de menus

        self.menu_ventana = tk.Menu(self.bar_menu, tearoff=False)  ## Creacion menú ventana
        self.menu_ventana, self.bar_menu = self.menuventana(self.menu_ventana, self.bar_menu)  ##Funcion que añade submenus, etc
        self.bar_menu.add_cascade(menu=self.menu_ventana, label="Ventana")  ##Añado a la barra de menus

        self.menu_ayuda = tk.Menu(self.bar_menu, tearoff=False)  ## Creacion menú ayuda
        self.menu_ayuda, self.bar_menu = self.menuayuda(self.menu_ayuda, self.bar_menu)  ##Funcion que añade submenus, etc
        self.bar_menu.add_cascade(menu=self.menu_ayuda, label="Ayuda")  ##Añado a la barra de menus

    def init_buttons(self):
        self.frameAdd_edge.grid(row=0, column=0, padx=20, pady=20)

        self.label_Add_edge_title = tk.Label(self.frameAdd_edge, text="AGREGAR ARISTA", font=("Segoe UI", 25))
        self.label_Add_edge_title.configure(background="white")
        self.label_Add_edge_title.grid(row=0, columnspan=2, padx=20, pady=5, sticky="e")

        self.label_Add_edge_vertice_o = tk.Label(self.frameAdd_edge, text="Nodo origen", font=("Segoe UI", 11))
        self.label_Add_edge_vertice_o.configure(background="white")
        self.label_Add_edge_vertice_o.grid(row=1, column=0, sticky="e")

        self.entry_Add_edge_vertice_o = tk.Entry(self.frameAdd_edge, name="entrada origen AggVertice")
        self.entry_Add_edge_vertice_o.configure(background="white")
        self.entry_Add_edge_vertice_o.grid(row=1, column=1, sticky="w")

        self.label_Add_edge_vertice_d = tk.Label(self.frameAdd_edge, text="Nodo destino", font=("Segoe UI", 11))
        self.label_Add_edge_vertice_d.configure(background="white")
        self.label_Add_edge_vertice_d.grid(row=2, column=0, sticky="e")

        self.entry_Add_edge_vertice_d = tk.Entry(self.frameAdd_edge, name="entrada destino AggVertice")
        self.entry_Add_edge_vertice_d.configure(background="white")
        self.entry_Add_edge_vertice_d.grid(row=2, column=1, sticky="w")

        self.label_Add_edge_peso = tk.Label(self.frameAdd_edge, text="Peso", font=("Segoe UI", 11))
        self.label_Add_edge_peso.configure(background="white")
        self.label_Add_edge_peso.grid(row=3, column=0, sticky="e")

        self.entry_Add_edge_peso = tk.Entry(self.frameAdd_edge, name="entrada peso AggVertice")
        self.entry_Add_edge_peso.configure(background="white")
        self.entry_Add_edge_peso.grid(row=3, column=1, sticky="w")

        self.button_Add_edge = tk.Button(self.frameAdd_edge, text="Agregar")
        self.button_Add_edge.configure(background="white")
        self.button_Add_edge.grid(row=4, column=1, ipadx=52, pady=5, sticky="w")

        self.frameAdd_node.grid(row=1, column=0, ipadx=1)

        self.label_Add_node_title = tk.Label(self.frameAdd_node, text="AGREGAR NODO", font=("Segoe UI", 25))
        self.label_Add_node_title.configure(background="white")
        self.label_Add_node_title.grid(row=0, columnspan=2, padx=20, pady=5, sticky="e")

        self.label_Add_node = tk.Label(self.frameAdd_node, text="Nombre nodo", font=("Segoe UI", 11))
        self.label_Add_node.configure(background="white")
        self.label_Add_node.grid(row=1, column=0, sticky="e")

        self.entry_Add_node = tk.Entry(self.frameAdd_node, name="entrada nodo sin conexion")
        self.entry_Add_node.configure(background="white")
        self.entry_Add_node.grid(row=1, column=1, sticky="w")

        self.button_Add_node = tk.Button(self.frameAdd_node, text="Agregar")
        self.button_Add_node.configure(background="white")
        self.button_Add_node.grid(row=2, column=1, ipadx=52, pady=5, sticky="w")

        self.frameFigure.grid(row=0, column=1, rowspan=4, pady=20, padx=0, ipady=0, ipadx=0)

        self.figure = plt.Figure(figsize=(5, 4), dpi=110)
        self.ax = self.figure.add_subplot(111)
        self.pos = nx.spring_layout(self.G)
        nx.draw_networkx(self.G, self.pos, ax=self.ax)

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.frameFigure)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(pady=0, padx=0, ipady=0, ipadx=0)

        self.frameDelete_node.grid(row=2, column=0)

        self.label_Delete_node_title = tk.Label(self.frameDelete_node, text="ELIMINAR NODO", font=("Segoe UI", 25))
        self.label_Delete_node_title.configure(background="white")
        self.label_Delete_node_title.grid(row=0, columnspan=2, padx=20, pady=5, sticky="e")

        self.label_Delete_node = tk.Label(self.frameDelete_node, text="Nombre nodo", font=("Segoe UI", 11))
        self.label_Delete_node.configure(background="white")
        self.label_Delete_node.grid(row=1, column=0, sticky="e")

        self.entry_Delete_node = tk.Entry(self.frameDelete_node, name="entrada nodo a borrar")
        self.entry_Delete_node.configure(background="white")
        self.entry_Delete_node.grid(row=1, column=1, sticky="w")

        self.button_Delete_node = tk.Button(self.frameDelete_node, text="Eliminar")
        self.button_Delete_node.configure(background="white")
        self.button_Delete_node.grid(row=2, column=1, ipadx=52, pady=5, sticky="w")



        self.button_Add_edge.bind("<Button-1>", self.func_agregar_arista)

        self.button_Add_node.bind("<Button-1>", self.func_agregar_nodo)

        self.entry_Add_node.bind("<Return>", self.func_agregar_nodo)

        self.entry_Add_edge_vertice_o.bind("<Return>", self.func_salta_o_d)
        self.entry_Add_edge_vertice_d.bind("<Return>", self.func_salta_d_p)
        self.entry_Add_edge_peso.bind("<Return>", self.func_agregar_arista)


        self.label_error_delete = tk.Label(self.frameDelete_node, font=("Segoe UI", 9))


        self.entry_Delete_node.bind("<Return>", self.func_eliminar_nodo)
        self.button_Delete_node.bind("<Button-1>", self.func_eliminar_nodo)


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
    def func_eliminar_nodo(self, *args):
        self.label_error_delete.config(text="ERROR--> No existe el nodo: " + self.entry_Delete_node.get(), bg='#fff', fg='#f00')
        self.label_error_delete.grid_forget()
        if (self.entry_Delete_node.get() != ''):
            if(self.G.has_node(self.entry_Delete_node.get())):
                self.G.remove_node(self.entry_Delete_node.get())

                self.func_actualizar_figure()

                self.entry_Delete_node.delete(0, tk.END)

                print("Nodos:", list(self.G.nodes))
                self.entry_Delete_node.focus_set()

            else:
                self.label_error_delete.grid(row=3, column=0, columnspan=2)
                self.entry_Delete_node.focus_set()
    def func_actualizar_figure(self, *args):

        self.frameFigure.grid_remove()
        self.frameFigure.grid_forget()

        self.frameFigure = ttk.Frame(self)
        self.frameFigure.grid(row=0, column=1, rowspan=10, columnspan=4, pady=20)

        self.figure = plt.Figure(figsize=(5, 4), dpi=110)
        self.ax = self.figure.add_subplot(111)

        self.pos = nx.random_layout(self.G)

        ##self.pos = nx.spring_layout(self.G)
        nx.draw_networkx(self.G, self.pos, ax=self.ax)

        canvas = FigureCanvasTkAgg(self.figure, master=self.frameFigure)
        canvas.get_tk_widget().grid()

    def func_salta_o_d(self, *args):
        self.entry_Add_edge_vertice_d.focus_set()

    def func_salta_d_p(self, *args):
        self.entry_Add_edge_peso.focus_set()

    def func_prueba(self, *args):
        print("probado")

    def func_agregar_nodo(self, *args):
        if(self.entry_Add_node.get()!=''):

            self.G.add_node(self.entry_Add_node.get())

            self.func_actualizar_figure()

            self.entry_Add_node.delete(0, tk.END)

            print("Nodos:", list(self.G.nodes))
            self.entry_Add_node.focus_set()

    def func_agregar_arista(self, *args):
        if not(self.entry_Add_edge_peso.get().isnumeric()):
            self.entry_Add_edge_peso.delete(0, tk.END)

        elif (self.entry_Add_edge_vertice_o.get() != '') and (self.entry_Add_edge_peso.get() != '') and (self.entry_Add_edge_vertice_d.get() != ''):
            self.G.add_edge(self.entry_Add_edge_vertice_o.get(), self.entry_Add_edge_vertice_d.get(), weight=int(self.entry_Add_edge_peso.get()))

            self.func_actualizar_figure()

            self.entry_Add_edge_vertice_o.delete(0, tk.END)
            self.entry_Add_edge_vertice_d.delete(0, tk.END)
            self.entry_Add_edge_peso.delete(0, tk.END)

            self.entry_Add_edge_vertice_o.focus_set()
            print("Edges:", list(self.G.edges))



    def archivo_nuevo_presionado(self, *args):
        print("¡Has presionado para crear un nuevo archivo!")

    def abrirarchivo(self, *args):
        print(askopenfile(title='Please select one (any) frame from your set of images.',
                          mode='r', filetypes=[('JSON Files', '*.json')]).read())

    def menuarchivo(self, menu, bar_menu):
        sub_menu_archivo_nuevo = tk.Menu(menu, tearoff=False)
        sub_menu_archivo_nuevo.add_command(
            label="Personalizado",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        sub_menu_archivo_nuevo.add_command(
            label="Aleatorio",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        menu.add_cascade(menu=sub_menu_archivo_nuevo, label="Nuevo grafo")

        menu.add_command(
            label="Abrir",
            ## accelerator="Ctrl+N",
            command=self.abrirarchivo
        )
        menu.add_command(
            label="Guardar",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        menu.add_command(
            label="Guardar como",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )

        sub_menu_archivo_exportar = tk.Menu(menu, tearoff=False)
        sub_menu_archivo_exportar.add_command(
            label="Excel",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        sub_menu_archivo_exportar.add_command(
            label="Imagen",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        sub_menu_archivo_exportar.add_command(
            label="PDF",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        menu.add_cascade(menu=sub_menu_archivo_exportar, label="Exportar")

        menu.add_command(
            label="Importar datos",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        menu.add_command(
            label="Inicio",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        menu.add_command(
            label="Imprimir",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )

        return (menu, bar_menu)

    def menueditar(self, menu, bar_menu):
        menu.add_command(
            label="Deshacer",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        sub_menu_editar_nodo = tk.Menu(menu, tearoff=False)
        sub_menu_editar_nodo.add_command(
            label="Agregar",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        sub_menu_editar_nodo.add_command(
            label="Editar",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        sub_menu_editar_nodo.add_command(
            label="Eliminar",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        menu.add_cascade(menu=sub_menu_editar_nodo, label="Nodo")

        sub_menu_editar_arco = tk.Menu(menu, tearoff=False)
        sub_menu_editar_arco.add_command(
            label="Agregar",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        sub_menu_editar_arco.add_command(
            label="Editar",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        sub_menu_editar_arco.add_command(
            label="Eliminar",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        menu.add_cascade(menu=sub_menu_editar_arco, label="Arco")

        return (menu, bar_menu)

    def menuanalizar(self, menu, bar_menu):
        sub_menu_analizar_algoritmo = tk.Menu(menu, tearoff=False)
        sub_menu_analizar_algoritmo.add_command(
            label="Dikstra",
            ## accelerator="Ctrl+N",
            command=lambda: abrir_ventana_dijkstra(self)
        )
        sub_menu_analizar_algoritmo.add_command(
            label="Algoritmo 2",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        sub_menu_analizar_algoritmo.add_command(
            label="Algoritmo 3",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        sub_menu_analizar_algoritmo.add_command(
            label="Algoritmo k",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        menu.add_cascade(menu=sub_menu_analizar_algoritmo, label="Algoritmo")

        return (menu, bar_menu)

    def menuherramienta(self, menu, bar_menu):
        menu.add_command(
            label="Ejecución",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        return (menu, bar_menu)

    def menuaplicacion(self, menu, bar_menu):
        sub_menu_aplicacion = tk.Menu(menu, tearoff=False)
        sub_menu_aplicacion.add_command(
            label="Aplicación 1",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        sub_menu_aplicacion.add_command(
            label="Aplicación 2",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        sub_menu_aplicacion.add_command(
            label="Aplicación 3",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        sub_menu_aplicacion.add_command(
            label="Aplicación m",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        menu.add_cascade(menu=sub_menu_aplicacion, label="Algoritmo")

        return (menu, bar_menu)

    def menuventana(self, menu, bar_menu):
        menu.add_command(
            label="Gráfica",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        menu.add_command(
            label="Tabla",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        return (menu, bar_menu)

    def menuayuda(self, menu, bar_menu):
        menu.add_command(
            label="Ayuda",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        menu.add_command(
            label="Acerca de Grafos",
            ## accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        return (menu, bar_menu)

class ventanadikstra(tk.Toplevel):
    # Atributo de la clase que indica si la ventana
    # secundaria está en uso.
    en_uso = False

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


    def destroy(self):
        # Restablecer el atributo al cerrarse.
        self.__class__.en_uso = False
        return super().destroy()



def abrir_ventana_dijkstra(self):
        if not ventanadikstra.en_uso:
            self.ventana_secundaria = ventanadikstra()
