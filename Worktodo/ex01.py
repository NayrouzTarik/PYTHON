#write a program in Python language that allows the exchange of the contents of three digital data (right rotation)


a = input("give the first arg ")
b = input("give the second arg ")
c = input("give the third arg ")
d = input("give the fourth arg ")

print ("the old list is : ")
print (a,b,c,d)
a, b, c, d= d, a, b, c
print ("the new list is : ")
print (a,b,c,d)
