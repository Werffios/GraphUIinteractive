import tkinter as tk


def archivo_nuevo_presionado():
    print("¡Has presionado para crear un nuevo archivo!")


def menuarchivo(menu_archivo, bar_menu):
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


    return (menu_archivo, bar_menu)


