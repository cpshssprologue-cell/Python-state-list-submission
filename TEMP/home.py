import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os
import subprocess

from Assets.Data import Data
from window import ArticleWindow


root = tk.Tk()
root.title("Heritage Display")
root.geometry("1200x700")

bg_img = Image.open("Assets/bg_img.jpg").resize((1200, 700))
bg_photo = ImageTk.PhotoImage(bg_img)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

logo_img = Image.open("Assets/logo.jpg").resize((200, 200))
logo_photo = ImageTk.PhotoImage(logo_img)

logo_label = tk.Label(root, image=logo_photo, bg="white")
logo_label.place(relx=0.5, rely=0.25, anchor="center")

heading = tk.Label(
    root,
    text="DICTIONARY BASED PYTHON HERITAGE SITE DISPLAY",
    font=("Arial", 20, "bold"),
    bg="white"
)
heading.place(relx=0.5, y=50, anchor="center")

key_entry = tk.Entry(root, font=("Arial", 14))
key_entry.place(relx=0.5, rely=0.45, anchor="center")

def open_article():
    try:
        key = int(key_entry.get())
        ArticleWindow(key)
    except:
        messagebox.showerror("Error", "Enter a valid key")

tk.Button(root, text="Open", command=open_article).place(relx=0.5, rely=0.5, anchor="center")

def open_random():
    ArticleWindow(random.choice(list(Data.keys())))

def open_entry():
    subprocess.Popen(["python3", "entry.py"])

def delete_key():
    try:
        k = int(key_entry.get())
        del Data[k]
        messagebox.showinfo("Deleted", f"Entry {k} deleted")
    except:
        messagebox.showerror("Error", "Invalid key")

def open_table(keys=None):
    win = tk.Toplevel()
    win.title("Table")
    win.geometry("900x500")

    if keys is None:
        keys = Data.keys()

    for k in keys:
        d = Data[k]
        row = f"{k} | {d[2]} | {d[4]} | {d[5]} | ₹{d[15]}"
        tk.Button(
            win,
            text=row,
            anchor="w",
            command=lambda x=k: ArticleWindow(x)
        ).pack(fill="x")

def open_search():
    win = tk.Toplevel()
    win.title("Search")

    entry = tk.Entry(win)
    entry.pack()

    def do_search():
        q = entry.get().lower()
        result = [
            k for k, v in Data.items()
            if any(q in str(x).lower() for x in v)
        ]
        open_table(result)

    tk.Button(win, text="Search", command=do_search).pack()

btn_frame = tk.Frame(root, bg="white")
btn_frame.place(relx=0.5, rely=0.9, anchor="center")

buttons = [
    ("Table", lambda: open_table()),
    ("Search", open_search),
    ("Deletion", delete_key),
    ("Entry", open_entry),
    ("Random", open_random)
]

for i, (txt, cmd) in enumerate(buttons):
    tk.Button(btn_frame, text=txt, command=cmd, width=10).grid(row=0, column=i, padx=5)

root.mainloop()
