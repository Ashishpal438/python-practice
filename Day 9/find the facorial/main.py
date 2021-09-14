num = int(input("Enter a number : "))
fact = 1
for i in range(num):
    fact = fact * (i+1)
print("factorial of ", num, "is",fact)