import company as cp
from threading import Lock, Thread
from time import sleep

class Agency(object):

    def __init__(self, companies: [cp.Company], varName:str ):
        global agLock
        agLock = Lock()
        agLock.acquire()
        self.name = varName
        self.companyList = companies
        self.avSeats = []
        self.initData()
        agLock.release()

    def update(self):
        while(True):
            try:
                global agLock
                agLock.acquire()
                #print('Starting update ' + self.name)
                self.avSeats.clear()
                print(self.name + ' updating')
                for comp in self.companyList:
                    companySeats = comp.getAvaiableSeats()
                    for seat in companySeats:
                        self.avSeats.append((comp , companySeats.index(seat) , comp.getCurrentPrice()))
                agLock.release()
                sleep(2)
            except:
                print('Exeption Caught in Update' + self.name)
                agLock.release()
                sleep(5)

    def initData(self):
        self.avSeats.clear()
        for comp in self.companyList:
            for seat in comp.seats:
                self.avSeats.append((comp, comp.seats.index(seat), comp.getCurrentPrice()))

    def getList(self):
        global agLock
        agLock.acquire()
        seatList = self.avSeats
        agLock.release()
        return seatList

    def run(self):
        print('Starting run ' + self.name)
        tr = Thread(target= self.update)
        tr.start()
        return True

    def sellToCLient(self, comp: cp.Company, seat: int):
        print('\nTrying to sell')
        global agLock
        agLock.acquire()
        print('\nSelling')
        for c , s in self.avSeats:
            if c == comp & s == seat:
                yield c, s
                break
        try:
            agLock.release()
            print('\nSOLD')
            return comp.sellSeat(s)
        except:
            print('\n Failed to sell')
            agLock.release()
            return False