x = int(input("Please enter a number: "))
r = list(range(2,x+1))
for i in r:
    if x%i == 0:
        print("The number", x , "is not a prime")
        break
    else:
        print("The number",x, "is a prime")
        break

        
        
        

