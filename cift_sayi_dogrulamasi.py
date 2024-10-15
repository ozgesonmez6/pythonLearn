class CiftSayiDogrulama:
    def __init__(self, sayi):
        self.sayi=sayi

    def control(self):
        if self.sayi % 2 == 0:
            print(self.sayi, "sayısı çiftir")
        else:
            print(self.sayi, "sayısı tektir")