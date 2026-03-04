import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import subprocess

def open_file(filename):
    if os.path.exists(filename):
        subprocess.Popen(['python', filename])
def main():
    root = tk.Tk()
    root.title("PYTHON STATE LIST SUBMISSION")
    bg_path = os.path.join("Assets", "Images", "bghome.jpg")
    try:
        bg_image = Image.open(bg_path)
        bg_photo = ImageTk.PhotoImage(bg_image)
        img_width, img_height = bg_image.size
        root.geometry(f"{img_width}x{img_height}")
        root.resizable(False, False)
        canvas = tk.Canvas(root, width=img_width, height=img_height, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    except Exception as exception1:
        root.geometry("1368x822")
        canvas = tk.Canvas(root, bg="#2c3e50")
        canvas.pack(fill="both", expand=True)
    button_style = {
        "font": ("Lucida Console", 10),
        "width": 10,
        "pady": 15,
    }
    frame = tk.Frame(root, bg="")
    frame.pack(side="top", fill="both", expand=True, padx=10, pady=10)
    buttons = [
        ("Entry", "entry.py"),
        ("Deletion", "deletion.py"),
        ("List", "table.py"),
        ("Search", "search.py"),
        ("Random", "random.py")
    ]
    for text, file in buttons:
        btn = tk.Button(
            frame, 
            text=text, 
            command=lambda f=file: open_file(f),
            **button_style
        )
        btn.pack(pady=0)
    canvas.create_window(img_width//2, img_height//2, window=frame)
    root.mainloop()
if __name__ == "__main__":
    main()
