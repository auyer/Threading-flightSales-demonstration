from threading import RLock, Thread
from time import sleep

from travelAgencies.company import Company


class Agency(object):
    def __init__(self, companies: [Company], varName:str ):
        global agLock
        agLock = RLock()
        agLock.acquire()
        self.name = varName
        self.companyList = companies
        self.avSeats = []
        self.initData()
        agLock.release()

    def update(self):
        try:
            global agLock
            agLock.acquire()
            #print('Starting update ' + self.name)
            self.avSeats.clear()
            for comp in self.companyList:
                companySeats = comp.getAvailableSeats()
                for seat in companySeats:
                    self.avSeats.append((comp , seat.number , comp.getCurrentPrice()))
            #print('-Update'+'\a') # Sound ALert
            agLock.release()
        except:
            print('Exeption Caught in Update ' + self.name)
            agLock.release()

    def autoUpdate(self):
        while(True):
            sleep(5)
            if not (self.update()):
                sleep(0.1)
                self.update()

    def initData(self):
        self.avSeats.clear()
        for comp in self.companyList:
            for seat in comp.seats:
                self.avSeats.append((comp, seat.number, comp.getCurrentPrice()))

    def getList(self):
        global agLock
        agLock.acquire()
        seatList = self.avSeats
        agLock.release()
        return seatList

    def run(self):
        print('Starting run ' + self.name)
        Thread(target= self.autoUpdate).start()

        return True

    def sellToCLient(self, comp: Company, seat: int):
        #print('\nTrying to sell')
        #global agLock
        #agLock.acquire()
        #print('\nSelling')
        for desiredCompany , desiredSeat, v  in self.avSeats:
            if desiredCompany == comp and desiredSeat == seat:
                break
        try:
            if(desiredCompany.sellSeat(desiredSeat)):
                print('\n', self.name, ' SOLD:' ,  desiredCompany, 'seat', desiredSeat)
        #        agLock.release()
                self.update()
                return True
            else:
                print('\n', self.name,' Failed to sell:',  desiredCompany,'seat', desiredSeat, ' (Sold Already)')
       #         agLock.release()
                return False
        except:
            print('Exeption Caught in sellToClient ' + self.name)
        #    agLock.release()
            return False