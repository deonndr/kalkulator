# ======================================================
# SISTEM KALKULATOR MULTI-FUNGSI
# Proyek Praktikum Pemrograman
# ======================================================

import os
from aritmatika import menu_aritmatika
from suhu import menu_suhu
from bilangan import menu_bilangan
from ip_calc import menu_ip
from utils.history import get_history, format_history_text, clear_history
from utils.exporter import export_to_txt

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        # Tampilan Menu Utama (Sesuai Soal 4)
        print("╔══════════════════════════════════════╗")
        print("║     SISTEM KALKULATOR MULTI-FUNGSI   ║")
        print("╠══════════════════════════════════════╣")
        print("║  1. Kalkulator Aritmatika            ║")
        print("║  2. Kalkulator Suhu                  ║")
        print("║  3. Kalkulator Konversi Bilangan     ║")
        print("║  4. Riwayat Perhitungan              ║")
        print("║  5. Export Hasil ke File             ║")
        print("║  6. Kalkulator IP (Bonus)            ║")
        print("║  0. Keluar                           ║")
        print("╚══════════════════════════════════════╝")
        
        choice = input("Pilih Menu: ")
        
        if choice == '1':
            menu_aritmatika()
        elif choice == '2':
            menu_suhu()
        elif choice == '3':
            menu_bilangan()
        elif choice == '4':
            print("\n" + format_history_text())
            input("\nTekan Enter untuk kembali...")
        elif choice == '5':
            history_text = format_history_text()
            if "Belum ada riwayat" in history_text:
                print("\nTidak ada data untuk diekspor.")
            else:
                success, msg = export_to_txt(history_text)
                if success:
                    print(f"\nBerhasil diekspor ke: {msg}")
                else:
                    print(f"\nGagal mengekspor: {msg}")
            input("\nTekan Enter untuk kembali...")
        elif choice == '6':
            menu_ip()
            input("\nTekan Enter untuk kembali...")
        elif choice == '0':
            print("\nTerima kasih telah menggunakan Sistem Kalkulator Multi-Fungsi!")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            input("\nTekan Enter untuk mencoba lagi...")
            
        # clear_screen() # Opsional agar tampilan tetap rapi

if __name__ == "__main__":
    main_menu()
