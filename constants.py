from enum import Enum
from turtle import st


class ParkingSpotType(Enum):
    COMPACT, LARGE, MOTORBIKE, ELECTRIC = 1, 2, 3, 4

class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6

class ParkingTicketStatus(Enum):
    ACTIVE, PAID, LOST = 1, 2, 3

class Address:
    def __init__(self,street,city,state,zipcode,country):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode
        self.__country = country
        print('Address object created successfully.')

class Person:
    def __init__(self,name,address,email,phone) -> None:
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        print('Person object created successfully.')


maxCompactSpots = 1
maxLargeSpots   = 25
maxBikeSpots    = 100

