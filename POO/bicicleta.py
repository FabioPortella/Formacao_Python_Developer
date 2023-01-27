class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18) -> None:
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor 
        self.aro = aro 

    def buzinar(self):
        print("Plim Plim ...")
    
    def parar(self):
        print("diminuindo velocidade ...  parando ...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm ...")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
if __name__ == "__main__":
    b1 = Bicicleta("Vermelha", "Caloi", 2022, 600)
    b1.buzinar()
    b1.parar()
    b1.correr()

    print(b1)