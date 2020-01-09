class Pesoa:
    def __init__(self, *filhos, nome = None, edad =32):
        self.nome = nome
        self.edad = edad
        self.filhos = list(filhos)

    def saludo(self):
        return f'Hola {id(self)}'

if __name__ == '__main__':
    elier = Pesoa(nome='Elier')
    diego = Pesoa(elier, nome="Diego", edad=65)
    print(elier.nome)
    print(elier.filhos)
    print(elier.edad)
    print("--------")
    print(diego.nome)
    for filhos in diego.filhos:
        print(type(filhos))
        print(filhos.nome)
        print(type(filhos.nome))
    print(diego.edad)