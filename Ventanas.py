import tkinter as tk
from tkinter import ttk


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


def archivo_nuevo_presionado():
    print("¡Has presionado para crear un nuevo archivo!")


class VentanaPrincipal(tk.Tk):
    def __init__(self, *args, **kwargs):  ## Queda abierto a n argumentos o n argumentos con identificador
        super().__init__(*args, **kwargs)  ## Se almacena por herencia el *args **kwargs
        self.config(width=400, height=300)
        self.title("Ventana principal")

        bar_menu = tk.Menu()  ## Crear barra de menú
        self.config(menu=bar_menu)  ## Insertar la barra de menús al la principal  (Se deben añadir menus, sino no se ve)
        menu_archivo = tk.Menu(bar_menu, tearoff=False)


        sub_menu_archivo_nuevo = tk.Menu(menu_archivo, tearoff=False)
        sub_menu_archivo_nuevo.add_command(
            label="Personalizado",
            ## accelerator="Ctrl+N",
            command=archivo_nuevo_presionado
        )
        sub_menu_archivo_nuevo.add_command(
            label="Aleatorio",
            ## accelerator="Ctrl+N",
            command=archivo_nuevo_presionado
        )
        menu_archivo.add_cascade(menu=sub_menu_archivo_nuevo, label="Nuevo grafo")

        menu_archivo.add_command(
            label="Abrir",
            ## accelerator="Ctrl+N",
            command=archivo_nuevo_presionado
        )
        menu_archivo.add_command(
            label="Guardar",
            ## accelerator="Ctrl+N",
            command=archivo_nuevo_presionado
        )
        menu_archivo.add_command(
            label="Guardar como",
            ## accelerator="Ctrl+N",
            command=archivo_nuevo_presionado
        )


        sub_menu_archivo_exportar = tk.Menu(menu_archivo, tearoff=False)
        sub_menu_archivo_exportar.add_command(
            label="Excel",
            ## accelerator="Ctrl+N",
            command=archivo_nuevo_presionado
        )
        sub_menu_archivo_exportar.add_command(
            label="Imagen",
            ## accelerator="Ctrl+N",
            command=archivo_nuevo_presionado
        )
        sub_menu_archivo_exportar.add_command(
            label="PDF",
            ## accelerator="Ctrl+N",
            command=archivo_nuevo_presionado
        )
        menu_archivo.add_cascade(menu=sub_menu_archivo_exportar, label="Exportar")

        menu_archivo.add_command(
            label="Importar datos",
            ## accelerator="Ctrl+N",
            command=archivo_nuevo_presionado
        )
        menu_archivo.add_command(
            label="Inicio",
            ## accelerator="Ctrl+N",
            command=archivo_nuevo_presionado
        )
        menu_archivo.add_command(
            label="Imprimir",
            ## accelerator="Ctrl+N",
            command=archivo_nuevo_presionado
        )






        bar_menu.add_cascade(menu=menu_archivo, label="Archivo")








    def abrir_ventana_secundaria(self):
        if not VentanaSecundaria.en_uso:
            self.ventana_secundaria = VentanaSecundaria()
