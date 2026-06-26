log_file_path = "server_log.txt"
blacklist_path = "crna_lista.txt"

#Set u koji cemo cuvati jedinstvene IP adrese napadaca
napadaci = set()

print("---AUTOMATIZOVANI SISTEM ZA BLOKADU POKRENUT ---\n")

with open(log_file_path, "r") as file:
	for linija in file:
		if "Failed login attempt" in linija:
			#razbijamo liniju na reci da bismo izvukli IP adresu, ona je poslenja u liniji
			reci = linija.split()
			ip_adresa = reci[-1]
			napadaci.add(ip_adresa)
			print(f"[DETEKCIJA] sumnjiva aktivnost sa adrese: {ip_adresa}")

#Ako smo pronasli napadace, upisujemo ih u fajl za blokadu
if napadaci:
	with open(blacklist_path, "w") as blacklist:
		for ip in napadaci:
			blacklist.write(f"{ip}\n")
	print(f"\n[AKCIJA] Uspesno generisana bleklista!")
	print(f"Adrese su poslate u fajl: '{blacklist_path}' za sistemsku blokadu.")
else:
	print("\n[INFO] Nema detekcija. Sistem je bezbedan.")
 
