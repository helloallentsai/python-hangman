import random


def random_word():
    with open('sowpods.txt') as file:
        words = list(file)
        word = random.choice(words).strip()

    return word


def play_game():
    # initialize
    word = list(random_word())
    hangman = word.copy()
    for i in range(0, len(word)):
        hangman[i] = '_'
    win = False
    guesses = 6
    guessed = list()

    print('Welcome to Hangman')
    while (guesses > 0):
        print(hangman)
        letter = input('Letter to guess: ').upper()
        while letter in guessed:
            letter = input(
                'Letter guessed already. Please provide another: ').upper()

        guessed.append(letter)
        if letter in word:
            # updates hangman for guessed letter
            for i in range(0, len(word)):
                if word[i] == letter:
                    hangman[i] = letter
            check_win = hangman.count('_')
            # if all letters guessed
            if check_win == 0:
                win = True
                break
            print(hangman)
            print(
                f'{guesses} guess(es) left\nYou have guessed these letters {guessed}\n')
        else:
            guesses -= 1
            if guesses == 0:
                break
            print(hangman)
            print(
                f'{guesses} guess(es) left\nYou have guessed these letters {guessed}\n')

    if win:
        print('Congrats, you won! 👍')
    else:
        print('Sorry, you lost 😢')

    play_again = input('Play again? (Y/N): ').upper()
    if play_again == 'Y':
        play_game()
    else:
        return('Good bye')


print(play_game())
