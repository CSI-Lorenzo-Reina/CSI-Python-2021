print("Welcome to the FONSECA concert ticket dispensery! The cost of one seat per section is as follows: Stage Seat = $95, Front Row Seat = $85, Mid Row Seat = $75, Back Row Seat = $65.")
Stage_Seat = int(input('How many stage seat tickets would you like to purchase?: '))
Front_Seat = int(input('How many front row seats would you like to purchase?: '))
Middle_Seat = int(input('How many middle row seats would you like to purchase?: '))
Back_Seat = int(input('How many back row seats would you like to purchase?: '))
def f(Stage_Seat, Front_Seat, Middle_Seat, Back_Seat):
    return Stage_Seat * 95 + Front_Seat * 85 + Middle_Seat * 75 + Back_Seat * 65
print("Your total price with tax would be $" + str(f(Stage_Seat, Front_Seat, Middle_Seat, Back_Seat) * 1.115) + '.')