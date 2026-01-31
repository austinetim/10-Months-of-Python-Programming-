from clear_terminal import clear
from art import gavel

print(gavel)

# Clear the screen
bid_data = {}

bidder_name = input("Enter your name: \n")
bid_price = input("Enter the amount: \n")
end_of_bid = True

while end_of_bid:  

    def add_bidders(name, price):
        bid_data["Bidder_name"] = name
        bid_data["bid_price"] = price

    add_bidders(name = bidder_name, price = bid_price)

    ask_bidder = input("Are there still other bidders? 'yes' or 'no':\n").lower
    if ask_bidder == "yes":
        clear()
        bidder_name = input("Enter your name: \n")
        bid_price = input("Enter the amount: \n")
        add_bidders(name = bidder_name, price = bid_price)
  
        #     max_value = bidder[]
        #     #Do something important
        # end_of_bid = False

print(bid_data)