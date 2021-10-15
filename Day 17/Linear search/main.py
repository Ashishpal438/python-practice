num = [10,20,40,62,78]
pos = 0
print("List elements are: ",end=' ')
for i in num:
    print(i,end=' ')
print()
find =  int(input("Enter the element to search: "))
flag = 0
for i in num:
    if(i == find):
        flag = 1
        pos = num.index(i)
        break
if flag == 1:
    print("Element found at index:",pos)   
else:
    print("Element not found")    