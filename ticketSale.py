# Python project - Purchase tickets.

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
            print(f'{err} Please try again.')
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