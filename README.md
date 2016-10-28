# TravelAgencies: a threading and Mutex Demo for Education with Python 3

An educational Python demonstration of threading and Mutex usage in a ticket selling model.

#### Read the problem below and [Click Here](GUIDE.md) to read the [GUIDE.md](GUIDE.md) explaining all the concepts behind this system (Under Construction)

#The problem

This system simulates sales of Airplane Tickets. In this simulation, there are:
- 4 companies that fly the same route, with the same plane and the same amount of seats.
- 2 Flight Agencies that sell the tickets to the clients
- a certain amount of clients

### Flight Company
Each flight company has:
- 5 seats per plane
- a total per flight cost of 1000.00 'coins'  
- a crazy manager that increases the price of the ticket in 10% incerements for each ticket sold.
- the company has to make sure not to sell the same ticket to two different agencies

### Travel Agency
Each agency has to:
- show to the client every seat available to buy. Info: price, company and number
- make sure not to sell the same ticket to two different clients

### Client
Every client follow these rules:
- He will buy only one ticket
- He will always buy the cheapest flight available. 


#The Model ( ER and UML )
(the ER also presents some unimplemented features described below ["Next Features"](https://github.com/auyer/TravelAgencies___a_threading-Mutex_Demonstration#next-features-) ) 

![ModelScreenShot](https://github.com/auyer/Threading-flightSales-demonstration/blob/master/models.draw_io/ModelScreenShot.png?raw=true "Model ScreenShot")

# Next Features :
- Make the program simulate real time.

##Companies

- Every week, tickets will be restored 
- Companies will make sales if the minimumRevenue hasn't been reached, and the week will end in two days. (Price will aim at reaching the minimumRevenue)
- Companies that had a Loss in the past week will make sales aiming to cover the loss.
- After Hitting the minimum revenue, companies will increase the price.

##Clients

- Create 3 types of clients: High, Mid and Low. The high class will buy whenever they decide to. The Mid will wait for the sales in the end of the week, but if they can't find any, they will travel anyways on the next week. The Low will only buy in the Sales.
- Clients that traveled this week won't travel in the next one. 
