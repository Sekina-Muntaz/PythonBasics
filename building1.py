# Use class keyword
# classname starts in Uppercase
# namespace is a list of variable identifiers
# you define with a block of code eg within a class
class Building():
    rooms=6
    doors=8
    # lawn=True
    # windows=10
    # garage=True
    # swimmingPool=False
    # def openDoors(doorNumber):
    #     print(f"door number {doorNumber} opened")
    # defining methods of a class we use functions
    # self refers to the object calling the methhod ie you can access the object attributes
    def openBuilding(self):
        print(f"{self.name} is now open")
    def closeBuildinf(self):
        print(f"{self.name} is now closed")
    def computeVaccant(self):
        print(self.rooms-self.occupiedRooms,"are vaccant")




# constructor is a special method used to initialize your object
cornerHouse=Building()
cornerHouse.rooms=100
cornerHouse.name="Corner House"
cornerHouse.occupiedRooms=42
cornerHouse.computeVaccant()
cornerHouse.openBuilding()
cornerHouse.closeBuildinf()
print(cornerHouse.rooms)
# print(cornerHouse.vaccantRooms)
print(cornerHouse.name)
# print(cornerHouse.basement)

kimathiHouse=Building()
kimathiHouse.name="Kimathi House"
kimathiHouse.rooms=150
print(kimathiHouse.rooms)
kimathiHouse.occupiedRooms=60
kimathiHouse.vaccantRooms=90
# instance attributes are associated only with the object eg basement
kimathiHouse.basement=True
kimathiHouse.openBuilding()
kimathiHouse.closeBuildinf()

print(kimathiHouse.basement)
print(kimathiHouse.name)



# local and global variable, non local variable


