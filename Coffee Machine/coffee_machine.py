BUY = 'buy'
FILL = 'fill'
TAKE = 'take'

water = 400
milk = 540
beans = 120
cups = 9
money = 550


def coffee_machine():
    machine_status()
    action = input('\nWrite action (buy, fill, take): ')
    if action == BUY:
        buy()
    elif action == FILL:
        fill()
    elif action == TAKE:
        take()


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
    coffee_choice = int(input(
        'What do you want to buy? '
        '1 - espresso, 2 - latte, 3 - cappuccino: '))
    if coffee_choice == 1:
        make_espresso()
    elif coffee_choice == 2:
        make_latte()
    elif coffee_choice == 3:
        make_cappuccino()


# allows a special worker to fill out all the supplies for the coffee machine
def fill():
    global water, milk, beans, cups
    water += int(input(
        'Write how many ml of water do you want to add: '))
    milk += int(input(
        'Write how many ml of milk do you want to add: '))
    beans += int(input(
        'Write how many grams of coffee beans do you want to add: '))
    cups += int(input(
        'Write how many disposable cups of coffee do you want to add: '))
    machine_status()


# allows a special worker to take out all of the money from the coffee machine
def take():
    global money
    print(f'I gave you ${money}')
    money = 0
    machine_status()


def make_espresso():
    global water, beans, cups, money
    water -= 250
    beans -= 16
    cups -= 1
    money += 4
    machine_status()


def make_latte():
    global water, milk, beans, cups, money
    water -= 350
    milk -= 75
    beans -= 20
    cups -= 1
    money += 7
    machine_status()


def make_cappuccino():
    global water, milk, beans, cups, money
    water -= 200
    milk -= 100
    beans -= 12
    cups -= 1
    money += 6
    machine_status()


coffee_machine()
