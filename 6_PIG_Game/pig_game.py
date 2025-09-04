import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

# Ask number of players
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Players must be b/w 2 - 4")
    else:
        print("Invalid try again.")

print("Number of players:", players)

# Game setup
max_score = 50
player_scores = [0 for _ in range(players)]

# Main Game
game_over = False
while not game_over:
    for player_idx in range(players):
        print("\n--- Player", player_idx + 1, "turn ---")
        print("Your total score is", player_scores[player_idx], "\n")
        
        current_score = 0
        while True:
            should_roll = input("Do you want to roll (y)? ").lower()

            if should_roll != 'y':
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn over.")
                current_score = 0
                break  # end turn immediately
            else:
                current_score += value
                print("You rolled a", value)
                print("Your score this turn is", current_score)

        # Add to total score
        player_scores[player_idx] += current_score
        print("Your total score is now", player_scores[player_idx])

    # After everyone’s turn → check if game should end
    if max(player_scores) >= max_score:
        game_over = True

# Determine winner
max_score_achieved = max(player_scores)
winning_index = player_scores.index(max_score_achieved)
print("\n🏆 Player", winning_index + 1, "is the winner with a score of", max_score_achieved, "!")
