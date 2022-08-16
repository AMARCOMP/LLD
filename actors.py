from constants import *
from utilObjects import *
from parkingSpots import *
from datetime import *

classHandler = {
    ParkingSpotType.COMPACT   : compactPS,
    ParkingSpotType.LARGE     : largePS,
    ParkingSpotType.MOTORBIKE : bikePS
}

class Customer:
    def __init__(self, address, person, custid, parkingSpot, license = None) -> None:
        self.__address = address
        self.__person = person
        self.__spotId = None
        self.__custId = custid
        self.__license = license
        self.__ticketId = None
        self.__parkingSpot = parkingSpot
        print('Customer profile created with Customer ID --> {0}'.format(custid))

    def getVehicleTypeSpotObj(self,vehicleType):
        if vehicleType == ParkingSpotType.COMPACT:
            return self.__parkingSpot.getCompactPSObj()
        elif vehicleType == ParkingSpotType.LARGE:
            return self.__parkingSpot.getLargePSObj()
        elif vehicleType == ParkingSpotType.MOTORBIKE:
            return self.__parkingSpot.getBikePSObj()

    def getLicense(self):
        return self.__license

    def getCustId(self):
        return self.__custId

    def checkAvailability(self,vehicleType):
        try:
            if self.getVehicleTypeSpotObj(vehicleType).isSpotAvailable():
                return True
            else:
                return False
        except:
            print('Vechile type not supported in this Parking Lot.')
        
    def setSpotId(self, spot):
        self.__spotId = spot

    def getSpot(self):
        return self.__spotId

    def setTicket(self,ticket):
        self.__ticketId = ticket

    def getTicket(self,vehicleType,license = None):
        if not license:
            license = self.getLicense() 
        if self.checkAvailability(vehicleType):
            vehicle = Vehicle(license,vehicleType)
            spot    = self.getVehicleTypeSpotObj(vehicleType).assignSpot(vehicle)
            ticket  = Ticket(self.getCustId(),vehicle,spot)
            self.setSpotId(spot)
            self.setTicket(ticket)
            print('Ticket created successfully for vehicle {0}'.format(vehicleType))
        else:
            print('All spots for this vehicle type FULL.')
    
    def getFare(self):
        startTime = self.__ticketId.getEntryTime()
        now = datetime.now()
        duration = now - startTime
        duration_in_s = duration.total_seconds()
        hours = divmod(duration_in_s, 3600)[0]
        if duration_in_s%3600 != 0:
            hours+=1
        rate = 100*hours
        return rate

    def returnTicket(self,vehicleType):
        self.getVehicleTypeSpotObj(vehicleType).freeSpot(self.getSpot())
        amount = self.getFare()
        print('Please pay {0}'.format(amount))

add1= Address('street1','Bangalore','Karnataka','43242334','India')
p1=Person('Amar',add1,'amar@gmail.com','7967986687786')
ps = ParkingLot(add1)
c1=Customer(add1,p1,'cust1234',ps,'license1234')
v1=ParkingSpotType.COMPACT
c1.getTicket(v1)
c1.getTicket(v1)
c1.returnTicket(v1)
c1.getTicket(v1)
