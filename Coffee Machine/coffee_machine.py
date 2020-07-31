water = 200  # in ml
milk = 50  # in ml
coffee_beans = 15  # in g

cups = int(input('Write how many cups of coffee you will need: '))
needed_water = cups * water
needed_milk = cups * milk
needed_coffee_beans = cups * coffee_beans
print(f'For {cups} cups of coffee you wil need:'
      f'\n{needed_water} ml of water'
      f'\n{needed_milk} ml of milk'
      f'\n{needed_coffee_beans} g of coffee beans')
