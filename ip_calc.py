# =============
# MODUL KALKULATOR IP ADDRESS (BONUS)
# =============
from utils.history import add_history

def ip_to_bin(ip):
    """Konversi IP Desimal ke Biner"""
    octets = ip.split('.')
    binary_octets = [bin(int(o))[2:].zfill(8) for o in octets]
    return '.'.join(binary_octets)

def prefix_to_mask(prefix):
    """Hitung Subnet Mask dari Prefix Length (/24 -> 255.255.255.0)"""
    mask_bin = ('1' * prefix) + ('0' * (32 - prefix))
    octets = [str(int(mask_bin[i:i+8], 2)) for i in range(0, 32, 8)]
    return '.'.join(octets)

def calculate_ip_info(ip, prefix):
    """Hitung Network, Broadcast, dan Host"""
    # Konversi IP ke 32-bit integer
    octets = [int(o) for o in ip.split('.')]
    ip_int = (octets[0] << 24) + (octets[1] << 16) + (octets[2] << 8) + octets[3]
    
    # Mask
    mask_int = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF
    
    # Network Address
    net_int = ip_int & mask_int
    net_ip = f"{(net_int >> 24) & 255}.{(net_int >> 16) & 255}.{(net_int >> 8) & 255}.{net_int & 255}"
    
    # Broadcast Address
    broad_int = net_int | (~mask_int & 0xFFFFFFFF)
    broad_ip = f"{(broad_int >> 24) & 255}.{(broad_int >> 16) & 255}.{(broad_int >> 8) & 255}.{broad_int & 255}"
    
    # Hosts
    num_hosts = (2 ** (32 - prefix)) - 2
    if num_hosts < 0: num_hosts = 0
    
    return {
        "network": net_ip,
        "broadcast": broad_ip,
        "hosts": num_hosts,
        "mask": prefix_to_mask(prefix)
    }

def menu_ip():
    print("\n=== KALKULATOR IP ADDRESS ===")
    try:
        ip = input("Masukkan IP Address (Contoh: 192.168.1.10): ")
        prefix = int(input("Masukkan Prefix Length (Contoh: 24): "))
        
        info = calculate_ip_info(ip, prefix)
        
        print(f"\nSubnet Mask: {info['mask']}")
        print(f"Network Address: {info['network']}")
        print(f"Broadcast Address: {info['broadcast']}")
        print(f"Jumlah Host: {info['hosts']}")
        print(f"IP dalam Biner: {ip_to_bin(ip)}")
        
        add_history("Kalkulator IP", f"{ip}/{prefix}", info['network'])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    menu_ip()
