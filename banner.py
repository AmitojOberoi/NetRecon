import socket


def grab_banner(ip, port):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        sock.connect((ip, port))

        # For HTTP, request headers first
        if port == 80:
            sock.send(b"HEAD / HTTP/1.1\r\nHost: localhost\r\n\r\n")

        elif port == 443:
            sock.close()
            return "HTTPS (Encrypted)"

        banner = sock.recv(1024).decode(errors="ignore").strip()

        sock.close()

        if banner:
            return banner.replace("\r", "").replace("\n", " ")

        return "No Banner"

    except Exception:
        return "Unavailable"