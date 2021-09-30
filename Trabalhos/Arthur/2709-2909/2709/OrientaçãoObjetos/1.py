class Televisão():
    def __init__(self, estado, canal, tamanho, marca):
        self.ligada = estado
        self.canal = canal
        self.tamanho = tamanho
        self.marca = marca

    def desligar(self):
        if(self.ligada == True):
            self.ligada = False
    
    def ligar(self):
        if(self.ligada == False):
            self.ligada = True

    def __str__(self):
        return f'A Televisão de {self.tamanho} polegadas da parca {self.marca} está {self.ligada} no Canal {self.canal}.'

tv = Televisão(False, 12, '42"', 'Philco')

tv_sala = Televisão(True, 4, '32"', 'Samsung')
tv_sala.canal = 4

print(tv)
print(tv_sala) # A Televisão está ligada no canal 4.