from clear_terminal import clear
from art import gavel
print(gavel)

bid_data = {}
end_of_bid = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, with a bid of ${highest_bid}")
        



while not end_of_bid:  
    bidder_name = input("Enter your name: ")
    bid_price = int(input("Enter your bid amount: $"))
    bid_data[bidder_name] = bid_price

    should_continue = input("Are there still other bidders? 'yes' or 'no':\n").lower()
    if should_continue == "no":
       end_of_bid = True
       find_highest_bidder(bid_data)
    elif should_continue == "yes":
        clear()