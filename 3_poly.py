# Nama  : Ketrin Vani Andini
# NIM   : 20210801348
# UAS PBO NOMER 3

class Plant:
    def __init__(self, Name, Jenis ):
        self.Name = Name
        self.Jenis = Jenis
    
    def Info(self):
        print("Nama Tumbuhan \t: {} \nJenis Tumbuhan \t: {} ".format(self.Name, self.Jenis))
    

class Animal:
    def __init__(self, Name, Jenis ):
        self.Name = Name
        self.Jenis = Jenis
    
    def Info(self):
        print("Nama Hewan \t: {} \nJenis Hewan \t: {} ".format(self.Name, self.Jenis))
    
tumbuhan = Plant("Anggrek","Tanaman Hias")
tumbuhan.Info()
hewan = Animal("Kucing","Karnivora")
hewan.Info()