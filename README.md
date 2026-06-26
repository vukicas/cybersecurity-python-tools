# Cybersecurity Automation & Network Tools

A collection of lightweight, custom Python scripts developed in a headless Kali Linux (CLI) environment. These tools are designed to demonstrate core concepts of network scanning, reconnaissance, and automated intrusion detection/prevention (IDS/IPS).

## 🛠️ Tools Included

### 1. Custom Network Port Scanner (`skener.py`)
A reconnaissance tool built using Python's native `socket` library to identify open ports and active services on a target system.
* **How it works:** Utilizes TCP three-way handshake logic (`connect_ex`) to sequentially audit ports 1-100.
* **Use Case:** Helps security administrators map network attack surfaces and find open vectors like SSH (22), FTP (21), or SMTP (25).

### 2. Automated IDS/IPS Log Parser (`analizator.py`)
An automated defensive script designed to parse server security logs, detect brute-force attacks, and mitigate threats.
* **How it works:** Iterates through log files to identify suspicious failed login patterns. It isolates malicious IP addresses using a `set` data structure to prevent duplicates and automatically exports them.
* **Mitigation:** Generates a real-time `crna_lista.txt` (blacklist) file, ready to be ingested by system firewalls for automated IP blocking.

## 🧰 Tech Stack & Skills
* **Languages:** Python 3 (Socket programming, File I/O, Data manipulation)
* **Environment:** Kali Linux (Command Line Interface / CLI)
* **Networking:** TCP/IP Suite, Protocol Analysis (SMTP, FTP, DNS, VoIP, RTP), Port Management
* **Version Control:** Git & GitHub CLI

## 👤 About the Author
Transitioning IT Infrastructure and Computer Networks Educator with deep domain knowledge of network protocols and system administration. Leveraging a strong background in teaching complex technical concepts to pivot into defensive cybersecurity (Blue Team / SOC operations).
