from utils.history import add_history  # import fungsi buat nyimpen riwayat

def desimal_ke_apapun(angka, basis):  # fungsi konversi desimal ke basis apapun
    if angka == 0: return "0", ["0 / {} = 0 sisa 0".format(basis)]  # edge case kalau inputnya 0
    
    simbol = "0123456789ABCDEF"  # karakter yang dipake, A-F buat heksadesimal
    list_langkah = []  # buat nyimpen tiap langkah pembagian
    hasil_teks = ""  # hasil akhir dalam bentuk string
    n = angka  # simpan angka ke variabel sementara
    
    while n > 0:  # loop sampe angkanya habis dibagi
        sisa = n % basis  # ambil sisa bagi
        list_langkah.append(f"{n} / {basis} = {n // basis} sisa {simbol[sisa]} ↑")  # catat langkahnya
        hasil_teks = simbol[sisa] + hasil_teks  # sisa ditaruh di depan (dibaca dari bawah ke atas)
        n //= basis  # angka dibagi basis, buang sisanya
        
    return hasil_teks, list_langkah  # return hasil + list langkah-langkahnya

def apapun_ke_desimal(teks_angka, basis):  # fungsi konversi basis apapun ke desimal
    simbol = "0123456789ABCDEF"  # karakter yang dikenali
    teks_angka = teks_angka.upper()  # pastiin hurufnya kapital, biar 'a' sama 'A' dianggap sama
    desimal = 0  # akumulator hasil
    catatan_perkalian = []  # buat nyimpen tiap langkah perkalian
    pangkat = len(teks_angka) - 1  # pangkat tertinggi = panjang angka - 1
    
    for s in teks_angka:  # loop tiap karakter dari kiri ke kanan
        nilai = simbol.index(s)  # cari nilai desimalnya, misal 'A' = 10
        hitung = nilai * (basis ** pangkat)  # kalikan sama basis pangkat sekian
        desimal += hitung  # tambahkan ke hasil
        catatan_perkalian.append(f"{nilai}×{basis}^{pangkat}")  # catat langkahnya
        pangkat -= 1  # turunin pangkat
        
    verif = f"Verifikasi: {' + '.join(catatan_perkalian)} = {desimal} ✓"  # rangkum semua langkah
    return desimal, verif  # return hasil desimal + teks verifikasi

def hitung_kolom(v1, v2, b, op):  # fungsi operasi aritmatika antar bilangan non-desimal
    d1, _ = apapun_ke_desimal(v1, b)  # konversi angka 1 ke desimal dulu
    d2, _ = apapun_ke_desimal(v2, b)  # konversi angka 2 ke desimal dulu
    
    if op == '+': res = d1 + d2  # kalau operasi tambah
    elif op == '-': res = d1 - d2  # kalau operasi kurang
    else: return "???"  # kalau operasi ga dikenal
    
    final, _ = desimal_ke_apapun(abs(res), b)  # konversi hasil balik ke basis asal
    if res < 0: final = "-" + final  # kalau hasilnya negatif, tambahin tanda minus
    
    lebar = max(len(v1), len(v2), len(final)) + 2  # hitung lebar kolom buat alignment
    print(f"\nProses Hitung (Basis {b}):")  # judul perhitungan
    print(f"{v1:>{lebar}}")  # tampilin angka 1 rata kanan
    print(f"{v2:>{lebar}} {op}")  # tampilin angka 2 + simbolnya
    print("-" * (lebar + 2))  # garis pemisah
    print(f"{final:>{lebar}}")  # tampilin hasil rata kanan
    return final  # return hasilnya

def menu_bilangan():  # fungsi menu utama kalkulator bilangan
    print("\n=== KALKULATOR BILANGAN ===")  # judul menu
    print("1. Konversi Basis\n2. Operasi Aritmatika Biner/Oktal/Heks")  # opsi menu
    
    pilih = input("User pilih menu: ")  # minta input user
    
    if pilih == '1':  # kalau pilih konversi basis
        peta_basis = {'1': 10, '2': 2, '3': 8, '4': 16}  # mapping angka ke nilai basis
        try:
            b_awal = peta_basis[input("Dari (1.Des, 2.Bin, 3.Okt, 4.Hex): ")]  # basis asal
            b_tujuan = peta_basis[input("Ke (1.Des, 2.Bin, 3.Okt, 4.Hex): ")]  # basis tujuan
            nilai = input("Nilainya: ")  # angka yang mau dikonversi
            
            d_val, verif_manual = apapun_ke_desimal(nilai, b_awal)  # konversi ke desimal dulu (jembatan)
            hasil_akhir, langkah_bagi = desimal_ke_apapun(d_val, b_tujuan)  # konversi ke basis tujuan
            
            print("\n--- Langkah Konversi ---")  # judul langkah-langkah
            if b_awal != 10: print(f"[Ke Desimal] {verif_manual}")  # tampilin langkah ke desimal kalau perlu
            for l in langkah_bagi: print(l)  # tampilin tiap langkah pembagian
            
            print(f"\nHasil: {hasil_akhir}")  # tampilin hasil akhir
            print(verif_manual)  # tampilin verifikasi buat bukti
            
            add_history("Bilangan", f"{nilai}(b{b_awal}) -> b{b_tujuan}", hasil_akhir)  # simpan ke riwayat
        except: print("Error input!")  # kalau input salah atau ga valid

    elif pilih == '2':  # kalau pilih operasi aritmatika
        m = {'1': 2, '2': 8, '3': 16}  # mapping ke nilai basis
        b = m.get(input("Pilih basis (1.Bin, 2.Okt, 3.Hex): "))  # ambil basis yang dipilih
        if not b: return  # kalau pilihan ga valid, langsung keluar
        n1 = input("Angka 1: ")  # input angka pertama
        op = input("Operasi (+/-): ")  # input operasi
        n2 = input("Angka 2: ")  # input angka kedua
        res = hitung_kolom(n1, n2, b, op)  # hitung dan tampilin hasilnya
        add_history(f"Arith-Base{b}", f"{n1}{op}{n2}", res)  # simpan ke riwayat

if __name__ == "__main__":  # kalau file ini dirun langsung
    menu_bilangan()  # panggil menu bilangan