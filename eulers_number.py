def fact(i):
    if i==1:
        return 1
    else:
        return i*fact(i-1)

power_of_e = int(input("Power of e: "))
iterations = int(input("Number of iterations: "))
sum = 1