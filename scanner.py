import socket
import sys

#definisemo cilj (localhost je moj kali sitem)
target="127.0.0.1"

#portovi koje zelimo da proverimo FTP, SSH, SMTP, HTTP)
ports=[21, 22, 25, 80]

print(f"Skeniram cilj: {target}")

for port in ports:
	#kreiramo socket objekat (AF_INET = IPv4, SOCK_STREAM = TCP)
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(1.0)#cekamo odgovor

	#pokusamo da se povezemo na port
	result = s.connect_ex((target, port))

	if result == 0:
		print(f"[*] Port {port} je OTVOREN")
	else:
		print(f"[-] Port je ZATVOREN")
	
	s.close()

