import math
from utils.history import add_history

# fungsi-fungsi dasar buat kalkulator
def tambah(a, b): return a + b
def kurang(a, b): return a - b
def kali(a, b): return a * b
def bagi(a, b):
    # cek biar ga error bagi nol
    if b == 0: raise ZeroDivisionError("Gabisa dibagi nol bos!")
    return a / b

def pangkat(a, b): return a**b
def modulo(a, b): return a % b
def akar(a):
    if a < 0: return "Error: harus positif"
    return math.sqrt(a)

def hitung_ekspresi(teks):
    # pake eval buat precedence otomatis (kabataku)
    try:
        return eval(teks)
    except:
        return "Input salah"

def menu_aritmatika():
    print("\n=== KALKULATOR ARITMATIKA ===")
    print("1. Operasi Dasar\n2. Operasi Ilmiah\n3. Ekspresi Berantai")
    
    pilih = input("Mau pilih nomor berapa? ")
    
    if pilih == "1":
        try:
            n1 = float(input("Angka pertama: "))
            ops = input("Pilih operator (+,-,*,/,^,%,sqrt): ")
            
            if ops == "sqrt":
                hasil = akar(n1)
                print(f"Hasilnya: {hasil}")
                add_history("Dasar", f"sqrt({n1})", str(hasil))
            else:
                n2 = float(input("Angka kedua: "))
                if ops == "+": hasil = tambah(n1, n2)
                elif ops == "-": hasil = kurang(n1, n2)
                elif ops == "*": hasil = kali(n1, n2)
                elif ops == "/": hasil = bagi(n1, n2)
                elif ops == "^": hasil = pangkat(n1, n2)
                elif ops == "%": hasil = modulo(n1, n2)
                else: 
                    print("Operator ga dikenal!")
                    return
                print(f"Hasilnya: {hasil}")
                add_history("Dasar", f"{n1}{ops}{n2}", str(hasil))
        except ZeroDivisionError as e: print(e)
        except ValueError: print("Isinya harus angka!")

    elif pilih == "2":
        # buat menu ilmiah sin/cos/tan dll
        print("Menu: sin, cos, tan, log, ln")
        pilih_ilmu = input("Pilih: ").lower()
        try:
            bil = float(input("Angka: "))
            if pilih_ilmu == "sin": r = math.sin(math.radians(bil))
            elif pilih_ilmu == "cos": r = math.cos(math.radians(bil))
            elif pilih_ilmu == "tan": r = math.tan(math.radians(bil))
            elif pilih_ilmu == "log": r = math.log10(bil)
            elif pilih_ilmu == "ln": r = math.log(bil)
            else: return
            print(f"Hasilnya: {r}")
            add_history("Ilmiah", f"{pilih_ilmu}({bil})", str(r))
        except: print("Error hitung!")

    elif pilih == "3":
        # bagian ekspresi berantai (soal 1C)
        ekspresi = input("Masukkan ekspresi (misal 5+3*2): ")
        hasil = hitung_ekspresi(ekspresi)
        print(f"Hasil: {hasil}")
        # tampilin langkah simpel sesuai contoh
        print(f"Langkah: {ekspresi} = {hasil}")
        add_history("Berantai", ekspresi, str(hasil))

if __name__ == "__main__":
    menu_aritmatika()