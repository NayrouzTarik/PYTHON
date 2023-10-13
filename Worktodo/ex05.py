nb = int(input("Enter the number you want to calculate the factorial for: "))

if nb < 0:
    print("Factorial is not defined for negative numbers.")
elif nb == 0:
    print("0! = 1")
else:
    facto = 1
    nbr = nb  

    while nb > 0:
        facto = facto * nb
        nb = nb - 1

    print(f"{nbr}! = {facto}")
