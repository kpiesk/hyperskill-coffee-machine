class CoffeeMachine:
    BUY = 'buy'
    FILL = 'fill'
    TAKE = 'take'
    EXIT = 'exit'
    REMAINING = 'remaining'
    BACK = 'back'

    ESPRESSO_CHOICE = '1'
    LATTE_CHOICE = '2'
    CAPPUCCINO_CHOICE = '3'

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = 'standby'

    def main(self):
        while True:
            self.state = input('\nWrite action (buy, fill, take, remaining, exit): ')
            if self.state == self.BUY:
                self.buy()
            elif self.state == self.FILL:
                self.fill()
            elif self.state == self.TAKE:
                self.take()
            elif self.state == self.REMAINING:
                self.machine_status()
            elif self.state == self.EXIT:
                break

    # prints current resources of the coffee machine
    def machine_status(self):
        print(f'\nThe coffee machine has'
              f'\n{self.water} of water'
              f'\n{self.milk} of milk'
              f'\n{self.beans} of coffee beans'
              f'\n{self.cups} of disposable cups'
              f'\n{self.money} of money')

    # allows the user to buy one of three types of coffee
    def buy(self):
        coffee_choice = input(
            '\nWhat do you want to buy? '
            '1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
        if coffee_choice == self.ESPRESSO_CHOICE:
            self.make_espresso()
        elif coffee_choice == self.LATTE_CHOICE:
            self.make_latte()
        elif coffee_choice == self.CAPPUCCINO_CHOICE:
            self.make_cappuccino()
        elif coffee_choice == self.BACK:
            return

    # allows a special worker to fill out all the supplies
    # for the coffee machine
    def fill(self):
        self.water += int(input(
            '\nWrite how many ml of water do you want to add: '))
        self.milk += int(input(
            'Write how many ml of milk do you want to add: '))
        self.beans += int(input(
            'Write how many grams of coffee beans do you want to add: '))
        self.cups += int(input(
            'Write how many disposable cups of coffee do you want to add: '))

    # allows a special worker to take out all of the money
    # from the coffee machine
    def take(self):
        print(f'\nI gave you ${self.money}')
        self.money = 0

    # checks whether there are enough resources for making a coffee
    # if there are, then makes the desired coffee
    def make_coffee(self, needed_water, needed_milk, needed_beans, price):
        if self.water < needed_water:
            print('Sorry, not enough water')
        elif self.milk < needed_milk:
            print('Sorry, not enough milk')
        elif self.beans < needed_beans:
            print('Sorry, not enough coffee beans')
        elif self.cups < 1:
            print('Sorry, not enough disposable cups')
        else:
            self.water -= needed_water
            self.milk -= needed_milk
            self.beans -= needed_beans
            self.cups -= 1
            self.money += price
            print('I have enough resources, making you a coffee!')

    def make_espresso(self):
        self.make_coffee(needed_water=250, needed_milk=0, needed_beans=16, price=4)

    def make_latte(self):
        self.make_coffee(needed_water=350, needed_milk=75, needed_beans=20, price=7)

    def make_cappuccino(self):
        self.make_coffee(needed_water=200, needed_milk=100, needed_beans=12, price=6)


coffee_machine = CoffeeMachine()
coffee_machine.main()
