import random
import time
from tracemalloc import start

def selection_sort(arr):
    for i in range(len(arr)):
        min_indx=i
        for j in range(min_indx+1,len(arr)):
            if arr[j]<arr[min_indx]:
                min_indx=j
        arr[i],arr[min_indx]=arr[min_indx],arr[i]
        

n=int(input("Enter the Number of Elements:"))
elements=[random.randint(1,99) for k in range(n)]

print("Array during sorting:")
print(elements)

start=time.time()
selection_sort(elements)
end=time.time()

print("Array after sorting in Ascending order:")
print(elements)

print("Time taken:")
print((end-start)*1000)