import tkinter as tk
from tkinter import messagebox

def encryption_block(data):
    return ((data * 2654435761 + 12345) & 0xFFFFFFFF)

def hash_function(message):
    H_prev = 0x67452301  
    result = ""

    for char in message:
        M = ord(char)

        H = encryption_block(H_prev ^ M) + M

        H = H & 0xFFFFFFFF

        H_prev = H

        result += f"{H:08x}"

    return result

def generate_hash():
    message = entry_message.get()
    if not message:
        messagebox.showerror("Ошибка", "Введите сообщение для хеширования!")
        return

    hash_result = hash_function(message)

    entry_result.delete(1.0, tk.END)
    entry_result.insert(tk.END, hash_result)

root = tk.Tk()
root.title("Хеш-функция")

label_message = tk.Label(root, text="Сообщение:")
label_message.pack()
entry_message = tk.Entry(root, width=70)
entry_message.pack(padx=10, pady=5)

tk.Button(root, text="Сгенерировать хеш", command=generate_hash).pack(pady=5)

tk.Label(root, text="Вывод хеша:").pack(anchor="w", padx=10, pady=5)
entry_result = tk.Text(root, height=5, width=70)
entry_result.pack(padx=10, pady=5)

root.mainloop()
