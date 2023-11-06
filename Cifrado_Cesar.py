import tkinter as tk
import tkinter.messagebox
import random
import math

def primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    else:
        for i in range(3, int(numero**0.5) + 1, 2):
            if numero % i == 0:
                return False
        return True

vali = False
while vali == False:
    p = random.randint(1, 50)
    vali = primo(p)
vali = False
q = 0
while vali == False or p == q:
    q = random.randint(1, 50)
    vali = primo(q)    

def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def son_coprimos(num1, num2):
    mcd = calcular_mcd(num1, num2)
    return mcd


p = 3
q = 11
n = p*q
phi = (p-1)*(q-1)

def publica():
    e=2
    validar = False
    while validar == False and e < phi:
        val = son_coprimos(e,phi)
        if val == 1:
            validar = True
        else:
            e = e+1
    return e,n

def privada(e):
    d1 = phi
    d2 = d1
    d3 = e
    d4 = 1
    d5 = math.floor(d1/d3)
    d6 = d5*d3
    d7 = d5*d4
    d8 = d1-d6
    d9 = d2-d7
    d = d9%phi
    if d8 == 1:
        return d, n
    else:
        while d8 != 1:
            d1 = d3
            d2 = d4
            d3 = d8
            d4 = d9
            d5 = math.floor(d1/d3)
            d6 = d5*d3
            d7 = d5*d4
            d8 = d1-d6
            d9 = d2-d7
            d = d9%phi
        return d, n
    
def rsa_encrypt():
    message = rsa_input_entry.get()
    if not message.isalpha():
        tkinter.messagebox.showerror("Error", "Por favor, ingresa solo letras en el mensaje.")
        return
    public = publica()
    print(message)
    print(public[0])
    print(n)
    encrypted_text = procesar_cadena(message, public[0], n)
    rsa_output_entry.config(state=tk.NORMAL)
    rsa_output_entry.delete(0, tk.END)
    rsa_output_entry.insert(tk.END, encrypted_text)
    rsa_output_entry.config(state=tk.DISABLED)
    return

def calcular_operacion(letra, exponente, n):
    valor = ord(letra) - ord('a')
    resultado = pow(valor, exponente, n) % 27
    return resultado

def procesar_cadena(cadena, exponente, n):
    alfabeto = "abcdefghijklmnopqrstuvwxyzñ "
    resultado = ""
    for letra in cadena:
        if letra.isalpha() or letra.isspace():
            if letra.isalpha():
                letra_resultante = alfabeto[(calcular_operacion(letra.lower(), exponente, n) + 27) % 27]
            else:
                letra_resultante = " "
            resultado += letra_resultante
        else:
            resultado += letra
    return resultado

#######################
    
#######################
# Función para desencriptar el mensaje usando el algoritmo RSA
def rsa_decrypt():
    message = rsa_input_entry.get()
    if not message.isalpha():
        tkinter.messagebox.showerror("Error", "Por favor, ingresa solo letras en el mensaje.")
        return
    public = publica()
    private = privada(public[0])
    print(message)
    print(public)
    print(private)
    print(n)
    decrypted_text = procesar_cadena(message, private[0], n)
    rsa_output_entry.config(state=tk.NORMAL)
    rsa_output_entry.delete(0, tk.END)
    rsa_output_entry.insert(tk.END, decrypted_text)
    rsa_output_entry.config(state=tk.DISABLED)
    return


# Función para mostrar la pantalla de encriptar/desencriptar con el algoritmo César
def show_cesar_screen():
    cesar_screen.pack()
    rsa_screen.pack_forget()
    info_Screen.pack_forget()

# Función para mostrar la pantalla de encriptar/desencriptar con el algoritmo RSA
def show_rsa_screen():
    rsa_screen.pack()
    cesar_screen.pack_forget()
    info_Screen.pack_forget()
    

# Función para mostrar el código fuente en pantalla
def show_source_code():
    info_Screen.pack()
    with open(__file__, "r") as file:
        source_code = file.read()
    info_Screen_text.config(state=tk.NORMAL)
    info_Screen_text.delete(1.0, tk.END)
    info_Screen_text.insert(tk.END, source_code)
    info_Screen_text.config(state=tk.DISABLED)

# Función para mostrar información sobre los algoritmos utilizados
def show_info():
    info_Screen.pack()
    info_Screen_text.config(state=tk.NORMAL)
    info_Screen_text.delete(1.0, tk.END)
    info_Screen_text.insert(tk.END, "Algoritmo César\nAlgoritmo RSA\n")
    info_Screen_text.config(state=tk.DISABLED)

# Función para mostrar información sobre los algoritmos al revés
def show_reversed_info():
    info_Screen.pack()
    info_Screen_text.config(state=tk.NORMAL)
    info_Screen_text.delete(1.0, tk.END)
    info_Screen_text.insert(tk.END, "aruteS ASR\nmaruaséC omíglitnA\n")
    info_Screen_text.config(state=tk.DISABLED)

# Función para encriptar el mensaje usando el método de César

def cesar_cipher(message, shift):
    result = ""
    for char in message:
        if char.isalpha() or char.isspace():
            if char.isalpha():
                shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
            else:
                shifted_char = char
            result += shifted_char
        else:
            result += char
    return result

def cesar_encrypt():
    message = input_entry.get()
    shift = shift_entry.get()

    # Validar que el mensaje y el desplazamiento sean válidos
    if not message.isalpha() or not shift.isdigit():
        tkinter.messagebox.showerror("Error", "Por favor, ingresa solo letras y números para el desplazamiento.")
        return

    shift = int(shift)
    encrypted_text = cesar_cipher(message, shift)
    output_entry.config(state=tk.NORMAL)
    output_entry.delete(0, tk.END)
    output_entry.insert(tk.END, encrypted_text)
    output_entry.config(state=tk.DISABLED)

# Función para desencriptar el mensaje usando el método de César
def cesar_decrypt():
    encrypted_text = input_entry.get()
    shift = shift_entry.get()

    # Validar que el mensaje cifrado y el desplazamiento sean válidos
    if not encrypted_text.isalpha() or not shift.isdigit():
        tkinter.messagebox.showerror("Error", "Por favor, ingresa solo letras y números para el desplazamiento.")
        return

    shift = int(shift)
    decrypted_text = cesar_cipher(encrypted_text, -shift)
    output_entry.config(state=tk.NORMAL)
    output_entry.delete(0, tk.END)
    output_entry.insert(tk.END, decrypted_text)
    output_entry.config(state=tk.DISABLED)

# Función para copiar el resultado al portapapeles
def copy_result():
    result = output_entry.get()
    root.clipboard_clear()
    root.clipboard_append(result)
    root.update()
    
    resultado = output_entry.get()
    input_entry.delete(0, tk.END)  # Limpiar el cuadro de entrada
    input_entry.insert(0, resultado)
    
    resultado = rsa_output_entry.get()
    rsa_input_entry.delete(0, tk.END)  # Limpiar el cuadro de entrada
    rsa_input_entry.insert(0, resultado)

def limpiar_entrada():
    input_entry.delete(0, tk.END)
    shift_entry.delete(0, tk.END)
    output_entry.delete(0, tk.END)
    rsa_input_entry.delete(0, tk.END)
    rsa_output_entry.delete(0, tk.END)



    
# Función para encriptar el mensaje usando el algoritmo RSA


# Crear la ventana principal
root = tk.Tk()
root.title("Cifrado")

# Crear pantalla de encriptar/desencriptar con el algoritmo César
cesar_screen = tk.Frame(root)
cesar_screen_label = tk.Label(cesar_screen, text="Cifrado César")
cesar_screen_label.grid(row=0, column=0, columnspan=2, pady=10)

input_label = tk.Label(cesar_screen, text="Mensaje:")
input_label.grid(row=1, column=0, padx=10, pady=5)
input_entry = tk.Entry(cesar_screen, width=40)
input_entry.grid(row=1, column=1, padx=10, pady=5)

shift_label = tk.Label(cesar_screen, text="Desplazamiento:")
shift_label.grid(row=2, column=0, padx=10, pady=5)
shift_entry = tk.Entry(cesar_screen, width=10)
shift_entry.grid(row=2, column=1, padx=10, pady=5)

encrypt_button = tk.Button(cesar_screen, text="Encriptar", command=cesar_encrypt)
encrypt_button.grid(row=3, column=0, columnspan=2, pady=10)

decrypt_button = tk.Button(cesar_screen, text="Desencriptar", command=cesar_decrypt)
decrypt_button.grid(row=3, column=1, columnspan=2, pady=10)

copy_button = tk.Button(cesar_screen, text="Copiar Resultado", command=copy_result)
copy_button.grid(row=5, column=1, columnspan=2, pady=10)

copy_button = tk.Button(cesar_screen, text="Limpiar", command=limpiar_entrada)
copy_button.grid(row=3, column=2, columnspan=2, pady=10)

output_label = tk.Label(cesar_screen, text="Resultado:")
output_label.grid(row=4, column=0, padx=10, pady=5)
output_entry = tk.Entry(cesar_screen, width=40, state=tk.DISABLED)
output_entry.grid(row=4, column=1, padx=10, pady=5)
# Resto de los elementos de la pantalla de encriptar/desencriptar con el algoritmo César


# Crear pantalla de encriptar/desencriptar con el algoritmo RSA



# Resto de los elementos de la pantalla de encriptar/desencriptar con el algoritmo RSA
# ...

# Crear elementos de la interfaz gráfica para el menú inicial
menu_label = tk.Label(root, text="Seleccione una opción:")
menu_label.pack()

options_menu = tk.Menu(root)
root.config(menu=options_menu)

options_menu.add_command(label="Algoritmo Cesar", command=show_cesar_screen)
options_menu.add_command(label="Algoritmo RSA", command=show_rsa_screen)
options_menu.add_command(label="Imprimir Código Fuente", command=show_source_code)
options_menu.add_command(label="Informacion1", command=show_info)
options_menu.add_command(label="Informacion2 (Al revés)", command=show_reversed_info)

# Crear pantalla de encriptar/desencriptar con el algoritmo RSA
rsa_screen = tk.Frame(root)
rsa_screen_label = tk.Label(rsa_screen, text="Cifrado RSA")
rsa_input_label = tk.Label(rsa_screen, text="Mensaje:")
rsa_input_label.grid(row=1, column=0, padx=10, pady=5)
rsa_input_entry = tk.Entry(rsa_screen, width=40)
rsa_input_entry.grid(row=1, column=1, padx=10, pady=5)

rsa_encrypt_button = tk.Button(rsa_screen, text="Encriptar", command=rsa_encrypt)
rsa_encrypt_button.grid(row=2, column=0, columnspan=2, pady=10)

rsa_decrypt_button = tk.Button(rsa_screen, text="Desencriptar", command=rsa_decrypt)
rsa_decrypt_button.grid(row=2, column=1, columnspan=8, pady=10)

rsa_copy_button = tk.Button(rsa_screen, text="Copiar Resultado", command=copy_result)
rsa_copy_button.grid(row=4, column=1, columnspan=2, pady=10)

rsa_copy_button = tk.Button(rsa_screen, text="Limpiar", command=limpiar_entrada)
rsa_copy_button.grid(row=2, column=2, columnspan=2, pady=10)

rsa_output_label = tk.Label(rsa_screen, text="Resultado:")
rsa_output_label.grid(row=3, column=0, padx=10, pady=5)
rsa_output_entry = tk.Entry(rsa_screen, width=40, state=tk.DISABLED)
rsa_output_entry.grid(row=3, column=1, padx=10, pady=5)


# Crear pantalla de encriptar/desencriptar con el algoritmo RSA
info_Screen = tk.Frame(root)
info_Screen_text = tk.Text(info_Screen, width=80, height=20)
info_Screen_text.config(state=tk.DISABLED)
info_Screen_text.pack()



# Iniciar el bucle de eventos de la interfaz gráfica
root.mainloop()
