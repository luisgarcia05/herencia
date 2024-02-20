class Vehicle:
    def __init__(self,color,year):
        self.color= color
        self.year= year
    
    def describe(self):
        return f"{self.color}/{self.year}"

#class car

class Car(Vehicle):
    def __init__(self,color,year,carbrand,carmodel):
        Vehicle.__init__(self,color,year)
        self.carbrand= carbrand
        self.carmodel= carmodel

    def describe(self):
        return f"color:{self.color} /año:{self.year} /marca:{self.carbrand} /modelo:{self.carmodel}"
    



#class ship

class Ship(Vehicle):
    def __init__(self,color,year,shipstorage,shipmodel):
        Vehicle.__init__(self,color,year)
        self.shipstorage= shipstorage
        self.shipmodel= shipmodel

    def describe(self):
        return f"color:{self.color} /año:{self.year} /Almacenamiento:{self.shipstorage} /modelo:{self.shipmodel}"




#clase airplane

class Airplane(Vehicle):
    def __init__(self,color,year,passengers,airmodel):
        Vehicle.__init__(self,color,year)
        self.passengers= passengers
        self.airmodel= airmodel

    def describe(self):
        return f"color:{self.color} /año:{self.year} /Numero de pasajeros:{self.passengers} /modelo:{self.airmodel}"



print("Registra las caracteristicas que desees de los siguientes vehiculos")




#atributos de vehicle

color=input("de que color quieres que sean los vehiculos?")
year=input("de que año quieres que sean los vehiculos?")



#atributos de car

print("Elige las caracteristicas de 2 carros")

carbrand1=input("de que marca quieres que sea el primer carro?")
carmodel1=input("de que modelo quieres que sea el primer carro?")

print("                                                                                                                                                   ")

carbrand2=input("de que marca quieres que sea el segundo carro?")
carmodel2=input("de que modelo quieres que sea el segundo carro?")

print("                                                                                                                                                   ")

car1=Car(color, year, carbrand1, carmodel1)

car2=Car(color, year, carbrand2, carmodel2)



#atributos de ship    


print("Elige las caracteristicas de 2 barcos")

shipstorage1=input("cuanto almacenamiento quieres que tenga el primer barco?")
shipmodel1=input("de que modelo quieres que sea el primer barco?")

print("                                                                                                                                                   ")

shipstorage2=input("cuanto almacenamiento quieres que tenga el segundo barco?")
shipmodel2=input("de que modelo quieres que sea el segundo barco?")

print("                                                                                                                                                   ")

ship1=Ship(color, year, shipstorage1, shipmodel1)

ship2=Ship(color, year, shipstorage2, shipmodel2)




#atributos de airplane   

print("Elige las caracteristicas de 2 aviones")


passengers1=input("cuanto es el maximo de pasajeros que quieres que tenga el primer avión?")
airmodel1=input("de que modelo quieres que sea el primer avión?")

print("                                                                                                                                                   ")

passengers2=input("cuanto es el maximo de pasajeros que quieres que tenga el segundo avión?")
airmodel2=input("de que modelo quieres que sea el segundo avión?")

print("                                                                                                                                                   ")

airplane1=Airplane(color, year, passengers1, airmodel1)

airplane2=Airplane(color, year, passengers2, airmodel2)

print("                                                                                                                                                                                                                                                                                           ")
#registro de los vehiculos

print("los vehiculos que registraste fueron:")


print("Carros registrados:")
print(car1.describe())
print(car2.describe())



print("Barcos registrados:")
print(ship1.describe())
print(ship2.describe())


print("Aviones registrados:")
print(airplane1.describe())
print(airplane2.describe())