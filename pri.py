from random import randint
num = randint(1,100)

print("Guess what i think?")
bingo = False

while bingo == False:
    answer = int(input())

    if answer > num:
        print('%d is Too big' %answer)
    if answer < num:
        print('%d is Too small' %answer)
    if answer == num:
        print('%d is BINGO!' %answer)
        bingo = True
