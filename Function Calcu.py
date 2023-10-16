# def sum(n1,n2):
#     print(n1+n2)
#
# def dif(n1,n2):
#     print(n1-n2)
#
# def mul(n1,n2):
#     print(n1*n2)
#
# def div(n1,n2):
#     print(n1/n2)
# n1=int(input("Enter the 1st number"))
# n2=int(input("Enter the 2nd number"))
# n=n2=int(input("Enter the choice : (1 for addition,2 for sub, 3 for mul, 4 for div"))
# if(n==1):
#
#

def cal(c):

    if c==1:
        n1=int(input("Enter the 1st number"))
        n2=int(input("Enter the 2nd number"))
        print(n1+n2)
    elif c == 2:
        n1 = int(input("Enter the 1st number"))
        n2 = int(input("Enter the 2nd number"))
        print(n1 - n2)
    elif c == 3:
        n1 = int(input("Enter the 1st number"))
        n2 = int(input("Enter the 2nd number"))
        print(n1 * n2)
    elif c == 4:
        n1 = int(input("Enter the 1st number"))
        n2 = int(input("Enter the 2nd number"))
        print(n1 / n2)
    else:
        print("Invalid ")
c=int(input("Enter the choice :"))

cal(c)



