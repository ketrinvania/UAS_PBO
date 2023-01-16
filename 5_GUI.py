# Nama  : Ketrin Vani Andini
# NIM   : 20210801348
# UAS PBO NOMER 5

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox 

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