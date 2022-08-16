from constants import *

class ParkingLot:
    def __init__(self,address) -> None:
        self.__address = address
        self.__compactps = compactPS()
        self.__largeps = largePS()
        self.__bikeps = bikePS()

    def getAddress(self):
        return self.__address

    def getCompactPSObj(self):
        return self.__compactps
    
    def getLargePSObj(self):
        return self.__largeps
    
    def getBikePSObj(self):
        return self.__bikeps

class parkngSpots:
    def __init__(self) -> None:
        pass

class compactPS(parkngSpots):
    def __init__(self) -> None:
        super().__init__()
        self.__floor = 2
        self.__maxVehicles = maxCompactSpots
        self.__avlSpots = [i for i in range(1,self.__maxVehicles+1)]
        print('Parking spots created with max capacity --> {0}'.format(self.__maxVehicles))
    
    def assignSpot(self, vehicle):
        spot = self.__avlSpots[0]
        self.__avlSpots = self.__avlSpots[1:]
        return spot

    def isSpotAvailable(self):
        if len(self.__avlSpots) > 0:
            return True
        return False

    def freeSpot(self,spot):
        self.__avlSpots.append(spot)

class largePS(parkngSpots):
    def __init__(self) -> None:
        super().__init__()
        self.__floor = 1
        self.__maxVehicles = maxLargeSpots
        self.__avlSpots = [i for i in range(1,self.__maxVehicles)]
        print('Parking spots created with max capacity --> {0}'.format(self.__maxVehicles))

    def assignSpot(self, vehicle):
        spot = self.__avlSpots[0]
        self.__avlSpots = self.__avlSpots[1:]
        return spot

    def isSpotAvailable(self):
        if len(self.__avlSpots) > 0:
            return True
        return False

    def freeSpot(self,spot):
        self.__avlSpots.append(spot)

class bikePS(parkngSpots):
    def __init__(self) -> None:
        super().__init__()
        self.__floor = 3
        self.__maxVehicles = maxBikeSpots
        self.__avlSpots = [i for i in range(1,self.__maxVehicles)]
        print('Parking spots created with max capacity --> {0}'.format(self.__maxVehicles))

    def assignSpot(self, vehicle):
        spot = self.__avlSpots[0]
        self.__avlSpots = self.__avlSpots[1:]
        return spot

    def isSpotAvailable(self):
        if len(self.__avlSpots) > 0:
            return True
        return False

    def freeSpot(self,spot):
        self.__avlSpots.append(spot)