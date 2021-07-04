n = int(raw_input())
arr = map(int, raw_input().split())
arr1 = arr*1
if arr1.count(max(arr1)) > 1:
  for num in range(arr.count(max(arr))):
    arr1.remove(max(arr1))
else:
  arr1.remove(max(arr1))     
print(max(arr1))
