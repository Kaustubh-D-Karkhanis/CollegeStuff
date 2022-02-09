import random
import timeit
from tracemalloc import start

def maxmin(arr,n,max, min):
    max=min=arr[1]
    for  i in range(2,n):
        if(arr[i]>max):
            arr[i]=max
        else:
            for j in range(2,n):
                if(arr[j]<min):
                     arr[j]=min
        
        return (max, min)

n=int(input("Enter number if elements:"))
arr=[random.randint(1,99) for k in range(n)]

print(arr)

print(maxmin(arr,n,max,min))

        