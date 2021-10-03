wtemp= ['Mon',45,'Tue',43,'Wed',42,'Thu',40,'Fri',38,'Sat',40,'Sun',38]
ln = len(wtemp)
days = []
temperature = []
for i in range(ln):
    if (i % 2 == 0):
        days.append(wtemp[i])
    else:
        temperature.append(wtemp[i])    
print("Original list is: ", wtemp)
print("The days are: ",days) 
print("The temperatures are : ",temperature)       