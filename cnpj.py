import requests
import os
import time

os.system("clear")
os.system("figlet Zoro")
print("Digite o cnpj Nesta Forma.\nEx: 00000000000191")
cnpj_input = input("\033[1;37mINFORME SEU CNPJ: ")

if len(cnpj_input) !=14:
	print(">>> CNPJ INVALIDO!! <<<")
	time.sleep(4)
	os.system("python3 cnpj.py")

cnpj=requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj_input))

cnpj_data=cnpj.json()

if "erro" not in cnpj_data:
	os.system("clear")
	os.system("figlet Zoro")
	print("===========================================")
	print("Situação: {}".format(cnpj_data["situacao"]))
	print("UF: {}".format(cnpj_data["uf"]))
	print("Municipio: {}".format(cnpj_data["municipio"]))
	print("Logradouro: {}".format(cnpj_data["logradouro"]))
	print("Numero: {}".format(cnpj_data["numero"]))
	print("Complemento: {}".format(cnpj_data["complemento"]))
	print("Natureza: {}".format(cnpj_data["natureza_juridica"]))
	print("Data de abertura: {}".format(cnpj_data["abertura"]))
	print("Tipo: {}".format(cnpj_data["tipo"]))
	print("============================================")
print("\033[1;37m[\033[1;32m1\033[1;37m]Nova Consulta\n\033[1;37m[\033[1;32m2\033[1;37m]Voltar ao Menu")
op = input(">>> ")
if op == "1":
    os.system("python3 banco.py")
if op == "2":
    os.system("python3 main.py")
else:
    os.system("python3 banco.py")