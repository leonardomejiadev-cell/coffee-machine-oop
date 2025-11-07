"""
Coffee Machine Program - OOP Version
A coffee machine simulator using Object-Oriented Programming principles.
"""

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    """Main function to run the coffee machine."""
    # Initialize objects
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    is_on = True

    print("☕ Welcome to the Coffee Machine!")

    while is_on:
        # Get available menu items
        options = menu.get_items()
        choice = input(f"\nWhat would you like? ({options}): ").lower()

        if choice == "off":
            print("Shutting down the coffee machine. Goodbye! 👋")
            is_on = False
        elif choice == "report":
            print("Coffee Machine Report")
            coffee_maker.report()
            money_machine.report()
        else:
            # Find the drink in the menu
            drink = menu.find_drink(choice)

            # Check if drink exists and process order
            if drink:
                # Check if there are enough resources
                if coffee_maker.is_resource_sufficient(drink):
                    # Process payment
                    if money_machine.make_payment(drink.cost):
                        # Make the coffee
                        coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()
