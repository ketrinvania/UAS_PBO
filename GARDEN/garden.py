# Nama  : Ketrin Vani Andini
# NIM   : 20210801348
# PBO GAME GARDEN

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox 


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

# child class
class Mawar(Plant):

    def __init__(self, JumlahAir, JumlahPupuk, StatusTumbuh, Jenis):
        self.Jenis = Jenis
        Plant.__init__(self, JumlahAir, JumlahPupuk, StatusTumbuh)
    
    def mawarTumbuh(self):
        if self.StatusTumbuh < 4:
            self.JumlahAir -= 3
            self.JumlahPupuk -= 1
            self.StatusTumbuh += 1
    
    def cekKondisiTumbuh(self):
        if self.JumlahAir >= 3 and self.JumlahPupuk >= 1:
            Mawar.mawarTumbuh()
    
    def getJenis(self):
        return self.Jenis
 
# child class
class Melati(Plant):

    def __init__(self, JumlahAir, JumlahPupuk, StatusTumbuh, Jenis):
        self.Jenis = Jenis
        Plant.__init__(self, JumlahAir, JumlahPupuk, StatusTumbuh)
    
    def melatiTumbuh(self):
        if self.StatusTumbuh < 4:
            self.JumlahAir -= 3
            self.JumlahPupuk -= 1
            self.StatusTumbuh += 1
    
    def cekKondisiTumbuh(self):
        if self.JumlahAir >= 3 and self.JumlahPupuk >= 1:
            Melati.melatiTumbuh()
    
    def getJenis(self):
        return self.Jenis
 
class Garden(Plant):

    def __init__(self,JumlahAir, JumlahPupuk, StatusTumbuh, Size, nTanaman, mGardenName,hasilpanen ):
        self.Size = Size
        self.nTanaman = nTanaman
        self.mGardenName = mGardenName
        self.pArrList = [" "]
        self.hasilpanen = hasilpanen
        Plant.__init__(self,JumlahAir,JumlahPupuk,StatusTumbuh)

    def Garden(self, pName):
        self.mGardenName = pName
    
    def addPlant(self):
        if self.nTanaman < self.Size:
            self.pArrList.append()
            self.nTanaman += 1
            return True
        else:
            return False
    
    def harvestPlant(self):
        tmpN = 0 
        i = 0
        length = len(self.pArrList)
        while self.pArrList != 0 and i < length:
            if self.pArrList[i] == 4 and Plant.getStatusTumbuh() == 4:
                self.pArrList.remove[i]
                self.nTanaman -= 1
                tmpN -= 1
                i = 0
            else:
                i += 1
            
            self.hasilpanen = self.hasilpanen + (tmpN *100)
            return tmpN

    def BeriAir(self):
        for i in range(0, len(self.pArrList)):
            self.pArrList[i] = Garden.BeriAir()
    
    def BeriPupuk(self):
        for i in range(0, len(self.pArrList)-1):
            self.pArrList[i] = Garden.BeriPupuk()
    
    def displayPlant(self):
        print("-------- {}".format(self.mGardenName))
        print("There are {} plants in the garden".format(self.nTanaman))
        print("Your harvest point : {}".format(self.hasilpanen))

        for i in range(0, len(self.pArrList)-1):
            self.pArrList[i] = Garden.displayPlant()
    
    def getHasilPanen(self):
        return self.hasilpanen
    

Tanaman1 = Anggrek(2, 3, 4, 'Anggrek')
print("Jenis Tanaman \t: {}".format(Tanaman1.Jenis))
Tanaman1.getStatusTumbuhText()
Tanaman1.DisplayPlant()


Tanaman2 = Mawar(1, 4, 2, 'Mawar')
print("\nJenis Tanaman \t: {}".format(Tanaman2.Jenis))
Tanaman2.getStatusTumbuhText()
Tanaman2.DisplayPlant()


Tanaman3 = Melati(3, 1, 1, 'Melati')
print("\nJenis Tanaman \t: {}".format(Tanaman3.Jenis))
Tanaman3.getStatusTumbuhText()
Tanaman3.DisplayPlant()



# GUI 

main_window = tk.Tk()
main_window.configure(bg="black")
main_window.geometry("500x400")
main_window.title("KEBUN BUNGA")

input_frame = ttk.Frame(main_window)
input_frame.pack(padx=10, pady=10,fill="x",expand=True)

def choose(*args):
    for a in args:
        a.destroy()

    def BeriAir():
        messagebox.showinfo( "KEBUN BUNGA", "Tanaman berhasil di beri Air") 


    B1 = tk.Button(input_frame, text ="Beri Air pada tanaman", command = BeriAir)
    B1.pack()

    def BeriPupuk():
        messagebox.showinfo( "KEBUN BUNGA", "Tanaman berhasil di beri pupuk") 

    B2 = tk.Button(input_frame, text ="Beri Pupuk pada tanaman", command = BeriPupuk)
    B2.pack()
        
        

text = tk.Label(input_frame, text="WELCOME TO THE FLOWER GARDEN")
text.pack(padx=10, pady=10,fill="y",expand=True)

button1 = tk.Button(input_frame,text= "1. Anggrek  ", command=lambda : choose(button1,button2,button3))
button1.pack(padx=10, pady=10,fill="y",expand=True)

button2 = tk.Button(input_frame,text= "2. Mawar", command=lambda : choose(button1, button2,button3))
button2.pack(padx=10, pady=10,fill="y",expand=True)

button3 = tk.Button(input_frame,text= "3. Melati", command=lambda : choose(button1, button2, button3))
button3.pack(padx=10, pady=10,fill="y",expand=True)


main_window.mainloop()








