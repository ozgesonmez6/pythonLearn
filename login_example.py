import tkinter as tk
from tkinter import messagebox
import os

from PIL import Image, ImageTk

# Tcl/Tk dizinini ayarlayın
os.environ['TCL_LIBRARY'] = r'C:\Users\Kamil\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Kamil\AppData\Local\Programs\Python\Python313\tcl\tk8.6'


# Giriş fonksiyonu
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Basit bir kontrol
    if username == "admin" and password == "1234":
        messagebox.showinfo("Giriş Başarılı", "Hoş geldiniz!")
    else:
        messagebox.showerror("Giriş Hatası", "Kullanıcı adı veya şifre hatalı.")

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Giriş Sayfası")
root.geometry("400x300")

# Arka plan resmi
bg_image = Image.open("login.jpg")  # Arka plan resminin yolu
bg_image = bg_image.resize((400, 300), Image.HUFFMAN_ONLY)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Kullanıcı adı etiketi ve girişi
label_username = tk.Label(root, text="Kullanıcı Adı:", bg='white', font=("Arial", 12))
label_username.place(x=50, y=50)
entry_username = tk.Entry(root, bg='lightgrey', font=("Arial", 12), bd=0, relief="flat")
entry_username.place(x=150, y=50, width=200)

# Şifre etiketi ve girişi
label_password = tk.Label(root, text="Şifre:", bg='white', font=("Arial", 12))
label_password.place(x=50, y=100)
entry_password = tk.Entry(root, show="*", bg='lightgrey', font=("Arial", 12), bd=0, relief="flat")
entry_password.place(x=150, y=100, width=200)

# Giriş butonu
button_login = tk.Button(root, text="Giriş Yap", command=login, bg='blue', fg='white', font=("Arial", 12))
button_login.place(x=150, y=150, width=100)

# Pencereyi çalıştır
root.mainloop()