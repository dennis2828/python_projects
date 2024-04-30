import random

def roll():
    min_value = 1
    max_value = 6

    return random.randint(min_value, max_value)


while True:
    players = input("How many players would you like to play in (2-4)?: ")

    if players.isdigit():
        players = int(players)

        if 2 <= players <= 4:
            break
        else: print(f"Cannot play in {players} players. Please enter a value between 2-4")
    else: print("Invalid format. Please enter a value between 2-4")


max_score = 50
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:
    for player_idx in range(players):
        print(f"\n\nPlayer number {player_idx+1} turn\nYour score is: {players_scores[player_idx]}")
        player_score = 0
        while True:
            rolling = input("Do you want to roll (y)? ").lower()
            if rolling !="y":
                break

            roll_value = roll()

            if roll_value == 1:
                player_score=0
                print(f"You rolled a 1! Turn done!\nYour score is: {players_scores[player_idx]}")
                break

            player_score += roll_value
            print(f"You rolled a {roll_value}")
            print(f"Your score is: {player_score}")
        
        players_scores[player_idx] += player_score

max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print(f"Player {winning_idx+1} won! The score is: {max_score}")