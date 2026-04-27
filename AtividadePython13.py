class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def exibir_saldo(self):
        print(f"Titular: {self._titular}")
        print(f"Saldo atual: R$ {self._saldo}")


conta = ContaBancaria("Lucas", 1000)


conta.depositar(500)
conta.sacar(300)
conta.exibir_saldo()