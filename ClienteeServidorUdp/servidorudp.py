import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso!!!")

host = 'localhost'
porta = 5432

s.bind((host, porta))

mensagem = 'Servidor : Oláaaaaa cliente e ai beleza'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensage...')
        s.sendto(dados + (mensagem.encode()), end)