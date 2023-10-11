#write a python script that allows you to search and then display the max value of N numbers entred by the users


range = int(input("give the number \n"))
if range < 0 :
    print("Please, give a positive number")
else :
    max = 0
    count = 1
    while count <= range:
        nbr = float(input(f"Enter the number {count} : "))
        if nbr > max :
            max = nbr
        count += 1
    if max != 0 :
        print (f"the max value is = {max}")
    else :
        print("please enter a valid number")
