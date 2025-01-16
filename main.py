import getpass
import socket
import psutil
import re
import subprocess

def show_interfaces():
    interfaces = psutil.net_if_addrs()

    if not interfaces:
        print("No network interfaces available.")
        return
    
    print(f"\n{"Interface":<12} {"IP address":<16} {"MAC":<18} {"MTU":<6} {"State":<6}")
    print("-" * 61)

    for interface, addrs in sorted(interfaces.items()):        
        mac = "00:00:00:00:00:00"
        ipv4s = []

        for addr in addrs:
            if addr.family == socket.AF_PACKET:
                mac = addr.address
            elif addr.family == socket.AF_INET:
                ipv4s.append(addr.address)

        stats = psutil.net_if_stats().get(interface, None)

        mtu = stats.mtu if stats.mtu > 0 else "N/A"

        state = "UP" if stats and stats.isup else "DOWN" if stats else "N/A"

        if ipv4s:
            print(f"{interface:<12} {ipv4s[0]:<16} {mac:<18} {mtu:<6} {state:<6}")

            for ip in ipv4s[1:]:
                print(f"{'':<12} {ip:<16} {'':<18} {'':<6} {'':<6}")
        else:
            print(f"{interface:<12} {'N/A':<16} {mac:<18} {mtu:<6} {state:<6}")

def ip_is_valid(ip):
    ip_regex = re.compile(r'''
            ^
            (?: 25[0-5]| 2[0-4][0-9]| 1[0-9]{2}| [1-9][0-9]| [0-9])\.
            (?: 25[0-5]| 2[0-4][0-9]| 1[0-9]{2}| [1-9][0-9]| [0-9])\.
            (?: 25[0-5]| 2[0-4][0-9]| 1[0-9]{2}| [1-9][0-9]| [0-9])\.
            (?: 25[0-5]| 2[0-4][0-9]| 1[0-9]{2}| [1-9][0-9]| [0-9])\/
            (?: 3[0-2]| [1-2][0-9]| [0-9])
            $''', flags=re.VERBOSE
        )
    
    return bool(ip_regex.match(ip))

def configure_interface(command):
    try:
        _, interface, _, ip = command.split()

        available_interfaces = list(psutil.net_if_addrs().keys())

        if not (interface in available_interfaces):
            raise ValueError(f"The interface '{interface}' doesn't exist.")

        if not(ip_is_valid(ip)):
            raise ValueError("Invalid IP address.")

        result = subprocess.run(
            ["sudo", "ip", "addr", "add", ip, "dev", interface],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(f"Success configured {ip} on {interface}!")
        else:
            print(f"Error configuring IP: {result.stderr.strip()}")

    except ValueError as ve:
        print(ve)

    except Exception as e:
        print(f"Unexpected error: {e}")

def verify_login(username, password, filepath):
    password = password+"\n"

    with open(filepath, "r") as file:

        lines = file.readlines()
        
        for line in lines:
            fields = line.split(",")

            if fields[0] == username and fields[1] == password:
                return True
    return False

def available_commands():
    print("\nAvailable commands:")
    print("1. Show interfaces")
    print("2. Configure <interface-name> ip <ip-address/mask>")
    print("3. Logout")
    print("4. Exit")

def parse_command(command):
    parts = command.strip().split()
    return parts if parts else []

def is_valid_command_configure(parts):
    return len(parts) == 4 and parts[0].lower() == "configure" and parts[2].lower() == "ip"

def is_invalid_command_configure(parts):
    return (len(parts) == 4 and (parts[0].lower() != "configure" or parts[2].lower() != "ip"))

def show_system_menu():
    print("\n##### Welcome to Config Linux Network System #####")
    available_commands()
    
    while True:
        command = input("> ").strip()
        parts = parse_command(command)

        if command.lower() == "show interfaces" or command == "1":
            show_interfaces()
        elif command == "2" or is_invalid_command_configure(parts):
            print("Invalid command format. Use: configure <interface-name> ip <ip-address/mask>")
        elif is_valid_command_configure(parts):
            configure_interface(command)
        elif command.lower() == "logout" or command == "3":
            print("\nLogout successful!\n")
            login()
        elif command.lower() == "exit" or command == "4":
            print("Exiting the system.")
            break
        elif len(command) == 0:
            print("\nNo command was typed, please type a command.")
            available_commands()
        else:
            print("\nUnknown command! try the commands below.")
            available_commands()

def login(): 
    filepath = "logins.txt"

    username = input("Login: ")
    password = getpass.getpass("Password: ")

    if verify_login(username, password, filepath):
        show_system_menu()
    elif len(username) == 0 or len(password) == 0:
        print("\nLogin and password cannot be empty!\n")
        login()
    else:
        print("\nIncorrect login credentials, please try again!\n")
        login() 

def main():
    try:
        login()
    except KeyboardInterrupt:
                print("\nProgram interrupted by user. Exiting the system.")

if __name__ == "__main__":
    main()