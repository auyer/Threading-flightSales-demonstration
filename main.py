from threading import RLock, Thread
from time import sleep

from agency import Agency
from clients import Client
from company import Company

if __name__ == "__main__":

    lock = RLock()
    lock.acquire()
    lock.release()

    threadList = []

    clientList = []
    companyList = []
    agencyList = []

    #Flight Companies

    latam = Company('LATAM')
    ryanair = Company('Ryanair')
    airFrance = Company('AirFrance')
    panAm = Company('PanAm')

    companyList = [latam,ryanair,airFrance,panAm]

    #Travel Agencies
    decolar = Agency(companyList,'Decolar.Com')
    skyScanner = Agency(companyList, 'Sky Scanner')

    agencyList = [decolar,skyScanner]

    for agency in agencyList:
        agency.run()

    sleep(2)

    # Creating Clients
    for i in range(10):
        clientList.append( Client(agencyList))
        threadList.append(Thread(target=clientList[i].run).start())