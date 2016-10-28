from random import randrange

class Company(object):
    def __init__(self, varName: str):
        self.name = varName
        self.sAmt = 5
        self.amtAvaiableSeats = 5
        self.seats = [False] * self.sAmt
        self.dispenses = 1000.00
        self.basePrice = 250
        self.currentPrice = self.basePrice + randrange(0,50,2)
        self.currentRevenue = 0
        self.minimumRevenue = self.dispenses + self.dispenses*0.5

    def __str__(self):
        return self.name

    def getCurrentPrice(self):
        return self.currentPrice

    def getAvaiableSeats(self):
        if not self.amtAvaiableSeats == 0:
            list = []
            for sNum, seat in enumerate(self.seats):
                if seat == True:
                    list.append(sNum)
            return list
        else:
            return False

    def sellSeat(self, seatNum):
        if self.seats[seatNum] == True:
            return False
        else:
            self.seats[seatNum] = True
            self.amtAvaiableSeats -=  1
            return True

    def manager(self):
        if  not self.amtAvaiableSeats  == self.sAmt:
            for i in range(self.amtAvaiableSeats):
                self.currentPrice += self.currentPrice * 0.1