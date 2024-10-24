import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox, filedialog

# Tcl/Tk dizinini ayarlayın
os.environ['TCL_LIBRARY'] = r'C:\Users\Kamil\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Kamil\AppData\Local\Programs\Python\Python313\tcl\tk8.6'

# Global değişkenler
excel_dosyaları = []
sheets = {}


# Excel dosyasını yüklemek için fonksiyon
def excel_yukle():
    dosya_yolu = filedialog.askopenfilename(title="Excel Dosyasını Seçin", filetypes=[("Excel Files", "*.xlsx;*.xls")])

    if dosya_yolu:
        dosya_adi = dosya_yolu.split("/")[-1]  # Dosya adını al
        excel_dosyaları.append(dosya_yolu)  # Yüklenen dosyayı kaydet
        sheets[dosya_adi] = pd.ExcelFile(dosya_yolu).sheet_names  # Sheetleri al

        # Yüklenen dosyaları ve sheetleri göster
        güncelle_dosya_listesi()


def güncelle_dosya_listesi():
    dosya_listesi_text.delete(1.0, tk.END)  # Önceki içeriği temizle
    for dosya in excel_dosyaları:
        dosya_adi = dosya.split("/")[-1]
        sheet_listesi = sheets[dosya_adi]
        dosya_listesi_text.insert(tk.END, f"{dosya_adi} - Sheetler: {', '.join(sheet_listesi)}\n")


def plaka_ara():
    aranan_deger = plaka_entry.get()
    bulunan_hücreler = []

    # Her yüklü dosya için sheet'leri gez
    for dosya in excel_dosyaları:
        dosya_adi = dosya.split("/")[-1]
        for sheet in sheets[dosya_adi]:
            df = pd.read_excel(dosya, sheet_name=sheet)
            data_list = df.values.tolist()

            # Her sheet'teki hücreleri kontrol et
            for i, row in enumerate(data_list):
                for j, value in enumerate(row):
                    if value == aranan_deger:
                        bulunan_hücreler.append(
                            (dosya_adi, sheet, i, j, data_list[i][j + 1], data_list[i][j + 2], data_list[i][j + 3]
                             , data_list[i][j + 4], data_list[i][j + 5], data_list[i][j + 6]))
                        break

    # Sonuçları yazdır
    if bulunan_hücreler:
        sonuçlar_text.delete(1.0, tk.END)  # Önceki sonuçları temizle
        for dosya_adi, sheet, satir, sutun, sabah_vardiyasi, sabah_yedek_sofor, oglen_vardiyasi, oglen_yedek_sofor, aksam_vardiyasi, gece_vardiyasi in bulunan_hücreler:
            sonuçlar_text.insert(tk.END, f"Dosya: {dosya_adi}, Sheet: {sheet}\n")
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

# Yüklenen Excel dosyalarının ve sheetlerin adlarını göstermek için metin alanı
dosya_listesi_text = tk.Text(root, height=10)
dosya_listesi_text.pack(side=tk.TOP, expand=True, fill=tk.BOTH, padx=5, pady=5)

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