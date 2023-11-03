import random


def play():
    user = input("What's your choice? rock, paper or scissors\n")
    computer = random.choice(['rock', 'paper', 'scissors'])

    if user == computer:
        return "It's a Tie!"
    if is_win(user, computer):
        return "Yay! You Won!"
# If none of the previous conditions (ties or user wins) are met,
# it means the computer has won. In the context of the game rules,
# if the user hasn't won and there is no tie, the only remaining
# outcome is the computer winning. So, this statement will be reached
# only when the computer emerges victorious, making it unnecessary
# to explicitly check for the computer's victory in an additional 'if' statement.
# Therefore, the function automatically returns 'You lost!' in this case
    return 'You lost!'


def is_win(player, opponent):
    # The 'if' statement checks the win conditions for the game of rock-paper-scissors.
    # In the game, rock wins over scissors, scissors win over paper, and paper wins over rock.
    # If the player's choice defeats the opponent's choice based on these rules,
    # the function returns 'True', indicating a win for the player.
    # If none of these winning conditions are met, the function returns 'False',
    # indicating that the player has not won in this particular round.
    if (player == 'rock' and opponent == 'scissors') or \
            (player == 'scissors' and opponent == 'paper') or \
            (player == 'paper' and opponent == 'rock'):
        return True


print(play())
