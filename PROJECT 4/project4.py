import socket
import os
import platform
import subprocess
import re

# Function to retrieve the IP address of the local machine
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Local IP Address: {ip_address}")

# Function to list available network interfaces along with their corresponding IP addresses and MAC addresses
def get_network_interfaces():
    if platform.system() == "Windows":
        command = "ipconfig /all"
    else:
        command = "ifconfig"

    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout

    # Display the output of the command
    print("Network Interfaces and their IP/MAC addresses:\n")
    print(output)

# Function to perform a ping test to check connectivity
def ping_test(host):
    print(f"Pinging {host}...\n")
    command = ["ping", "-c", "4", host] if platform.system() != "Windows" else ["ping", host]

    result = subprocess.run(command, capture_output=True, text=True)
    output = result.stdout

    # Display the ping test results
    print(output)

    # Extract and display response times and packet loss
    if platform.system() != "Windows":
        packet_loss = re.search(r'(\d+)% packet loss', output).group(1)
        avg_response_time = re.search(r'avg = (\d+\.\d+)/', output).group(1)
        print(f"Packet Loss: {packet_loss}%")
        print(f"Average Response Time: {avg_response_time} ms")
    else:
        # On Windows, ping output differs, so just display the raw output for simplicity
        pass

def main():
    while True:
        print("\nNetwork Information Retrieval Tool")
        print("1. Display IP Address")
        print("2. List Network Interfaces")
        print("3. Perform Ping Test")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            get_ip_address()
        elif choice == '2':
            get_network_interfaces()
        elif choice == '3':
            host = input("Enter the host or IP address to ping: ")
            ping_test(host)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()