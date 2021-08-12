import requests
import os
import time
# Api - https://api.cpfcnpj.com.br
print("\033[1;37m")
os.system("clear")
os.system("figlet FullD")
cpf_input = input("CPF: ")
if len(cpf_input) !=11:
    print("ERROR!!")
    time.sleep(3)
    os.system("python3 cpf.py")

cpf=requests.get("https://api.cpfcnpj.com.br/5ae973d7a997af13f0aaf2bf60e65803/9/{}".format(cpf_input))

cpf_data=cpf.json()

if "erro" not in cpf_data:
    os.system("clear")
    print("-=-=--=-=-=-=-=-=-=-=-=-=-=-=-")
    print("CPF: {}".format(cpf_data["cpf"]))
    print("Status: {}".format(cpf_data["status"]))
    print("SEXO: {}".format(cpf_data["genero"]))
    print("SITUAÇÃO: {}".format(cpf_data["situacao"]))
    print("Nome Da mãe: {}".format(cpf_data["mae"]))
    print("SALDO: {}".format(cpf_data["saldo"]))
    print("NASCIMENTO: {}".format(cpf_data["nascimento"]))
    print("Delay: {}".format(cpf_data["delay"]))
    print("-------------------------------")
print("\033[1;37m[\033[1;32m1\033[1;37m]Nova Consulta\n\033[1;37m[\033[1;32m2\033[1;37m]Menu")
op = input(">>> ")

if op == "1":
    os.system("python3 cpf2.py")
if op == "2":
    os.system("python3 main.py")
else:
    os.system("python3 cpf2.py")