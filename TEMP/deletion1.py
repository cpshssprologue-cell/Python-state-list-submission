import os
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

# --- Configuration ---
FOLDER = "Assets"
FILE_PATH = os.path.join(FOLDER, "Data.py")
BG_PATH = os.path.join(FOLDER, "images", "bgdel.jpg")

# --- Data Loading ---
def load_data():
    try:
        # We use a trick to read the file without 'import' to avoid caching issues
        namespace = {}
        with open(FILE_PATH, "r") as f:
            exec(f.read(), namespace)
        return namespace.get("Data", {})
    except Exception:
        return {}

def save_data(data_dict):
    with open(FILE_PATH, "w") as f:
        f.write(f"Data = {repr(data_dict)}")

def delete_entry():
    selection = combo.get()
    if not selection:
        messagebox.showwarning("Selection Required", "Please select an entry to delete.")
        return

    # Extract the ID from the string "ID: Name"
    try:
        selected_id = int(selection.split(":")[0])
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete '{selection}'?\nThis will re-order all following IDs.")
        
        if confirm:
            current_data = load_data()
            if selected_id in current_data:
                # 1. Remove the item
                current_data.pop(selected_id)
                
                # 2. Re-index everything to close the gap
                # Sort keys first to ensure we process them in order
                sorted_vals = [current_data[k] for k in sorted(current_data.keys())]
                new_data = {i+1: val for i, val in enumerate(sorted_vals)}
                
                # 3. Save and Refresh
                save_data(new_data)
                messagebox.showinfo("Deleted", "Entry removed and IDs re-indexed.")
                refresh_list()
    except Exception as e:
        messagebox.showerror("Error", f"Deletion failed: {e}")

def refresh_list():
    """Updates the dropdown with current entries from the file."""
    data = load_data()
    # Create a list of strings like "1: PARIS", "2: LONDON"
    display_list = [f"{k}: {v[2]}" for k, v in data.items()]
    combo['values'] = display_list
    combo.set("") # Clear selection

# --- UI Setup ---
root = tk.Tk()
root.title("Delete Entry Portal")
root.geometry("400x300")

# Background
try:
    bg_img = Image.open(BG_PATH).resize((400, 300), Image.LANCZOS)
    bg_render = ImageTk.PhotoImage(bg_img)
    tk.Label(root, image=bg_render).place(x=0, y=0, relwidth=1, relheight=1)
except:
    root.configure(bg="#2c3e50")

frame = tk.Frame(root, bg='white', padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor='center')

tk.Label(frame, text="Select Entry to Delete", bg='white', font=("Arial", 10, "bold")).pack()

combo = ttk.Combobox(frame, width=30, state="readonly")
combo.pack(pady=10)

btn_del = tk.Button(frame, text="DELETE PERMANENTLY", command=delete_entry, 
                    bg="#e74c3c", fg="white", font=("Arial", 9, "bold"))
btn_del.pack(pady=10)

refresh_list()

root.mainloop()
