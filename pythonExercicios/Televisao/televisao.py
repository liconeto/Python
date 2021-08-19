class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5


    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True


    def aumenta_canal(self):
        self.canal += 1


    def diminiu_canal(self):
        self.canal -= 1

televisao = Televisao()
print(f'Televisão está ligada? {televisao.ligada}')
televisao.power()
print(f'Televisão está ligada? {televisao.ligada}')
televisao.power()
print(f'Televisão está ligada? {televisao.ligada}')
print(f'Canal : {televisao.canal}')
televisao.aumenta_canal()
televisao.aumenta_canal()
print(f'Canal : {televisao.canal}')
televisao.diminiu_canal()
print(f'Canal : {televisao.canal}')