import math

a = float(input("give the first param \n"))
b = float(input("give the second param \n"))
c = float(input("give the third param \n"))

print("the equation is :",end = " ")
print(f"{a}x2 + {b}x + {c}")

if a != 0 :
    delta = (b * b) - (4 * a * c)
    if delta > 0 :
        deltasqrt = math.sqrt(delta)
        x1 = (-b - deltasqrt) / (2 * a)
        x2 = (-b + deltasqrt) / (2 * a)
        print (f"the results of this equations are x1 = {x1} and x2 = {x2}")
    elif delta == 0 :
        x = (-b) / (2*a)        
        print (f"the only solution is x = {x}")
    else :
        print("the solutions are an imaginary solutions")
        real = (-b) / (2 * a)
        negdelta = math.sqrt(-delta)
        imaginary = negdelta / (2 * a)
        print (f"the solutions are c1 = {real} + {imaginary}i and c2 = {real} - {imaginary}i")
else :
    print ("we are solving a first degree equation")
    print(f"the equation become : {b}x + {c}")
    if b == 0 :
        if c == 0:
            print("the number of solutions is infinite")
        else:
            print("Absurde")
    else :
        x = -c / b
        print(f"The solution to the equation {b}x + {c} is x = {x}")