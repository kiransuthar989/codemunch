a = int(input())
b = int(input())
lst = []
lst_result = []
count = 0
     
print(lst_result)   
print(lst)
if a < b:
    for i in range(10 - a):
        lst.append(i + 1)
    for j in range(10 - a):
        if b <= count:  
            lst_result.append(lst[j])
        count += 1
else:
    for i in range(a):
        lst.append(i + 1)
    for j in range(a):
        if b <= count:  
            lst_result.append(lst[j])
        count += 1
print(lst)
print(lst_result)
