def od(n):
    if(n%2==0):
        print("Even")

x= int(input("Enter the number to be checked :"))
try:
    od(x)
except NameError:
    raise NameError("Error aan guis")