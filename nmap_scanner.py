import subprocess
import time
import os
from datetime import datetime


def save_nmap_report(scan_name, output):

    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"reports/nmap_{scan_name}_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(output)

    print(f"\n📄 Nmap Report Saved Successfully!")
    print(f"Location : {filename}")


def run_scan(command, scan_name):

    print("\n" + "=" * 70)
    print(scan_name.upper())
    print("=" * 70)

    start = time.time()

    try:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        print(result.stdout)

        save_nmap_report(
            scan_name.replace(" ", "_").lower(),
            result.stdout
        )

        end = time.time()

        print("-" * 70)
        print("✅ Scan Completed")
        print(f"Time Taken : {end-start:.2f} seconds")
        print("-" * 70)

    except FileNotFoundError:
        print("❌ Nmap not found. Install Nmap or add it to PATH.")

    except Exception as e:
        print(f"Error : {e}")


def quick_scan(target):

    command = [
        "nmap",
        "-T4",
        "-F",
        target
    ]

    run_scan(command, "Quick Scan")


def service_scan(target):

    command = [
        "nmap",
        "-sV",
        target
    ]

    run_scan(command, "Service Version Detection")


def os_scan(target):

    command = [
        "nmap",
        "-O",
        target
    ]

    run_scan(command, "Operating System Detection")


def aggressive_scan(target):

    command = [
        "nmap",
        "-A",
        target
    ]

    run_scan(command, "Aggressive Scan")


def ping_scan(target):

    command = [
        "nmap",
        "-sn",
        target
    ]

    run_scan(command, "Ping Scan")