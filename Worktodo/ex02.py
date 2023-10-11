a = int(input("give the first number\n"))
b = int(input("give the second number\n"))

if a >= 0 and b >= 0: #we suppose that 0 is positive
    print("they are both positive")
elif a < 0 and b < 0:
    print("they are both negative")
else :
    print("the numbers have two diffrents signs")