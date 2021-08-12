import requests
import os
import time
import json

os.system("clear")
os.system("figlet FullD")
print("Esta Opção esta OFFLINE!!")
print("\033[1;37m[\033[1;32m1\033[1;37m]Nova Consulta\n\033[1;37m[\033[1;32m2\033[1;37m]Voltar ao Menu")
op = input(">>> ")
if op == "1":
    os.system("python3 numero.py")
if op == "2":
    os.system("python3 main.py")
else:
    os.system("python3 numero.py")