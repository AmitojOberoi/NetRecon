import socket


def port_scan(ip, start_port, end_port):

    print("\n========== PORT SCANNER ==========")
    print(f"Target : {ip}")
    print(f"Scanning Ports {start_port} - {end_port}\n")
    print("\nPORT      SERVICE        STATUS")
    print("-" * 35)

    for port in range(start_port, end_port + 1):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(0.5)

        result = sock.connect_ex((ip, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "Unknown"
            print(f"{port:<10}{service:<15}OPEN")

        sock.close()