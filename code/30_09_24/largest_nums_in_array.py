arr = [1,2,3,100,1000]
c=0
for i in range (0,len(arr)):
    if arr[i] > c:
        c = arr[i]
print(c)        