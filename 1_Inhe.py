# Nama  : Ketrin Vani Andini
# NIM   : 20210801348
# UAS PBO NOMER 1

# Parent class
class Plant(object):
    
    def __init__(self, JumlahAir, JumlahPupuk, StatusTumbuh):
        self.JumlahAir = JumlahAir
        self.JumlahPupuk = JumlahPupuk
        self.StatusTumbuh = StatusTumbuh

    def Tumbuh(self):
        if self.StatusTumbuh < 4:
            self.JumlahAir -= 3
            self.JumlahPupuk -= 1
            self.StatusTumbuh += 1

    def cekKondisiTumbuh(self):
        if self.JumlahAir >= 3 and self.JumlahPupuk >= 1:
            Plant.Tumbuh(self)
    
    def BeriAir(self):
        self.JumlahAir += 1
        Plant.cekKondisiTumbuh(self)
    
    def BeriPupuk(self):
        self.JumlahPupuk += 1
        Plant.cekKondisiTumbuh(self)
    
    def getStatusTumbuhText(self):
        if self.StatusTumbuh == 0:
            print("Benih") 
        elif self.StatusTumbuh == 1:
            print("Tunas")
        elif self.StatusTumbuh == 2:
            print("Tanaman Kecil")
        elif self.StatusTumbuh == 3:
            print("Tanaman Dewasa")
        else:
            print("Berbunga")

    def DisplayPlant(self):
        # print(Plant.getStatusTumbuhText)
        print("Jumlah Air \t: {} \nJumlah Pupuk \t: {}".format(self.JumlahAir, self.JumlahPupuk))


    def getJumlahAir(self):
        return self.JumlahAir
    
    def setJumlahAir(self, n):
        self.JumlahAir = n
    
    def getJumlahPupuk(self):
        return self.JumlahPupuk
    
    def setJumlahPupuk(self, n):
        self.JumlahPupuk = n 
    
    def getStatusTumbuh(self):
        return self.StatusTumbuh
    
    def setStatusTumbuh(self, n):
        self.StatusTumbuh = n

# child class
class Anggrek(Plant):

    def __init__(self, JumlahAir, JumlahPupuk, StatusTumbuh, Jenis):
        self.Jenis = Jenis
        Plant.__init__(self, JumlahAir, JumlahPupuk, StatusTumbuh)
    
    def anggrekTumbuh(self):
        if self.StatusTumbuh < 4:
            self.JumlahAir -= 3
            self.JumlahPupuk -= 2
            self.StatusTumbuh += 1
    
    def cekKondisiTumbuh(self):
        if self.JumlahAir >= 3 and self.JumlahPupuk >= 2:
            Anggrek.anggrekTumbuh()
    
    def getJenis(self):
        return self.Jenis

Tanaman1 = Anggrek(2, 3, 4, 'Anggrek')
print("Jenis Tanaman \t: {}".format(Tanaman1.Jenis))
Tanaman1.getStatusTumbuhText()
Tanaman1.DisplayPlant()
