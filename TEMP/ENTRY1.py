import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

FOLDER = "Assets"
FILE_PATH = os.path.join(FOLDER, "Data.py")
BG_PATH = os.path.join(FOLDER, "images", "bgentry.jpg")

if not os.path.exists(FOLDER):
    os.makedirs(FOLDER)

Data = {}
try:
    from Assets.Data import Data as olddata
    Data = olddata
except (ImportError, SyntaxError, ModuleNotFoundError):
    Data = {}

def save_data(entry_dict):
    """Writes the dictionary back to the Assets/Data.py file."""
    try:
        with open(FILE_PATH, "w") as f:
            f.write(f"Data = {repr(entry_dict)}")
        messagebox.showinfo("Success", "Entry saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save: {e}")

def submit():
    """Gathers data from inputs and updates the Data dictionary."""
    try:

        entry_id = len(Data) + 1
        

        new_entry = [
            entries["IMG"].get().lower(),
            entries["FONT"].get().lower(),
            entries["NAME"].get().upper(),
            entries["WIKI"].get().lower(),
            entries["STATE"].get().upper(),
            entries["LOCATION"].get().upper(),
            entries["YEAR"].get().upper(),
            int(entries["SINCE"].get()),
            entries["AIRPORT"].get().upper(),
            entries["AIRPORT_URL"].get().lower(),
            entries["RAIL"].get().upper(),
            entries["RAIL_URL"].get().lower(),
            entries["HOURS"].get().upper(),
            entries["HOTEL"].get().upper(),
            entries["HOTEL_URL"].get().lower(),
            entries["FEES"].get(),
            entries["DESC"].get(),
            entries["PREC"].get()
        ]
        
        Data[entry_id] = new_entry
        save_data(Data)
        
        for e in entries.values():
            e.delete(0, tk.END)
            
    except ValueError:
        messagebox.showerror("Input Error", "Please ensure 'Since' is a number.")

root = tk.Tk()
root.title("Data Entry Portal")
root.geometry("500x700")

try:
    bg_img = Image.open(BG_PATH)
    bg_img = bg_img.resize((500, 700), Image.LANCZOS)
    bg_render = ImageTk.PhotoImage(bg_img)
    bg_label = tk.Label(root, image=bg_render)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception:
    print("Background image not found. Proceeding with default background.")

frame = tk.Frame(root, bg='#ffffff', bd=2)
frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=600)

canvas = tk.Canvas(frame, bg='white')
scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scroll_frame = tk.Frame(canvas, bg='white')

scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

fields = [
    ("BG Image Path", "IMG"), ("Font Name", "FONT"), ("Place Heading", "NAME"),
    ("Wiki Address", "WIKI"), ("State", "STATE"), ("Location", "LOCATION"),
    ("Year Listed", "YEAR"), ("Since (Year)", "SINCE"), ("Airport Label", "AIRPORT"),
    ("Airport URL", "AIRPORT_URL"), ("Railway Label", "RAIL"), ("Railway URL", "RAIL_URL"),
    ("Visiting Hours", "HOURS"), ("Hotels", "HOTEL"), ("Hotel URL", "HOTEL_URL"),
    ("Travel Fees", "FEES"), ("Description", "DESC"), ("Precautions", "PREC")
]

entries = {}

for label_text, key in fields:
    lbl = tk.Label(scroll_frame, text=label_text, bg='white', font=("Arial", 9, "bold"))
    lbl.pack(pady=(10, 0))
    ent = tk.Entry(scroll_frame, width=40, bd=2)
    ent.pack(pady=2)
    entries[key] = ent

btn_submit = tk.Button(scroll_frame, text="SAVE ENTRY", command=submit, bg="#2ecc71", fg="white", font=("Arial", 10, "bold"))
btn_submit.pack(pady=20)

root.mainloop()
