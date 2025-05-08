Author
Bishop Paul
📧 bishop.elaigwu@mohawkcollege.ca
🖥️ Passionate about IT support, system administration, and automating troubleshooting tasks with bash scripting.
# SysCheck Utility

A lightweight system check utility script designed to help junior IT Support Technicians quickly gather and display essential system information directly from the terminal. Ideal for troubleshooting, diagnostics, and general system health checks.

## 🛠️ Features

- Displays system hostname and IP address
- Shows OS type, kernel version, and uptime
- Lists current user and login information
- Reports disk usage and memory stats
- Checks active network interfaces and statuses

## 🔧 Requirements

- Bash (Linux or macOS)
- Basic terminal access

## 🚀 How to Use

1. **Clone the repository**
   ```bash
   git clone https://github.com/BishopElaigwu/syscheck-utility.git
   cd syscheck-utility

===== SYSTEM INFORMATION =====
Hostname: my-machine
IP Address: 192.168.1.15
OS Type: Linux
Kernel Version: 5.15.0-101
Uptime: 2 days, 4 hours, 15 minutes

===== USER SESSION =====
Current User: bishop
Last Login: Tue May 6 19:12

===== DISK USAGE =====
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   30G   20G  60% /

===== MEMORY =====
              total        used        free
Mem:           8.0G        3.2G        4.8G

===== NETWORK INTERFACES =====
eth0: UP - 192.168.1.15
lo: UP - 127.0.0.1
