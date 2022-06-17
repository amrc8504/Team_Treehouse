#fString
# f_name=input("What is your first name?  ")
# capsName = f_name.title()
# print(f'Hello, {capsName}! Welcome!')

#Puzzle
# def display_blanks(word):
#     blanks = "-" * len(word)
#     print(blanks)

# print("Puzzle 1:")
# display_blanks("treehouse")
# print("Puzzle 2:")
# display_blanks( "python")

# Check for password - while loops
# import sys

# MASTER_PASSWORD = 'opensesame'
# password = input("Please enter your password: ")
# attempts = 1
# while password != MASTER_PASSWORD:
#     if attempts > 3:
#         sys.exit("Too many attempts, please try again later.")
#     password = input("Invalid password, please try again: ")
#     attempts += 1
# print("Welcome to secret town.")

#for loops
# banner = "Happy Birthday!"
# for letter in banner:
#     print(letter.upper())

# Each iteration through the iterable produces the next letter.
# for letter in "You got this!":
#     if letter in "oh":
#         print(letter)

#Python project - Purchase tickets.

def ticketSale():

    SERVICE_FEE = 2
    
    TICKET_PRICE = 10

    tickets_remaining = 100

    def calculate_price(purchase):
        return purchase * TICKET_PRICE + SERVICE_FEE

    while tickets_remaining != False:
        print(f'Buy now! There are only {tickets_remaining} tickets remaining!')
        user_name = input("Welcome! What is your name? ")
        username = user_name.title()
        print(f'Hello {username}!')
        purchase = input(f'How many tickets would you like to buy {username}? ')
        try:
            purchase = int(purchase)
            if purchase > tickets_remaining:
                raise ValueError(f'There are only {tickets_remaining} tickets remaining.')
        except ValueError as err:
            print(f'I did not quite understand that. {err} Please try again.')
        else:
            total = calculate_price(purchase)
            print(f'{purchase} tickets will cost ${total}.')
            confirm = input('Do you want to complete this order? [Y/N] ')
            if confirm.lower() == "y":
                print("Sold!")
                tickets_remaining -= purchase
            else:
                print(f'Ok, {username}. Your order has been cancelled.')
    print("Sorry the tickets are sold out. :(")
ticketSale()