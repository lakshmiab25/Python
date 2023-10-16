num=int(input("Enter the number"))
if(num==1):
        print("The number is neither prime or composite")

for i in range(2,num):
    if(num%i==0):
      flag=0
      break
    else:
      flag=1

if(flag==0):
    print("The number is composite ")
else:
    print("The number is prime")
                  
              
