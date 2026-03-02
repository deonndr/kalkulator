# =============
# MODUL HISTORY
# =============

_history = []

def add_history(activity, expression, result):
    """Menambahkan riwayat perhitungan (Max 10)"""
    global _history
    entry = {
        "activity": activity,
        "expression": expression,
        "result": result
    }
    _history.append(entry)
    # Jaga agar tetap 10 terakhir
    if len(_history) > 10:
        _history.pop(0)

def get_history():
    """Mengambil semua riwayat"""
    return _history

def clear_history():
    """Menghapus riwayat"""
    global _history
    _history = []

def format_history_text():
    """Mengembalikan string terformat untuk riwayat"""
    if not _history:
        return "Belum ada riwayat perhitungan."
    
    output = "=== RIWAYAT PERHITUNGAN (10 TERAKHIR) ===\n"
    for i, item in enumerate(_history, 1):
        output += f"{i}. [{item['activity']}] {item['expression']} = {item['result']}\n"
    return output
