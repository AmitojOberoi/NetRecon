# 🛡️ NetRecon

A modular Python-based Network Reconnaissance Tool built for learning socket programming, networking fundamentals, and cybersecurity concepts.

---

## Features

- Host Discovery
- DNS Hostname Resolution
- TCP Port Scanning
- Service Detection
- Multithreaded Scanning
- Banner Grabbing
- JSON Report Generation
- HTML Report Generation
- Nmap Integration
- Scan History
- Rich Terminal Interface

---

## Technologies

- Python
- Socket Programming
- TCP/IP
- DNS
- ThreadPoolExecutor
- JSON
- Nmap

---

## Project Structure

NetRecon/
├── main.py
├── scanner.py
├── host_discovery.py
├── banner.py
├── report.py
├── utils.py
├── reports/
├── README.md
└── requirements.txt

---

## Installation

```bash
git clone https://github.com/AmitojOberoi/NetRecon.git
cd NetRecon
pip install -r requirements.txt
python main.py
```

---

## Sample Output

```text
========== NETRECON ==========

Target : scanme.nmap.org
IP Address : 45.33.32.156

PORT     SERVICE     STATUS
22       ssh         OPEN
80       http        OPEN

Scan Complete
```

---

## Future Improvements

- Banner Grabbing
- HTML Reports
- Nmap Automation
- CIDR Scanning
- Export Reports
- Rich Terminal UI
- Logging
- Packet Capture Support

---

## Inspiration

This project was inspired by networking and reconnaissance concepts I was exposed to during my cybersecurity internship. I wanted to deepen my understanding by implementing the core techniques myself in Python instead of relying solely on existing tools.