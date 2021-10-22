tuple = (1,2,3,4,5,6)
n=int(input("Enter element to be searched: "))
flag =False
for i in range(len(tuple)):
    if tuple[i]==n:
        print("Element found at index", i)
        flag = True

if flag ==True:
    print("Successful search")

else:
    print("Not Found")