import tkinter as tk
from tkinter import ttk


class VentanaSecundaria(tk.Toplevel):
    # Atributo de la clase que indica si la ventana
    # secundaria está en uso.
    en_uso = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=300, height=200)
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
    def __init__(self, *args, **kwargs):    ## Queda abierto a n argumentos o n argumentos con identificador
        super().__init__(*args, **kwargs)   ## Se almacena por herencia el *args **kwargs
        self.config(width=400, height=300)
        self.title("Ventana principal")
        self.boton_abrir = ttk.Button(
            self,
            text="Abrir ventana secundaria",
            command=self.abrir_ventana_secundaria
        )
        self.boton_abrir.place(x=100, y=100)

    def abrir_ventana_secundaria(self):
        if not VentanaSecundaria.en_uso:
            self.ventana_secundaria = VentanaSecundaria()