#Write a program to implement binary search.  Also print running time of this algorithm.
from time import process_time
t1_start = process_time()  
def binary(list1,l,r,x):
	if r>=l:
		mid = int((l+r)/2)
		if list1[mid] == x:
			return mid
		elif list1[mid] > x:
			return binary(list1,l,mid-1,x)
		else:
			return binary(list1,mid+1,r,x)
	return -1


list1 = [5,4,1,8,3,2,0]

	
list1.sort()
length = len(list1)
print(list1)

l = 0
r = length-1
x = int(input("Enter element do you want to search"))	
result = binary(list1,l,r,x)

if result==-1:
	print("Element is not found in the list")
else:
	print("Index is ",result)

t1_stop = process_time()

print("Elapsed time during the whole program in seconds:", t1_stop-t1_start)  