class Pesoa:
    def __init__(self, nome = None):
        self.nome = nome

    def saludo(self):
        return f'Hola {id(self)}'

if __name__ == '__main__':
    p = Pesoa('Elier')
    print(p.saludo())
    print(id(p))
    print()
    print(p.nome)