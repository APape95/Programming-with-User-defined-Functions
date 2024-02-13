def display_citys():
    """Displays the city options to the user."""
    print("Please choose an option:")
    print("1. Spain")
    print("2. Germany")
    print("3. Portugal")
    print("4. Greece")
    print("5. France")
    print("6. Exit")

def get_user_choice():
    while True:
        display_citys()
        des_choice = input("Enter your choice: ")
        
        if des_choice in ['1', '2', '3', '4', '5', '6']:
            return choice
        else:
            print("Invalid choice. Please select a number bettween 1 and 6.")

while True: 
    user_choice = get_user_choice()
    
    if user_choice == '1':
        des_choice = 100
        print("Spain selected")
        break

    elif user_choice == '2':
        des_choice = 200
        print("Germany selected.")
        break

    elif user_choice == '3':
        des_choice = 300
        print("Portugal selected.")
        break

    elif user_choice == '4':
        des_choice = 400
        print("Greece selected.")
        break

    elif user_choice == '5':
        des_choice = 500
        print("France selected.")
        break

    elif user_choice == '6':
        print("Exiting program.")
        break

    else:
        print("An unexpected error occurred.")
        break

num_nights = int(input("How many nights do you want to stay?"))
rent_days = int(input("How many days car rental do you want?"))

