# main.py

from vehiclePackage.vehichleClass  import *

if __name__ == "__main__":
    #Instantiate an object if type vehicle
    myCorvette = Vehicle("car", 120, "black", "NA") # Trigger a call to constructor
    myCorvette.printType() #Invoke the method on the object 
    
    # Invoke the getter for maximum speed, store the return value in a variable
    # print that out
    
    Max_Speed = myCorvette.getSpeed()
    print("Maximum Speed: ")
    
    # instantiate another vehicle object 
    myMazda3 = Vehicle("Car", 100, "Black","Seven")
    myBoat = Vehicle("Boat", 45, "White", "S.S. Laughlin")
    mySpaceShip = Vehicle("Spaceship", 10000, "Blue", "Apollo 100")
    myMazda3.printType()
    myBoat.printType()
    mySpaceShip.printType()