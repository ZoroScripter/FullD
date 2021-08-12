import requests
import os
import time

os.system("clear")
os.system("figlet Zoro")
print("Ex: 179.125.127.182")
ip_input = input("Digite o IP Para Ser Consultado!\n>>>")

if len(ip_input) !=15:
	print("===> IP INVALIDO!! <===")
	time.sleep(4)
	os.system("python3 ip.py")

api=requests.get("http://ipwhois.app/json/")

ip_data=api.json()

if "erro" not in ip_data:
	os.system("clear")
	print("====================================")
	print("IP: {}".format(ip_data["ip"]))
	print("TIPO: {}".format(ip_data["type"]))
	print("CONTINENTE: {}".format(ip_data["continent"]))
	print("C?DIGO DO CONTINENTE: {}".format(ip_data["continent_code"]))
	print("PAIS: {}".format(ip_data["country"]))
	print("C?DIGO DO PA?S: {}".format(ip_data["country"]))
	print("CAPITAL DO PAIS: {}".format(ip_data["country_capital"]))
	print("C?DIGO TELEFONICO DO PAIS: {}".format(ip_data["country_phone"]))
	print("PAISES VIZINHOS: {}".format(ip_data["country_neighbours"]))
	print("REGIÃO: {}".format(ip_data["region"]))
	print("CIDADE: {}".format(ip_data["city"]))
	print("=====================================")
	print("===> Aguarde!! <===")
	time.sleep(4)
	print("""
	=======================
	vc fzr uma nv consulta??
	1 sim
	2 não
	""")
	op = input(">>>")
	
	if op == "1":
		os.system("python3 ip.py")
	elif op == "2":
		os.system("python3 main.py")
else:
	os.system("python3 ip.py")
