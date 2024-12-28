def display(L1,L2):
    print("1.Union\t 2.Intersection\t3.Set difference\t4.Symmetric difference")
    option=int(input("Enter a option"))
    if (option==1):
        print("Union of L1 and L2 is ",L1 | L2)
        display(L1,L2)
    elif (option==2):
        print("Intersection of L1 and L2 is ",L1 & L2)
        display(L1,L2)
    elif (option==3):
        print("Difference of L1 and L2 is ",L1 - L2)
        display(L1,L2)
    elif (option==4):
        print("Symmetric difference of L1 and L2 is ",L1 ^ L2)
        display(L1,L2)
L1 = {'Pitch', 'Syllabus', 'Script', 'Grammar', 'Sentences'};
L2 = {'Grammar', 'Syllabus', 'Context', 'Words', 'Phonetics'};
display(L1,L2)

