import random 
import time
from tracemalloc import start
import sys
sys.setrecursionlimit(20000)

def insertionSortRecursive(arr, n):
    
    if n <= 1:
        return 
    insertionSortRecursive(arr, n - 1)
    last = arr[n - 1]
    j = n - 2
    while (j >= 0 and arr[j] > last):
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j + 1] = last
 
 
f=int(input("Enter no. of elements:"))
A=[random.randint(1,99) for k in range(f)]
n = len(A)
print("Array before sorting: ")
print(A)

start=time.time()
insertionSortRecursive(A, n)
end=time.time()

print("Array after sorting: ")
print(A)

print("Time taken:")
print((end-start)*1000)

 