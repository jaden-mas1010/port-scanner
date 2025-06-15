import socket

def scan_ports(target, start_port, end_port):
    print(f"Scanning from{target} from port {start_port} to {end_port}")
    for port in range(start_port,end_port+1):
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target,port))
            if result == 0:
                print(f"[+]Port {port} is open")
                sock.close()
        except socket.error as e:
            print("Something is wrong",e)
if __name__=="__main__":
    target = input("enter target ip or hostname:  ")
    scan_ports(target,20,100)
