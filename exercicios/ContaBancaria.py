class ContaBancaria:
    
    def __init__(self, titular='', saldo=0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Titular: {self._titular} | Saldo: R${self._saldo}'
    
    @classmethod
    def ativa_conta(cls, conta):
        conta._ativo = True
        
conta1 = ContaBancaria('Rafael', 5000)
conta2 = ContaBancaria('Francisco', 12500)

print(conta1)
print(conta2)

print(conta1._ativo)
ContaBancaria.ativa_conta(conta1)
print(conta1._ativo)