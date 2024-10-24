# terminalde pip install pandas openpyxl komutu çalıştırılarak pandas kütüphanesi eklendi.
import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox, filedialog

# Tcl/Tk dizinini ayarlayın
os.environ['TCL_LIBRARY'] = r'C:\Users\Kamil\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Kamil\AppData\Local\Programs\Python\Python313\tcl\tk8.6'

# Excel dosyasının path ini belirt
# file_path = 'kocavilayet.xlsx'


# Excel dosyasındaki sayfa isimlerini al
# sayfa_isimleri = pd.ExcelFile(file_path).sheet_names
# print(sayfa_isimleri)


# Excel dosyasını oku
# df = pd.read_excel(file_path)

# Belirli bir sayfayı oku
# df_sheet1 = pd.read_excel(file_path, sheet_name=sayfa_isimleri[3])

# Verileri bir listeye çevir
# veri_listesi = df_sheet1.values.tolist()

# Listeyi yazdır
# print(veri_listesi)

# listenin uzunlugunu öğrenme
# print(len(veri_listesi))

# Excel dosyasını oku
#excel_dosyasi = 'kocavilayet.xlsx'
#sheets = pd.ExcelFile(excel_dosyasi).sheet_names

excel_dosyasi = ''
sheets = None


# Excel dosyasını yüklemek için fonksiyon
def excel_yukle():
    global excel_dosyasi, sheets
    excel_dosyasi = filedialog.askopenfilename(title="Excel Dosyasını Seçin",
                                               filetypes=[("Excel Files", "*.xlsx;*.xls")])

    if excel_dosyasi:
        sheets = pd.ExcelFile(excel_dosyasi).sheet_names
        dosya_adi = excel_dosyasi.split("/")[-1]  # Dosya adını al
        dosya_label.config(text=f"Yüklenen Excel Dosyası: {dosya_adi}")  # Etiket güncelle
        messagebox.showinfo("Bilgi", "Excel dosyası başarıyla yüklendi.")

def plaka_ara():
    aranan_deger = plaka_entry.get()
    bulunan_hücreler = []

    # Her sheet'i gez
    for sheet in sheets:
        df = pd.read_excel(excel_dosyasi, sheet_name=sheet)
        data_list = df.values.tolist()

        # Her sheet'teki hücreleri kontrol et
        for i, row in enumerate(data_list):
            for j, value in enumerate(row):
                if value == aranan_deger:
                    bulunan_hücreler.append((sheet, i, j, data_list[i][j + 1], data_list[i][j + 2], data_list[i][j + 3]
                                             , data_list[i][j + 4], data_list[i][j + 5], data_list[i][j + 6]))
                    break

        # Sonuçları yazdır
    if bulunan_hücreler:
        sonuçlar_text.delete(1.0, tk.END)  # Önceki sonuçları temizle
        for sheet, satir, sutun, sabah_vardiyasi, sabah_yedek_sofor, oglen_vardiyasi, oglen_yedek_sofor, aksam_vardiyasi, gece_vardiyasi, in bulunan_hücreler:
            sonuçlar_text.insert(tk.END, f"Sheet: {sheet}\n", 'sheet')
            sonuçlar_text.insert(tk.END, f"Satır: {satir + 2}, Sütun: {sutun + 1}\n")
            sonuçlar_text.insert(tk.END, f"SABAH VARDIYASI : {sabah_vardiyasi}\n")
            sonuçlar_text.insert(tk.END, f"SABAH YEDEK SOFÖR : {sabah_yedek_sofor}\n")
            sonuçlar_text.insert(tk.END, f"ÖĞLEN VARDIYASI : {oglen_vardiyasi}\n")
            sonuçlar_text.insert(tk.END, f"ÖĞLEN YEDEK SÖFOR : {oglen_yedek_sofor}\n")
            sonuçlar_text.insert(tk.END, f"AKŞAM VARDIYASI : {aksam_vardiyasi}\n")
            sonuçlar_text.insert(tk.END, f"GECE VARDIYASI : {gece_vardiyasi}\n")
            sonuçlar_text.insert(tk.END, f"--------------------\n")

    else:
        messagebox.showerror("UYARI", f"Değer '{aranan_deger}' bulunamadı.")


# Tkinter arayüzü
root = tk.Tk()
root.title("Plaka Ara")

# Excel dosyası yükle butonu
yukle_button = tk.Button(root, text="Excel Yükle", command=excel_yukle)
yukle_button.pack(pady=5)

# Yüklenen Excel dosyasının adını göstermek için etiket
dosya_label = tk.Label(root, text="Yüklenen Excel Dosyası: Yok")
dosya_label.pack(pady=5)

# Plaka girişi
plaka_label = tk.Label(root, text="Plaka Girişi:")
plaka_label.pack(pady=5)

plaka_entry = tk.Entry(root)
plaka_entry.pack(pady=5)

# Ara butonu
ara_button = tk.Button(root, text="Ara", command=plaka_ara)
ara_button.pack(pady=10)

# Sonuçları göstermek için metin alanı
sonuçlar_text = tk.Text(root)
sonuçlar_text.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)
sonuçlar_text.tag_configure('sheet', foreground='red', font=('Arial', 12, 'bold'))

# Renk tanımlamaları
frame = tk.Frame(root)
frame.pack(expand=True, fill=tk.BOTH)

# Kaydırma çubuğu
scrollbar = tk.Scrollbar(frame, command=sonuçlar_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

sonuçlar_text.config(yscrollcommand=scrollbar.set)
# Arayüzü başlat
root.mainloop()

# print(
#    f"Değer '{aranan_deger}' bulundu! Sheet: {sheet}, Satır: {satir + 2}, Sütun: {sutun + 1},SABAH VARDIYASI : {sabah_vardiyasi}"
#   f",SABAH YEDEK SOFÖR : {sabah_yedek_sofor},ÖĞLEN VARDIYASI : {oglen_vardiyasi},ÖĞLEN YEDEK SÖFOR : {oglen_yedek_sofor},AKŞAM VARDIYASI : {aksam_vardiyasi},GECE VARDIYASI : {gece_vardiyasi}\n")
