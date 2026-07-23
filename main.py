import host_discovery
import scanner
import utils
import nmap_scanner


while True:

    print("\n========== NETRECON ==========")
    print("1. Host Discovery")
    print("2. Custom Port Scanner")
    print("3. Nmap Scanner")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    # ----------------------------
    # HOST DISCOVERY
    # ----------------------------
    if choice == "1":

        ip = input("Enter IP Address: ")

        host_discovery.host_discovery(ip)

    # ----------------------------
    # CUSTOM PORT SCANNER
    # ----------------------------
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

            scanner.port_scan(
                target,
                ip,
                start_port,
                end_port
            )

        except ValueError:

            print("❌ Please enter valid port numbers.")

    # ----------------------------
    # NMAP SCANNER
    # ----------------------------
    elif choice == "3":

        target = input("\nEnter Target (IP or Hostname): ")

        while True:

            print("\n========== NMAP SCANNER ==========")
            print("1. Quick Scan")
            print("2. Service Version Detection")
            print("3. Operating System Detection")
            print("4. Aggressive Scan")
            print("5. Ping Scan")
            print("6. Back")

            nmap_choice = input("\nEnter your choice: ")

            if nmap_choice == "1":

                nmap_scanner.quick_scan(target)

            elif nmap_choice == "2":

                nmap_scanner.service_scan(target)

            elif nmap_choice == "3":

                nmap_scanner.os_scan(target)

            elif nmap_choice == "4":

                nmap_scanner.aggressive_scan(target)

            elif nmap_choice == "5":

                nmap_scanner.ping_scan(target)

            elif nmap_choice == "6":

                break

            else:

                print("❌ Invalid Choice!")

    # ----------------------------
    # EXIT
    # ----------------------------
    elif choice == "4":

        print("\nThank you for using NetRecon!")
        print("Goodbye 👋")

        break

    # ----------------------------
    # INVALID OPTION
    # ----------------------------
    else:

        print("❌ Invalid Choice!")