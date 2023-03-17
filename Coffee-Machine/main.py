#Program requirements
#Print report
#Check resources sufficient
#Process coins
#Check transaction successful
#Make Coffee
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()#calling money machine
coffee_maker = CoffeeMaker()#calling coffee maker
menu = Menu()   #so we going to creaet an object from this menu blue print. 



is_on = True#creating variable is_on


while is_on:#if coffee machine is on then
    options = menu.get_items()#we can offer the user and get that by calling that method get_items
    #get_items() is a method that is associated with an object
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()#calling report method and prints the total quantity of requirements for making coffee
        money_machine.report()#Prints the current amount of money in the machine
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

