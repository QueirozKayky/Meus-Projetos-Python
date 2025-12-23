import random

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("=-=-=-=-=-JOGO DA FORCA=-=-=-=-=-")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

word_list = [
    "python", "programacao", "desafio", "computador", "linguagem",
    "internet", "algoritmo", "desenvolvimento", "interface", "codigo"
]

secret_word = random.choice(word_list)
user_progress = []
user_try = 10
for letter in secret_word:
    user_progress.append("*")


print(">>Guess the word<<")

while True:
    print(" ".join (user_progress))
    print(f'You have {user_try} coins to play the game')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    guess = str(input("Guess a letter: "))
    if len(guess) >1:
        print('Please, type just one letter.')
        continue
    if guess in secret_word:
        for index, letter in enumerate(secret_word):
            if letter == guess:
                user_progress[index] = guess
            pass
        if "*" not in user_progress:
            print(f'Congratulations!!! You guess the word: >>>>{secret_word}<<<<')
            break
    else:
        user_try -=1
        if user_try <=0:
            print('OPS, You failed!')
            print(f'The word was {secret_word}')
            break


