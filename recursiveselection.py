import random 
import time
from tracemalloc import start
import sys
sys.setrecursionlimit(3000)

def swap(A, i, j):
 
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
 
 

def selectionSort(A, i, n):
 
    
    min = i
    for j in range(i + 1, n):
 
        
        if A[j] < A[min]:
            min = j            
    swap(A, min, i)
 
    if i + 1 < n:
        selectionSort(A, i + 1, n)
   
n=int(input("Enter no. of elements:"))
A=[random.randint(1,99) for k in range(n)]

print("Array during sorting:")
print(A)

start=time.time()
selectionSort(A, 0, len(A))
end=time.time()
   
print("Array after sorting in Ascending order:")
print(A)

print("Time taken:")
print((end-start)*1000)

 
