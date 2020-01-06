#Write a program to check whether a passed letter is a vowel or not.
vowels = "aeiouAEIOU"
char = input("Enter a letter : ")

if char in vowels:
    print("It is a vowel")
else:
    print("It is not a vowel")