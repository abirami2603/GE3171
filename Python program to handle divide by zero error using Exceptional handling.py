try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = a / b
except ValueError:
    print("You have entered wrong data")
except ZeroDivisionError:
    print("Divide by Zero Error!!!")
else:
    print("The result:", c)


