from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from staff import Staff

coffee_machine = CoffeeMaker()
menu_items = Menu()
money_machine = MoneyMachine()
staff = Staff()

is_on = True

while is_on:
    # TODO: 1. Prompt user to make a selection
    user_choice = input(f"What would you like? ({menu_items.get_items()}): ").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == staff.employer or user_choice == staff.employee:
        staff.refil_resources(coffee_machine)
        print("Would you like to end the machine?")
        answer = input("yes or no?: ")
        if answer == "yes":
            is_on = False
            if user_choice == staff.employer:
                print(f"Currently the profit is: ${money_machine.profit}")
    else:
        # TODO: 2. Find the cost of the item
        item = menu_items.find_drink(user_choice)
        # TODO: 3.Enough resources?
        can_make_coffee = coffee_machine.is_resource_sufficient(item)
        if can_make_coffee:
            # TODO: 3. Process, calculate the coins receieved and return change!
            successful_payment = money_machine.make_payment(item.cost)
            if successful_payment:
                coffee_machine.make_coffee(item)