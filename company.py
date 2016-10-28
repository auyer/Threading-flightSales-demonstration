from random import randrange
from threading import Lock
from time import sleep

class Seat(object):

    def __init__(self, index:int):
        self.number = index
        self.available = True

    def __str__(self):
        return str(self.number)

    def __int__(self):
        return self.number

class Company(object):
    def __init__(self, varName: str):
        global cpLock
        cpLock = Lock()
        cpLock.acquire()
        self.name = varName
        self.baseSeatAmt = 5
        self.amtAvailableSeats = 0
        self.seats = []
        for i in range(self.baseSeatAmt):
            self.seats.append(Seat(i))
            self.amtAvailableSeats+=1
        self.dispenses = 1000.00
        self.basePrice = 250.00
        self.currentPrice = self.basePrice + randrange(0,50,2)
        self.currentRevenue = 0
        self.minimumRevenue = self.dispenses + self.dispenses*0.5
        cpLock.release()

    def __str__(self):
        return self.name

    def getCurrentPrice(self):
        global cpLock
        cpLock.acquire()
        price = self.currentPrice
        cpLock.release()
        return price

    def getAvailableSeats(self):
        global cpLock
        cpLock.acquire()
        #print('cpLock aquired in ' + self.name)
        list = []
        if self.amtAvailableSeats > 0:
            for seat in self.seats:
                if seat.available:
                    #print(seat)
                    list.append(seat)
            cpLock.release()
            return list
        else:
            cpLock.release()
            return list

    def sellSeat(self, seatNum):
        global cpLock
        cpLock.acquire()
        if self.seats[seatNum].available :
            self.seats[seatNum].available = False
            self.amtAvailableSeats -=  1
            self.priceIncrease()
            cpLock.release()
            return True
        else: #second try
            sleep(1)
            if self.seats[seatNum].available :
                self.seats[seatNum].avaiable = False
                self.amtAvailableSeats -= 1
                self.priceIncrease()
                cpLock.release()
                return True
            else:
                cpLock.release()
                return False

    def priceIncrease(self):
        self.currentPrice += self.currentPrice * 0.1

    def manager(self):
        global cpLock
        cpLock.acquire()
        if  not self.amtAvailableSeats  == self.baseSeatAmt:
            for i in range(self.amtAvailableSeats):
                self.priceIncrease()
        cpLock.release()