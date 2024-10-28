from menu import Menu
from coffee_maker import CoffeeMarker
from money_machine import MoneyMachine

will_continue = True
menu = Menu()
name = menu.get_items()
money_machine = MoneyMachine()
coffee_marker = CoffeeMarker()

while will_continue:
    choice = input(f'{name}\n\nWhat would you like: ').lower()
    if choice == 'off':
        will_continue = False
    elif choice == 'report':
        coffee_marker.report()
        money_machine.report()
    else:

        drink = menu.find_drink(choice)
        if coffee_marker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_marker.make_coffee(drink)
