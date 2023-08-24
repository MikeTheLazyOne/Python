class coffe_machine:
    def __init__(self):
        self.water_level = 100
        self.coffe_level = 100
        self.milk_level = 100
        self.money = 0
        self.status = True
    def add_money(self, money):
        if self.status == True:
            
            for elem in range(len(money)):
                if elem == 0:
                    self.money = self.money + int(money[elem])*0.25
                elif elem == 1:
                   self.money = self.money + int(money[elem])*0.1
                elif elem == 2:
                   self.money = self.money + int(money[elem])*0.05
                elif elem == 3:
                   self.money = self.money + int(money[elem])*0.01 
        else:
            print(f"Machine status is {self.status}")
    def turn_off(self):
        self.status = False
    def add(self, what, amount):
        if what == "milk":
            self.milk_level = self.milk_level + amount
        elif(what == "water"):
            self.water_level = self.water_level + amount
        elif(what == "coffe"):
            self.coffe_level = self.coffe_level + amount
        else:
            print("Product not recognized")
    def make_coffe(self, type):
        if type == "espresso":
            if self.money >= 2.1 and self.water_level >= 50 and self.coffe_level >= 18:
                print("here is your's espresso")
                self.money -= 2.1
                self.water_level -= 50
                self.coffe_level -= 18
            else:
                print("There is not enough of one or more ingridient")
                ask = input("Do you want to see the report?Y/N")
                if ask == "Y":
                    self.report()
        elif type == "latte":
            if self.money >= 3.1 and self.water_level >= 40 and self.coffe_level >= 15 and self.milk_level >= 30:
                print("here is your's latte")
                self.money -= 3.1
                self.water_level -= 40
                self.coffe_level -= 15
                self.milk_level -= 30
            else:
                print("There is not enough of one or more ingridient")
                ask = input("Do you want to see the report?Y/N")
                if ask == "Y":
                    self.report()
        elif type == "cappuccino":
            if self.money >= 1.6 and self.water_level >= 30 and self.coffe_level >= 20 and self.milk_level >= 10:
                print("here is your's latte")
                self.money -= 1.6
                self.water_level -= 30
                self.coffe_level -= 20
                self.milk_level -= 10
            else:
                print("There is not enough of one or more ingridient")
                ask = input("Do you want to see the report?Y/N")
                if ask == "Y":
                    self.report()
    def report(self):
        print(f"the machine has {self.water_level} of water'\n{self.coffe_level} of coffe\n{self.milk_level} of milk and \n{self.money} of money")

machine = coffe_machine()

while True:
    ask = input("would you like a cup of coffe? Y/N ")
    if ask == "Y":

        
        ask_2 = input("What would you like espresso/latte/cappuccino ")
        if ask_2 == "report":
            machine.report()
        elif ask_2 == "latte":
            question = input("would you like to put 3.1$? ")
            if question == "Y":
                print("Insert amount of maney seperated by comma quoters, dimes, nicles, pennies")
                money = input()
                money = money.split(",")
                print(money)
                machine.add_money(money)
            machine.make_coffe("latte")
        elif ask_2 == "espresso":
            question = input("would you like to put 2.1$? ")
            if question == "Y":
                print("Insert amount of maney seperated by comma quoters, dimes, nicles, pennies")
                money = input()
                money.split(",")
                machine.add_money(money)
            machine.make_coffe("espresso")
        elif ask_2 == "cappucciono":
            question = input("would you like to put 1.8$? ")
            if question == "Y":
                print("Insert amount of maney seperated by comma quoters, dimes, nicles, pennies")
                money = input()
                money.split(",")
                machine.add_money(money)
            machine.make_coffe("cappucciono")
        else:
            print("Not recogized we will start over")
    else:
        ask = input("Would you like to put some ingridients?")
        if ask == "Y":
            ask_3 = input("What would you like to put")
            if ask_3 == "milk":
                amount = input("how much would you like")
                machine.add("milk", amount)
            elif ask_3 == "water":
                amount = input("how much would you like")
                machine.add("water", amount)
            elif ask_3 == "coffe":
                amount = input("how much would you like")
                machine.add("coffe", amount)
        else:
            quit()