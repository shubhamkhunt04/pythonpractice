#Write a program to filter positive numbers from a list.
l1 = []
l2 =[]
n = int(input("Enter total number of element :-"))
for i in range(n):
   a= int(input("Enter element :"))
   l1.append(a)
print(l1)
for i in l1:
   if i > 0:
   	l2.append(i)
print("List of positive number :")
print(l2)
