import random
import time

print("🎮 Rock–Paper–Scissors")
def get_user_choice() -> str:
    choice = input("1 for 🪨, 2 for 📄, or 3 for ✂️: ")
    print("user choice -> ", end="")
    if choice == "1":
        return "rock 🪨"
    elif choice == "2":
        return "paper 📄"
    elif choice == "3":
        return "scissors ✂️"

    """
    get choice from user until got a valid choice
    :return:  str - 'rock', 'paper', 'scissors'
    """
    pass

def get_random_computer_choice() -> str:
    print("computer choice -> ", end="")
    return random.choice(["rock 🪨", "paper 📄", "scissors ✂️"])
    """
    random 1 options from 'rock', 'paper', 'scissors'
    :return:  str - 'rock', 'paper', 'scissors'
    """

def print_user_choice_icon_and_delay(choice, how_long_sleep) -> None:
    """
    print the user choice + icon and sleep 2-3
    :param choice:  str - 'rock', 'paper', 'scissors'
    :param how_long_sleep:  how long sleep in seconds
    :return: None
    """

    print(user_choice)
    time.sleep(how_long_sleep)


def print_computer_choice_icon(choice) -> None:
    print(computer_choice)
    """
    print computer choice + icon
    :param choice:  str - 'rock', 'paper', 'scissors'
    :return:
    """


def get_game_result(user_choice, computer_choice) -> str:
    if user_choice == computer_choice:
        return "draw"
    elif user_choice == "rock 🪨" and computer_choice == "scissors ✂️" :
        return "user win"
    elif user_choice == "paper 📄" and computer_choice == "rock 🪨":
        return "user win"
    elif user_choice == "scissors ✂️" and computer_choice == "paper 📄":
        return "user win"
    else:
        return "computer win"

    """
    :param user_choice:  str - 'rock', 'paper', 'scissors'
    :param computer_choice: str - 'rock', 'paper', 'scissors'
    :return: str winner - 'user', 'draw', 'computer'
    """


def print_result_and_icon(get_result) -> None:
    for _ in range(12):
        print('-', end="")
        time.sleep(2/12)
    print('| ', end="")
    match get_result:
        case "user win":
            print(" user is the winner 👋")
        case "computer win":
            print(" computer is the winner 💥")
        case "draw":
            print("draw 🤝")

    """
    👋 💥🤝✅
    Print result with icon
    :param get_result: str winner - 'user', 'draw', 'computer'
    :return: None
    """

# Icons for each choice
ICONS = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️",
}
user_choice = get_user_choice()
print_user_choice_icon_and_delay(user_choice , 2)
computer_choice = get_random_computer_choice()
print_computer_choice_icon(computer_choice)
get_result = get_game_result(user_choice, computer_choice)
print_result_and_icon(get_result)