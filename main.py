import tkinter as tk
from tkinter import ttk
import random
import string

root = tk.Tk()
root.title("Menadżer haseł")
photo = tk.PhotoImage(file="key.png")
root.iconphoto(False, photo)

style = ttk.Style(root)
root.tk.call("source", "breeze-dark.tcl")
style.theme_use("breeze-dark")

w = 800
h = 650
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
root.geometry('+%d+%d' % (x, y))

font_large = ("Arial", 20)
font_medium = ("Arial", 18)
font_small = ("Arial", 14)

password_length = 0
lowercase_quantity = 0
uppercase_quantity = 0
digits_quantity = 0
special_quantity = 0
free_characters = 0
final_password = ""
password = []


def show_generate_frame():
    frame_main.pack_forget()
    frame_generate_main.pack()
    frame_generate.pack()
    back_button.pack()

def show_main_frame():
    for widget in frame_generate.winfo_children():
        widget.destroy()
        for widget in frame_generate_main.winfo_children():
            widget.destroy()
    frame_generate.pack_forget()
    frame_generate_main.pack_forget()
    frame_main.pack()

def get_password_length():
    global free_characters
    global password_length
    password_length = int(password_length_spinbox.get())
    if password_length >= 8:
        free_characters = password_length
        lowercase_quantity_label.grid(row=2, column=0, columnspan=2, padx=15, pady=5, sticky="nsew")
        lowercase_quantity_spinbox.configure(state="readonly", from_=1, to=free_characters - 3)
        lowercase_quantity_spinbox.grid(row=3, column=0, padx=15, pady=5, sticky="nsew")
        ok_lowercase_button.grid(row=3, column=1, padx=15, pady=5, sticky="nsew")


def get_lowercase_quantity():
    global lowercase_quantity
    global free_characters
    lowercase_quantity = int(lowercase_quantity_spinbox.get())
    if lowercase_quantity >= 1 and lowercase_quantity <= free_characters - 3:
        free_characters -= lowercase_quantity
        lowercase_quantity_spinbox.configure(state="disable")
        uppercase_quantity_label.grid(row=4, column=0, columnspan=2, padx=15, pady=5, sticky="nsew")
        uppercase_quantity_spinbox.configure(state="readonly", from_=1, to=free_characters - 2)
        uppercase_quantity_spinbox.grid(row=5, column=0, padx=15, pady=5, sticky="nsew")
        ok_uppercase_button.grid(row=5, column=1, padx=15, pady=5, sticky="nsew")


def get_uppercase_quantity():
    global uppercase_quantity
    global free_characters
    uppercase_quantity = int(uppercase_quantity_spinbox.get())
    if uppercase_quantity >= 1 and uppercase_quantity <= free_characters - 2:
        free_characters -= uppercase_quantity
        uppercase_quantity_spinbox.configure(state="disable")
        digits_quantity_label.grid(row=6, column=0, columnspan=2, padx=15, pady=5, sticky="nsew")
        digits_quantity_spinbox.configure(state="readonly", from_=1, to=free_characters - 1)
        digits_quantity_spinbox.grid(row=7, column=0, padx=15, pady=5, sticky="nsew")
        ok_digits_button.grid(row=7, column=1, padx=15, pady=5, sticky="nsew")


def get_digits_quantity():
    global digits_quantity
    global free_characters
    digits_quantity = int(digits_quantity_spinbox.get())
    if digits_quantity >= 1 and digits_quantity <= free_characters - 1:
        free_characters -= digits_quantity
        digits_quantity_spinbox.configure(state="disable")
        special_quantity_label.grid(row=8, column=0, columnspan=2, padx=15, pady=5, sticky="nsew")
        special_quantity_spinbox.configure(state="readonly", from_=1, to=free_characters)
        special_quantity_spinbox.grid(row=9, column=0, padx=15, pady=5, sticky="nsew")
        ok_special_button.grid(row=9, column=1, padx=15, pady=5, sticky="nsew")


def get_special_quantity():
    global special_quantity
    global free_characters
    global lowercase_quantity
    special_quantity = int(special_quantity_spinbox.get())
    if special_quantity >= 1 and special_quantity <= free_characters:
        if free_characters > 1:
            free_characters_label.configure(
                text=f"Pozostało {free_characters - 1} wolnych znaków, zostaną uzupełnione małymi literami.")
            free_characters_label.grid(row=10, column=0, columnspan=2, padx=15, pady=5, sticky="nsew")
            lowercase_quantity += free_characters - 1
        generate_button.grid(row=11, column=0, padx=15, pady=5, sticky="nsew")
        special_quantity_spinbox.configure(state="disable")


def generate_password():
    global lowercase_quantity
    global uppercase_quantity
    global special_quantity
    global digits_quantity
    global final_password
    global password_length
    lower = lowercase_quantity
    upper = uppercase_quantity
    special = special_quantity
    digits = digits_quantity
    password.clear()
    for i in range(password_length):
        if lower > 0:
            password.append(random.choice(string.ascii_lowercase))
            lower -= 1
        if upper > 0:
            password.append(random.choice(string.ascii_uppercase))
            upper -= 1
        if special > 0:
            password.append(random.choice(string.punctuation))
            special -= 1
        if digits > 0:
            password.append(random.choice(string.digits))
            digits -= 1
    random.shuffle(password)
    final_password = "".join(password)
    final_password_label.configure(text=f"Twoje hasło to: {final_password}")
    final_password_label.grid(row=12, column=0, columnspan=2, padx=15, pady=5, sticky="nsew")


###########MainFrame#############
frame_main = ttk.Frame(root)
frame_main.pack()

welcome_label = ttk.Label(frame_main, text="Witaj w menadżerze haseł!", font=font_large)
welcome_label.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=10)

choice_label = ttk.Label(frame_main, text="Wybierz co chcesz zrobić", font=font_medium)
choice_label.grid(row=1, column=0, columnspan=2, pady=10)

button_generate = ttk.Button(frame_main, text="Wygeneruj hasło", command=lambda: show_generate_frame())
button_generate.grid(row=2, column=0, sticky="nsew", pady=6)

button_read = ttk.Button(frame_main, text="Odczytaj hasła")
button_read.grid(row=2, column=1, sticky="nsew", pady=6)

#############GenerateFrame##########

frame_generate_main = ttk.Frame(root)

frame_generate = ttk.Frame(frame_generate_main)



#Powrót do menu głownego

back_button = ttk.Button(frame_generate_main, text="Powrót", command=lambda: show_main_frame())


#Długość hasła
password_length_label = ttk.Label(frame_generate, text="Podaj długość hasła (minimum 8 znaków)", font=font_medium)
password_length_label.grid(row=0, column=0, columnspan=2, padx=15, pady=5, sticky="nsew")

password_length_spinbox = ttk.Spinbox(frame_generate, from_=8, to=100)
password_length_spinbox.insert(8, "8")
password_length_spinbox.grid(row=1, column=0, padx=15, pady=5, sticky="nsew")

ok_length_button = ttk.Button(frame_generate, text="OK", command=lambda: get_password_length())
ok_length_button.grid(row=1, column=1, padx=15, pady=5, sticky="nsew")

# Warunki hasła
# Ilość małych liter
lowercase_quantity_label = ttk.Label(frame_generate, text="Podaj ilość małych liter (minimum 1)",
                                     font=font_medium)

lowercase_quantity_spinbox = ttk.Spinbox(frame_generate)
lowercase_quantity_spinbox.insert(1, "1")

ok_lowercase_button = ttk.Button(frame_generate, text="OK", command=lambda: get_lowercase_quantity())

# Ilość wielkich liter
uppercase_quantity_label = ttk.Label(frame_generate, text="Podaj ilość wielkich liter (minimum 1)",
                                     font=font_medium)

uppercase_quantity_spinbox = ttk.Spinbox(frame_generate)
uppercase_quantity_spinbox.insert(1, "1")

ok_uppercase_button = ttk.Button(frame_generate, text="OK", command=lambda: get_uppercase_quantity())

# Ilość cyfr
digits_quantity_label = ttk.Label(frame_generate, text="Podaj ilość cyfr (minimum 1)",
                                  font=font_medium)

digits_quantity_spinbox = ttk.Spinbox(frame_generate)
digits_quantity_spinbox.insert(1, "1")

ok_digits_button = ttk.Button(frame_generate, text="OK", command=lambda: get_digits_quantity())

# Ilość znaków specjalnych
special_quantity_label = ttk.Label(frame_generate, text="Podaj ilość znaków specjlanych (minimum 1)",
                                   font=font_medium)

special_quantity_spinbox = ttk.Spinbox(frame_generate)
special_quantity_spinbox.insert(1, "1")

ok_special_button = ttk.Button(frame_generate, text="OK", command=lambda: get_special_quantity())

# Niewykorzystane znaki w haśle
free_characters_label = ttk.Label(frame_generate, font=("Arial", 8))

# Generowanie hasłą
generate_button = ttk.Button(frame_generate, text="Generuj hasło", command=lambda: generate_password())

# Wyświetlenie wygenerowanego hasła
final_password_label = ttk.Label(frame_generate, font=font_small)

root.mainloop()
