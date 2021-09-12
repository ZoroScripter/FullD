from requests import post
import os

os.system("clear")
print("""\033[1;34m
   _     _     _     _     _  
  / \   / \   / \   / \   / \ 
 ( F ) ( U ) ( L ) ( L ) ( D )
  \_/   \_/   \_/   \_/   \_/
""")
quant = int(input("Quant: "))
for i in range(0, quant):
	req = post("https://www.4devs.com.br/ferramentas_online.php",{"acao":"gerar_pessoa","pontuacao":"S","sexo":"M","idade":"20"})
	resposta = req.text
	print(resposta)
	print("""\033[1;37m
    =---------------------------=
    \033[1;37m[\033[1;34m1\033[1;37m]Voltar Ao Menu
    \033[1;37m[\033[1;34m2\033[1;37m]Nova Consulta
    =---------------------------=
    """)
    op = input("\033[1;31m_!_")
    
    if op == "1":
    	os.system("python3 main.py")
    if op == "2":
    	os.system("python3 meuip.py")
