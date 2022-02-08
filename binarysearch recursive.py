import random
import timeit
from tracemalloc import start

def insertion_sort(arr):
    for i in range(1,len(arr)):
        curr_variable=arr[i]

        while arr[i-1]>curr_variable and i>0:
            arr[i-1],arr[i]=arr[i],arr[i-1]
            i=i-1



def binarySearch(arr, l, r, x):

	
	if r >= l:

		mid = l + (r - l) // 2

		
		if arr[mid] == x:
			return mid

		
		elif arr[mid] > x:
			return binarySearch(arr, l, mid-1, x)

		
		else:
			return binarySearch(arr, mid + 1, r, x)

	else:
		
		return -1




n=int(input("Enter no. of elements:"))
arr=[random.randint(1,99) for k in range(n)]

print(arr)

x = int(input("Enter element to be found: "))

insertion_sort(arr)
print("Array after sorting")
print(arr)

t1=timeit.default_timer()
result = binarySearch(arr, 0, len(arr)-1, x)
t2=timeit.default_timer()

if result != -1:
	print("Element is present at index % d"  % result )
else:
	print("Element is not present in array")


print("Time taken",((t2-t1)*1000))
