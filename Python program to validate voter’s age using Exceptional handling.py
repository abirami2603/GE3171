try:
    age=int(input("Enter your age"))
    if age>=18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote") 
except:
    print("age must be a valid number")   
