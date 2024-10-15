class BasitHesapMakinesi:
    def __init__(self,birinci_sayi,ikinci_sayi):
        self.birinci_sayi = birinci_sayi
        self.ikinci_sayi = ikinci_sayi

    def topla(self):
        return self.birinci_sayi + self.ikinci_sayi

    def carpma(self):
        return self.birinci_sayi * self.ikinci_sayi


