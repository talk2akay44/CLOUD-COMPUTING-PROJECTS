import socket
import psutil
import os

# Function to get the IP address of the local machine
def get_local_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Function to retrieve network interface information
def get_network_interfaces():
    interfaces = psutil.net_if_addrs()
    interface_info = {}
    
    for interface_name, addresses in interfaces.items():
        for address in addresses:
            if str(address.family) == 'AddressFamily.AF_INET':  # IP address (IPv4)
                ip = address.address
            elif str(address.family) == 'AddressFamily.AF_PACKET':  # MAC address
                mac = address.address
        
        interface_info[interface_name] = {
            "IP Address": ip if 'ip' in locals() else 'N/A',
            "MAC Address": mac if 'mac' in locals() else 'N/A'
        }
    return interface_info

# Function to perform a ping test
def ping_test(host):
    response = os.system(f"ping -c 4 {host}")  # "-c 4" sends 4 packets on Linux/Mac
    if response == 0:
        return f"Ping to {host} was successful"
    else:
        return f"Ping to {host} failed"

# Displaying the local machine's IP address
def display_ip_address():
    ip_address = get_local_ip()
    print(f"Local IP Address: {ip_address}")

# Display network interfaces
def display_network_interfaces():
    interfaces = get_network_interfaces()
    print("Network Interfaces Information:")
    for interface, info in interfaces.items():
        print(f"Interface: {interface}")
        print(f"  IP Address: {info['IP Address']}")
        print(f"  MAC Address: {info['MAC Address']}")

# Main function for the network tool
def main():
    print("1. Display Local IP Address")
    print("2. Display Network Interfaces")
    print("3. Perform a Ping Test")
    print("4. Exit")
    
    while True:
        choice = input("\nChoose an option (1-4): ")

        if choice == '1':
            display_ip_address()
        elif choice == '2':
            display_network_interfaces()
        elif choice == '3':
            host = input("Enter a host or IP address to ping: ")
            result = ping_test(host)
            print(result)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()