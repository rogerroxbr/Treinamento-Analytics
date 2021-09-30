class Conta():
    def __init__ (self, clientes, numero, saldo = 0, operacoes = []):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.operacoes = operacoes

    def resumo(self):
        print(f"CC Número {self.numero} \nSaldo: {self.saldo}")

    def saque(self, quantidade):
        if quantidade <= self.saldo:
            self.saldo -= quantidade
            array = ['Saque', quantidade]
            self.operacoes.append(array)
            return True
        else:
            return False

    def deposito(self, valor):
        self.saldo += valor
        array = ['Deposito', valor]
        self.operacoes.append(array)

    def extrato(self):
        print(f"\nExtrato CC N* {self.numero}")
        for o in self.operacoes:
            print(f"{o[0]} : {o[1]} ")
        print(f"\nSaldo: {self.saldo}")

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo = 0, limite = 0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite


conta_1 = Conta('Arthur', 100, 1200)
conta_2 = ContaEspecial('Arthur', 100, 2200, 2400)

print("Conta 1: ")
print(conta_1.saque(1200)) # True
print(conta_1.saldo) # 0
print(conta_1.deposito(2400))
conta_1.extrato()

print("\n")

print("Conta 2: ")
print(conta_2.saque(1200))
print(conta_2.saldo) # 0
