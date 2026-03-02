from utils.history import add_history

# algoritma manual buatan sendiri tanpa bin/hex/oct
def desimal_ke_apapun(angka, basis):
    if angka == 0: return "0", ["0 / {} = 0 sisa 0".format(basis)]
    
    simbol = "0123456789ABCDEF"
    list_langkah = []
    hasil_teks = ""
    n = angka
    
    # loop pembagian berulang sesuai instruksi soal
    while n > 0:
        sisa = n % basis
        list_langkah.append(f"{n} / {basis} = {n // basis} sisa {simbol[sisa]} ↑")
        hasil_teks = simbol[sisa] + hasil_teks
        n //= basis
        
    return hasil_teks, list_langkah

def apapun_ke_desimal(teks_angka, basis):
    simbol = "0123456789ABCDEF"
    teks_angka = teks_angka.upper()
    desimal = 0
    catatan_perkalian = []
    pangkat = len(teks_angka) - 1
    
    # hitung satu-satu angkanya dari depan
    for s in teks_angka:
        nilai = simbol.index(s)
        hitung = nilai * (basis ** pangkat)
        desimal += hitung
        catatan_perkalian.append(f"{nilai}×{basis}^{pangkat}")
        pangkat -= 1
        
    verif = f"Verifikasi: {' + '.join(catatan_perkalian)} = {desimal} ✓"
    return desimal, verif

def hitung_kolom(v1, v2, b, op):
    # ngerjain aritmatika non-desimal pake gaya kolom
    d1, _ = apapun_ke_desimal(v1, b)
    d2, _ = apapun_ke_desimal(v2, b)
    
    if op == '+': res = d1 + d2
    elif op == '-': res = d1 - d2
    else: return "???"
    
    final, _ = desimal_ke_apapun(abs(res), b)
    if res < 0: final = "-" + final
    
    # tampilan output gaya perhitungan manual di kolom
    lebar = max(len(v1), len(v2), len(final)) + 2
    print(f"\nProses Hitung (Basis {b}):")
    print(f"{v1:>{lebar}}")
    print(f"{v2:>{lebar}} {op}")
    print("-" * (lebar + 2))
    print(f"{final:>{lebar}}")
    return final

def menu_bilangan():
    print("\n=== KALKULATOR BILANGAN ===")
    print("1. Konversi Basis\n2. Operasi Aritmatika Biner/Oktal/Heks")
    
    pilih = input("User pilih menu: ")
    
    if pilih == '1':
        # mapping manual biar ga kaku
        peta_basis = {'1': 10, '2': 2, '3': 8, '4': 16}
        try:
            b_awal = peta_basis[input("Dari (1.Des, 2.Bin, 3.Okt, 4.Hex): ")]
            b_tujuan = peta_basis[input("Ke (1.Des, 2.Bin, 3.Okt, 4.Hex): ")]
            nilai = input("Nilainya: ")
            
            # konversi dlu ke desimal (jembatan)
            d_val, verif_manual = apapun_ke_desimal(nilai, b_awal)
            # trus ke tujuan
            hasil_akhir, langkah_bagi = desimal_ke_apapun(d_val, b_tujuan)
            
            print("\n--- Langkah Konversi ---")
            if b_awal != 10: print(f"[Ke Desimal] {verif_manual}")
            for l in langkah_bagi: print(l)
            
            print(f"\nHasil: {hasil_akhir}")
            print(verif_manual) # buat bukti ke guru
            
            add_history("Bilangan", f"{nilai}(b{b_awal}) -> b{b_tujuan}", hasil_akhir)
        except: print("Error input!")

    elif pilih == '2':
        # aritmatika non-desimal (Soal 3 Bagian 2)
        m = {'1': 2, '2': 8, '3': 16}
        b = m.get(input("Pilih basis (1.Bin, 2.Okt, 3.Hex): "))
        if not b: return
        n1 = input("Angka 1: ")
        op = input("Operasi (+/-): ")
        n2 = input("Angka 2: ")
        res = hitung_kolom(n1, n2, b, op)
        add_history(f"Arith-Base{b}", f"{n1}{op}{n2}", res)

if __name__ == "__main__":
    menu_bilangan()
