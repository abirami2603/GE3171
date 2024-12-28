f = open("file1.txt", "wt")
f.write("Python is an interpreted high-level general-purpose programming language.")

with open("file1.txt") as f:
    with open("file2.txt", "w") as f1:
        for line in f:
            f1.write(line)
f2=open("file2.txt","rt")
print("File copied successfully.The contents are:\n",f2.read())

