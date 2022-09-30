num=int(input("Enter your number:\n"))
prime = True
for h in range(2, num):
    if (num%h==0):
        prime = False
        break
if prime:
    print("prime")
else:
    print("not  a prime")

    


