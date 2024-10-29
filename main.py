from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

will_continue = True
menu = Menu()
name = menu.get_items()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

while will_continue:
    try:
        choice = input(f'{name}\n\nWhat would you like: ').lower()

        if choice == 'off':
            will_continue = False
        elif choice == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)

            if drink is None:
                print("\n🔎Sorry, that item is not on the menu.🔎\n\n")
                continue

            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    except ValueError as ve:
        print(f"\n💲📥💲Please insert a valid money💲📥💲\n\n")
