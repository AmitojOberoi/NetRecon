import socket
from concurrent.futures import ThreadPoolExecutor
import banner
import report


def scan_single_port(ip, port, open_ports):
    """
    Scan a single TCP port.
    If the port is open, identify the service and attempt banner grabbing.
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        result = sock.connect_ex((ip, port))

        if result == 0:

            # Identify service name
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "Unknown"

            # Grab banner
            banner_text = banner.grab_banner(ip, port)

            # Store result for JSON report
            open_ports.append({
                "port": port,
                "service": service,
                "banner": banner_text
            })

            # Display result
            print(
                f"{port:<8}"
                f"{service:<12}"
                f"{'OPEN':<10}"
                f"{banner_text}"
            )

    except Exception as e:
        print(f"Error scanning port {port}: {e}")

    finally:
        sock.close()


def port_scan(target, ip, start_port, end_port):
    """
    Scan a range of TCP ports using multithreading.
    """

    open_ports = []

    print("\n========== PORT SCANNER ==========")
    print(f"Target : {target}")
    print(f"Resolved IP : {ip}")
    print(f"Scanning Ports {start_port} - {end_port}\n")

    print(f"{'PORT':<8}{'SERVICE':<12}{'STATUS':<10}BANNER")
    print("-" * 90)

    with ThreadPoolExecutor(max_workers=100) as executor:

        futures = []

        for port in range(start_port, end_port + 1):

            futures.append(
                executor.submit(
                    scan_single_port,
                    ip,
                    port,
                    open_ports
                )
            )

        for future in futures:
            future.result()

    print("-" * 90)

    # Save JSON Report
    report.save_report(target, ip, open_ports)

    print("✅ Scan Complete!")
    print("-" * 90)