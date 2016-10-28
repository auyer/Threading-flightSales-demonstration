from random import randrange
from threading import Lock

class Company(object):
    def __init__(self, varName: str):
        global cpLock
        cpLock = Lock()
        cpLock.acquire()
        self.name = varName
        self.baseSeatAmt = 5
        self.amtAvaiableSeats = 5
        self.seats = [False] * self.baseSeatAmt
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

    def getAvaiableSeats(self):
        global cpLock
        cpLock.acquire()
        #print('cpLock aquired in ' + self.name)
        list = []
        if not self.amtAvaiableSeats == 0:
            for seat in self.seats:
                if seat == False:
                    list.append(self.seats.index(seat))
            cpLock.release()
            return list
        else:
            cpLock.release()
            return list

    def sellSeat(self, seatNum):
        global cpLock
        cpLock.acquire()
        if self.seats[seatNum] == True:
            cpLock.release()
            return False
        else:
            self.seats[seatNum] = True
            self.amtAvaiableSeats -=  1
            cpLock.release()
            return True

    def manager(self):
        global cpLock
        cpLock.acquire()
        if  not self.amtAvaiableSeats  == self.baseSeatAmt:
            for i in range(self.amtAvaiableSeats):
                self.currentPrice += self.currentPrice * 0.1
        cpLock.release()