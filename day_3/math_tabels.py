import sys 
number=int(sys.argv[1])
print(f"user given a number is {number}")
for i in range (1,21):
    print(f"%d*%2d=%3d (number * i = number * i)")  
    #print(f"{number} * {i} = {number * i}") this  will get op but not formated  alignment