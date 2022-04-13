
from tkinter import ttk
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
        self.config(width=1200, height=700)
        self.title("Ventana principal")





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

    def abrir_ventana_secundaria(self):
        if not VentanaSecundaria.en_uso:
            self.ventana_secundaria = VentanaSecundaria()
