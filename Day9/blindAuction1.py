import replit
import art
#HINT: You can call clear() to clear the output in the console.

print(art.logo)

print('Welcom to the secret auction program.')

bids = {}
on_going = 'yes'
while on_going == 'yes':
    name = input("What is your name?: ")
    bid_Amount = int(input("What's your bid? $"))
    bids[name] = bid_Amount    
    on_going = input("Are there any other bidders? Type 'yes or 'no'.\n")

    replit.clear()


highestBidAmount = 0
highestBidder = ''
for bidder in bids:
    if highestBidAmount < bids[bidder]:
        highestBidAmount = bids[bidder]
        highestBidder = bidder

print(f"The winner is {highestBidder} with a bid of ${highestBidAmount}")


