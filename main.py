import requests
import os
import time
####################################################
#\033[1;30m Branco
#\033[1;31m Vermelho
#\033[1;32m Verde
#\033[1;33m Amarelo
#\033[1;34m Azul
#\033[1;35m Roxo
#\033[1;36m Ciano
#\033[1;37m Cinza Claro
os.system("clear")
os.system("figlet FullD")
#Recado
print("""
\033[1;37m[\033[1;33m!\033[1;37m]
Eu (Zoro) Tento atualizar o Script todo dia, mais ñ é preciso Ja que
As consultas são publicas ksksksksksksks
\033[1;37m[\033[1;33m!\033[1;37m]
""")
#Banner
print("""
\033[1;37m[\033[1;32m*\033[1;37m] CONSULTAS:\n\n
\033[1;37m[\033[1;32m1\033[1;37m] Consultar CEP
\033[1;37m[\033[1;32m2\033[1;37m] Consultar CNPJ
\033[1;37m[\033[1;32m3\033[1;37m] Consultar IP
\033[1;37m[\033[1;32m4\033[1;37m] Consultar COVID
\033[1;37m[\033[1;32m5\033[1;37m] Gerar CPF
\033[1;37m[\033[1;32m6\033[1;37m] Consulta BANCO
\033[1;37m[\033[1;32m7\033[1;37m] Consulta NUMERO
\033[1;37m[\033[1;32m8\033[1;37m] Consultar CPF
\033[1;37m[\033[1;32m9\033[1;37m] Consultar CPF2\n
\033[1;37m[\033[1;32m0\033[1;37m] Exit
""")

op = input(">>> ")
#Consultas
if op == "1":
	os.system("python3 cep.py")
elif op == "2":
	os.system("python3 cnpj.py")
elif op == "3":
	os.system("python3 ip.py")
elif op == "4":
	os.system("python covid.py")
elif op == "5":
	os.system("python3 cpf_gerar.py")
elif op == "6":
	os.system("python3 banco.py")
elif op == "7":
	os.system("clear")
	print("Esta consulta esta Offline")
	time.sleep(4)
	os.system("python3 main.py")
elif op == "8":
	os.system("python3 cpf.py")
elif op == "9":
	os.system("python3 cpf2.py")
elif op == "0":
	os.system("clear")
	print("Adeus, Até a proxima Versão")
	time.sleep(3)
	exit()
else:
	os.system("python3 main.py")
	