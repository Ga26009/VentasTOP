import tkinter as tk
from tkinter import ttk, Entry, Label, Button, StringVar, OptionMenu
from PIL import Image, ImageTk
import cv2
import threading
import time

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

# Función para calcular ingresos
def calcular_ingresos(pedido):
    ingresos_totales = 0
    for producto, cantidades in pedido.items():
        for canal, cantidad in cantidades.items():
            precio = precios[producto][canal]
            ingresos_totales += precio * cantidad
    return ingresos_totales

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
        cambiar_a_metodo_pago()  # Llamar a la función para cambiar a la pestaña de método de pago

    # Ventana para registrar un pedido
    ventana_pedido = tk.Toplevel()
    ventana_pedido.title("Registrar Pedido")
    ventana_pedido.geometry("600x600")

    # Configuración de etiquetas en verde con fuente Arial 14
    label_nombre_consumidor = tk.Label(ventana_pedido, text="Nombre del consumidor:", bg="green", fg="white", font=("Arial", 14))
    label_producto = tk.Label(ventana_pedido, text="Producto a comprar:", bg="green", fg="white", font=("Arial", 14))
    label_cantidad = tk.Label(ventana_pedido, text="Cantidad en kg:", bg="green", fg="white", font=("Arial", 14))
    label_canal_distribucion = tk.Label(ventana_pedido, text="Canal de distribución:", bg="green", fg="white", font=("Arial", 14))

    # Resto de las etiquetas y configuración de entrada aquí...
    entrada_nombre_consumidor = tk.Entry(ventana_pedido, font=("Arial", 14))
    entrada_producto = tk.Entry(ventana_pedido, font=("Arial", 14))
    entrada_cantidad = tk.Entry(ventana_pedido, font=("Arial", 14))
    canal_var = tk.StringVar()
    canal_option = tk.OptionMenu(ventana_pedido, canal_var, "Mayorista", "Venta al por menor")

    # Botón para registrar el pedido
    boton_registrar = tk.Button(ventana_pedido, text="Registrar Pedido", command=registrar,
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

# Función para cargar la imagen de fondo
def cargar_imagen_de_fondo(ventana):
    img = Image.open("E:\\OPTIFARM/trd.jpg")  # Ruta a la imagen
    img = img.resize((ventana.winfo_screenwidth(), ventana.winfo_screenheight()), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    etiqueta_imagen = tk.Label(ventana, image=img)
    etiqueta_imagen.place(x=0, y=0, relwidth=1, relheight=1)

    ventana.img = img

# Función para cambiar a la pestaña "Método de Pago"
def cambiar_a_metodo_pago():
    notebook.select(1)  # Cambia a la segunda pestaña (0-indexed)

# Función para registrar un método de pago (puedes agregar tu lógica aquí)
def registrar_metodo_pago():
    pass

# Función para mostrar la ventana de productos y precios
def mostrar_precios_productos():
    ventana_productos_precios = tk.Toplevel()
    ventana_productos_precios.title("Productos y Precios")

    # Crear etiquetas con los productos y precios
    for producto, precios_producto in precios.items():
        label_producto = tk.Label(ventana_productos_precios, text=f"{producto}:", font=("Arial", 14))
        label_producto.pack()

        for canal, precio in precios_producto.items():
            label_precio = tk.Label(ventana_productos_precios, text=f"{canal}: ${precio}", font=("Arial", 12))
            label_precio.pack()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Aplicación")
ventana.geometry("800x600")

# Crear el objeto Notebook para las pestañas
notebook = ttk.Notebook(ventana)
notebook.pack(fill='both', expand='yes')

# Crear pestañas
pestaña_pedidos = ttk.Frame(notebook)
pestaña_metodo_pago = ttk.Frame(notebook)

# Agregar pestañas al Notebook
notebook.add(pestaña_pedidos)
# Continuación del código...

notebook.add(pestaña_pedidos, text="Pedidos")
notebook.add(pestaña_metodo_pago, text="Método de Pago")

# Agregar contenido a la pestaña de Pedidos
cargar_imagen_de_fondo(pestaña_pedidos)
mostrar_precios_productos()

# Agregar contenido a la pestaña de Método de Pago
# Puedes agregar tu lógica para el método de pago aquí

# Mostrar la ventana principal
ventana.mainloop()

