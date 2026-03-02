import os  # buat ngecek OS
from aritmatika import menu_aritmatika  # import menu aritmatika
from suhu import menu_suhu  # import menu suhu
from bilangan import menu_bilangan  # import menu konversi bilangan
from ip_calc import menu_ip  # import menu IP (bonus)
from utils.history import get_history, format_history_text, clear_history  # fungsi-fungsi history
from utils.exporter import export_to_txt  # fungsi export ke file txt

def clear_screen():  # fungsi buat bersihin layar
    os.system('cls' if os.name == 'nt' else 'clear')  # cls = Windows, clear = Linux/Mac

def main_menu():  # fungsi menu utama
    while True:  # loop terus sampe user keluar
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
        
        choice = input("Pilih Menu: ")  # minta input dari user
        
        if choice == '1':  # kalau pilih 1
            menu_aritmatika()  # jalanin menu aritmatika
        elif choice == '2':  # kalau pilih 2
            menu_suhu()  # jalanin menu suhu
        elif choice == '3':  # kalau pilih 3
            menu_bilangan()  # jalanin menu konversi bilangan
        elif choice == '4':  # kalau pilih 4
            print("\n" + format_history_text())  # tampilin riwayat
            input("\nTekan Enter untuk kembali...")  # tunggu enter
        elif choice == '5':  # kalau pilih 5
            history_text = format_history_text()  # ambil riwayat
            if "Belum ada riwayat" in history_text:  # cek apakah kosong
                print("\nTidak ada data untuk diekspor.")  # kasih tau kalau kosong
            else:  # kalau ada datanya
                success, msg = export_to_txt(history_text)  # coba export, return 2 nilai
                if success:  # kalau berhasil
                    print(f"\nBerhasil diekspor ke: {msg}")  # tampilin nama file
                else:  # kalau gagal
                    print(f"\nGagal mengekspor: {msg}")  # tampilin pesan error
            input("\nTekan Enter untuk kembali...")  # tunggu enter
        elif choice == '6':  # kalau pilih 6
            menu_ip()  # jalanin menu IP
            input("\nTekan Enter untuk kembali...")  # tunggu enter
        elif choice == '0':  # kalau pilih 0
            print("\nTerima kasih telah menggunakan Sistem Kalkulator Multi-Fungsi!")  # pesan keluar
            break  # stop loop
        else:  # kalau input ga valid
            print("\nPilihan tidak valid. Silakan coba lagi.")  # kasih tau user
            input("\nTekan Enter untuk mencoba lagi...")  # tunggu enter

if __name__ == "__main__":  # kalau file ini dirun langsung (bukan di-import)
    main_menu()  # panggil fungsi utama