# PORT SCAN DO LÚPICO

# Importando socket e iniciando scanner
import socket

# Identificando o Código ao Usuário
print("## INICIANDO PORTSCAN DO LUPICO ##")
print("## ESTE SCAN PASSARÁ PELAS PORTAS 0 A 1023 ##")

# Solicitando IP e Porta a Serem Pesquisados
host = input("Qual o domínio ou IP do servidor? ")

# Escaneando portas
for x in range(0, 1024):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.01)
    conn = s.connect_ex((host, x))
    if conn == 0:
        # Resultado do Scan
        print("Porta ", x, " << ABERTA >>")
print(" ## FIM DO SCAN ## ")
print("DIGITE <SAIR> PARA SAIR: ")

saida = exit

if input(""):
    exit()
