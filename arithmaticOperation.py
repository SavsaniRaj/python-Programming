r = int(input(" enter 1st number : "))
n = int(input("enter 2nd number : "))
a = (input("enter arithmatic operator : "))
if a == '+':
    print("addition is ",r+n)
elif a == '-':
    print("substraction is",r-n)
elif a =='*':
    print("multiplication is ", r*n)
else :
    print(" division is : ", r/n)