import math
l=int(input("length of the tromboloid"))
b=int(input("Breadth of the tromboloid"))
h=int(input("Height of the tromboloid"))
k=pow(l,2)+pow(b,2)pow(h,2)
v=float((pow(b,2)*pow(h,2)/math.sqrt(k))
print("volume of tromboloid",v.format(".3f"))
r=((v*3/(4*math.pi))**(1/3))
print("radius",r.format(".3f"))
