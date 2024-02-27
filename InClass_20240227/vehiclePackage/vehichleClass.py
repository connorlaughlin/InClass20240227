# vehicleClass.py

class Vehicle:
    '''
    Vehicle Class
    This class models a vehicle on a used car lot
    Order: Some developers need to use the constructor without having to provide a max speed
    '''
    # Constructor. It's called when... we instantiate an object of vehicle type
    def __init__(self, type, max_speed, color, nickname):
        self.type = type;
        self.max_speed = max_speed
        self.color = color
        self.nickname = nickname
        '''
        @param type: the type of vehicle
        '''
    def printType(self):
        print(self.type);
        
    def getSpeed(self):  # getter
        return self.max_speed
    def getColor(self):
        return self.color
    def getNickname(self):
        return self.nickname

        
if __name__ == "__main__":
    # Some code to test the class would go here.
    # If there's no code, just pass
    pass    

