# Author : Bishop Paul Elaigwu - 08/May/2025
import socket
import subprocess
import platform

def ping_host(host):
    print(f"\nPinging {host}...\n")
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    subprocess.run(['ping', param, '4', host])

def dns_lookup(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        print(f"\n{hostname} resolves to {ip}\n")
    except socket.gaierror:
        print(f"\nUnable to resolve hostname: {hostname}\n")

def traceroute(host):
    print(f"\nTraceroute to {host}...\n")
    command = ['tracert', host] if platform.system().lower() == 'windows' else ['traceroute', host]
    subprocess.run(command)

def port_scanner(host, ports=[22, 80, 443, 3389]):
    print(f"\nScanning ports on {host}...\n")
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            status = "Open" if result == 0 else "Closed"
            print(f"Port {port}: {status}")

def show_local_ip_info():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"\nHostname: {hostname}")
    print(f"Local IP Address: {local_ip}\n")

def main():
    while True:
        print("\nNetwork Diagnostic Toolkit")
        print("1. Ping a Host")
        print("2. DNS Lookup")
        print("3. Traceroute")
        print("4. Port Scanner")
        print("5. Show Local IP Info")
        print("6. Exit")
        choice = input("\nSelect an option: ")

        if choice == '1':
            host = input("Enter host to ping: ")
            ping_host(host)
        elif choice == '2':
            hostname = input("Enter hostname for DNS lookup: ")
            dns_lookup(hostname)
        elif choice == '3':
            host = input("Enter host for traceroute: ")
            traceroute(host)
        elif choice == '4':
            host = input("Enter host for port scanning: ")
            port_scanner(host)
        elif choice == '5':
            show_local_ip_info()
        elif choice == '6':
            print("Exiting Toolkit. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
