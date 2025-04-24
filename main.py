# Binary to Emoji Convertor GUI
# Author - Nishanth C
# Description - Converts binary string input to emoji representation

import tkinter as tk
from tkinter import messagebox

def convert_to_emoji():
    binary = entry.get()
    if not set(binary).issubset({'0', '1'}):
        messagebox.showerror("Invalid Input", "Please enter only 0s and 1s.")
        return

    emoji_output = ''.join(['🟢' if bit == '1' else '🔴' for bit in binary])
    result_label.config(text=emoji_output)

def clear_all():
    entry.delete(0, tk.END)
    result_label.config(text='')

# Set up window
root = tk.Tk()
root.title("Binary to Emoji Converter")
root.geometry("400x200")
root.resizable(False, False)

# Widgets
title = tk.Label(root, text="Binary to Emoji Converter", font=("Helvetica", 16, "bold"))
title.pack(pady=10)

entry = tk.Entry(root, font=("Courier", 14), justify='center')
entry.pack(pady=5)

convert_btn = tk.Button(root, text="Convert", command=convert_to_emoji, width=12)
convert_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack(pady=10)

clear_btn = tk.Button(root, text="Clear", command=clear_all, width=12)
clear_btn.pack()

# Run
root.mainloop()
