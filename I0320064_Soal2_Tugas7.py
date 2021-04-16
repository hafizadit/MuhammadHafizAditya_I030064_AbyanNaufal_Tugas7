import sys
import math

def headerFooter(teks):
    print("")
    print("="*50)
    print(teks.center(50))
    print("="*50)
    print("")

def absolut():
    print("\n-----Program Nilai Absolut-----\n")
    x = "dummy"
    data = []
    print("Masukkan Angka (Tekan Enter untuk melihat hasil)")
    while x != "":
        x = input(">>")
        if x == "":
            print("\nHasil Nilai Absolut :")
            for i in data:
                print(abs(i))
            print("")
            mainMenu()
            sys.exit()
        data.append(float(x))

def ceilFloor():
    print("\n-----Program Ceil dan Floor-----\n")
    x = "dummy"
    data = []
    print("Masukkan Angka (Tekan Enter untuk melihat hasil)")
    while x != "":
        x = input(">>")
        if x == "":
            print("\nHasil Nilai Floor :")
            for i in data:
                print(math.floor(i))
            print("\nHasil Nilai Ceil :")
            for i in data:
                print(math.ceil(i))
            print("")
            mainMenu()
            sys.exit()
        data.append(float(x))

def minMax():
    print("\n-----Program Min Max-----\n")
    x = "dummy"
    data = []
    print("Masukkan Angka (Tekan Enter untuk melihat hasil)")
    while x != "":
        x = input(">>")
        if x == "":
            print(f"\nNilai min : {min(data)}")
            print(f"Nilai max : {max(data)}")
            print("")
            mainMenu()
            sys.exit()
        data.append(float(x))

def akar():
    print("\n-----Program Akar-----\n")
    x = "dummy"
    data = []
    print("Masukkan Angka (Tekan Enter untuk melihat hasil)")
    while x != "":
        x = input(">>")
        if x == "":
            print("\nHasil Nilai Floor :")
            for i in data:
                print(math.sqrt(i))
            print("")
            mainMenu()
            sys.exit()
        data.append(float(x))


def mainMenu():
    headerFooter("Program Numerik")
    print("""=====Silakan Pilih Menu=====
1. Nilai Absolut
2. Nilai Ceil dan Floor
3. Nilai Min dan Max
4. Nilai Akar
s untuk selesai\n""")
    x = "dummy"
    while x != "s":
        x = input("\nMasukkan Menu yang Anda Pilih :")
        if x == "1" or x == "2" or x == "3" or x == "4":
            if x == "1":
                absolut()
            elif x == "2":
                ceilFloor()
            elif x == "3":
                minMax()
            elif x == "4":
                akar()
        elif x == "s":
            headerFooter("Program Selesai")
        else:
            print("\nInput yang anda masukkan salah, silakan Mengulang!")
            mainMenu()
            sys.exit()
        
if __name__ == "__main__":
    mainMenu()