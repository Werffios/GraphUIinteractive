import tkinter as tk
from tkinter.filedialog import askopenfile

def archivo_nuevo_presionado():
    print("¡Has presionado para crear un nuevo archivo!")

def abrirarchivo():
    print( askopenfile(title='Please select one (any) frame from your set of images.',
                       mode ='r', filetypes =[('JSON Files', '*.json')]).read())

def menuarchivo(menu, bar_menu):
    sub_menu_archivo_nuevo = tk.Menu(menu, tearoff=False)
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
    menu.add_cascade(menu=sub_menu_archivo_nuevo, label="Nuevo grafo")

    menu.add_command(
        label="Abrir",
        ## accelerator="Ctrl+N",
        command=abrirarchivo
    )
    menu.add_command(
        label="Guardar",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    menu.add_command(
        label="Guardar como",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )

    sub_menu_archivo_exportar = tk.Menu(menu, tearoff=False)
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
    menu.add_cascade(menu=sub_menu_archivo_exportar, label="Exportar")

    menu.add_command(
        label="Importar datos",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    menu.add_command(
        label="Inicio",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    menu.add_command(
        label="Imprimir",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )


    return(menu, bar_menu)

def menueditar(menu, bar_menu):
    menu.add_command(
        label="Deshacer",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    sub_menu_editar_nodo = tk.Menu(menu, tearoff=False)
    sub_menu_editar_nodo.add_command(
        label="Agregar",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    sub_menu_editar_nodo.add_command(
        label="Editar",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    sub_menu_editar_nodo.add_command(
        label="Eliminar",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    menu.add_cascade(menu=sub_menu_editar_nodo, label="Nodo")

    sub_menu_editar_arco = tk.Menu(menu, tearoff=False)
    sub_menu_editar_arco.add_command(
        label="Agregar",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    sub_menu_editar_arco.add_command(
        label="Editar",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    sub_menu_editar_arco.add_command(
        label="Eliminar",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    menu.add_cascade(menu=sub_menu_editar_arco, label="Arco")


    return(menu, bar_menu)

def menuanalizar(menu, bar_menu):
    sub_menu_analizar_algoritmo = tk.Menu(menu, tearoff=False)
    sub_menu_analizar_algoritmo.add_command(
        label="Algoritmo 1",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    sub_menu_analizar_algoritmo.add_command(
        label="Algoritmo 2",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    sub_menu_analizar_algoritmo.add_command(
        label="Algoritmo 3",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    sub_menu_analizar_algoritmo.add_command(
        label="Algoritmo k",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    menu.add_cascade(menu=sub_menu_analizar_algoritmo, label="Algoritmo")

    return(menu, bar_menu)

def menuherramienta(menu, bar_menu):
    menu.add_command(
        label="Ejecución",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    return(menu, bar_menu)

def menuaplicacion(menu, bar_menu):
    sub_menu_aplicacion = tk.Menu(menu, tearoff=False)
    sub_menu_aplicacion.add_command(
        label="Aplicación 1",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    sub_menu_aplicacion.add_command(
        label="Aplicación 2",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    sub_menu_aplicacion.add_command(
        label="Aplicación 3",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    sub_menu_aplicacion.add_command(
        label="Aplicación m",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    menu.add_cascade(menu=sub_menu_aplicacion, label="Algoritmo")

    return(menu, bar_menu)

def menuventana(menu, bar_menu):
    menu.add_command(
        label="Gráfica",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    menu.add_command(
        label="Tabla",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    return(menu, bar_menu)

def menuayuda(menu, bar_menu):
    menu.add_command(
        label="Ayuda",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    menu.add_command(
        label="Acerca de Grafos",
        ## accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    return(menu, bar_menu)
