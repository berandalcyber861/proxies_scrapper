import requests
from bs4 import BeautifulSoup
import socket
import socks

# Daftar URL sumber proxy
proxy_sources = [
    'https://www.free-proxy-list.net/',
    'https://www.us-proxy.org/',
    'https://www.proxy-list.download/api/v1/get?type=https',
    'https://www.sslproxies.org/',
    'https://www.proxy-list.download/api/v1/get?type=socks4',
    'https://www.proxy-list.download/api/v1/get?type=socks5',
    'https://www.proxyscan.io/',
    'https://www.geonames.org/faq/how-to-find-a-proxy-server.html',
    'https://www.freeproxy.world/',
    'https://www.proxynova.com/proxy-server-list/'
]


# Input untuk jenis proxy
proxy_type = input("Masukkan jenis proxy (http/socks4/socks5, default http): ").lower() or 'http'

# Fungsi untuk memfilter proxy sesuai jenis
def filter_proxies(proxies, proxy_type):
    filtered_proxies = set()
    for proxy in proxies:
        if proxy_type in proxy:
            filtered_proxies.add(proxy)
    return filtered_proxies

# Fungsi utama
def main():
    quantity = input("Masukkan jumlah proxy yang ingin diambil (default 100, max 2000): ")
    quantity = int(quantity) if quantity.isdigit() else 100
    quantity = min(quantity, 2000)  # Batasi maksimum 2000
    
    proxies = get_proxies(quantity)
    if proxy_type != 'http':
        proxies = filter_proxies(proxies, proxy_type)
    
    live_proxies = []
    unknown_proxies = []

    for proxy in proxies:
        if check_proxy(proxy):
            display_result(proxy, 'LIVE')
            live_proxies.append(proxy)
        else:
            display_result(proxy, 'UNKNOWN')
            unknown_proxies.append(proxy)

    # Menyimpan hasil ke file
    with open('live_proxies.txt', 'w') as live_file:
        for proxy in live_proxies:
            live_file.write(f"{proxy}\n")

    with open('unknown_proxies.txt', 'w') as unknown_file:
        for proxy in unknown_proxies:
            unknown_file.write(f"{proxy}\n")

if __name__ == "__main__":
    main()
