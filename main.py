import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import io

class App:
    def __init__(self):
        self.window1 = tk.Tk()
        self.window1.title("Image Viewer")
        self.window1.geometry("400x100")
        self.window1.resizable(False, False)
        self.window1.configure(bg="#212121")

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TEntry', foreground="#FFFFFF", fieldbackground="#424242", bordercolor="#212121")
        style.configure('TLabel', background="#212121", foreground="#FFFFFF")
        style.configure('TButton', background="#616161", foreground="#FFFFFF", padding=10, font=("Helvetica", 12), bordercolor="#212121")
        style.map('TButton', background=[('active', '#424242')])

        self.link_entry = ttk.Entry(self.window1, font=("Helvetica", 14))
        self.link_entry.insert(0, "Insert link")
        self.link_entry.pack(pady=10)

        self.start_button = ttk.Button(self.window1, text="Start", command=self.start_process)
        self.start_button.pack()

        self.window2 = tk.Toplevel(self.window1)
        self.window2.title("Image Viewer")
        self.window2.resizable(False, False)
        self.window2.configure(bg="#212121")
        self.window2.withdraw()

        self.image_label = tk.Label(self.window2)
        self.image_label.pack(pady=10)

        self.close_button = ttk.Button(self.window2, text="Close", command=self.close_window2)
        self.close_button.pack()

        self.photo = None

    def start_process(self):
        link = self.link_entry.get()
        response = requests.get(link)
        img = Image.open(io.BytesIO(response.content))
        self.photo = ImageTk.PhotoImage(img)
        self.image_label.config(image=self.photo)
        self.window2.deiconify()
        self.window1.withdraw()
        self.update_image()

    def update_image(self):
        link = self.link_entry.get()
        response = requests.get(link)
        img = Image.open(io.BytesIO(response.content))
        self.photo = ImageTk.PhotoImage(img)
        self.image_label.config(image=self.photo)
        self.window2.after(200, self.update_image)

    def close_window2(self):
        self.window1.deiconify()
        self.window2.withdraw()

app = App()
app.window1.mainloop()
