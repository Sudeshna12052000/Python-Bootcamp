def inp():
    return input("Enter three numbers ")

z=inp().split()


p=int(z[0])
q=int(z[1])
r=int(z[2])

a=max(p,q,r)
print(a,"is the greatest number among ",p,",",q," and" ,r)


num1 = int(input())
num2 = int(input())
num3 = int(input())
if (num1 >= num2) and (num1 >= num3):
 largest = num1
elif (num2 >= num1) and (num2 >= num3):
 greatest = num2
else:
 greatest = num3
print("The greatest number is",greatest )


