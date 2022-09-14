def self_Number(n): 
    number = n 
    for i in list(str(n)): 
        number += int(i) 
    return number 

arr = [] 

for i in range(10000): 
    arr.append(self_Number(i)) 

for j in range(10000): 
    if j in arr: 
        pass 
    else:
        print(j) 