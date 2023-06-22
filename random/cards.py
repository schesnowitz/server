import random 

deck = list(range(1, 53))
random.shuffle(deck)
print(deck)

#  do not use choice as we want unique cards and choice may select same card
hand = random.sample(deck, k=5)
print(hand)