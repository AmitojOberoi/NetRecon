# 🛡️ NetRecon

**NetRecon** is a modular Python-based network reconnaissance toolkit designed to perform host discovery, custom TCP port scanning, banner grabbing, report generation, and advanced Nmap-based network scanning. The project combines a custom-built multithreaded scanner with industry-standard Nmap integration to provide a complete reconnaissance solution.

---

# ✨ Features

## 🔍 Host Discovery
- Discover whether a host is online.
- Fast ICMP-based reachability checks.

## 🌐 DNS Resolution
- Resolve hostnames to IP addresses.
- Reverse lookup support.

## ⚡ Custom TCP Port Scanner
- Multithreaded socket-based TCP port scanner.
- Scan any custom port range.
- Fast concurrent scanning using Python ThreadPoolExecutor.

## 🔖 Service Detection
- Identify well-known services running on open ports.

Example:

```
22    ssh
80    http
443   https
```

## 📡 Banner Grabbing
Attempts to identify services by retrieving banners from open ports.

Example:

```
HTTP/1.1 200 OK
Apache/2.4.58
OpenSSH 9.7
```

## 📄 JSON Report Generation
Automatically generates detailed JSON reports after every custom scan.

Example:

```
reports/
    scan_2026-07-24_18-30-14.json
```

## 🌐 HTML Report Generation
Automatically creates professional HTML reports that can be opened directly in any web browser.

Example:

```
reports/
    scan_2026-07-24_18-30-14.html
```

## 🛰️ Nmap Integration

NetRecon includes an advanced Nmap scanning module with multiple scan modes.

Supported scans:

- ✅ Quick Scan (`-T4 -F`)
- ✅ Service Version Detection (`-sV`)
- ✅ Operating System Detection (`-O`)
- ✅ Aggressive Scan (`-A`)
- ✅ Ping Scan (`-sn`)

Every Nmap scan is automatically saved as a text report.

Example:

```
reports/
    nmap_quick_scan_2026-07-24_18-40-18.txt
```

---

# 🏗️ Project Structure

```
NetRecon/

├── main.py
├── scanner.py
├── host_discovery.py
├── banner.py
├── utils.py
├── report.py
├── html_report.py
├── nmap_scanner.py
├── reports/
├── README.md
└── .gitignore
```

---

# 🛠️ Technologies Used

- Python 3
- Socket Programming
- ThreadPoolExecutor
- Subprocess
- JSON
- HTML
- Nmap
- Git
- GitHub

---

# 📚 Concepts Demonstrated

- Computer Networking
- TCP/IP
- Socket Programming
- DNS Resolution
- Multithreading
- Concurrent Programming
- Banner Grabbing
- Modular Programming
- Report Generation
- File Handling
- Exception Handling
- Command Line Interfaces
- External Tool Integration

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/AmitojOberoi/NetRecon.git
```

Move into the project:

```bash
cd NetRecon
```

Install dependencies (if required):

```bash
pip install -r requirements.txt
```

> **Note:** Nmap must be installed separately and available in your system PATH to use the Nmap Scanner module.

---

# ▶️ Running the Project

Run:

```bash
python main.py
```

Main Menu:

```
========== NETRECON ==========

1. Host Discovery
2. Custom Port Scanner
3. Nmap Scanner
4. Exit
```

---

# 📊 Reports

NetRecon automatically generates reports inside the `reports` directory.

Supported formats:

- JSON
- HTML
- TXT (Nmap)

---

# 🎯 Future Improvements

- Export Nmap scans as XML
- CSV Report Generation
- Dark Theme HTML Reports
- Scan Progress Indicator
- Logging Support
- Scan History
- Rich Terminal UI
- Whois Lookup
- Traceroute Support
- UDP Port Scanner
- Optional GUI Version

---

# 📸 Screenshots

Screenshots will be added in a future update.

---

# 👨‍💻 Author

**Amitoj Oberoi**

GitHub:
https://github.com/AmitojOberoi

---

# ⭐ If you found this project useful

If you like this project, consider giving it a ⭐ on GitHub.