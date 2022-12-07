import math
sideA = input("Input side A")
sideB = input("Input side B")
sideC = input("Input side C")
p = (int(sideA)+int(sideB)+int(sideC))/2
x = (p*(p-int(sideA))*(p-int(sideB))*(p-int(sideC)))
S = math.sqrt(x)
print ("The area of the triangle is {}".format(S))