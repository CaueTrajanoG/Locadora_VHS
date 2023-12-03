class Carro:
    def __init__(self, renavam, modelo, ano):
        self.renavam = renavam
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f'{self.modelo} | {self.renavam} | {self.ano}'

    def __eq__(self, outro):
        return self.renavam == outro.renavam

    def __lt__(self, outro):
        return self.renavam < outro.renavam

    def __gt__(self, outro):
        return self.renavam >= outro.renavam