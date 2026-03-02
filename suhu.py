# mengaktifkan fitur pencatatan riwayat
from utils.history import add_history

def classified_temp(celsius):
    """Fungsi klasifikasi suhu sesuai kriteria Soal 2B"""
    if celsius <= 0: return "Beku"
    elif 1 <= celsius <= 15: return "Dingin"
    elif 16 <= celsius <= 25: return "Normal"
    elif 26 <= celsius <= 35: return "Panas"
    else: return "Sangat Panas"

# Rumus-rumus konversi suhu berdasarkan tabel Soal 2C
def c_to_f(c): return (c * 9/5) + 32
def c_to_k(c): return c + 273.15
def c_to_r(c): return c * 4/5
def f_to_c(f): return (f - 32) * 5/9
def k_to_c(k): return k - 273.15
def r_to_c(r): return r * 5/4

def convert_temp(val, from_u, to_u):
    """Mengonversi nilai suhu antar satuan dengan Celsius sebagai jembatan"""
    # Langkah 1: Ubah input ke Celsius
    if from_u == 'C': c = val
    elif from_u == 'F': c = f_to_c(val)
    elif from_u == 'K': c = k_to_c(val)
    elif from_u == 'R': c = r_to_c(val)
    
    # Langkah 2: Dari Celsius ke unit tujuan
    if to_u == 'C': res = c
    elif to_u == 'F': res = c_to_f(c)
    elif to_u == 'K': res = c_to_k(c)
    elif to_u == 'R': res = c_to_r(c)
    
    return res, c # mengembalikan hasil konversi dan nilai celcius untuk klasifikasi

def display_table():
    """Menampilkan tabel konversi 0-100 step 10 sesuai Soal 2B"""
    print("\n=== TABEL KONVERSI SUHU (0°C - 100°C) ===")
    header = f"{'Celsius':<8} | {'Fahr':<8} | {'Kelv':<8} | {'Reau':<8} | {'Status'}"
    print(header)
    print("-" * len(header))
    for c in range(0, 101, 10):
        # hitung tiap satuan
        f, k, r = c_to_f(c), c_to_k(c), c_to_r(c)
        status = classified_temp(c) # ambil klasifikasi
        print(f"{c:<8}°C | {f:<8.1f}°F | {k:<8.1f}K | {r:<8.1f}°R | {status}")

def menu_suhu():
    """Menu utama kalkulator suhu sesuai Soal 2D"""
    print("\n=== KALKULATOR SUHU ===")
    print("1. Konversi Satuan")
    print("2. Tabel Konversi")
    print("3. Klasifikasi Suhu")
    
    choice = input("Pilih: ")
    
    if choice == '1':
        # menu konversi dua arah sesuai Soal 2B
        u = {'1': 'Celsius', '2': 'Fahrenheit', '3': 'Kelvin', '4': 'Reaumur'}
        print("Pilih: 1.C, 2.F, 3.K, 4.R")
        try:
            f_idx = input("Dari: ")
            t_idx = input("Ke: ")
            val = float(input("Nilai: "))
            
            # ambil inisial (C, F, K, R)
            f_char, t_char = u[f_idx][0], u[t_idx][0]
            res, c_val = convert_temp(val, f_char, t_char)
            status = classified_temp(c_val) # klasifikasi otomatis
            
            print(f"\nHasil: {res:.1f}°{t_char}")
            print(f"Klasifikasi: {status}")
            
            add_history("Suhu", f"{val}{f_char} to {t_char}", f"{res:.1f}{t_char}")
        except Exception as e: print(f"Error: {e}")

    elif choice == '2': display_table()
    elif choice == '3':
        try:
            c = float(input("Masukkan suhu Celsius: "))
            print(f"Klasifikasi: {classified_temp(c)}")
        except: print("Gagal!")

if __name__ == "__main__":
    menu_suhu()
