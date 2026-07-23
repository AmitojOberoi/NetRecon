import socket


def grab_banner(ip, port):
    """
    Grab a banner from a service.

    Currently supports:
    - HTTP (Port 80)

    Other services will return "-" for now.
    """

    # Only attempt banner grabbing for HTTP
    if port != 80:
        return "-"

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        sock.connect((ip, port))

        # Send a simple HTTP HEAD request
        request = (
            f"HEAD / HTTP/1.1\r\n"
            f"Host: {ip}\r\n"
            "Connection: close\r\n\r\n"
        )

        sock.send(request.encode())

        response = sock.recv(1024).decode(errors="ignore")

        sock.close()

        if response:
            # Return only the first line
            return response.split("\n")[0].strip()

        return "No Banner"

    except Exception:
        return "-"