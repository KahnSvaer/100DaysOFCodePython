import os
from art import logo

logo = logo + "\n Welcome to the Secret Auction"

bidding = True
bids_dict = {}
while bidding:
    print(logo)
    name = input("What is the bidder's name?\t")
    bid = int(input("What is your bid?\t$").strip())

    bids_dict[name] = bid

    end = input("Are there anymore bidders? Yes/no\t").strip().lower()
    if end == 'no':
        bidding = False
    os.system('cls')

max_bidder = ''
max_bid = 0

for bidder in bids_dict:
    if bids_dict[bidder]>max_bid:
        max_bid = bids_dict[bidder]
        max_bidder = bidder

print(logo)
print(f"Sold!!! To {max_bidder} for ${max_bid}.")