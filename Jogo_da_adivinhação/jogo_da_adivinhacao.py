import random

print("-------------------------------")
print(">>>>>>Jogo da Adivinhação<<<<<<")
print("-------------------------------")
computer_choice = random.randint(1, 100)

while True:

    user_choice = int(input("Type a number between 1 and 100 to match: "))

    if user_choice > computer_choice:
        print("-------------------------------")
        print("OPS. Muito alto")
        print("-------------------------------")
        
    elif user_choice < computer_choice:
        print("-------------------------------")
        print("Ops. Muito Baixo!")
        print("-------------------------------")
        
    else:
        print("------------------------------------------------------")
        print(f"!!!PARABENS!!! >voce acertou< o numero é {computer_choice}")
        print("------------------------------------------------------")
        break
