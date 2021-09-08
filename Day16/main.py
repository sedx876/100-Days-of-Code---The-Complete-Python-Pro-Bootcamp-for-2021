#Object Oriented Programming
#Class- A blueprint
#Object- an instance of a class

from turtle import Turtle, Screen
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on= True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)


