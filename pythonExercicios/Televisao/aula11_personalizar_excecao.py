class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input('Entre com uma nota de 0 até 10: '))
        print(f'{x}')
        if x > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0!')
        break
    except ValueError:
        print(f'Valor invalido. Deve-se digitar apenas números.')
    except InputError as ex:
        print(f'{ex}')

