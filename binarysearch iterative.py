from unittest import result
import random
import timeit


def binarysearch(arr ,num, count):

    min=0
    max=len(arr)-1
    mid=0

    while min<=max:
        count=count+1
        mid=(min+max)//2
        if arr[mid]==num:
            return (mid,count)
        elif arr[mid]<num:
            min=mid+1
        elif arr[mid]>num:
            max=mid-1
    return (-1,0)

count=0
n=int(input("Enter the Number of Elements:"))
elements=[random.randint(1,99) for k in range(n)]

print(elements)
num=int(input("Enter the Number you want to Search:"))

t1=timeit.default_timer()
result,itr=binarysearch(elements,num,count)
t2=timeit.default_timer()

if result!=-1:
    print("Number found at Index:",str(result))
    print(itr)
else:
    print("Number not Present in The List")



print("Time Taken: ",((t2-t1)*1000))