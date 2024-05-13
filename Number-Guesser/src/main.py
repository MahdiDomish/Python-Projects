import random


def input_validator(user_guess):
    if not user_guess.isdigit():
        print('invalid input. please enter a number between 1 and 100 again!')
        return False

    user_guess = int(user_guess)
    if user_guess < 1 and user_guess > 100:
        print('invalid input. please enter a number between 1 and 100 again!')
        return False

    return True

def play_game():
    rand_number = random.randint(1, 100)
    score = 100
    while True:
        user_guess = input('please enter your guess between 1 and 100: ')
        if user_guess == 'q':
            print('Thanks for your playing. Goodbye!')
            break

        if not input_validator(user_guess):
            continue

        user_guess = int(user_guess)
        if user_guess == rand_number:
            score = max(score, 0)
            print(f'your guess is correct and your score is: {score}')
            break
        elif user_guess > rand_number:
            print('your guess is too high, try again')
            score -= 10
        else:
            print('your guess is too low, try again')
            score -= 10

if __name__ == "__main__":
    play_game()
