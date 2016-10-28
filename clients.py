import agency


class Client:
    def buy(self, ag : agency.Agency):
        seatSearch = ag.getList()
        choice = seatSearch[seatSearch.index(min(seatSearch, key=lambda t: t[2]))]
        print(choice, '  ', choice[0], '  ', choice[1])
        ag.sellToCLient(choice[0], choice[1])
