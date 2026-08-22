import random
while True:
    ans = random.randint(1,10)
    print("Guess Number!")
    print(ans)

    while True:
        guess = input("Import a Number:")
        guess = int(guess)
        if guess > ans:
            print("Too Big")
        elif guess < ans:
            print("Too Small")
        else:
            print("Bingo!!")
            break
    again = input("Another Round? y/n :")
    if again == 'n':
        print("See You Soon~~")
        break
