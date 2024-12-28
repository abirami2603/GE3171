f = open("demofile.txt", "wt")
f.write("Python is an interpreted high-level general-purpose programming language.")

f = open("demofile.txt", "rt")
data = f.read()
words = data.split()
print("The total number of words are:",len(words))
f.close()
