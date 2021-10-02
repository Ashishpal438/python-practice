list1 = [10,20,30,40,10,50,10]
num = eval(input("enter a number:"))
count = 0
for i in list1:
    if num == i:
     count = count + 1
     print(num,"is present", count, "number of times")