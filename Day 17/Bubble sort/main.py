num = [10,50,30,20,40]
ctr = i = 0
n = len(num)
print("The Original list is:")
for i in range (0,n):
    print(num[i], end= " ")
for i in range (n):
    for j in range (n-1):
        if(num[j] > num[j+1]):
            ctr += 1
            tmp = num[j]
            num[j] = num[j+1]
            num[j+1] = tmp
print()
print("The sorted list is:")
for i in range (0,n):
    print(num[i],end=' ')