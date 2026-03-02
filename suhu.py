from utils.history import add_history  # import fungsi buat nyimpen riwayat

def classified_temp(celsius):  # fungsi klasifikasi suhu berdasarkan nilainya
    if celsius <= 0: return "Beku"  # 0 ke bawah = beku
    elif 1 <= celsius <= 15: return "Dingin"  # 1-15 = dingin
    elif 16 <= celsius <= 25: return "Normal"  # 16-25 = normal
    elif 26 <= celsius <= 35: return "Panas"  # 26-35 = panas
    else: return "Sangat Panas"  # di atas 35 = sangat panas

def c_to_f(c): return (c * 9/5) + 32  # rumus Celsius ke Fahrenheit
def c_to_k(c): return c + 273.15  # rumus Celsius ke Kelvin
def c_to_r(c): return c * 4/5  # rumus Celsius ke Reaumur
def f_to_c(f): return (f - 32) * 5/9  # rumus Fahrenheit ke Celsius
def k_to_c(k): return k - 273.15  # rumus Kelvin ke Celsius
def r_to_c(r): return r * 5/4  # rumus Reaumur ke Celsius

def convert_temp(val, from_u, to_u):  # fungsi konversi antar satuan
    if from_u == 'C': c = val  # kalau dari Celsius, langsung pakai
    elif from_u == 'F': c = f_to_c(val)  # kalau dari Fahrenheit, konversi dulu ke Celsius
    elif from_u == 'K': c = k_to_c(val)  # kalau dari Kelvin, konversi dulu ke Celsius
    elif from_u == 'R': c = r_to_c(val)  # kalau dari Reaumur, konversi dulu ke Celsius
    
    if to_u == 'C': res = c  # kalau tujuan Celsius, langsung pakai
    elif to_u == 'F': res = c_to_f(c)  # kalau tujuan Fahrenheit, konversi dari Celsius
    elif to_u == 'K': res = c_to_k(c)  # kalau tujuan Kelvin, konversi dari Celsius
    elif to_u == 'R': res = c_to_r(c)  # kalau tujuan Reaumur, konversi dari Celsius
    
    return res, c  # return hasil konversi + nilai celsius buat klasifikasi

def display_table():  # fungsi nampilin tabel konversi
    print("\n=== TABEL KONVERSI SUHU (0°C - 100°C) ===")  # judul tabel
    header = f"{'Celsius':<8} | {'Fahr':<8} | {'Kelv':<8} | {'Reau':<8} | {'Status'}"  # header kolom
    print(header)  # tampilin header
    print("-" * len(header))  # garis pemisah sepanjang header
    for c in range(0, 101, 10):  # loop dari 0 sampai 100, loncat 10
        f, k, r = c_to_f(c), c_to_k(c), c_to_r(c)  # hitung semua satuan
        status = classified_temp(c)  # ambil klasifikasi suhu
        print(f"{c:<8}°C | {f:<8.1f}°F | {k:<8.1f}K | {r:<8.1f}°R | {status}")  # tampilin satu baris

def menu_suhu():  # fungsi menu utama kalkulator suhu
    print("\n=== KALKULATOR SUHU ===")  # judul menu
    print("1. Konversi Satuan")  # opsi 1
    print("2. Tabel Konversi")  # opsi 2
    print("3. Klasifikasi Suhu")  # opsi 3
    
    choice = input("Pilih: ")  # minta input user
    
    if choice == '1':  # kalau pilih konversi
        u = {'1': 'Celsius', '2': 'Fahrenheit', '3': 'Kelvin', '4': 'Reaumur'}  # mapping angka ke nama satuan
        print("Pilih: 1.C, 2.F, 3.K, 4.R")  # tampilin pilihan satuan
        try:  # pakai try buat antisipasi input salah
            f_idx = input("Dari: ")  # input satuan asal
            t_idx = input("Ke: ")  # input satuan tujuan
            val = float(input("Nilai: "))  # input nilai suhu, diubah ke float
            
            f_char, t_char = u[f_idx][0], u[t_idx][0]  # ambil huruf pertama, misal 'Celsius' → 'C'
            res, c_val = convert_temp(val, f_char, t_char)  # konversi suhu
            status = classified_temp(c_val)  # klasifikasi berdasarkan nilai Celsius-nya
            
            print(f"\nHasil: {res:.1f}°{t_char}")  # tampilin hasil konversi
            print(f"Klasifikasi: {status}")  # tampilin klasifikasi suhu
            
            add_history("Suhu", f"{val}{f_char} to {t_char}", f"{res:.1f}{t_char}")  # simpan ke riwayat
        except Exception as e: print(f"Error: {e}")  # kalau ada error, tampilin pesannya

    elif choice == '2': display_table()  # kalau pilih 2, tampilin tabel
    elif choice == '3':  # kalau pilih 3, klasifikasi manual
        try:
            c = float(input("Masukkan suhu Celsius: "))  # minta input suhu
            print(f"Klasifikasi: {classified_temp(c)}")  # tampilin hasil klasifikasi
        except: print("Gagal!")  # kalau input bukan angka

if __name__ == "__main__":  # kalau file ini dirun langsung
    menu_suhu()  # panggil menu suhu