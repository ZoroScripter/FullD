#####################
import requests    #
import os         #
import time      #
##################

os.system("clear")
print("""\033[1;36m
================
Ex: 01010-010
================
""")
cep_input = input("\033[1;37mDigite o Cep para Ser Consultado\n>>>")

if len(cep_input) !=9:
    print("Quantidade de numeros INVALIDA!!")
    print("Volte ao Inicio!!")
    time.sleep(5)
    os.system("clear")
    os.system("python3 cep.py")

requests = requests.get("https://viacep.com.br/ws/{}/json/".format(cep_input))

address_data = requests.json()

if "erro" not in address_data:
    os.system("clear")
    print("======================================")
    print("===> CEP ENCONTRADO!! <===")
    print("CEP: {}".format(address_data["cep"]))
    print("BAIRRO: {}".format(address_data["bairro"]))
    print("CIDADE: {}".format(address_data["localidade"]))
    print("ESTADO: {}".format(address_data["uf"]))
    print("GIA: {}".format(address_data["gia"]))
    print("======================================")
print("\033[1;37m[\033[1;32m1\033[1;37m]Nova Consulta\n\033[1;37m[\033[1;32m2\033[1;37m]Voltar ao Menu")
op = input(">>> ")
if op == "1":
    os.system("python3 banco.py")
if op == "2":
    os.system("python3 main.py")
else:
    os.system("python3 banco.py")