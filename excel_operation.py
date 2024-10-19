#terminalde pip install pandas openpyxl komutu çalıştırılarak pandas kütüphanesi eklendi.
import pandas as pd


# Excel dosyasının path ini belirt
file_path = 'ornekexcel.xlsx'


# Excel dosyasındaki sayfa isimlerini al
sayfa_isimleri = pd.ExcelFile(file_path).sheet_names
print(sayfa_isimleri)


# Excel dosyasını oku
#df = pd.read_excel(file_path)

# Belirli bir sayfayı oku
df_sheet1 = pd.read_excel(file_path, sheet_name=sayfa_isimleri[1])

# Verileri bir listeye çevir
veri_listesi = df_sheet1.values.tolist()

# Listeyi yazdır
print(veri_listesi)

#listenin uzunlugunu öğrenme
print(len(veri_listesi))