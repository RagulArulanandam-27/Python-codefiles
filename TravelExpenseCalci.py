
"""
USER INPUTS FOR THE TRAVEL EXPENSES
"""
expense_hotel_stay = float(input("Enter the totla expenses of the hotal stay: "))
total_days = int(input("Enter the total day of the travel: "))
expense_public_transport = float(input("Enter the totla expenses of the public transport: "))
total_miles = int(input("Enter the total miles travelled in the car: "))

"""
CALCULATIONS
"""
car_fuel_per_mile = 0.43
expense_car_fuel = car_fuel_per_mile*total_miles
expense_food = 50*total_days




def calc_expense(expense_hotel_stay, expense_food, expense_public_transport, expense_car_fuel):
    return expense_hotel_stay + expense_food + expense_public_transport + expense_car_fuel


print("The Total expenses of the travel is £ {0:.2f} ".format(calc_expense(expense_hotel_stay, expense_food, expense_public_transport, expense_car_fuel)))