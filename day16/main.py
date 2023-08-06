from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Print Report(s)
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

# Loop while coffee machine is operational 
is_operational = True
while is_operational:

    # Get the menu items
    menu_items = menu.get_items()
    print(menu_items)

    choice = input(f"What would you like? ({menu_items}off/report)")

    if "off" == choice:
        is_operational = False
    elif "report" == choice:
        coffee_maker.report()
        money_machine.report()
    else:

        # Get the requested item
        menu_item = menu.find_drink(choice)

        # Check to see if coffee maker can make it
        if coffee_maker.is_resource_sufficient(menu_item):

            coffee_maker.make_coffee(menu_item)
            print(f"That will be: ${menu_item.cost}")
            money_machine.make_payment(menu_item.cost)
        
        else:
            print (f"Insufficient resources to make a {menu_item.name}")
        
