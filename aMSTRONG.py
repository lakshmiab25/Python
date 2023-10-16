a= int(input("Enter the number"))
temp=a
sum=0
while(a>0):
    K=a%10
    sum=K*K*K+sum
    a=a//10
if(temp==sum):
  print("Amstrong")
else:
  print("Not") 
    
    
