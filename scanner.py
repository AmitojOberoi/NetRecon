import socket
from concurrent.futures import ThreadPoolExecutor
import banner


def scan_single_port(ip, port):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)

        result = sock.connect_ex((ip, port))

        if result == 0:

            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "Unknown"

            banner_text = banner.grab_banner(ip, port)

            print(
                f"{port:<8}"
                f"{service:<12}"
                f"{'OPEN':<10}"
                f"{banner_text}"
            )

        sock.close()

    except Exception:
        pass


def port_scan(ip, start_port, end_port):

    print("\n========== PORT SCANNER ==========")
    print(f"Target : {ip}")
    print(f"Scanning Ports {start_port} - {end_port}\n")

    print(f"{'PORT':<8}{'SERVICE':<12}{'STATUS':<10}BANNER")
    print("-" * 90)

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_single_port, ip, port)

    print("\n===================================")
    print("✅ Scan Complete!")
    print("===================================\n")