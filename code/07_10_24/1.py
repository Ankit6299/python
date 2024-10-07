# Python program to find the average of all numbers

import array as arr
a = arr.array('i', [10, 5, 15, 4, 6, 20, 9])
print(a)
s = 0
for i in range(len(a)):
    s += a[i]
avg = s / len(a)
print("Average:", avg)

# Using sum() function
avg = sum(a) / len(a)
print("Average:", avg)
