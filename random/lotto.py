import random
import json

white_ball_possibilities = list(range(1, 70))
red_ball_possibilities = list(range(1, 27))
tickets_per_drawing = 5
number_of_drawings = 100
total_spent = 0
winnings = 0

times_won = {
    "5+p" : 0,
    "5" : 0,
    "4+p" : 0,
    "4" : 0,
    "3+p" : 0,
    "3" : 0,
    "2+p" : 0,
    "1+p" : 0,
    "p" : 0,
    "0" : 0,
}


def calc_winnings(my_numbers, winning_numbers):
    win_amount = 0
    white_matches = len(my_numbers["whites"].intersection(winning_numbers["whites"]))
    power_match = my_numbers["red"] == winning_numbers["red"]

    if white_matches == 5:
        if power_match:
            win_amount = 2_000_000_000
            times_won["5+p"] += 1
        else:
            win_amount = 1_000_000
            times_won["5"] += 1

    elif white_matches == 4:
        if power_match:
            win_amount = 50_000
            times_won["4+p"] += 1
        else:
            win_amount = 100
            times_won["4"] += 1 
    elif white_matches == 3:
        if power_match:
            win_amount = 100
            times_won["3+p"] += 1
        else:
            win_amount = 7
            times_won["3"] += 1 
    elif white_matches == 2 and power_match:
            win_amount = 7
            times_won["2+p"] += 1
    elif white_matches == 1 and power_match:
            win_amount = 4
            times_won["1+p"] += 1
    elif power_match:
            win_amount = 4
            times_won["p"] += 1
    else:
         times_won["0"] += 1        
    return win_amount


for drawing in range(number_of_drawings):
    white_ball_draw = set(random.sample(white_ball_possibilities, k=5))
    red_ball_draw = random.choice(red_ball_possibilities)

    winning_numbers = {
        "whites": white_ball_draw,
        "red": red_ball_draw
    }

for ticket in range(tickets_per_drawing):
    total_spent += 2
    white_ball_picks = set(random.sample(white_ball_possibilities, k=5))
    red_ball_picks = random.choice(red_ball_possibilities)




    my_numbers = {
        "whites": white_ball_picks,
        "red": red_ball_picks
    }

    winning_amount = calc_winnings(my_numbers, winning_numbers)
    winnings += winning_amount


print(f"Spent: ${total_spent}")
print(f"Earnings ${winnings}")    

print(json.dumps(times_won, indent=2))