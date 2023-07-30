class Animal:
    def __init__(self, nro_patas) -> None:
        self.nro_patas = nro_patas

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw) -> None:
        super().__init__(**kw)
        self.cor_pelo = cor_pelo


class Ave(Animal):
    def __init__(self, cor_bico, **kw) -> None:
        super().__init__(**kw)
        self.cor_bico = cor_bico
        

class Ornitorrinco(Mamifero, Ave):
    pass


ornito = Ornitorrinco(nro_patas = 4, cor_pelo = "branco", cor_bico = "amarelo")
print(f'Ornito = {ornito}')

