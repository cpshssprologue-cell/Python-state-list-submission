import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import random
from PIL import Image, ImageTk
from Assets.Data import Data
from Window import ArticleWindow # Assuming Window.py contains the class you shared
import os

class HomeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Home")
        self.root.geometry("1000x600")
        self.custom_font = ("Rajdhani", 24, "bold")
        self.kesar_yellow = "#FF9933" # Indian Saffron / Kesar

        # 2. Set Background
        bg_path = "Assets/Images/bgimg.jpg"
        if os.path.exists(bg_path):
            img = Image.open(bg_path).resize((1000, 600))
            self.bg_img = ImageTk.PhotoImage(img)
            bg_label = tk.Label(self.root, image=self.bg_img)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # 3. Heading
        heading = tk.Label(
            self.root, text="HELLO INDIA", 
            font=self.custom_font, fg=self.kesar_yellow, bg="black"
        )
        heading.pack(pady=50)

        # 4. Buttons Frame
        btn_frame = tk.Frame(self.root, bg="black")
        btn_frame.pack(pady=20)

        buttons = [
            ("View List", self.open_list),
            ("Search", self.open_search),
            ("Random Site", self.open_random),
            ("Add Entry", self.add_entry),
            ("Delete Entry", self.delete_entry)
        ]

        for text, cmd in buttons:
            tk.Button(btn_frame, text=text, width=15, command=cmd).pack(pady=5)

    def open_list(self):
        list_win = tk.Toplevel(self.root)
        list_win.title("Heritage Site List")
        list_win.geometry("800x400")

        # Table (Treeview)
        cols = ("ID", "Name", "State", "City", "Established")
        tree = ttk.Treeview(list_win, columns=cols, show="headings")
        
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        for key, val in Data.items():
            # Index 2: Name, 4: State, 5: City, 7: Year
            tree.insert("", "end", values=(key, val[2], val[4], val[5], val[7]))

        tree.pack(fill="both", expand=True)

        # Double click to open the Article Window
        tree.bind("<Double-1>", lambda e: self.launch_article(tree))

    def launch_article(self, tree):
        selected = tree.selection()
        if selected:
            item_id = tree.item(selected[0])['values'][0]
            ArticleWindow(item_id) # Launches your class from Window.py

    def open_random(self):
        if Data:
            random_key = random.choice(list(Data.keys()))
            ArticleWindow(random_key)

    def open_search(self):
        # Implementation for search pop-up...
        pass

    def add_entry(self):
        # Logic to take input and append to Data.py 
        # (Requires file handling to make it permanent)
        messagebox.showinfo("Feature", "Entry System Triggered")

    def delete_entry(self):
        # Logic to pop item from Data dictionary
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = HomeApp(root)
    root.mainloop()
