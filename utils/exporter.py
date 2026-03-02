import datetime  # buat ngambil waktu sekarang

def export_to_txt(content, filename="hasil_kalkulator.txt"):  # fungsi export ke file txt, nama file bisa diganti
    try:
        with open(filename, "w", encoding="utf-8") as f:  # buka/buat file, "w" = tulis ulang kalau udah ada
            f.write("=== EXPORT HASIL KALKULATOR MULTI-FUNGSI ===\n")  # tulis header
            f.write(f"Tanggal: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")  # tulis timestamp sekarang
            f.write("=" * 45 + "\n\n")  # tulis garis pemisah
            f.write(content)  # tulis isi riwayatnya
        return True, filename  # kalau berhasil, return True + nama filenya
    except Exception as e:
        return False, str(e)  # kalau gagal, return False + pesan errornya