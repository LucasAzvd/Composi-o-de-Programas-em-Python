from atv_2 import Conta, ContaCorrente, ContaPoupanca

conta_corrente = ContaCorrente(1, 1.50)
conta_corrente.depositar(10)
conta_corrente.cobrar_taxa()

conta_corrente = Conta(1)
conta_corrente.depositar(10)