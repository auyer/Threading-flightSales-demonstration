from agency import Agency
from time import sleep
from random import randrange
from threading import currentThread

class Client(object):

    def __init__(self, knownAgencies: [Agency]):
        self.agencies = knownAgencies
        self.agencyChosen = self.agencies[randrange(0,self.agencies.__len__())]


    def run(self):
        self.buy(self.agencyChosen)


    def buy(self, ag : Agency):
        try:
            seatSearch = ag.getList()
            choice = seatSearch[seatSearch.index(min(seatSearch, key=lambda t: t[2]))]
            #print(choice, '  ', choice[0], '  ', choice[1], ' ', choice[2])
            if (ag.sellToCLient(choice[0], choice[1])):
                # Travel
                sleep(10)
                return True
            else:
                sleep(0.01)
                self.buy(ag)
        except:
            sleep(0.1)
            print('\n\nThe Client '+ str(currentThread)+ ' Could not Find any flights') # in case there are more clients than seats