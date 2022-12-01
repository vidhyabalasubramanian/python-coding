# Defining the class passenger details
#Method 1

class Passengerdata:

    Location = "Chennai"
    State = "Tamil Nadu"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def passengeridproof(self, idproof):
        print(idproof)

def main():

    passesnger1 = Passengerdata("Ragul", 25)

    print(passesnger1.name)
    print(passesnger1.age)
    print(passesnger1.Location)
    print(passesnger1.State)

    passesnger1.passengeridproof(1234)

if __name__ == "__main__":
    main()

#Method 2

#Defining the class passenger details

class Passengerdata:

    
    def __init__(self, name, age, idproof):
        self.name = name
        self.age = age
        self.idproof = idproof
    
def main():

    passenger1 = Passengerdata("Ragul", 25, 5674)
    passenger2 = Passengerdata("Vikram", 34, 8765)
    passenger3 = Passengerdata("Aarumugam", 65, 6579)
	

    print(passenger1.name)
    print(passenger1.age)
    print(passenger1.idproof)
   
    print(passenger2.name)
    print(passenger2.age)
    print(passenger2.idproof)
   
	
    print(passenger3.name)
    print(passenger3.age)
    print(passenger3.idproof)
   
if __name__ == "__main__":
    main()

