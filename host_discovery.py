import subprocess


def host_discovery(ip):
    print(f"\n[*] Pinging {ip}...\n")

    result = subprocess.run(
        ["ping", "-n", "1", ip],   # Windows uses -n
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"[+] Host {ip} is UP")
    else:
        print(f"[-] Host {ip} is DOWN or unreachable")