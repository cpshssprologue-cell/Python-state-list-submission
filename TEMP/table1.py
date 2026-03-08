import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# --- Configuration ---
FOLDER = "Assets"
FILE_PATH = os.path.join(FOLDER, "Data.py")
BG_PATH = os.path.join(FOLDER, "images", "bgtable.jpg")

def load_data():
    try:
        namespace = {}
        with open(FILE_PATH, "r") as f:
            exec(f.read(), namespace)
        return namespace.get("Data", {})
    except Exception as e:
        print(f"Error loading data: {e}")
        return {}

# --- UI Setup ---
root = tk.Tk()
root.title("Database Viewer")
root.geometry("1000x600")

# Background Image
try:
    bg_img = Image.open(BG_PATH).resize((1000, 600), Image.LANCZOS)
    bg_render = ImageTk.PhotoImage(bg_img)
    tk.Label(root, image=bg_render).place(x=0, y=0, relwidth=1, relheight=1)
except:
    root.configure(bg="#34495e")

# Container for Treeview and Scrollbars
frame = tk.Frame(root, bg='white', bd=2)
frame.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.9, relheight=0.8)

# Define Column Headers
columns = ("ID", "NAME", "STATE", "LOCATION", "YEAR", "SINCE", "AIRPORT", "RAILWAY", "FEES")

# Create Treeview
tree = ttk.Treeview(frame, columns=columns, show='headings', selectmode="browse")

# Define Headings and Column widths
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor="center")

# Scrollbars
vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

# Layout
tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')

frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(0, weight=1)

# --- Populating Data ---
def populate_table():
    data = load_data()
    # Clear existing rows
    for item in tree.get_children():
        tree.delete(item)
    
    # Insert new rows
    for entry_id, info in data.items():
        # Mapping specific indices from your list to the table columns
        # Indices: NAME(2), STATE(4), LOCATION(5), YEAR(6), SINCE(7), AIRPORT(8), RAIL(10), FEES(15)
        row_values = (
            entry_id, 
            info[2], info[4], info[5], info[6], 
            info[7], info[8], info[10], info[15]
        )
        tree.insert("", tk.END, values=row_values)

populate_table()

# Optional: Refresh button
btn_refresh = tk.Button(root, text="REFRESH DATA", command=populate_table, bg="#3498db", fg="white", font=("Arial", 10, "bold"))
btn_refresh.pack(side="bottom", pady=20)

root.mainloop()
