import tkinter as tk
from tkinter import messagebox
import webbrowser
from PIL import Image, ImageTk
from Assets.Data import Data
import os


class ArticleWindow:
    def __init__(self, key):
        if key not in Data:
            messagebox.showerror("Error", "Invalid Key")
            return

        self.data = Data[key]

        self.root = tk.Toplevel()
        self.root.title(self.data[2])
        self.root.geometry("1200x700")

        bg_path = self.data[0]
        bg_img = Image.open(bg_path).resize((1200, 700))
        self.bg_photo = ImageTk.PhotoImage(bg_img)

        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)


        wiki_btn = tk.Button(
            self.root,
            text="Wikipedia",
            command=lambda: webbrowser.open(self.data[3]),
            bg="black",
            fg="white"
        )
        wiki_btn.place(x=20, y=20)


        title = tk.Label(
            self.root,
            text=self.data[2],
            font=("Arial", 28, "bold"),
            bg="white"
        )
        title.place(relx=0.5, y=60, anchor="center")

        info_frame = tk.Frame(self.root, bg="white")
        info_frame.place(relx=0.5, rely=0.55, anchor="center")

        labels = [
            f"State: {self.data[4]}",
            f"Location: {self.data[5]}",
            f"Year Listed: {self.data[7]}",
            f"Visiting Hours: {self.data[12]}",
            f"Fees: ₹{self.data[15]}",
            f"\nDescription:\n{self.data[16]}",
            f"\nPrecautions:\n{self.data[17]}"
        ]

        for txt in labels:
            tk.Label(info_frame, text=txt, bg="white", wraplength=800, justify="left").pack(anchor="w")

        btn_frame = tk.Frame(self.root, bg="white")
        btn_frame.place(relx=0.5, rely=0.88, anchor="center")

        tk.Button(
            btn_frame,
            text=self.data[8],
            command=lambda: webbrowser.open(self.data[9])
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            btn_frame,
            text=self.data[10],
            command=lambda: webbrowser.open(self.data[11])
        ).grid(row=0, column=1, padx=10)

        tk.Button(
            btn_frame,
            text="Hotels",
            command=lambda: webbrowser.open(self.data[14])
        ).grid(row=0, column=2, padx=10)
