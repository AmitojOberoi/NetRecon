import host_discovery

while True:
    print("\n========== NETRECON ==========")
    print("1. Host Discovery")
    print("2. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
         ip = input("Enter IP Address: ")
         host_discovery.host_discovery(ip)

    elif choice == "2":
        print("Goodbye!")
        break

    else:
     print("Invalid choice!")