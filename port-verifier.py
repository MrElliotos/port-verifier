allowed_ports = [22, 80, 443, 8080]
def check_port(port):
    if port in allowed_ports :
        print(f"[+] Port {port} is open and secure")
    else:
        print(f"[!] ATTENTION: Port {port} is closed or considered suspicious!")
print("=== Network port scanner ===")
try :
    muno = int(input("write the port number "))
    check_port(muno)
except ValueError:
    print("Please enter numbers, not letters")
else:
    loka = input("Do you want to add this port to the allowed list? (yes/no): ").strip().lower()
    if loka == "yes" :
     if muno not in allowed_ports:
        allowed_ports.append(muno)
        print(f"Port {muno} successfully added!")
     else:
         print("This port is already in the list!")
    if loka == "no":
        print("Fine")
print("Final list of allowed ports:")
for port in allowed_ports:
     print("-", port)
    




