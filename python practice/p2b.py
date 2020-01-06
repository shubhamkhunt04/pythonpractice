#Write a program to get the maximum and minimum value from a dictionary- without using inbuild function(min,max).

dict1 ={}

n= int(input("\nEnter total number of element\n"))

for i in range(n):
	dict1.update({ int(input("\nEnter key :-")) : int(input("\nEnter value :-")) })
	
print(dict1)
maxs = 0
mins = 999

for i in dict1.values():
      if maxs < i:
          	maxs = i
      if mins > i:
      	mins = i    	
print("Maximum value is :- ",maxs)
print("Minimum value is :- ",mins)

		
