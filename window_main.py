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
# Clase para la ventana de la selección de tipo de grafo
from window_start import *


class VentanaPrincipal(tk.Tk):
    def __init__(self, *args, **kwargs):  # Queda abierto a n argumentos o n argumentos con identificador
        super().__init__(*args, **kwargs)  # Se almacena por herencia el *args **kwargs
        ntkutils.placeappincenter(self)  # Se coloca en el centro de la pantalla
        self.iconbitmap(r'icon.ico')  # Se carga el icono
        init = TypeGraph(self, "Selección")  # Se crea la ventana de selección de tipo de grafo
        print(init.var.get())  # Se imprime el valor de la variable
        # Creación del grafo         <----------------------------
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
        self.label_error_delete = None
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
        # Inicializar menus
        self.menu_archivo = None
        self.menu_analizar = None
        self.menu_herramienta = None
        self.menu_aplicacion = None
        self.menu_ventana = None
        self.menu_ayuda = None
        self.bar_menu = None
        # CONFIGURACIÓN DE VENTANA
        self.geometry("1200x700")
        self.title("")

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
                                                                    self.bar_menu)  # Función que añade submenus, etc.
        self.bar_menu.add_cascade(menu=self.menu_herramienta, label="Herramienta")  # Añado a la barra de menus

        self.menu_aplicacion = tk.Menu(self.bar_menu, tearoff=False)  # Creación menú aplicación
        self.menu_aplicacion, self.bar_menu = self.menuaplicacion(self.menu_aplicacion,
                                                                  self.bar_menu)  # Función que añade submenus, etc.
        self.bar_menu.add_cascade(menu=self.menu_aplicacion, label="Aplicación")  # Añado a la barra de menus

        self.menu_ventana = tk.Menu(self.bar_menu, tearoff=False)  # Creación menú ventana
        self.menu_ventana, self.bar_menu = self.menuventana(self.menu_ventana,
                                                            self.bar_menu)  # Función que añade submenus, etc.
        self.bar_menu.add_cascade(menu=self.menu_ventana, label="Ventana")  # Añado a la barra de menus

        self.menu_ayuda = tk.Menu(self.bar_menu, tearoff=False)  # Creación menú ayuda
        self.menu_ayuda, self.bar_menu = self.menuayuda(self.menu_ayuda,
                                                        self.bar_menu)  # Función que añade submenus, etc.
        self.bar_menu.add_cascade(menu=self.menu_ayuda, label="Ayuda")  # Añado a la barra de menus

    def init_buttons(self):
        self.frameAdd_edge.grid(row=0, column=0, padx=20, pady=20)  # Agrego el frame de agregar aristas

        self.label_Add_edge_title = ttk.Label(self.frameAdd_edge, text="AGREGAR ARISTA",
                                              font=("Segoe UI", 25))  # Creo el label de agregar aristas
        self.label_Add_edge_title.grid(row=0, columnspan=2, padx=20, pady=5)  # Agrego el label de agregar aristas

        self.label_Add_edge_vertice_o = ttk.Label(self.frameAdd_edge, text="Nodo origen",
                                                  font=("Segoe UI", 11))  # Creo el label de nodo origen
        self.label_Add_edge_vertice_o.grid(row=1, column=0)  # Agrego el label de nodo origen

        self.entry_Add_edge_vertice_o = ttk.Entry(self.frameAdd_edge,
                                                  name="entrada origen AggVertice")  # Creo el entry de nodo origen
        self.entry_Add_edge_vertice_o.grid(row=1, column=1, pady=3)  # Agrego el entry de nodo origen

        self.label_Add_edge_vertice_d = ttk.Label(self.frameAdd_edge, text="Nodo destino",
                                                  font=("Segoe UI", 11))  # Creo el label de nodo destino
        self.label_Add_edge_vertice_d.grid(row=2, column=0)  # Agrego el label de nodo destino

        self.entry_Add_edge_vertice_d = ttk.Entry(self.frameAdd_edge,
                                                  name="entrada destino AggVertice")  # Creo el entry de nodo destino
        self.entry_Add_edge_vertice_d.grid(row=2, column=1, pady=3)  # Agrego el entry de nodo destino

        self.label_Add_edge_peso = ttk.Label(self.frameAdd_edge, text="Peso",
                                             font=("Segoe UI", 11))  # Creo el label de peso
        self.label_Add_edge_peso.grid(row=3, column=0)  # Agrego el label de peso

        self.entry_Add_edge_peso = ttk.Entry(self.frameAdd_edge,
                                             name="entrada peso AggVertice")  # Creo el entry de peso
        self.entry_Add_edge_peso.grid(row=3, column=1, pady=3)  # Agrego el entry de peso

        self.button_Add_edge = ttk.Button(self.frameAdd_edge, text="Agregar")  # Creo el botón de agregar aristas
        self.button_Add_edge.grid(row=4, column=1, ipadx=52, pady=5)  # Agrego el botón de agregar aristas

        self.frameAdd_node.grid(row=1, column=0, ipadx=1)  # Agrego el frame de agregar nodos

        self.label_Add_node_title = ttk.Label(self.frameAdd_node, text="AGREGAR NODO",
                                              font=("Segoe UI", 25))  # Creo el label de agregar nodos
        self.label_Add_node_title.grid(row=0, columnspan=2, padx=20, pady=5)  # Agrego el label de agregar nodos

        self.label_Add_node = ttk.Label(self.frameAdd_node, text="Nombre nodo",
                                        font=("Segoe UI", 11))  # Creo el label de nombre nodo
        self.label_Add_node.grid(row=1, column=0)  # Agrego el label de nombre nodo

        self.entry_Add_node = ttk.Entry(self.frameAdd_node,
                                        name="entrada nodo sin connection")  # Creo el entry de nombre nodo
        self.entry_Add_node.grid(row=1, column=1, pady=3)  # Agrego el entry de nombre nodo

        self.button_Add_node = ttk.Button(self.frameAdd_node, text="Agregar")  # Creo el botón de agregar nodos
        self.button_Add_node.grid(row=2, column=1, ipadx=52, pady=5)  # Agrego el botón de agregar nodos

        self.frameFigure.grid(row=0, column=1, rowspan=4, pady=20)  # Agrego el frame de la gráfica

        self.label_Delete_node_title = ttk.Label(self.frameDelete_node, text="ELIMINAR NODO",
                                                 font=("Segoe UI", 25))  # Creo el label de eliminar nodos
        self.label_Delete_node_title.grid(row=0, columnspan=2, padx=20, pady=5)  # Agrego el label de eliminar nodos

        self.label_Delete_node = ttk.Label(self.frameDelete_node, text="Nombre nodo",
                                           font=("Segoe UI", 11))  # Creo el label de nombre nodo
        self.label_Delete_node.grid(row=1, column=0)  # Agrego el label de nombre nodo

        self.entry_Delete_node = ttk.Entry(self.frameDelete_node,
                                           name="entrada nodo a borrar")  # Creo el entry de nombre nodo
        self.entry_Delete_node.grid(row=1, column=1, pady=3)  # Agrego el entry de nombre nodo

        self.button_Delete_node = ttk.Button(self.frameDelete_node, text="Eliminar")  # Creo el botón de eliminar nodos
        self.button_Delete_node.grid(row=2, column=1, ipadx=52, pady=5)  # Agrego el botón de eliminar nodos

        self.bind_all('<Control-Key-G>', self.guardar_archivo)  # Evento para guardar el archivo
        self.bind_all('<Control-Key-g>', self.guardar_archivo)  # Evento para guardar el archivo

        self.button_Add_edge.bind("<Button-1>", self.func_agregar_arista)  # Evento para agregar aristas

        self.button_Add_node.bind("<Button-1>", self.func_agregar_nodo)  # Evento para agregar nodos

        self.entry_Add_node.bind("<Return>", self.func_agregar_nodo)  # Evento para agregar nodos

        self.entry_Add_edge_vertice_o.bind("<Return>",
                                           self.func_salta_o_d)  # Evento para saltar a la entrada de destino
        self.entry_Add_edge_vertice_d.bind("<Return>", self.func_salta_d_p)  # Evento para saltar a la entrada de peso
        self.entry_Add_edge_peso.bind("<Return>", self.func_agregar_arista)  # Evento para agregar aristas

        self.label_error_delete = ttk.Label(self.frameDelete_node, font=("Segoe UI", 9))  # Creo el label de error

        self.entry_Delete_node.bind("<Return>", self.func_eliminar_nodo)  # Evento para eliminar nodos
        self.button_Delete_node.bind("<Button-1>", self.func_eliminar_nodo)  # Evento para eliminar nodos

        self.frameDelete_node.grid(row=2, column=0)  # Agrego el frame de eliminar nodos

        self.func_actualizar_figure()  # Actualizo la gráfica

    def func_actualizar_figure(self, *args):
        self.frameFigure.grid_remove()  # Elimino el frame de la gráfica
        self.frameFigure.grid_forget()  # Elimino el frame de la gráfica

        self.frameFigure = ttk.Frame(self)  # Creo el frame de la gráfica
        self.frameFigure.grid(row=0, column=1, rowspan=4, pady=20)  # Agrego el frame de la gráfica

        self.figure = plt.figure(frameon=True, figsize=(7, 5), dpi=100)  # Creo la gráfica
        canvas = FigureCanvasTkAgg(self.figure, master=self.frameFigure)  # Creo el canvas de la gráfica

        self.figure.set_facecolor('#eafff5')  # Cambio el color de la gráfica
        plt.axis('off')  # Deshabilito los ejes de la gráfica

        pos = nx.spring_layout(self.G, 25)  # Posiciono los nodos de la gráfica
        nx.draw_networkx(self.G, pos=pos, alpha=0.9, node_color='#44e011', edge_color='#bb85f0')  # Dibujo la gráfica
        nx.draw_networkx_edge_labels(self.G, pos,
                                     nx.get_edge_attributes(self.G, "weight"))  # Dibujo los pesos de las aristas

        canvas.draw()  # Dibujo la gráfica en la figura
        canvas.get_tk_widget().pack()  # Agrego el canvas de la gráfica

    def func_eliminar_nodo(self, *args):
        self.label_error_delete.config(
            text="ERROR--> No existe el nodo: " + self.entry_Delete_node.get())  # Cambio el label de error
        self.label_error_delete.grid_forget()  # Elimino el label de error
        if self.entry_Delete_node.get() != '':  # Si el entry de nombre nodo no está vacío
            if self.G.has_node(self.entry_Delete_node.get()):  # Si el nodo existe
                self.G.remove_node(self.entry_Delete_node.get())  # Elimino el nodo
                self.func_actualizar_figure()  # Actualizo la gráfica
                self.entry_Add_node.focus_set()  # Foco en el entry de agregar nodos
                self.entry_Delete_node.delete(0, tk.END)  # Borro el entry de eliminar nodos
                self.entry_Delete_node.focus_set()  # Foco en el entry de eliminar nodos

                print("Nodos:", list(self.G.nodes))  # Imprimo los nodos
            else:
                self.label_error_delete.grid(row=3, column=0, columnspan=2)  # Agrego el label de error
                self.entry_Delete_node.focus_set()  # Foco en el entry de eliminar nodos

    def func_salta_o_d(self, *args):
        if self.entry_Add_edge_vertice_o.get() != '':  # Si el entry de origen no está vacío
            self.entry_Add_edge_vertice_d.focus_set()

    def func_salta_d_p(self, *args):
        if self.entry_Add_edge_vertice_d.get() != '':  # Si el entry de destino no está vacío
            self.entry_Add_edge_peso.focus_set()

    def func_prueba(self, *args):  # Función de prueba
        print("probado")

    def func_agregar_nodo(self, *args):  # Función para agregar nodos
        if (self.entry_Add_node.get() != ''):  # Si el entry de nombre nodo no está vacío
            self.G.add_node(self.entry_Add_node.get())  # Agrego el nodo

            self.func_actualizar_figure()  # Actualizo la gráfica

            self.entry_Add_node.delete(0, tk.END)  # Borro el entry de agregar nodos

            print("Nodos:", list(self.G.nodes))  # Imprimo los nodos
            self.entry_Delete_node.focus_set()  # Foco en el entry de eliminar nodos
            self.entry_Add_node.focus_set()  # Foco en el entry de agregar nodos

    def func_agregar_arista(self, *args):
        if not (self.entry_Add_edge_peso.get().isnumeric()):  # Si el peso no es un número
            self.entry_Add_edge_peso.delete(0, tk.END)  # Borro el entry de peso

        elif (self.entry_Add_edge_vertice_o.get() != '') and (self.entry_Add_edge_peso.get() != '') and (
                self.entry_Add_edge_vertice_d.get() != ''):  # Si los entries de origen, peso y destino no están vacíos
            self.G.add_edge(self.entry_Add_edge_vertice_o.get(), self.entry_Add_edge_vertice_d.get(),
                            weight=int(self.entry_Add_edge_peso.get()))  # Agrego la arista

            self.func_actualizar_figure()  # Actualizo la gráfica

            self.entry_Add_edge_vertice_o.delete(0, tk.END)  # Borro el entry de origen
            self.entry_Add_edge_vertice_d.delete(0, tk.END)  # Borro el entry de destino
            self.entry_Add_edge_peso.delete(0, tk.END)  # Borro el entry de peso

            self.entry_Add_edge_vertice_o.focus_set()  # Foco en el entry de origen
            print("Edges:", list(self.G.edges))  # Imprimo las aristas

    def archivo_nuevo_presionado(self, *args):
        print("¡Has presionado para crear un nuevo archivo!")  # Imprimo que se presionó para crear un nuevo archivo

    def exportar_CSV(self, *args):
        if self.urlCSV_export == None:  # Si el urlCSV_export es None
            self.urlCSV_export = asksaveasfile(filetypes=[('CSV', '*.csv')],
                                               defaultextension=[('CSV', '*.csv')],
                                               initialfile="grafo_en_csv.csv")  # Pido al usuario que guarde el archivo
        if self.urlCSV_export != None:  # Si el urlCSV_export no es None
            json_archivo = json.loads(json.dumps(json_graph.node_link_data(self.G)))  # Convierto la gráfica en JSON
            print("CSV guardado en:", str(self.urlCSV_export.name))  # Imprimo el nombre del archivo
            with open(self.urlCSV_export.name, 'w') as f:  # Abro el archivo
                for key in json_archivo.keys():  # Para cada key en el JSON
                    f.write(
                        key + "," + str(json_archivo[key]) + "\n")  # Escribo la key y el valor de la key en el archivo
                f.close()  # Cierro el archivo
            self.urlCSV_export = None  # Reseteo el urlCSV_export

    def importar_CSV(self, *args):
        ubication = (askopenfile(title='Por favor, seleccione un archivo de Excel (CSV).',
                                 mode='r',
                                 filetypes=[('CSV Files', '*.csv')]))  # Pido al usuario que seleccione un archivo
        graph_import = {}  # Creo un diccionario para guardar los datos del archivo
        if (ubication != None):  # Si el archivo no es None
            with open(ubication.name, 'r') as f:  # Abro el archivo
                lines = f.readlines()  # Leo el archivo
                for line in lines:  # Para cada línea en el archivo
                    line = line.strip()  # Elimino los espacios en blanco
                    if line[
                       line.index(',') + 1:] == 'False':  # Si la línea tiene una coma y el siguiente caracter es False
                        graph_import[line[:line.index(',')]] = False  # Agrego el nodo con el valor False
                    elif line[
                         line.index(',') + 1:] == 'True':  # Si la línea tiene una coma y el siguiente caracter es True
                        graph_import[line[:line.index(',')]] = True  # Agrego el nodo con el valor True
                    elif line[line.index(',') + 1:] == '{}':  # Si la línea tiene una coma y el siguiente caracter es {}
                        graph_import[line[:line.index(',')]] = {}  # Agrego el nodo con el valor {}
                    elif line[line.index(
                            ',') + 1:] == "{'directed': True}":  # Si la línea tiene una coma y el siguiente caracter es {'directed': True}
                        graph_import[line[:line.index(',')]] = {
                            'directed': True}  # Agrego el nodo con el valor {'directed': True}
                    else:  # Si no es ninguno de los anteriores
                        if line[:line.index(',')] not in graph_import:  # Si el nodo no está en el diccionario
                            graph_import[line[:line.index(',')]] = list()  # Agrego el nodo con una lista vacía
                        if line[:line.index(',')] == 'nodes':  # Si el nodo es nodes
                            for data in line[line.index(',') + 1:].split(','):  # Para cada dato en la línea
                                graph_import[line[:line.index(',')]].append(
                                    {data.split("'")[1]: data.split("'")[3]})  # Agrego el nodo con el valor de la data
                        else:  # Si no es nodes
                            for data in line[line.index(',') + 1:].replace("}, {", "}|{").split(
                                    "|"):  # Para cada dato en la línea
                                temp = data.split("'")  # Separo los datos por comillas
                                graph_import[line[:line.index(',')]].append(
                                    {temp[1]: float(temp[2].replace(':', '').replace(',', '')), temp[3]: temp[5],
                                     temp[7]: temp[9]})  # Agrego el nodo con el valor de la data
            f.close()  # Cierro el archivo
            self.G = json_graph.node_link_graph(graph_import)  # Convierto el diccionario en una gráfica
            self.func_actualizar_figure()  # Actualizo la gráfica

    def exportar_PDF(self, *args):  # Función para exportar a PDF
        if self.urlPDF == None:  # Si el urlPDF es None
            self.urlPDF = asksaveasfile(filetypes=[('PDF', '*.pdf')],
                                        defaultextension=[('PDF', '*.pdf')],
                                        initialfile="grafo_en_pdf.pdf")  # Pido al usuario que guarde el archivo
        if self.urlPDF != None:  # Si el urlPDF no es None
            print("PDF guardado en:", str(self.urlPDF.name))  # Imprimo el nombre del archivo
            plt.savefig(str(self.urlPDF.name), format="PDF")  # Guardo la gráfica en el archivo
            self.urlPDF = None  # Reseteo el urlPDF

    def exportar_imagen(self, *args):  # Función para exportar a PNG
        if self.urlPNG == None:  # Si el urlPNG es None
            self.urlPNG = asksaveasfile(filetypes=[('PNG', '*.png')],
                                        defaultextension=[('PNG', '*.png')],
                                        initialfile="grafo_en_png.png")  # Pido al usuario que guarde el archivo
        if self.urlPNG != None:  # Si el urlPNG no es None
            print("Imagen guardada en:", str(self.urlPNG.name))  # Imprimo el nombre del archivo
            plt.savefig(str(self.urlPNG.name), format="PNG")  # Guardo la gráfica en el archivo
            self.urlPNG = None  # Reseteo el urlPNG

    def guardar_archivo(self, *args):  # Función para guardar el archivo
        if self.urlGraph == None:  # Si el urlGraph es None
            self.urlGraph = asksaveasfile(filetypes=[('JSON Document', '*.json')],
                                          defaultextension=[('JSON Document', '*.json')],
                                          initialfile="nuevo_archivo.json")  # Pido al usuario que guarde el archivo
        if self.urlGraph != None:  # Si el urlGraph no es None
            with open(self.urlGraph.name, "w") as fw:  # Abro el archivo
                json.dump(node_link_data(self.G), fw)  # Guardo el archivo
            fw.close()  # Cierro el archivo

    def abrirarchivo(self, *args):  # Función para abrir un archivo
        ubication = (askopenfile(title='Por favor, seleccione un archivo JSON.',
                                 mode='r', filetypes=[('JSON Files', '*.json')]))  # Pido al usuario que seleccione un archivo
        if ubication != None:  # Si el archivo no es None
            with open(ubication.name) as f:  # Abro el archivo
                js_graph = json.load(f)  # Cargo el archivo
            self.G = json_graph.node_link_graph(js_graph)  # Convierto el diccionario en una gráfica
            self.func_actualizar_figure()  # Actualizo la gráfica

    def menuarchivo(self, menu, bar_menu):  # Función para el menú de archivo
        sub_menu_archivo_nuevo = tk.Menu(menu, tearoff=False)  # Creo un submenú

        menu.add_command(
            label="Abrir",
            # accelerator="Ctrl+N",
            command=self.abrirarchivo  # Agrego el comando para abrir un archivo
        )
        menu.add_command(
            label="Guardar",
            # accelerator="Ctrl+N",
            command=self.guardar_archivo  # Agrego el comando para guardar un archivo
        )
        menu.add_command(
            label="Guardar como",
            # accelerator="Ctrl+N",
            command=self.guardar_archivo  # Agrego el comando para guardar un archivo
        )

        sub_menu_archivo_exportar = tk.Menu(menu, tearoff=False)  # Creo un submenú

        sub_menu_archivo_exportar.add_command(
            label="Excel",
            # accelerator="Ctrl+N",
            command=self.exportar_CSV  # Agrego el comando para exportar a CSV
        )
        sub_menu_archivo_exportar.add_command(
            label="Imagen",
            # accelerator="Ctrl+N",
            command=self.exportar_imagen  # Agrego el comando para exportar a PNG
        )
        sub_menu_archivo_exportar.add_command(
            label="PDF",
            # accelerator="Ctrl+N",
            command=self.exportar_PDF  # Agrego el comando para exportar a PDF
        )
        menu.add_cascade(menu=sub_menu_archivo_exportar, label="Exportar")  # Agrego el submenú de exportar

        menu.add_command(
            label="Importar datos",
            # accelerator="Ctrl+N",
            command=self.importar_CSV  # Agrego el comando para importar datos
        )
        menu.add_command(
            label="Imprimir",
            # accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado  # Agrego el comando para imprimir
        )

        return menu, bar_menu  # Retorno el menu y la barra de menú

    def menuanalizar(self, menu, bar_menu):
        sub_menu_analizar_algoritmo = tk.Menu(menu, tearoff=False)
        sub_menu_analizar_algoritmo.add_command(
            label="Kernighan Lin",
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

        return menu, bar_menu

    def menuherramienta(self, menu, bar_menu):
        menu.add_command(
            label="Ejecuciones",
            # accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        return menu, bar_menu

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

        return menu, bar_menu

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
        return menu, bar_menu

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
        return menu, bar_menu


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

    def destroy(self):  # Se cierra la ventana
        # Restablecer el atributo al cerrarse.
        self.__class__.en_uso = False  # Restablecer el atributo
        return super().destroy()  # Se llama al método destroy de la clase padre.


def abrir_ventana_partition(self, Graph):  # Se abre la ventana secundaria
    if not PartitionKL.en_uso:  # Si no está en uso
        self.ventana_secundaria = PartitionKL(Graph=Graph, master=self)  # Se crea la ventana secundaria
