import tkinter as tk
from tkinter import Entry, Label, Button, StringVar, OptionMenu
from PIL import Image, ImageTk

# Diccionario de producción y precios
produccion = {
    "Naranjas": 10000,
    "Mandarinas": 7000,
    "Limones": 4000,
    "Mangos": 6000
}

precios = {
    "Naranjas": {
        "Mayorista": 1500,
        "Venta al por menor": 2000
    },
    "Mandarinas": {
        "Mayorista": 1800,
        "Venta al por menor": 2200
    },
    "Limones": {
        "Mayorista": 2000,
        "Venta al por menor": 2500
    },
    "Mangos": {
        "Mayorista": 2200,
        "Venta al por menor": 2800
    }
}

# Diccionario para almacenar pedidos de los consumidores
pedidos = {}

# Función para registrar un pedido
def registrar_pedido():
    def registrar():
        nombre_consumidor = entrada_nombre_consumidor.get()
        producto = entrada_producto.get()
        cantidad = float(entrada_cantidad.get())
        canal = canal_var.get()
        if nombre_consumidor not in pedidos:
            pedidos[nombre_consumidor] = {}
        if producto not in pedidos[nombre_consumidor]:
            pedidos[nombre_consumidor][producto] = {}
        pedidos[nombre_consumidor][producto][canal] = cantidad
        ventana_pedido.destroy()

    # Ventana para registrar un pedido
    ventana_pedido = tk.Toplevel()
    ventana_pedido.title("Registrar Pedido")
    ventana_pedido.geometry("600x600")

    # Configuración de etiquetas en verde con fuente Arial 14
    label_nombre_consumidor = Label(ventana_pedido, text="Nombre del consumidor:", bg="green", fg="white", font=("Arial", 14))
    label_producto = Label(ventana_pedido, text="Producto a comprar:", bg="green", fg="white", font=("Arial", 14))
    label_cantidad = Label(ventana_pedido, text="Cantidad en kg:", bg="green", fg="white", font=("Arial", 14))
    label_canal_distribucion = Label(ventana_pedido, text="Canal de distribución:", bg="green", fg="white", font=("Arial", 14))

    # Resto de las etiquetas y configuración de entrada aquí...
    entrada_nombre_consumidor = Entry(ventana_pedido, font=("Arial", 14))
    entrada_producto = Entry(ventana_pedido, font=("Arial", 14))
    entrada_cantidad = Entry(ventana_pedido, font=("Arial", 14))
    canal_var = StringVar()
    canal_option = OptionMenu(ventana_pedido, canal_var, "Mayorista", "Venta al por menor")

    # Botón para registrar el pedido
    boton_registrar = Button(ventana_pedido, text="Registrar Pedido", command=registrar,
                            font=("Arial", 14), bg="green", fg="white")

    # Posición de los elementos
    label_nombre_consumidor.grid(row=0, column=0, padx=10, pady=10)
    entrada_nombre_consumidor.grid(row=0, column=1, padx=10, pady=10)
    label_producto.grid(row=1, column=0, padx=10, pady=10)
    entrada_producto.grid(row=1, column=1, padx=10, pady=10)
    label_cantidad.grid(row=2, column=0, padx=10, pady=10)
    entrada_cantidad.grid(row=2, column=1, padx=10, pady=10)
    label_canal_distribucion.grid(row=3, column=0, padx=10, pady=10)
    canal_option.grid(row=3, column=1, padx=10, pady=10)
    boton_registrar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Aplicación")
ventana.geometry("800x600")
# Cargar la imagen de fondo
background_image = Image.open("E:\OPTIFARM/trd.jpg")  # Reemplaza "4a.jpg" con tu propia imagen de fondo
background_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(ventana, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Botón para registrar un pedido
boton_registrar_pedido = tk.Button(ventana, text="Registrar Pedido", command=registrar_pedido,
                            font=("Arial", 20), bg="green", fg="white")
boton_registrar_pedido.pack()

ventana.mainloop()