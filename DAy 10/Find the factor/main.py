n = int(input("Enter a number to find its factor : "))
print(1, end=' ')
factor = 2
while factor <= n/2:
    if n% factor == 0:
        print(factor, end=' ')
        factor += 1
print(n, end=' ')    
