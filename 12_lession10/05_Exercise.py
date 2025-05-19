# Write a class Train which has methods to book a ticket,get status(no of seats) and get fare info. of train running under indian railways.

class Train:
    ticketFare = 325
    noOfSeats = 100
    travelRoute = "Neral to Matheran"     

    def bookTicket(self, noOfTicket):
        if noOfTicket <= self.noOfSeats: 
            self.noOfSeats -= noOfTicket  # Update available seats
            print(f"The Number of Train Tickets you have booked is: {noOfTicket}\n")
        else:
            print(f"Only {self.noOfSeats} seats are available. You requested {noOfTicket}.\n")
    
    def getStatus(self):
        print(f"Currently the train has -> {self.noOfSeats} <- seats left! BOOK NOW :)\n")

    def trainInfo(self):
        print(f"The train ticket fare is -> ₹{self.ticketFare} <- and the route is: {self.travelRoute}")

customer1 = Train()

# Book Ticket
bookTicket = int(input("How many train tickets do you want to book?"))
customer1.bookTicket(bookTicket)

# Seat Status Check
seatStatus = input("Do you want to check the seat status?\nType 'YES' = ")
if seatStatus.strip().lower() == "yes": 
    customer1.getStatus()

# Train Info Check
trainInfo = input("Do you want to check the train route and fare?\nType 'YES' = ")
if trainInfo.strip().lower() == "yes": 
    customer1.trainInfo()

        
        