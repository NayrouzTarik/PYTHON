# a program that calculate the square of a number that the user must choose, if the user choose 0 you have to exit
while True:
    nbr = int(input("Give the number you want : "))
    if nbr == 0:
        break
    nbr = nbr * nbr
    print(f"The result is {nbr}")
