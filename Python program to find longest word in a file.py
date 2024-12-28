# Open the file in write mode and write some text
with open("demofile.txt", "wt") as f:
    f.write("Python is an interpreted high-level general-purpose programming language.")

# Open the file in read mode and find the longest word
with open("demofile.txt", "r") as fin:
    str = fin.read()

# Split the content into words
words = str.split()

# Find the length of the longest word
max_len = len(max(words, key=len))

# Loop through words to find the longest word
for word in words:
    if len(word) == max_len:
        longest_word = word

# Print the longest word
print("The longest word in the file is", longest_word)
