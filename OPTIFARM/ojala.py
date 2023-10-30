import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import threading

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
    ventana_pedido.geometry("400x400")

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

   
    # Botón para registrar el pedido
    boton_registrar = tk.Button(ventana_pedido, text="Registrar Pedido", command=registrar,
                            font=("Arial", 20), bg="green", fg="white")
def prr():
    from tkinter import tk, Entry, PhotoImage

# Crear una ventana
    ventana = tk.Tk()

# Cargar la imagen redonda (reemplaza 'imagen_redonda.png' con la ruta de tu imagen)
    imagen_redonda = PhotoImage(file='C:\Users\gabag\OneDrive\Escritorio\OPTIFARM')

# Crear un cuadro de entrada con la imagen redonda como fondo
    cuadro_redondo = Entry(ventana, borderwidth=0, highlightthickness=0)
    cuadro_redondo.config(font=('Arial', 14))  # Establecer la fuente
    cuadro_redondo.config(highlightbackground="black")  # Color de fondo
    cuadro_redondo.config(highlightcolor="black")  # Color del resalte
    cuadro_redondo.config(justify='center')  # Alinear el texto al centro
    cuadro_redondo.config(insertbackground="white")  # Color del cursor
    cuadro_redondo.config(background='red')  # Fondo rojo (el color que desees)
    cuadro_redondo.config(image=imagen_redonda)  # Establecer la imagen como fondo

    # Colocar el cuadro de entrada en la ventana
    cuadro_redondo.pack(padx=10, pady=10)

# Iniciar la ventana
ventana.mainloop()

# Función para cargar un video como fondo
def cargar_video_de_fondo(ventana):
    cap = cv2.VideoCapture("C:/Users/gabag/OneDrive/Escritorio/OPTIFARM/vid_inter.mp4")  # Ruta al video
    width = int(cap.get(3))
    height = int(cap.get(4))

    def reproducir():
        nonlocal cap
        while True:
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = ImageTk.PhotoImage(Image.fromarray(frame))
                etiqueta_video.img = img
                etiqueta_video.configure(image=img)
            else:
                cap = cv2.VideoCapture("C:/Users/gabag/OneDrive/Escritorio/OPTIFARM/vid_inter.mp4")  # Reiniciar el video al final

    hilo_reproduccion = threading.Thread(target=reproducir)
    hilo_reproduccion.daemon = True
    hilo_reproduccion.start()

    etiqueta_video = ttk.Label(ventana)
    etiqueta_video.place(relwidth=1, relheight=1)

# Función para iniciar la ventana principal
def iniciar_aplicacion():
    ventana = tk.Tk()
    ventana.title("Aplicación con Video de Fondo")
    ventana.geometry("1200x1080")  # Tamaño de la ventana

    cargar_video_de_fondo(ventana)

    # Botón para registrar un pedido
    boton_registrar_pedido = tk.Button(ventana, text="Registrar Pedido", command=registrar_pedido,
                                    font=("Arial", 20), bg="green", fg="white")
    boton_registrar_pedido.pack()

    ventana.mainloop()

if __name__ == "__main__":
    iniciar_aplicacion()

