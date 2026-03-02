import math  # import library math buat fungsi ilmiah kayak sin, cos, sqrt
from utils.history import add_history  # import fungsi buat nyimpen riwayat

def tambah(a, b): return a + b  # penjumlahan
def kurang(a, b): return a - b  # pengurangan
def kali(a, b): return a * b  # perkalian
def bagi(a, b):  # pembagian, tapi dicek dulu biar ga error
    if b == 0: raise ZeroDivisionError("Gabisa dibagi nol bos!")  # tolak kalau pembaginya 0
    return a / b

def pangkat(a, b): return a**b  # perpangkatan, misal 2^3 = 8
def modulo(a, b): return a % b  # sisa bagi, misal 10%3 = 1
def akar(a):  # fungsi akar kuadrat
    if a < 0: return "Error: harus positif"  # akar dari negatif ga valid
    return math.sqrt(a)  # hitung akar pake math

def hitung_ekspresi(teks):  # fungsi hitung ekspresi berantai kayak "5+3*2"
    try:
        return eval(teks)  # eval otomatis handle urutan operasi (kali dulu baru tambah)
    except:
        return "Input salah"  # kalau ekspresinya ga valid

def menu_aritmatika():  # fungsi menu utama kalkulator aritmatika
    print("\n=== KALKULATOR ARITMATIKA ===")  # judul
    print("1. Operasi Dasar\n2. Operasi Ilmiah\n3. Ekspresi Berantai")  # opsi menu
    
    pilih = input("Mau pilih nomor berapa? ")  # minta input user
    
    if pilih == "1":  # kalau pilih operasi dasar
        try:
            n1 = float(input("Angka pertama: "))  # input angka pertama, diubah ke float
            ops = input("Pilih operator (+,-,*,/,^,%,sqrt): ")  # input operator
            
            if ops == "sqrt":  # kalau sqrt, cukup 1 angka
                hasil = akar(n1)  # hitung akar
                print(f"Hasilnya: {hasil}")  # tampilin hasil
                add_history("Dasar", f"sqrt({n1})", str(hasil))  # simpan riwayat
            else:
                n2 = float(input("Angka kedua: "))  # kalau bukan sqrt, minta angka kedua
                if ops == "+": hasil = tambah(n1, n2)  # pilih fungsi sesuai operator
                elif ops == "-": hasil = kurang(n1, n2)
                elif ops == "*": hasil = kali(n1, n2)
                elif ops == "/": hasil = bagi(n1, n2)
                elif ops == "^": hasil = pangkat(n1, n2)
                elif ops == "%": hasil = modulo(n1, n2)
                else: 
                    print("Operator ga dikenal!")  # kalau operatornya aneh
                    return
                print(f"Hasilnya: {hasil}")  # tampilin hasil
                add_history("Dasar", f"{n1}{ops}{n2}", str(hasil))  # simpan riwayat
        except ZeroDivisionError as e: print(e)  # tangkap error bagi nol
        except ValueError: print("Isinya harus angka!")  # tangkap error input bukan angka

    elif pilih == "2":  # kalau pilih operasi ilmiah
        print("Menu: sin, cos, tan, log, ln")  # tampilin pilihan
        pilih_ilmu = input("Pilih: ").lower()  # input fungsi, langsung dijadiin huruf kecil
        try:
            bil = float(input("Angka: "))  # input angka
            if pilih_ilmu == "sin": r = math.sin(math.radians(bil))  # sin, input derajat diubah ke radian
            elif pilih_ilmu == "cos": r = math.cos(math.radians(bil))  # cos
            elif pilih_ilmu == "tan": r = math.tan(math.radians(bil))  # tan
            elif pilih_ilmu == "log": r = math.log10(bil)  # log basis 10
            elif pilih_ilmu == "ln": r = math.log(bil)  # log natural (basis e)
            else: return  # kalau ga dikenal, langsung keluar
            print(f"Hasilnya: {r}")  # tampilin hasil
            add_history("Ilmiah", f"{pilih_ilmu}({bil})", str(r))  # simpan riwayat
        except: print("Error hitung!")  # kalau ada error apapun

    elif pilih == "3":  # kalau pilih ekspresi berantai
        ekspresi = input("Masukkan ekspresi (misal 5+3*2): ")  # input ekspresi
        hasil = hitung_ekspresi(ekspresi)  # hitung ekspresinya
        print(f"Hasil: {hasil}")  # tampilin hasil
        print(f"Langkah: {ekspresi} = {hasil}")  # tampilin ulang biar keliatan prosesnya
        add_history("Berantai", ekspresi, str(hasil))  # simpan riwayat

if __name__ == "__main__":  # kalau file ini dirun langsung
    menu_aritmatika()  # panggil menu aritmatika