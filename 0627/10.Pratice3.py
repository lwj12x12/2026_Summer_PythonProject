import random
while True:
    ans = random.randint(1,100)
    print("Guess Number!")
    low = 1
    high = 100
    #print(ans)

    while True:
        guess = input("Import a Number:")
        guess = int(guess)
        if guess > ans:
            high = guess
            print(f'Too Big {low}~{high}')
        elif guess < ans:
            low = guess
            print(f'Too Small {low}~{high}')
        else:
            print("Bingo!!")
            break
    again = input("Another Round? y/n :")
    if again.lower() == 'n':
        print("See You Soon~~")
        break
