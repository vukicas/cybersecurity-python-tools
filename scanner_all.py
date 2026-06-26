import socket
import sys

target = input("Ukucaj IP adresu za skeniranje (npr 127.0.0.1): ")

print(f"\nSkeniram cilj: {target}")
print("Molim sacekajte, ovo moze potrajati...")

for port in range(1, 101):
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.1)

	result = s.connect_ex((target, port))

	if result == 0:
		print(f"[*] Port {port} je OTVOREN")
	#else:
	#	printf("[-] Port { port }je ZATVOREN")
	s.close()

print("\nSkeniranje je zavrseno")

