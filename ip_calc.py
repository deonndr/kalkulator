from utils.history import add_history  # import fungsi buat nyimpen riwayat

def ip_to_bin(ip):  # fungsi konversi IP ke biner
    octets = ip.split('.')  # pecah IP jadi 4 bagian, misal ['192','168','1','10']
    binary_octets = [bin(int(o))[2:].zfill(8) for o in octets]  # tiap bagian diubah ke biner 8 digit
    return '.'.join(binary_octets)  # gabung lagi pake titik

def prefix_to_mask(prefix):  # fungsi ubah prefix (/24) jadi subnet mask (255.255.255.0)
    mask_bin = ('1' * prefix) + ('0' * (32 - prefix))  # bikin 32 bit, depannya 1 sebanyak prefix sisanya 0
    octets = [str(int(mask_bin[i:i+8], 2)) for i in range(0, 32, 8)]  # potong jadi 4 bagian, konversi ke desimal
    return '.'.join(octets)  # gabung jadi format IP

def calculate_ip_info(ip, prefix):  # fungsi hitung info lengkap jaringan
    octets = [int(o) for o in ip.split('.')]  # pecah IP jadi list integer
    ip_int = (octets[0] << 24) + (octets[1] << 16) + (octets[2] << 8) + octets[3]  # gabung jadi 1 angka 32-bit
    
    mask_int = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF  # bikin subnet mask dalam bentuk integer
    
    net_int = ip_int & mask_int  # network address = IP di-AND sama mask
    net_ip = f"{(net_int >> 24) & 255}.{(net_int >> 16) & 255}.{(net_int >> 8) & 255}.{net_int & 255}"  # ubah balik ke format IP
    
    broad_int = net_int | (~mask_int & 0xFFFFFFFF)  # broadcast = network di-OR sama kebalikan mask
    broad_ip = f"{(broad_int >> 24) & 255}.{(broad_int >> 16) & 255}.{(broad_int >> 8) & 255}.{broad_int & 255}"  # ubah balik ke format IP
    
    num_hosts = (2 ** (32 - prefix)) - 2  # jumlah host = 2^(sisa bit) dikurangi 2 (network & broadcast)
    if num_hosts < 0: num_hosts = 0  # antisipasi kalau prefix 31 atau 32
    
    return {  # return semua hasil dalam bentuk dictionary
        "network": net_ip,  # alamat network
        "broadcast": broad_ip,  # alamat broadcast
        "hosts": num_hosts,  # jumlah host yang bisa dipakai
        "mask": prefix_to_mask(prefix)  # subnet mask
    }

def menu_ip():  # fungsi menu utama kalkulator IP
    print("\n=== KALKULATOR IP ADDRESS ===")  # judul menu
    try:  # pakai try buat antisipasi input salah
        ip = input("Masukkan IP Address (Contoh: 192.168.1.10): ")  # minta input IP
        prefix = int(input("Masukkan Prefix Length (Contoh: 24): "))  # minta input prefix, diubah ke int
        
        info = calculate_ip_info(ip, prefix)  # hitung semua info jaringan
        
        print(f"\nSubnet Mask: {info['mask']}")  # tampilin subnet mask
        print(f"Network Address: {info['network']}")  # tampilin network address
        print(f"Broadcast Address: {info['broadcast']}")  # tampilin broadcast address
        print(f"Jumlah Host: {info['hosts']}")  # tampilin jumlah host
        print(f"IP dalam Biner: {ip_to_bin(ip)}")  # tampilin IP versi biner
        
        add_history("Kalkulator IP", f"{ip}/{prefix}", info['network'])  # simpan ke riwayat
    except Exception as e:  # kalau ada error
        print(f"Error: {e}")  # tampilin pesan errornya

if __name__ == "__main__":  # kalau file ini dirun langsung
    menu_ip()  # panggil menu IP