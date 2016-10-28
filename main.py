import company as cp
import agency as ag
from clients import Client
#import clients as cl
import threading as th
from time import sleep

if __name__ == "__main__":

    lock = th.Lock()
    lock.acquire()
    lock.release()

    threadList = []

    clientList = []
    companyList = []
    agencyList = []

    #Flight Companies

    latam = cp.Company('LATAM')
    ryanair = cp.Company('Ryanair')
    airFrance = cp.Company('AirFrance')
    panAm = cp.Company('PanAm')

    companyList = [latam,ryanair,airFrance,panAm]

    #Travel Agencies
    decolar = ag.Agency(companyList,'Decolar.Com')
    skyScanner = ag.Agency(companyList, 'Sky Scanner')

    agencyList = [decolar,skyScanner]

    for agency in agencyList:
        agency.run()

    sleep(2)

    # Creating Clients
    for i in range(10):
        clientList.append( Client(agencyList))
        threadList.append(th.Thread(target=clientList[i].run).start())