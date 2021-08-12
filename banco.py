import requests
import os
import time
os.system("clear")
print("\033[1;34m")
os.system("figlet Banco")
banco_input = input("Digite o numero bancario:\n>>> ")
if len(banco_input) !=3:
    print("""
    Codigo Bancario invalido!!
    formato do codigo:
    Ex; 237
    """)
    time.sleep(4)
    os.system("python3 b.py")

banco  = requests.get("https://brasilapi.com.br/api/banks/v1/{}".format(banco_input))

banco_data=banco.json()

if "erro" not in banco_data:
    os.system("clear")
    print("\033[1;37m")
    print("---------------------------------------")
    print("===>  CODIGO BANCARIO ENCOTRADO!!  <===")
    print("Codigo Bancario: {}".format(banco_data["code"]))
    print("Nome: {}".format(banco_data["name"]))
    print("Nome Completo: {}".format(banco_data["fullName"]))
    print("ISPB: {}".format(banco_data["ispb"]))
    print("=======================================")
time.sleep(3)
print("\033[1;37m[\033[1;32m1\033[1;37m]Nova Consulta\n\033[1;37m[\033[1;32m2\033[1;37m]Voltar ao Menu")
op = input(">>> ")
if op == "1":
    os.system("python3 banco.py")
if op == "2":
    os.system("python3 main.py")
else:
    os.system("python3 banco.py")