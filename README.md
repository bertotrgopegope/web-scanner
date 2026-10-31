![Web Scanner Banner](8b6e88236c0a91ebf72f59214cd1c230.jpg)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Termux-green?style=for-the-badge&logo=android" alt="Termux">
  <img src="https://img.shields.io/badge/Security-Testing-red?style=for-the-badge&logo=hackthebox" alt="Security">
</p>
  # Web Scanner (Termux)

Alat pemindaian kerentanan web sederhana untuk memeriksa informasi server, HTTP Headers, dan port yang terbuka. Dioptimalkan untuk Termux (Android).

## Fitur
- Cek HTTP Status dan Server Header.
- Deteksi HSTS (Keamanan Transport).
- Resolusi IP Address dari Domain.
- Pemindaian Port Umum (21, 22, 80, 443, 3306, 8080).

## Instalasi (Termux)

Buka Termux, lalu jalankan perintah berikut:

```bash
pkg update && pkg upgrade -y
pkg install python git chafa -y
pip install requests
```

Cara Pakai

1. Clone Repository
   ```bash
   git clone https://github.com/bertotrgopegope/web-scanner.git
   cd web-scanner
   ```
2. Jalankan Scanner
   ```bash
   python web_scanner.py
   ```
3. **Masukkan Target**
   Ketik nama domain (contoh: `google.com`) saat diminta, lalu tekan Enter.
