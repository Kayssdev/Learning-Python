import socket

def check_port(host, porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    res = s.connect_ex((host, porta))
    s.close()

    if res == 0:
        print(f"Porta {porta}: ABERTA")
    else:
        print(f"Porta {porta}: FECHADA")

check_port("scanme.nmap.org", 80)
check_port("scanme.nmap.org", 9999)
