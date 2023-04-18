class Train:
    def __init__(self,name,fare,seats) :
        self.name = name
        self.fare = fare
        self.seats = seats

    def info(self):
        print(f"The name of the train is {self.name}")
        print(f"The fare per seat is Rs: {self.fare}")
        print(f"The seats in {self.name} is {self.seats}")


    def ticketBook(self):
        if self.seats > 0:
            print(f"Your ticket has been booked successfully.\nYour seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry! All the seats are full.\nPlease try again later.")
    
    def available_seats(self):
        print(f"The total seats available is {self.seats}")




ahmedabad = Train("Rajdhani Exp 12050",500,3200)
ahmedabad.info()
ahmedabad.ticketBook()
ahmedabad.available_seats()
ahmedabad.ticketBook()
ahmedabad.available_seats()