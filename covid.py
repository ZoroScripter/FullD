import os
import requests
import time

os.system("clear")
os.system("figlet Zoro")
uf_input = input("Digite O estado Para ser consultado!!\n===> ")

data = requests.get("https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{}".format(uf_input))

data_data=data.json()

if data_data:
	os.system("clear")
	print("Estado: {}".format(data_data["state"]))
	print("UF: {}".format(data_data["uf"]))
	print("UID: {}".format(data_data["uid"]))
	print("Casos: {}".format(data_data["cases"]))
	print("Mortes: {}".format(data_data["deaths"]))
	print("Suspeitas: {}".format(data_data["suspects"]))
	print("Recusados: {}".format(data_data["refuses"]))
print("\033[1;37m[\033[1;32m1\033[1;37m]Nova Consulta\n\033[1;37m[\033[1;32m2\033[1;37m]Voltar ao Menu")
op = input(">>> ")
if op == "1":
    os.system("python3 banco.py")
if op == "2":
    os.system("python3 main.py")
else:
    os.system("python3 banco.py")