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

class TelevisaoSmart(Televisão):
    def __init__(self, estado, canal, tamanho, marca, conectada_com_alexa = False):
        Televisão.__init__(self, estado, canal, tamanho, marca)
        self.conectada_com_alexa = conectada_com_alexa
    