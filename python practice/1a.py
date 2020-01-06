#Write a program to count total number of vowels in given string
vowels = "aeiouAEIOU"
count=0
sen = input("Enter a sentence \n")
for i in range(len(vowels)):
    for j in range(len(sen)):
        if(vowels[i]==sen[j]):
            count+=1
print("Total number of vowels : ",count)