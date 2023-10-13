A = int(input("Donner A = "))
B = int(input("Donner B = "))

while B != 0:
    R = A % B
    A = B
    B = R
print(f"Le PGCD des deux nombres est = {A}")
