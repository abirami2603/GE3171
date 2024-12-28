s= input("enter the string") 
length=len(s) 
rev=s[length::-1]
if s==rev:
    print("The string is palindrome")
else:
    print("The string is not palindrome")
 