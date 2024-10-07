# Python 3 code to find sum of elements in given array

# Initialize a variable to store the sum while iterating through the array
sum = 0

# Initialize array
arr = [1, 2, 3, 4, 5]

# Loop through the array to calculate sum of elements
for i in range(0, len(arr)):
    sum = sum + arr[i]

print("Sum of all the elements of an array: " + str(sum))
