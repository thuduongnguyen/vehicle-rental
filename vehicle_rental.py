sign1 = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
sign2 = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

#Constants
CHECKMARK = "\u2713"

DURATION_1 = 1
DURATION_2 = 2
DURATION_3 = 3
DURATION_4 = 4
DURATION_7 = 7
DURATION_8 = 8

DISCOUNT_0 = 0
DISCOUNT_4 = 4
DISCOUNT_10 = 10
DISCOUNT_20 = 20


print(sign1)
print("~ Welcome to Best Cars Inc. ~")
print(sign1)

#Choice Loop
counter = 0
sum = 0
choice = 'Y'

#Create tuple values for Step 1
vehicle_type = ("Compact", "Sedan", "SUV", "Luxury")
daily_rate = (25, 35, 50, 60)

##########################################################
while choice == 'Y':
#Step 1: Vehicle Type Selection
    print("\nStep 1. Choose the type of vehicle you wish to rent.")

#Print vehicle
    print("Vehicle Type \tDaily Rate")
    index = 0
    for item in vehicle_type:
        print(f"{index+1:>2}. {item:<19} {daily_rate[index]}") 
        index += 1

#Loop for vehicle selection input with conditions
    selection = True
    while selection == True:
        vehicle = int(input("Your selection: ")) - 1
        if 0 <= vehicle <= 3:
            print(f"You have chosen {vehicle_type[vehicle]}. The base rental rate is ${daily_rate[vehicle]:.2f} per day")  
            selection = False
            counter += 1
        else:
            print('Error: Invalid selection. Please enter one of the option numbers displayed.')
            continue

##########################################################

#Step 2: Vehicle Rental Duration / Discount Conditions
    print("\nStep 2. Specify the duration of this vehicle rental.")
#Loop for rental duration input with conditions
    day = True
    while day == True:
        rental_duration = int(input("Enter the number of days needed: "))
        if rental_duration == DURATION_1:
            discount = DISCOUNT_0
            day = False
        elif DURATION_2 <= rental_duration <= DURATION_3:
            discount = DISCOUNT_4
            day = False
        elif DURATION_4 <= rental_duration <= DURATION_7:
            discount = DISCOUNT_10
            day = False
        elif DURATION_8 <= rental_duration:
            discount = DISCOUNT_20
            day = False
        else:
            print("Error: Value cannot be less than 1")
            continue

#Print dicount
    print(f"Discount to be applied is {discount}%")
    discounted_rental_rate = daily_rate[vehicle] - discount / 100 * (daily_rate[vehicle])
    print(f"The dicounted rental rate is ${discounted_rental_rate:.2f} per day")

##########################################################

#Step 3: Additional Features/ Services
    print("\nStep 3. Choose your desired additional features or services.")
    print('Option \t\t\t\tDaily Rate')

#Tuple for features / services
    option = ("GPS Navigation", "Mobile Wi-Fi", "Child Seat", "Toll Pass", "Roadside Assistance Plus")
    option_rate = (5, 8, 2, 4.50, 5)

#Tuple loop
    valid = False
    feature_cost = 0
    selected = set()

    while not valid:
#Print selection with/without checkmark       
        index = 0
        for item in option:
            if index in selected:
                print(f"{index+1:>2}. {item:<33} {option_rate[index]:.2f} " + CHECKMARK) 
            else:
                print(f"{index+1:>2}. {item:<33} {option_rate[index]:.2f}")
            index += 1

#User input & check
        feature = int(input("Enter option # or 0 to proceed: ")) - 1
        if feature not in selected:
            selected.add(feature)
        else:
            print('Feature is already selected.')
            continue

#Feature condition
        if -1 < feature < 5:
            print(f"Feature: {option[feature]} added for ${option_rate[feature]:.2f}")
            feature_cost += option_rate[feature]
        elif feature == -1:
            valid = True
        else:
            print("Error: Invalid selection, please try again.")
            continue

#Calculations, final output
    cost_day = discounted_rental_rate + feature_cost
    before_tax = cost_day * rental_duration
    sum += before_tax
    print(f"\nSuccess! Your reservation for a {rental_duration} day {vehicle_type[vehicle]} rental is complete.")
    print(f"The price (not including GST) is ${cost_day:.2f} per day or ${before_tax:.2f} for the rental.")

#Choice loop input for another vehicle
    choice = input('Do you want to rent another vehicle? (Y/N): ').upper()

##########################################################
#Rental Billing Summary
gst = 0.05 * sum
total_amount = sum + gst

print(sign2)
print('~~~      RENTAL BILLING SUMMARY      ~~~')
print(f'Number of vehicles rented:{counter:>14}')
print(f'Amount due before tax:{sum:>18.2f}')
print(f'GST:{gst:>36.2f}')
print(f'Total amount due:{total_amount:>23.2f}')
print(sign2)
print('\nThank you for choosing Best Cars!')

#Group Members
"""
Thu Duong Nguyen - 000928653
Stanlee Fabian - 000938729
"""