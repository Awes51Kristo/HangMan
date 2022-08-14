import random
import string


print("H A N G M A N")

attempts = 8
wins = 0
loses = 0

while True:
    doing = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if doing == "play":
        words = ["python", "java", "swift", "javascript"]
        secret_word = list(random.choice(words))
        hidden_word = list("-" * len(secret_word))
        letters_in_word = set(secret_word)
        while attempts > 0:
            guess = input(f"\n{''.join(hidden_word)}\nInput a letter:")
            wrong_chars = []

            if len(guess) != 1:
                print("Please, input a single letter.")
                continue
            elif guess not in string.ascii_lowercase:
                print("Please, enter a lowercase letter from the English alphabet.")
                continue
            else:
                pass

            if guess not in hidden_word and guess in letters_in_word:
                pass
            elif guess not in secret_word and attempts != 0:
                attempts -= 1
                if attempts == 0:
                    print("You lost!")
                    loses += 1
                    break
                print("That letter doesn't appear in the word.")
                wrong_chars.append(guess)
                continue
            elif guess in hidden_word or guess in wrong_chars:
                print("You've already guessed this letter.")
                continue

            if guess in letters_in_word:
                for i in range(len(secret_word)):
                    if secret_word[i] == guess:
                        hidden_word[i] = secret_word[i]

            if hidden_word == secret_word and attempts != 0:
                print(f"\nYou guessed the word {''.join(secret_word)}!\nYou survived!")
                wins += 1
                break
    elif doing == "results":
        print(f"You won: {wins} times.")
        print(f"You lost: {loses} times.")
    elif doing == "exit":
        break
