import company as cp
import threading
from time import sleep

class Agency(object):

    def __init__(self, companies: [cp.Company], varName:str ):
        global lock
        lock = threading.Lock()
        self.name = varName
        self.companyList = companies
        self.avSeats = []
        self.initData()

    def update(self):
        while(True):
            try:
                global lock
                #print('Starting update ' + self.name)
                lock.acquire()
                self.avSeats.clear()
                for comp in self.companyList:
                    for seat in comp.seats:
                        self.avSeats.append((comp , comp.seats.index(seat) , comp.getCurrentPrice()))
                lock.release()
                #print('lock release')
                sleep(2)
            except:
                sleep(5)
gi
    def initData(self):
        self.avSeats.clear()
        for comp in self.companyList:
            for seat in comp.seats:
                self.avSeats.append((comp.name , comp.seats.index(seat) , comp.getCurrentPrice()))

    def getList(self):
        global lock
        lock.acquire()
        seatList = self.avSeats
        lock.release()
        return seatList

    def run(self):
        print('Starting run ' + self.name)
        tr = threading.Thread(target= self.update)
        tr.start()
        return True

    def sellToCLient(self, comp: cp.Company, seat: int):
        print('\nTrying to sell')
        global lock
        lock.acquire()
        print('\nSelling')
        for c , s in self.avSeats:
            if c == comp & s == seat:
                yield c, s
                break
        try:
            lock.release()
            print('\nSOLD')
            return comp.sellSeat(s)
        except:
            print('\n Failed to sell')
            lock.release()
            return False