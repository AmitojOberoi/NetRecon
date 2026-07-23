import json
import os
from datetime import datetime


def save_report(target, ip, open_ports):

    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"reports/scan_{timestamp}.json"

    report = {
        "target": target,
        "resolved_ip": ip,
        "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_open_ports": len(open_ports),
        "open_ports": open_ports
    }

    with open(filename, "w") as file:
        json.dump(report, file, indent=4)

    print("\n📄 JSON Report Saved Successfully!")
    print(f"Location : {filename}")