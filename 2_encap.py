# Nama  : Ketrin Vani Andini
# NIM   : 20210801348
# UAS PBO NOMER 2

class Mahasiswa():
    def __init__(self):
        self.__nama = "Ketrin Vani Andini"
        self.__nim = "20210801348"

    def getInfo(self):
        print("NAMA \t: {}".format(self.__nama))
        print("NIM \t: {}".format(self.__nim))

    def setInfo(self, nama, nim):
        self.__nama = nama
        self.__nim = nim

Data = Mahasiswa()
Data.getInfo()
Data.setInfo("Jennie Ruby Jane","20210928111")
Data.getInfo()




