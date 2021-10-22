def fact(i):
    if i==1:
        return 1
    else:
        return i*fact(i-1)

power_of_e = int(input("Power of e: "))
iterations = int(input("Number of iterations: "))
sum = 1

for i in range(1,iterations+1):
    sum = sum + pow(power_of_e,i)/fact(i)
    print(f"{sum:.20}")

print(f"The exponential value of {power_of_e} is {sum}")