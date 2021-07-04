numbs = [int(input(f"{j + 1} num is: ")) for j in range(int(input("Enter the length of list: ")))]
print(numbs)
i = int(input("enter the incremental number:\n" ))
n = 0
for num in numbs:
    numbs[n] = numbs[n] + i
    n = n + 1
print(numbs)
