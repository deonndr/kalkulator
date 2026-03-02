# =============
# MODUL EXPORTER
# =============
import datetime

def export_to_txt(content, filename="hasil_kalkulator.txt"):
    """Mengekspor konten ke file .txt dengan timestamp"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("=== EXPORT HASIL KALKULATOR MULTI-FUNGSI ===\n")
            f.write(f"Tanggal: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 45 + "\n\n")
            f.write(content)
        return True, filename
    except Exception as e:
        return False, str(e)
