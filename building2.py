class Building():
    # constructor: called when an object is instantiated
    def __init__(self,name,totalRooms,occupiedRooms,securityGuards):
        self.name=name
        self.totalRooms=totalRooms
        self.occupiedRooms=occupiedRooms
        self.securityGuards=securityGuards

    def computeVaccant(self):
        self.vaccantRooms=self.totalRooms-self.occupiedRooms
        return self.vaccantRooms

    def bookRooms(self,numberToBook):
        self.occupiedRooms=self.occupiedRooms+numberToBook
        self.vaccantRooms-=numberToBook

        return f"Number of occupied rooms is {self.occupiedRooms} and vaccant rooms is {self.vaccantRooms}"




hazinaTowers=Building("hazina towers",150,50,20)
print(hazinaTowers.name)
print(hazinaTowers.totalRooms)
print(hazinaTowers.occupiedRooms)
print(hazinaTowers.securityGuards)

hazinaTowers.computeVaccant()
print(hazinaTowers.vaccantRooms)

print(hazinaTowers.bookRooms(4))


# print(hazinaTowers.computeVaccant())



