import random
import time
from tracemalloc import start

def insertion_sort(arr):
    for i in range(1,len(arr)):
        curr_variable=arr[i]

        while arr[i-1]>curr_variable and i>0:
            arr[i-1],arr[i]=arr[i],arr[i-1]
            i=i-1

n=int(input("Enter the Number of Elements:"))
elements=[random.randint(1,99) for k in range(n)]


print("Array before sorting:")
print(elements)

start=time.time()
insertion_sort(elements)
end=time.time()

print("Array after sorting in Ascending order:")
print(elements)

print("Time Taken:")
print((end-start)*1000)
