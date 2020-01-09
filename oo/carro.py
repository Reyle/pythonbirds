
# EJEMPO DE COMPOCICION DE CLASES DONDE UNA CLASE CARRO TIENE COMO PARAMETRO DOS CLASES -MOTOR Y - DIRECCION

class Carro:
    def __init__(self, motor, direccion):
        self.direccion = direccion
        self.motor = motor

    def direccio(self):
        return self.direccion.result

    def calculo_velocidad(self):
        return self.motor.velocidad
    def acelerando(self):
        return self.motor.acelerar()
    def frenar(self):
        return self.motor.frenado()




class Motor:
    #velocidad = 0
    def __init__(self, velocidad=0):
        self.velocidad = velocidad

    def aceleracio(self):
        if self.velocidad <= 199:
            self.velocidad += 1


    def frenado(self):
         self.velocidad -= 2
         self.velocidad = max(0,  self.velocidad)

class Direccion:
   position = 0
   result = 'Norte'
   def __init__(self):
       self.direccion = ('Norte','Este', 'Sur', 'Oeste')
       self.position = 0
   def giro_dereita(self):
        if self.position == 3:
            self.position = 0
        else:
            self.position += 1
        Direccion.result = self.direccion[self.position]

   def giro_izquierda(self):
       if self.position == -3:
           self.position = 0
       else:
           self.position -= 1
       Direccion.result = self.direccion[self.position]

m = Motor()
d = Direccion()
c = Carro(m, d)




'''m = Motor()
m.aceleracio()
m.aceleracio()
m.aceleracio()
print(m.velocidad)
m.frenado()
m.frenado()
print(m.velocidad)


d = Direccion()
print(d.result)
d.giro_dereita()

print(d.result)
d.giro_dereita()

print(d.result)
d.giro_dereita()

print(d.result)

d.giro_izquierda()
print(d.result)'''