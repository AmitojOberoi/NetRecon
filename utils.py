import socket


def resolve_hostname(target):

    try:
        ip = socket.gethostbyname(target)
        hostname = socket.gethostbyaddr(ip)[0]

        return ip, hostname

    except socket.gaierror:
        return None, None

    except:
        return None, "Unknown"