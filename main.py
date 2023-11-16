import random

def check(comp, user):
    if comp == user:
        return 0

    if (comp == 0 and user == 1) or (comp == 1 and user == 2) or (comp == 2 and user == 0):
        return 1

    return -1

comp = random.randint(0, 2)

while True:
    try:
        user = int(input("0 for Stone, 1 for Paper, and 2 for Scissors:\n"))
        if 0 <= user <= 2:
            break  # Valid input, exit the loop
        else:
            print("Invalid input. Please enter 0, 1, or 2.")
    except ValueError:
        print("Invalid input. Please enter a number.")

score = check(comp, user)

print("You: ", user)
print("Computer: ", comp)

if score == 0:
    print("It's a draw")
elif score == -1:
    print("You lose")
else:
    print("You won")
