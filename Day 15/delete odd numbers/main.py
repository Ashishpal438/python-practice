L1 = [1,2,3,4,5,6,7,8]
len1 = len(L1)
i=0
while i<len1:
    if (L1[i] % 2 != 0):
      del(L1[i])
    len1 = len1 - 1
    i=i+1

print("list after deletion is :", L1)    