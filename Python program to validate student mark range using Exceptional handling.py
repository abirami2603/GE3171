try:
    mark=int(input("Enter your mark"))
    if mark>0 and mark<=100:
        print("Valid Mark")
    else:
        print("Invalid mark") 
except:
    print("Mark must be a valid number")    
