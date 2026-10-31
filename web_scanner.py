import sys
import requests
import socket
import concurrent.futures
import time
import os
import subprocess

# Warna ANSI
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def tampilkan_banner():
    clear_screen()
    # PATH GAMBAR LU
    image_path = "/storage/emulated/0/avg/8b6e88236c0a91ebf72f59214cd1c230.jpg"
    
    try:
        # Nampilin gambar pake chafa
        subprocess.run(["chafa", "--size=35x15", "--align=center", image_path])
    except Exception:
        pass # Kalau chafa error, lanjut aja

    print(f"{CYAN}========================================={RESET}")
    print(f"{YELLOW}       [ WEB VULNERABILITY SCANNER ]{RESET}")
    print(f"{CYAN}========================================={RESET}\n")

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((ip, port)) == 0:
                return port
    except:
        pass
    return None

def run_scanner():
    tampilkan_banner()
    
    target = input(f"{WHITE}Masukkan domain target (contoh: google.com): {RESET}").strip()
    if not target:
        print(f"{RED}[!] Target tidak boleh kosong.{RESET}")
        return

    if not target.startswith('http'):
        target = 'http://' + target

    print(f"\n{GREEN}[*] Memindai {target}...{RESET}")
    time.sleep(1)

    # 1. Scan Headers
    try:
        resp = requests.get(target, timeout=5, headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects=True)
        print(f"\n{CYAN}[+] Informasi Header & Server:{RESET}")
        print(f"  - HTTP Status   : {resp.status_code}")
        print(f"  - Server        : {resp.headers.get('Server', 'Tidak diketahui')}")
        print(f"  - X-Powered-By  : {resp.headers.get('X-Powered-By', 'Tidak diketahui')}")
        print(f"  - Content-Type  : {resp.headers.get('Content-Type', 'Tidak diketahui')}")
        
        hsts = resp.headers.get('Strict-Transport-Security', None)
        if not hsts:
            print(f"  - HSTS          : {RED}Tidak ada (Rentan){RESET}")
        else:
            print(f"  - HSTS          : {GREEN}Aktif{RESET}")

        # 2. Dapetin IP
        domain = target.replace('http://', '').replace('https://', '').split('/')[0]
        ip = socket.gethostbyname(domain)
        print(f"  - IP Address    : {ip}")

        # 3. Scan Port Umum
        print(f"\n{CYAN}[+] Memindai Port Umum...{RESET}")
        common_ports = [21, 22, 80, 443, 3306, 8080]
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            for port in executor.map(lambda p: scan_port(ip, p), common_ports):
                if port:
                    print(f"  - Port {port:<4} : {GREEN}OPEN{RESET}")
                else:
                    print(f"  - Port {port:<4} : {RED}CLOSED{RESET}")

    except requests.exceptions.RequestException as e:
        print(f"{RED}[!] Gagal terhubung ke target: {e}{RESET}")
    except socket.gaierror:
        print(f"{RED}[!] Domain tidak ditemukan / tidak bisa di-resolve.{RESET}")

if __name__ == '__main__':
    try:
        run_scanner()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Program dihentikan.{RESET}")
