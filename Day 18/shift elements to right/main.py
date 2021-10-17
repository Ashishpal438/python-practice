list1 = [2,4,6,8,10]
temp = list1[len(list1)-1]
for i in range(len(list1)-1,-1,-1):
    list1[i] = list1[i-1]
list1[0] = temp
print(list1)    