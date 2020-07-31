water = 200  # in ml
milk = 50  # in ml
beans = 15  # in g

available_water = int(input(
      'Write how many ml of water the coffee machine has: '))
available_milk = int(input(
      'Write how many ml of milk the coffee machine has: '))
available_beans = int(input(
      'Write how many grams of coffee beans the coffee machine has: '))
cups = int(input('Write how many cups of coffee you will need: '))

available_cups = 0
while True:
    available_water -= water
    available_milk -= milk
    available_beans -= beans
    if available_water >= 0 and available_milk >= 0 and available_beans >= 0:
        available_cups += 1
    else:
        break

if cups == available_cups:
    print('Yes, I can make that amount of coffee')
elif available_cups > cups:
    print(f'Yes, I can make that amount of coffee'
          f' (and even {available_cups - cups} more than that)')
else:
    print(f'No, I can make only {available_cups} of coffee')
