import getpass
import socket
import psutil
import re

class InvalidIPError(Exception):
    """IP is invalid."""
    pass

def show_interfaces():
    interfaces = psutil.net_if_addrs()

    print(f"{"Interface":<12} {"IP address":<16} {"MAC":<18} {"MTU":<6} {"State":<6}")
    print("-" * 61)

    for interface, addrs in interfaces.items():        
        mac = "Don't have MAC"
        ipv4s = []

        for addr in addrs:
            if addr.family == socket.AF_PACKET:
                mac = addr.address
            elif addr.family == socket.AF_INET:
                ipv4s.append(addr.address)

        stats = psutil.net_if_stats().get(interface, None)

        mtu = stats.mtu if stats else "Don't have MTU"

        state = "UP" if stats and stats.isup else "DOWN" if stats else "UNKNOWN"

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

        if not(ip_is_valid(ip)):
            raise InvalidIPError("Invalid IP address")

        print(f"Configuring interface {interface} with IP {ip}")
    
    except InvalidIPError:
        print("Invalid IP address.")

    except ValueError:
        print("Invalid command format. Use: configure <interface-name> ip <ip-address/mask>")
    


def verify_login(userame, password, filepath):
    try:
        password = password+"\n"

        with open(filepath, "r") as file:

            lines = file.readlines()
            
            for line in lines:

                fields = line.split(",")

                if fields[0] == userame and fields[1] == password:
                    return True
    except Exception:
        print(Exception)                

def available_commands():
    print("\nAvailable commands:")
    print("1. Show interfaces")
    print("2. Configure <interface-name> ip <ip-address/mask>")
    print("3. Exit")

def show_system_menu():
    print("\n##### Welcome to Config Linux Network System #####")
    available_commands()

    while True:
        command = input("> ").strip()
        if command.lower() == "show interfaces" or command == "1":
            show_interfaces()
        elif command.startswith("configure") or command == "2":
            configure_interface(command)
        elif command.lower() == "exit" or command == "3":
            print("Exiting the system.")
            break    
        else:
            print("Unknown command! try the commands below.")
            print()
            available_commands()

def main():
    filepath = "logins.txt"

    username = input("Login: ")
    password = getpass.getpass("Password: ")

    if verify_login(username, password, filepath):
        show_system_menu()
    else:
        print("Usuário ou senha incorretos. Tente novamente.")

if __name__ == "__main__":
    main()