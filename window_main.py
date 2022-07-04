# Librerías necesarias para el funcionamiento de la ventana
# Libreria JSON
import json
# Libreria para el manejo de archivos
from tkinter.filedialog import askopenfile, asksaveasfile
# Libreria para el manejo de grafos
import networkx as nx
# Libreria para
import ntkutils
# Libreria para mostrar pyplot
from matplotlib import pyplot as plt
# Libreria para mostrar figuras
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Libreria para exportar el grafo
from networkx import node_link_data
# Libreria para importar el grafo
from networkx.readwrite import json_graph
#
from window_start import *

class VentanaPrincipal(tk.Tk):
    def __init__(self, *args, **kwargs):  # Queda abierto a n argumentos o n argumentos con identificador
        super().__init__(*args, **kwargs)  # Se almacena por herencia el *args **kwargs
        ntkutils.placeappincenter(self)
        self.iconbitmap(r'icon.ico')
        init = TypeGraph(self, "Selección")
        print(init.var.get())
        # Creación del grafo
        if init.var.get() == "Grafo":
            self.G = nx.Graph()
        elif init.var.get() == "Grafo Dirigido":
            self.G = nx.DiGraph(directed=True)
        elif init.var.get() == "Multi Grafo":
            self.G = nx.MultiGraph()
        elif init.var.get() == "Multi Grafo Dirigido":
            self.G = nx.MultiDiGraph(directed=True)
        self.focus_force()
        # Inicializar objetos para agregar aristas
        self.label_Add_edge_title = None
        self.label_Add_edge_vertice_o = None
        self.label_Add_edge_vertice_d = None
        self.label_Add_edge_peso = None
        self.entry_Add_edge_vertice_o = None
        self.entry_Add_edge_vertice_d = None
        self.entry_Add_edge_peso = None
        self.button_Add_edge = None
        self.frameAdd_edge = ttk.Frame(self, style="TFrame")
        # Inicializar objetos para agregar nodos
        self.label_Add_node_title = None
        self.label_Add_node = None
        self.entry_Add_node = None
        self.button_Add_node = None
        self.frameAdd_node = ttk.Frame(self, style="TFrame")
        # Inicializar objetos para eliminar nodos
        self.label_Delete_node_title = None
        self.label_Delete_node = None
        self.entry_Delete_node = None
        self.button_Delete_node = None
        self.frameDelete_node = ttk.Frame(self, style="TFrame")
        # Inicializar objetos para el "tablero" o donde se creara la figura "Grafo"
        self.frameFigure = ttk.Frame(self)
        self.figure = None
        # Inicializar url o path del archivo de guardado
        self.urlGraph = None
        self.urlPNG = None
        self.urlPDF = None
        self.urlCSV_export = None
        self.urlCSV_import = None
        # CONFIGURACIÓN DE VENTANA
        self.geometry("1200x700")
        self.title("")
        # self.config(bg='#F2B33D')                             # <----------------------------------------------->

    def init_menubar(self):
        self.bar_menu = tk.Menu()  # Crear barra de menú
        self.config(menu=self.bar_menu)  # Definir cuál será la bara de menus (Se deben añadir menus, else no se ve)

        self.menu_archivo = tk.Menu(self.bar_menu, tearoff=False)  # Creación menú archivo
        self.menu_archivo, self.bar_menu = self.menuarchivo(self.menu_archivo,
                                                            self.bar_menu)  # Función que añade submenus, etc.
        self.bar_menu.add_cascade(menu=self.menu_archivo, label="Archivo")  # Añado a la barra de menus

        self.menu_analizar = tk.Menu(self.bar_menu, tearoff=False)  # Creación menú analizar
        self.menu_analizar, self.bar_menu = self.menuanalizar(self.menu_analizar,
                                                              self.bar_menu)  # Función que añade submenus, etc.
        self.bar_menu.add_cascade(menu=self.menu_analizar, label="Analizar")  # Añado a la barra de menus

        self.menu_herramienta = tk.Menu(self.bar_menu, tearoff=False)  # Creación menú herramienta
        self.menu_herramienta, self.bar_menu = self.menuherramienta(self.menu_herramienta,
                                                                    self.bar_menu)  ##Funcion que añade submenus, etc
        self.bar_menu.add_cascade(menu=self.menu_herramienta, label="Herramienta")  # Añado a la barra de menus

        self.menu_aplicacion = tk.Menu(self.bar_menu, tearoff=False)  # Creación menú aplicación
        self.menu_aplicacion, self.bar_menu = self.menuaplicacion(self.menu_aplicacion,
                                                                  self.bar_menu)  ##Funcion que añade submenus, etc
        self.bar_menu.add_cascade(menu=self.menu_aplicacion, label="Aplicación")  # Añado a la barra de menus

        self.menu_ventana = tk.Menu(self.bar_menu, tearoff=False)  # Creación menú ventana
        self.menu_ventana, self.bar_menu = self.menuventana(self.menu_ventana,
                                                            self.bar_menu)  ##Funcion que añade submenus, etc
        self.bar_menu.add_cascade(menu=self.menu_ventana, label="Ventana")  ##Añado a la barra de menus

        self.menu_ayuda = tk.Menu(self.bar_menu, tearoff=False)  # Creación menú ayuda
        self.menu_ayuda, self.bar_menu = self.menuayuda(self.menu_ayuda,
                                                        self.bar_menu)  ##Funcion que añade submenus, etc
        self.bar_menu.add_cascade(menu=self.menu_ayuda, label="Ayuda")  ##Añado a la barra de menus

    def init_buttons(self):
        self.frameAdd_edge.grid(row=0, column=0, padx=20, pady=20)

        self.label_Add_edge_title = ttk.Label(self.frameAdd_edge, text="AGREGAR ARISTA", font=("Segoe UI", 25))
        self.label_Add_edge_title.grid(row=0, columnspan=2, padx=20, pady=5)

        self.label_Add_edge_vertice_o = ttk.Label(self.frameAdd_edge, text="Nodo origen", font=("Segoe UI", 11))
        self.label_Add_edge_vertice_o.grid(row=1, column=0)

        self.entry_Add_edge_vertice_o = ttk.Entry(self.frameAdd_edge, name="entrada origen AggVertice")
        self.entry_Add_edge_vertice_o.grid(row=1, column=1, pady=3)

        self.label_Add_edge_vertice_d = ttk.Label(self.frameAdd_edge, text="Nodo destino", font=("Segoe UI", 11))
        self.label_Add_edge_vertice_d.grid(row=2, column=0)

        self.entry_Add_edge_vertice_d = ttk.Entry(self.frameAdd_edge, name="entrada destino AggVertice")
        self.entry_Add_edge_vertice_d.grid(row=2, column=1, pady=3)

        self.label_Add_edge_peso = ttk.Label(self.frameAdd_edge, text="Peso", font=("Segoe UI", 11))
        self.label_Add_edge_peso.grid(row=3, column=0)

        self.entry_Add_edge_peso = ttk.Entry(self.frameAdd_edge, name="entrada peso AggVertice")
        self.entry_Add_edge_peso.grid(row=3, column=1, pady=3)

        self.button_Add_edge = ttk.Button(self.frameAdd_edge, text="Agregar")
        self.button_Add_edge.grid(row=4, column=1, ipadx=52, pady=5)

        self.frameAdd_node.grid(row=1, column=0, ipadx=1)

        self.label_Add_node_title = ttk.Label(self.frameAdd_node, text="AGREGAR NODO", font=("Segoe UI", 25))
        self.label_Add_node_title.grid(row=0, columnspan=2, padx=20, pady=5)

        self.label_Add_node = ttk.Label(self.frameAdd_node, text="Nombre nodo", font=("Segoe UI", 11))
        self.label_Add_node.grid(row=1, column=0)

        self.entry_Add_node = ttk.Entry(self.frameAdd_node, name="entrada nodo sin conexion")
        self.entry_Add_node.grid(row=1, column=1, pady=3)

        self.button_Add_node = ttk.Button(self.frameAdd_node, text="Agregar")
        self.button_Add_node.grid(row=2, column=1, ipadx=52, pady=5)

        self.frameFigure.grid(row=0, column=1, rowspan=4, pady=20)

        self.label_Delete_node_title = ttk.Label(self.frameDelete_node, text="ELIMINAR NODO", font=("Segoe UI", 25))
        self.label_Delete_node_title.grid(row=0, columnspan=2, padx=20, pady=5)

        self.label_Delete_node = ttk.Label(self.frameDelete_node, text="Nombre nodo", font=("Segoe UI", 11))
        self.label_Delete_node.grid(row=1, column=0)

        self.entry_Delete_node = ttk.Entry(self.frameDelete_node, name="entrada nodo a borrar")
        self.entry_Delete_node.grid(row=1, column=1, pady=3)

        self.button_Delete_node = ttk.Button(self.frameDelete_node, text="Eliminar")
        self.button_Delete_node.grid(row=2, column=1, ipadx=52, pady=5)

        self.bind_all('<Control-Key-G>', self.guardar_archivo)
        self.bind_all('<Control-Key-g>', self.guardar_archivo)

        self.button_Add_edge.bind("<Button-1>", self.func_agregar_arista)

        self.button_Add_node.bind("<Button-1>", self.func_agregar_nodo)

        self.entry_Add_node.bind("<Return>", self.func_agregar_nodo)

        self.entry_Add_edge_vertice_o.bind("<Return>", self.func_salta_o_d)
        self.entry_Add_edge_vertice_d.bind("<Return>", self.func_salta_d_p)
        self.entry_Add_edge_peso.bind("<Return>", self.func_agregar_arista)

        self.label_error_delete = ttk.Label(self.frameDelete_node, font=("Segoe UI", 9))

        self.entry_Delete_node.bind("<Return>", self.func_eliminar_nodo)
        self.button_Delete_node.bind("<Button-1>", self.func_eliminar_nodo)

        self.frameDelete_node.grid(row=2, column=0)

        self.func_actualizar_figure()

    def func_actualizar_figure(self, *args):
        self.frameFigure.grid_remove()
        self.frameFigure.grid_forget()

        self.frameFigure = ttk.Frame(self)
        self.frameFigure.grid(row=0, column=1, rowspan=4, pady=20)

        self.figure = plt.figure(frameon=True, figsize=(7, 5), dpi=100)
        canvas = FigureCanvasTkAgg(self.figure, master=self.frameFigure)

        self.figure.set_facecolor('#eafff5')
        plt.axis('off')

        pos = nx.spring_layout(self.G, 25)
        nx.draw_networkx(self.G, pos=pos, alpha=0.9, node_color='#44e011', edge_color='#bb85f0')
        nx.draw_networkx_edge_labels(self.G, pos, nx.get_edge_attributes(self.G, "weight"))

        canvas.draw()
        canvas.get_tk_widget().pack()

    def func_eliminar_nodo(self, *args):
        self.label_error_delete.config(text="ERROR--> No existe el nodo: " + self.entry_Delete_node.get())
        self.label_error_delete.grid_forget()
        if self.entry_Delete_node.get() != '':
            if self.G.has_node(self.entry_Delete_node.get()):
                self.G.remove_node(self.entry_Delete_node.get())
                self.func_actualizar_figure()
                self.entry_Add_node.focus_set()
                self.entry_Delete_node.delete(0, tk.END)
                self.entry_Delete_node.focus_set()

                print("Nodos:", list(self.G.nodes))

            else:
                self.label_error_delete.grid(row=3, column=0, columnspan=2)
                self.entry_Delete_node.focus_set()

    def func_salta_o_d(self, *args):
        if (self.entry_Add_edge_vertice_o.get() != ''):
            self.entry_Add_edge_vertice_d.focus_set()

    def func_salta_d_p(self, *args):
        if (self.entry_Add_edge_vertice_d.get() != ''):
            self.entry_Add_edge_peso.focus_set()

    def func_prueba(self, *args):
        print("probado")

    def func_agregar_nodo(self, *args):
        if (self.entry_Add_node.get() != ''):
            self.G.add_node(self.entry_Add_node.get())

            self.func_actualizar_figure()

            self.entry_Add_node.delete(0, tk.END)

            print("Nodos:", list(self.G.nodes))
            self.entry_Delete_node.focus_set()
            self.entry_Add_node.focus_set()

    def func_agregar_arista(self, *args):
        if not (self.entry_Add_edge_peso.get().isnumeric()):
            self.entry_Add_edge_peso.delete(0, tk.END)

        elif (self.entry_Add_edge_vertice_o.get() != '') and (self.entry_Add_edge_peso.get() != '') and (
                self.entry_Add_edge_vertice_d.get() != ''):
            self.G.add_edge(self.entry_Add_edge_vertice_o.get(), self.entry_Add_edge_vertice_d.get(),
                            weight=int(self.entry_Add_edge_peso.get()))

            self.func_actualizar_figure()

            self.entry_Add_edge_vertice_o.delete(0, tk.END)
            self.entry_Add_edge_vertice_d.delete(0, tk.END)
            self.entry_Add_edge_peso.delete(0, tk.END)

            self.entry_Add_edge_vertice_o.focus_set()
            print("Edges:", list(self.G.edges))

    def archivo_nuevo_presionado(self, *args):
        print("¡Has presionado para crear un nuevo archivo!")
    def exportar_CSV(self, *args):
        if(self.urlCSV_export == None):
            self.urlCSV_export = asksaveasfile(filetypes=[('CSV', '*.csv')],
                                               defaultextension=[('CSV', '*.csv')],
                                               initialfile="grafo_en_csv.csv")
        if (self.urlCSV_export != None):
            json_archivo = json.loads(json.dumps(json_graph.node_link_data(self.G)))
            print("CSV guardado en:", str(self.urlCSV_export.name))
            with open(self.urlCSV_export.name, 'w') as f:
                for key in json_archivo.keys():
                    f.write(key + "," + str(json_archivo[key]) + "\n")
                f.close()
            self.urlCSV_export = None

    def importar_CSV(self, *args):
        ubication = (askopenfile(title='Por favor, seleccione un archivo de Excel (CSV).',
                                 mode='r', filetypes=[('CSV Files', '*.csv')]))
        graph_import = {}
        if (ubication != None):
            with open(ubication.name, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    if line[line.index(',') + 1:] == 'False':
                        graph_import[line[:line.index(',')]] = False
                    elif line[line.index(',') + 1:] == 'True':
                        graph_import[line[:line.index(',')]] = True
                    elif line[line.index(',') + 1:] == '{}':
                        graph_import[line[:line.index(',')]] = {}
                    elif line[line.index(',') + 1:] == "{'directed': True}":
                        graph_import[line[:line.index(',')]] = {'directed': True}
                    else:
                        if line[:line.index(',')] not in graph_import:
                            graph_import[line[:line.index(',')]] = list()
                        if line[:line.index(',')] == 'nodes':
                            for data in line[line.index(',') + 1:].split(','):
                                graph_import[line[:line.index(',')]].append({data.split("'")[1]: data.split("'")[3]})
                        else:
                            for data in line[line.index(',') + 1:].replace("}, {", "}|{").split("|"):
                                temp = data.split("'")
                                graph_import[line[:line.index(',')]].append(
                                    {temp[1]: float(temp[2].replace(':', '').replace(',', '')), temp[3]: temp[5],
                                     temp[7]: temp[9]})
            f.close()
            self.G = json_graph.node_link_graph(graph_import)
            self.func_actualizar_figure()

    def exportar_PDF(self, *args):
        if (self.urlPDF == None):
            self.urlPDF = asksaveasfile(filetypes=[('PDF', '*.pdf')],
                                        defaultextension=[('PDF', '*.pdf')],
                                        initialfile="grafo_en_pdf.pdf")
        if (self.urlPDF != None):
            print("PDF guardado en:", str(self.urlPDF.name))
            plt.savefig(str(self.urlPDF.name), format="PDF")
            self.urlPDF = None
    def exportar_imagen(self, *args):
        if (self.urlPNG == None):
            self.urlPNG = asksaveasfile(filetypes=[('PNG', '*.png')],
                                        defaultextension=[('PNG', '*.png')],
                                        initialfile="grafo_en_png.png")
        if (self.urlPNG != None):
            print("Imagen guardada en:", str(self.urlPNG.name))
            plt.savefig(str(self.urlPNG.name), format="PNG")
            self.urlPNG = None
    def guardar_archivo(self, *args):
        if (self.urlGraph == None):
            self.urlGraph = asksaveasfile(filetypes=[('JSON Document', '*.json')],
                                          defaultextension=[('JSON Document', '*.json')],
                                          initialfile="nuevo_archivo.json")
        if (self.urlGraph != None):
            with open(self.urlGraph.name, "w") as fw:
                json.dump(node_link_data(self.G), fw)
            fw.close()

    def abrirarchivo(self, *args):
        ubication = (askopenfile(title='Por favor, seleccione un archivo JSON.',
                                 mode='r', filetypes=[('JSON Files', '*.json')]))
        if (ubication != None):
            with open(ubication.name) as f:
                js_graph = json.load(f)
            self.G = json_graph.node_link_graph(js_graph)
            self.func_actualizar_figure()

    def menuarchivo(self, menu, bar_menu):
        sub_menu_archivo_nuevo = tk.Menu(menu, tearoff=False)

        menu.add_command(
            label="Abrir",
            # accelerator="Ctrl+N",
            command=self.abrirarchivo
        )
        menu.add_command(
            label="Guardar",
            # accelerator="Ctrl+N",
            command=self.guardar_archivo
        )
        menu.add_command(
            label="Guardar como",
            # accelerator="Ctrl+N",
            command=self.guardar_archivo
        )

        sub_menu_archivo_exportar = tk.Menu(menu, tearoff=False)

        sub_menu_archivo_exportar.add_command(
            label="Excel",
            # accelerator="Ctrl+N",
            command=self.exportar_CSV
        )
        sub_menu_archivo_exportar.add_command(
            label="Imagen",
            # accelerator="Ctrl+N",
            command=self.exportar_imagen
        )
        sub_menu_archivo_exportar.add_command(
            label="PDF",
            # accelerator="Ctrl+N",
            command=self.exportar_PDF
        )
        menu.add_cascade(menu=sub_menu_archivo_exportar, label="Exportar")

        menu.add_command(
            label="Importar datos",
            # accelerator="Ctrl+N",
            command=self.importar_CSV
        )
        menu.add_command(
            label="Imprimir",
            # accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )

        return (menu, bar_menu)

    def menuanalizar(self, menu, bar_menu):
        sub_menu_analizar_algoritmo = tk.Menu(menu, tearoff=False)
        sub_menu_analizar_algoritmo.add_command(
            label="Dikstra",
            # accelerator="Ctrl+N",
            command=lambda: abrir_ventana_partition(self, self.G)
        )
        sub_menu_analizar_algoritmo.add_command(
            label="Kernighan Lin",
            # accelerator="Ctrl+N",
            command=lambda: abrir_ventana_partition(self, self.G)
        )
        sub_menu_analizar_algoritmo.add_command(
            label="Algoritmo 3",
            # accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        sub_menu_analizar_algoritmo.add_command(
            label="Algoritmo k",
            # accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        menu.add_cascade(menu=sub_menu_analizar_algoritmo, label="Partitioner")

        return (menu, bar_menu)

    def menuherramienta(self, menu, bar_menu):
        menu.add_command(
            label="Ejecuciones",
            # accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        return (menu, bar_menu)

    def menuaplicacion(self, menu, bar_menu):
        sub_menu_aplicacion = tk.Menu(menu, tearoff=False)
        sub_menu_aplicacion.add_command(
            label="Aplicación 1",
            # accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        sub_menu_aplicacion.add_command(
            label="Aplicación 2",
            # accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        sub_menu_aplicacion.add_command(
            label="Aplicación 3",
            # accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        sub_menu_aplicacion.add_command(
            label="Aplicación m",
            # accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        menu.add_cascade(menu=sub_menu_aplicacion, label="Aplicación")

        return (menu, bar_menu)

    def menuventana(self, menu, bar_menu):
        menu.add_command(
            label="Gráfica",
            # accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        menu.add_command(
            label="Tabla",
            # accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        return (menu, bar_menu)

    def menuayuda(self, menu, bar_menu):
        menu.add_command(
            label="Ayuda",
            # accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        menu.add_command(
            label="Acerca de Grafos",
            # accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        return (menu, bar_menu)


class PartitionKL(tk.Toplevel):
    # Atributo de la clase que indica si la ventana
    # secundaria está en uso.
    en_uso = False


    def __init__(self, Graph, *args, **kwargs):  # Queda abierto a n argumentos o n argumentos con identificador
        super().__init__(*args, **kwargs)  # Se almacena por herencia el *args **kwargs
        self.__class__.en_uso = True
        sv_ttk.set_theme("dark")
        ntkutils.dark_title_bar(self)
        ntkutils.blur_window_background(self)
        self.G = Graph
        self.frameFigure = ttk.Frame(self)
        self.frameFigure.grid(row=0, column=1, rowspan=4, pady=20)

        self.figure = plt.figure(frameon=True, figsize=(7, 5), dpi=100)
        canvas = FigureCanvasTkAgg(self.figure, master=self.frameFigure)

        self.figure.set_facecolor('#eafff5')
        plt.axis('off')
        communities = nx.algorithms.community.girvan_newman(self.G, most_valuable_edge=None)

        node_groups = []
        for com in next(communities):
            node_groups.append(list(com))

        color_map = []
        for node in self.G:
            if node in node_groups[0]:
                color_map.append('blue')
            else:
                color_map.append('green')
        pos = nx.spring_layout(self.G, 25)
        nx.draw_networkx(self.G, pos=pos, node_color=color_map, alpha=0.9, edge_color='#bb85f0')
        nx.draw_networkx_edge_labels(self.G, pos, nx.get_edge_attributes(self.G, "weight"))

        canvas.draw()
        canvas.get_tk_widget().pack()

    def destroy(self):
        # Restablecer el atributo al cerrarse.
        self.__class__.en_uso = False
        return super().destroy()


def abrir_ventana_partition(self, Graph):
    if not PartitionKL.en_uso:
        self.ventana_secundaria = PartitionKL(Graph=Graph, master=self)
