import sqlite3
import tkinter as tk
from tkinter import Entry, Label, Button, StringVar

from PIL import Image, ImageTk

# Crear o conectar a la base de datos
con = sqlite3.connect('usuarios.db')
cursor = con.cursor()

# Crear la tabla de usuarios si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
con.commit()

# Función para registrar un nuevo usuario
def registrar_usuario():
    username = entrada_username.get()
    password = entrada_password.get()
    cursor.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', (username, password))
    con.commit()
    mensaje_registro.config(text="Usuario registrado con éxito.", fg="green")

# Función para verificar las credenciales del usuario al iniciar sesión
def iniciar_sesion():
    username = entrada_username.get()
    password = entrada_password.get()
    cursor.execute('SELECT * FROM usuarios WHERE username = ? AND password = ?', (username, password))
    usuario = cursor.fetchone()
    if usuario:
        mensaje_login.config(text="Sesión iniciada con éxito.", fg="green")
    else:
        mensaje_login.config(text="Credenciales incorrectas.", fg="red")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Registro e Inicio de Sesión")
ventana.geometry("800x600")

# Cargar la imagen de fondo
background_image = Image.open("E:\OPTIFARM/happy.jpg")  # Reemplaza "tu_imagen.jpg" con la ruta de tu imagen de fondo
background_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(ventana, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Crear etiquetas y entradas para usuario y contraseña
etiqueta_username = Label(ventana, text="Nombre de Usuario:", font=("Arial", 14))
etiqueta_username.pack(pady=20)
entrada_username = Entry(ventana, font=("Arial", 14))
entrada_username.pack(pady=10)

etiqueta_password = Label(ventana, text="Contraseña:", font=("Arial", 14))
etiqueta_password.pack(pady=20)
entrada_password = Entry(ventana, show="*", font=("Arial", 14))
entrada_password.pack(pady=10)

# Crear botones para Registro e Inicio de Sesión
boton_registro = Button(ventana, text="Registrar", command=registrar_usuario, font=("Arial", 14))
boton_registro.pack(pady=20)

boton_login = Button(ventana, text="Iniciar Sesión", command=iniciar_sesion, font=("Arial", 14))
boton_login.pack(pady=10)

# Crear etiquetas para mensajes de registro e inicio de sesión
mensaje_registro = Label(ventana, text="", font=("Arial", 14))
mensaje_registro.pack()

mensaje_login = Label(ventana, text="", font=("Arial", 14))
mensaje_login.pack()

ventana.mainloop()

# Cerrar la conexión a la base de datos
con.close()
