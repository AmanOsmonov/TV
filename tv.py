class Tv():
    def __init__(self, model):
        self.model = model
        print("телевизор", model, " включон")

    def kanal(self, num):
        if num > 0 and num < 16:
            print("тв", self.model, " переключон на ", str(num), "канал")
        else:
            print("нет такого канала")

    def zvuk(self):
        a = 50
        print("звук сейчас=", str(a))
        a = int(input("введите урвень громкости"))

        if a >= 0 and a <= 100:
            print("звук на уровне", a)
        else:
            print("звук не может быть меньше 0 и больше 100\n ")


mytv = Tv("lg")
mytv.kanal(2)
mytv.zvuk()