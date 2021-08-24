import datetime
from datetime import date, time

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %d %B %Y')
    print(f'{type(data_atual)}')
    print(f'{data_atual_str}')
    print(f'{type(data_atual_str)}')


def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    horario_str = horario.strftime("%H:%M:%S")
    print(f'{horario_str}')


def trabalhando_com_datetime():
    data_atual = datetime.datetime.now()
    print(f'{data_atual}')
    print(f'{data_atual.strftime("%A %d, %m %Y %H %M %S")}')
    print(f'{data_atual.strftime("%c")}')
    print(f'{data_atual.weekday()}')
    tupla = ('Segunda', 'Terça', ' Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(f'{tupla[data_atual.weekday()]}')
    mes = ('Dezembro','Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro')
    print(f'{mes[data_atual.month]}')
    print(f'{data_atual.month}')
    data_criada = datetime.datetime(2018, 6, 20, 15, 30, 20)
    print(f'{data_criada}')
    print(f'{data_criada.strftime("%c")}')
    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(f'{data_convertida}')
    nova_data = data_convertida - datetime.timedelta(days=365, hours=2, minutes=15)
    print(f'{nova_data}')


if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()