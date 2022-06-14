water = 0
coffee = 0
milk = 0

'''items to make a coffee'''
def add_items():
    global water, coffee, milk
    wa = int(input("enter the amount of water you want to add"))
    co = int(input("enter the amount of coffee you want to add"))
    mil = int(input("enter the amount of milk you want to add"))
    water += wa
    coffee += co
    milk += mil
    return water, coffee, milk

'''there are four different types coins in usa penny=1 cent,dime=10 cent ,nickel = 5 cent, quater = 25 cent'''
def coin_operators():
    penny = int(input("enter the number of penny "))
    dime = int(input("enter the number of Dime "))
    nickel = int(input("enter the number of Nickel "))
    quater = int(input("enter the number of Quater "))
    dollar = ((penny / 100) + (dime / 10) + (nickel / 20) + (quater / 4))
    return dollar

'''types of coffee'''
def make_espresso():
    global water, coffee
    if water < 50 or coffee < 18:
        print("insufficient items to make coffee please check report")
        print(f"amount of water = {water},\namount of coffee = {coffee},\namount of milkr = {milk}\n")
        add_items()
        water -= 50
        coffee -= 18

    else:
        water -= 50
        coffee -= 18


def make_latte():
    global water, coffee, milk
    if water < 200 or coffee < 24 or milk < 150:
        print("insufficient items to make coffee please check report")
        print(f"amount of water = {water},\namount of coffee = {coffee},\namount of milkr = {milk}\n")
        add_items()
        water -= 200
        coffee -= 24
        milk -= 150

    else:
        water -= 200
        coffee -= 24
        milk -= 150


def make_cappaccino():
    global water, coffee, milk
    if water < 50 or coffee < 18:
        print("insufficient items to make coffee please check report")
        print(f" amount of water = {water},\namount of coffee = {coffee},\namount of milkr = {milk}\n")
        add_items()
        water -= 250
        coffee -= 24
        milk -= 100

    else:
        water -= 250
        coffee -= 24
        milk -= 100


def make_coffee(type):
    coins = coin_operators()
    cost_Espresso = 1.50
    cost_Latte = 2.50
    cost_Cappuccino = 3
    if type == 1:
        if cost_Espresso < coins:
            print("tansaction succefull , Thankyou")
            make_espresso()
            return coins - cost_Espresso
    if type == 2:
        if cost_Latte < coins:
            print("tansaction succefull , Thankyou")
            make_latte()
            return coins - cost_Latte
    if type == 3:
        if cost_Cappuccino < coins:
            print("tansaction succefull , Thankyou")
            make_cappaccino()
            return coins - cost_Cappuccino


def coffee_maker():
    do_coffee = True
    while do_coffee:
        def type_coffee():
            print("Which type of coffee you want to taste")
            type = int(input("'Espresso''cost = 1.50' press 1 \n'Latte''cost = 2.50' press 2\n'Cappuccino' 'cost = 3 'press' 3\n"))

            if type == 1 or type == 2 or type == 3:

                return make_coffee(type)

            else:
                print("sorry: you entered wrong number")

        if 'enter' == input("type 'enter' to make coffee"):
            print(f"change ${type_coffee()}")
        else:
            print("buit to serve you,Thankyou")
            do_coffee = False


if "power" == input(" press 'power' to start").lower():
    if "report" ==input("type 'report' to get report or else tyoe no"):
        print(f"amount of water = {water},\namount of coffee = {coffee},\namount of milkr = {milk}\n")
        if "add" == input("type 'add' to add itmes to the machine"):
            add_items()
    coffee_maker()
else:
    print("buit to serve you,Thankyou")
