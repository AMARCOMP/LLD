from datetime import *

class Ticket:
    def __init__(self,custid,vehicle,spot) -> None:
        self.__entry = datetime.now()
        self.__custtomerID = custid
        self.__vehicle = vehicle
        self.__spotId  = spot

    def setCustId(self,custid):
        self.__custtomerID = custid

    def getCustId(self):
        return self.__custtomerID

    def getEntryTime(self):
        return self.__entry

class Vehicle:
    def __init__(self,licence,type) -> None:
        self.__licence = licence
        self.__type = type

    def getLicence(self):
        return self.__licence
    
    def getType(self):
        return self.__type
