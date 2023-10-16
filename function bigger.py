def sum(n1,n2):
    temp=0
    if(n1<n2):
        temp=n1
        n1=n2
        n2=temp
    print("Largest number is :",n1)
a=int(input("Enter the 1st number :"))
b=int(input("Enter the 2nd number :"))

sum(a,b)