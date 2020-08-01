BUY = 'buy'
FILL = 'fill'
TAKE = 'take'
EXIT = 'exit'
REMAINING = 'remaining'

water = 400
milk = 540
beans = 120
cups = 9
money = 550


def coffee_machine():
    while True:
        action = input('\nWrite action (buy, fill, take, remaining, exit): ')
        if action == BUY:
            buy()
        elif action == FILL:
            fill()
        elif action == TAKE:
            take()
        elif action == REMAINING:
            machine_status()
        elif action == EXIT:
            break


# prints current resources of the coffee machine
def machine_status():
    print(f'\nThe coffee machine has'
          f'\n{water} of water'
          f'\n{milk} of milk'
          f'\n{beans} of coffee beans'
          f'\n{cups} of disposable cups'
          f'\n{money} of money')


# allows the user to buy one of three types of coffee
def buy():
    coffee_choice = input(
        '\nWhat do you want to buy? '
        '1 - espresso, 2 - latte, 3 - cappuccino, back - to min menu: ')
    if coffee_choice == '1':
        make_espresso()
    elif coffee_choice == '2':
        make_latte()
    elif coffee_choice == '3':
        make_cappuccino()
    elif coffee_choice == 'back':
        return


# allows a special worker to fill out all the supplies for the coffee machine
def fill():
    global water, milk, beans, cups
    water += int(input(
        '\nWrite how many ml of water do you want to add: '))
    milk += int(input(
        'Write how many ml of milk do you want to add: '))
    beans += int(input(
        'Write how many grams of coffee beans do you want to add: '))
    cups += int(input(
        'Write how many disposable cups of coffee do you want to add: '))


# allows a special worker to take out all of the money from the coffee machine
def take():
    global money
    print(f'\nI gave you ${money}')
    money = 0


# checks whether there are enough resources for making a coffee
# if there are, then makes the desired coffee
def make_coffee(needed_water, needed_milk, needed_beans, price):
    global water, milk, beans, cups, money
    if water < needed_water:
        print('Sorry, not enough water')
    elif milk < needed_milk:
        print('Sorry, not enough milk')
    elif beans < needed_beans:
        print('Sorry, not enough coffee beans')
    elif cups < 1:
        print('Sorry, not enough disposable cups')
    else:
        water -= needed_water
        milk -= needed_milk
        beans -= needed_beans
        cups -= 1
        money += price
        print('I have enough resources, making you a coffee!')


def make_espresso():
    make_coffee(needed_water=250, needed_milk=0, needed_beans=16, price=4)


def make_latte():
    make_coffee(needed_water=350, needed_milk=75, needed_beans=20, price=7)


def make_cappuccino():
    make_coffee(needed_water=200, needed_milk=100, needed_beans=12, price=6)


coffee_machine()
