import company as cp
import agency as ag
import clients as cl
import threading as th
from time import sleep

if __name__ == "__main__":

    lock = th.Lock()

    lock.acquire()

    lock.release()

    threadList = []

    #Companhias Aéreas
    a = cp.Company('a')
    b = cp.Company('b')
    c = cp.Company('c')
    d = cp.Company('d')

    #Agências de viagem
    decolar = ag.Agency([a,b,c,d],'decolar')
    busao = ag.Agency([a,b,c,d], 'busao')



    print('Prebus')
    busao.run()
    print('predecolar')
    decolar.run()


    sleep(10)
    '''
    print('cliente busao')
    for seat in busao.getList():
        print(seat[2])
    '''

    print('Cliente decolar')
    c1 = cl.Client()
    c1.buy(decolar)
'''
    #Criado Clientes
    for i in range (5):
        t = th.Thread(target=clientRich, args=None)
        t.start()
        threadList.append(t)

    for i in range (25):
        th.Thread(target=clientRich, args=None)

    for i in range (70):
        th.Thread(target=clientRich, args=None)





def clientRich():
    x = 1#bla

'''