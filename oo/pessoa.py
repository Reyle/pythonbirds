class Pesoa:
    # de esta manera definimos atributos de la clase
    olhos = 2
   # con esta funcion definimos atributos de un objeto
    def __init__(self, *filhos, nome = None, edad =32):
        self.nome = nome
        self.edad = edad
        self.filhos = list(filhos)

    def saludo(self):
        return f'Hola {id(self)}'

if __name__ == '__main__':
    elier = Pesoa(nome='Elier')
    diego = Pesoa(elier, nome="Diego", edad=65)
    print("--------")
    print('Atributos de los objetos "diego" y "elier')
    print('Nombre: ', elier.nome)
    print('Filhos: ', elier.filhos)
    print('Edad: ', elier.edad)
    print()
    print('Nombre: ', diego.nome)
    for filhos in diego.filhos:
        print(type(filhos))
        print('Filhos: ', filhos.nome)
        print(type(filhos.nome))
    print('Edad: ', diego.edad)


    print("-------------------")
    print('Atributo de la clase Pesoa: "olhos"')
    print('Clae Pesoa: ', Pesoa.olhos)
    print('Objeto diego: ', diego.olhos)
    elier.olhos = 1;
    print('Objeto elier: ', elier.olhos)
