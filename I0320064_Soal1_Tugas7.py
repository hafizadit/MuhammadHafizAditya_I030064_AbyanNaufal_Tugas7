import math
import sys

def headerFooter(teks):
    print("")
    print("="*50)
    print(teks.center(50))
    print("="*50)
    print("")

def kapital():
    print("\n-----Huruf Kapital-----\n")
    print("\nHasil Kapitalisasi :")
    print(teks.title())
    mainmenu()
    sys.exit()

def string():
    global teks
    teks = input("\nMasukkan String Anda :")
    mainmenu()
    sys.exit()

def upperLower():
    print("\n-----Upper dan Lower-----\n")
    print(f'String Upper : {teks.upper()}')
    print(f'String Lower : {teks.lower()}')
    mainmenu()
    sys.exit()

def cari():
    print("\n-----Cari Karakter-----\n")
    cari = input("Karakter yang ingin dicari :")
    hasil = teks.find(cari)
    if hasil == -1:
        print("Teks tidak ditemukan")
    else:
        print(f'Karakter {cari} ditemukan di index : {hasil}')
    mainmenu()
    sys.exit()

def mainmenu():
    headerFooter("Program Fungsi String")
    print("\nString Anda :")
    print(teks)
    print("""\n====Silakan Pilih Menu=====
1. Kapitalisasi
2. Upper dan Lower
3. Cari Karakter
4. Ganti String
s untuk Selesai""")
    x = "dummy"
    while x != "s":
        x = input("\nMasukkan Menu yang Anda Pilih :")
        if x == "1" or x == "2" or x == "3" or x == "4":
            if x == "1":
                kapital()
            elif x == "2":
                upperLower()
            elif x == "3":
                cari()
            elif x == "4":
                string()
        elif x == "s":
            headerFooter("Program Selesai")
        else:
            print("\nInput yang anda masukkan salah, silakan Mengulang!")
            mainmenu()
            sys.exit()

if __name__ == "__main__":
    string()