str = input("Enter a string: ")
dict1 = {}
for ch in str:
    if ch in dict1:
        dict1[ch] += 1
    else:
        dict1[ch] = 1
for key in dict1:
    print(key, ':', dict1[key])            