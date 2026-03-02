# modul buat nyimpen riwayat perhitungan

_history = []  # list global tempat nyimpen semua riwayat

def add_history(activity, expression, result):  # fungsi tambah riwayat baru
    global _history  # akses variabel _history yang ada di luar fungsi
    entry = {  # bikin satu data riwayat dalam bentuk dictionary
        "activity": activity,  # jenis kalkulatornya, misal "Suhu" atau "Dasar"
        "expression": expression,  # ekspresi yang dihitung, misal "100C to F"
        "result": result  # hasilnya
    }
    _history.append(entry)  # tambahin ke list
    if len(_history) > 10:  # kalau udah lebih dari 10 data
        _history.pop(0)  # hapus yang paling lama (paling depan)

def get_history():  # fungsi buat ngambil semua riwayat
    return _history  # langsung return listnya

def clear_history():  # fungsi buat hapus semua riwayat
    global _history  # akses variabel globalnya
    _history = []  # reset jadi list kosong

def format_history_text():  # fungsi buat nampilin riwayat dalam bentuk teks rapi
    if not _history:  # kalau list kosong
        return "Belum ada riwayat perhitungan."  # kasih pesan ini
    
    output = "=== RIWAYAT PERHITUNGAN (10 TERAKHIR) ===\n"  # header
    for i, item in enumerate(_history, 1):  # loop tiap item, nomor mulai dari 1
        output += f"{i}. [{item['activity']}] {item['expression']} = {item['result']}\n"  # format tiap baris
    return output  # return teks lengkapnya