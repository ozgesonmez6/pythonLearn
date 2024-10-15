from basit_hesap_makinesi import BasitHesapMakinesi
from cift_sayi_dogrulamasi import CiftSayiDogrulama

toplama_carpma_nesnesi = BasitHesapMakinesi(25,31)
print("TOPLAMA = " , toplama_carpma_nesnesi.topla())
print("ÇARPMA = " , toplama_carpma_nesnesi.carpma())


ciftcontrol= CiftSayiDogrulama(8)
ciftcontrol.control()
