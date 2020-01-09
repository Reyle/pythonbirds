class Pesoa:
    # de esta manera definimos atributos de la clase
    olhos = 2
   # con esta funcion definimos atributos de un objeto(filhos, nome, edad), ademas esta funcion es un metodo del objeto
    def __init__(self, *filhos, nome = None, edad =32):
        self.nome = nome
        self.edad = edad
        self.filhos = list(filhos)
# Metodo de un objeto o instancia
    def saludo(self):
        return f'Hola {id(self)}'

# Metodos de la clase comoensan con los decoreiton (@), estos son usados para realizar operaciones independientes tanto de la clase como del objeto
    @staticmethod
    def metodo_statico():
        return 42



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

    print("-------------------")
    print(Pesoa.metodo_statico())
    print(elier.metodo_statico())