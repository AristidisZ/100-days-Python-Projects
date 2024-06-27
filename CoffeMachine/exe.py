from replit import clear

bidder = {}
x= True

def bestBidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(winner,highest_bid)


while x:
    name = input("Name : ")
    bid = float(input("bid : "))

    bidder[name] = bid


    print(bidder)

    countinue = input("any other bidders : yes / no :")

    if countinue == "yes":
        clear()

    elif countinue == "no":
        x = False
        bestBidder(bidder)






