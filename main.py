from Ventanas import *

Ventana = VentanaPrincipal()
Ventana.focus()
Ventana.init_menubar()
Ventana.init_buttons()

"""# Makes the window topmost
Ventana.wm_attributes('-topmost', True)

# Makes the window ubication center, n, ne, nw, etc
Ventana.anchor("center")

# Makes the icon of the window
Ventana.wm_iconbitmap("error")


# Makes the window transparent
Ventana.wm_attributes('-alpha', 0.9)

# Disable the window
Ventana.wm_attributes('-disabled', True)

# Set the geometry of the window
Ventana.wm_geometry('700x350')"""

Ventana.mainloop()