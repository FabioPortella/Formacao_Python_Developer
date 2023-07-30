class Veiculo:
    def __init__(self, cor, placa, numero_rodas) -> None:
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('Ligado Motor')

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado) -> None:
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'}")

caminhao = Caminhao('verde', 'HCH-0909', 8, False)
moto = Motocicleta('amarela', 'FOC-5656', 2)
carro = Carro('branco', 'GOF-7852', 4)
print(carro)
print(moto)
print(caminhao)