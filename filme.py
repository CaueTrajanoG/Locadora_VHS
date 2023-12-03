class Filme:
    def __init__(self, title, price):
        self.titulo = title
        self.preco = price
        self.estado = "disponivel"

    def __str__(self):
        return f'{self.titulo} | {self.preco} | {self.estado}'

    def __eq__(self, outro):
        return self.titulo == outro.titulo

    def __lt__(self, outro):
        return self.titulo < outro.titulo

    def __gt__(self, outro):
        return self.titulo >= outro.titulo