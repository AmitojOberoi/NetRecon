import host_discovery
import scanner
import utils

while True:
    print("\n========== NETRECON ==========")
    print("1. Host Discovery")
    print("2. Port Scanner")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        ip = input("Enter IP Address: ")
        host_discovery.host_discovery(ip)

    elif choice == "2":
        target = input("Enter Target (IP or Hostname): ")

        ip, hostname = utils.resolve_hostname(target)

        if ip is None:
            print("❌ Invalid Host.")
            continue

        print(f"\nResolved IP : {ip}")
        print(f"Hostname    : {hostname}")

        try:
            start_port = int(input("Enter Start Port: "))
            end_port = int(input("Enter End Port: "))

            scanner.port_scan(target, ip, start_port, end_port)

        except ValueError:
            print("❌ Please enter valid port numbers.")

    elif choice == "3":
        print("\nGoodbye!")
        break

    else:
        print("❌ Invalid choice!")