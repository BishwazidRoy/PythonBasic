class BikeShop:
    def __init__(self,stock):
        self.stock=stock

    def displayBike(self):
        print("Total Bike :--- ", self.stock)

    def rentForBike(self,q):
        if q<=0:
            print("Please Enter the value more then Zero")
        elif q>self.stock:
            print("Please Enter the value less then stock")
        else:
            self.stock=self.stock-q
            print("Your Total Price is:-- ", q*100)
            print("Now available Bike:--", self.stock)

while True:
    obj=BikeShop(100)
    uc=int(input('''
         1 Display Stocks
         2 Rent Bike
         3 Exit
    '''))
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("Enter The Questity:--"))
        obj.rentForBike(n)
    else:
        break
