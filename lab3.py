import tkinter as tk
from tkinter import PhotoImage
import random
import string
import pygame

def generate_key():
    user_input = input_field.get().strip()
    try:
        dec_value = int(user_input, 16)
        dec_str = str(dec_value)
        if len(dec_str) < 5:
            dec_str = dec_str.zfill(5)
    except ValueError:
        key_field.delete(0, tk.END)
        key_field.insert(0, "Ошибка: неверный HEX формат")
        return

    first_digit = dec_str[0]
    second_digit = dec_str[1]
    third_digit = dec_str[2]
    last_two_digits = dec_str[-2:]

    block1 = f"{first_digit}{''.join(random.choices(string.ascii_uppercase
            + string.digits, k=4))}"
    block2 = f"{second_digit}{''.join(random.choices(string.ascii_uppercase
            + string.digits, k=4))}"
    block3 = f"{third_digit}{''.join(random.choices(string.ascii_uppercase
            + string.digits, k=4))}"

    key = f"{block1}-{block2}-{block3} {last_two_digits}"

    key_field.delete(0, tk.END)
    key_field.insert(0, key)

def animate():
    current_color = key_label.cget("bg")
    next_color = "#ff9999" if current_color == "#ddeeff" else "#ddeeff"
    key_label.config(bg=next_color)
    root.after(500, animate)

pygame.mixer.init()
pygame.mixer.music.load("8bit_music.mp3")
pygame.mixer.music.play(-1)

root = tk.Tk()
root.title("Keygen")
root.geometry("500x400")
root.resizable(False, False)

background_image = PhotoImage(file="background.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

input_label = tk.Label(root, text="Введите HEX число:",
            font=("Arial", 12), bg="#ddeeff")
input_label.place(x=20, y=20)

input_field = tk.Entry(root, font=("Arial", 12), width=30)
input_field.place(x=20, y=50)

key_label = tk.Label(root, text="Сгенерированный ключ:",
            font=("Arial", 12), bg="#ddeeff")
key_label.place(x=20, y=100)

key_field = tk.Entry(root, font=("Arial", 12), width=30)
key_field.place(x=20, y=130)

generate_button = tk.Button(root, text="Генерировать ключ",
                font=("Arial", 12), command=generate_key, bg="#ddeeff")
generate_button.place(x=20, y=180)

animate()
root.mainloop()



