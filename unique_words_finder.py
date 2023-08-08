''' Exercise 4: Find all unique words in a file
Shakespeare used over 20,000 words in his works. 
List all unique words, sorted in alphabetical order, 
that are stored in a file romeo.txt 
containing a subset of Shakespeare's work.
To get started, download a copy of the file 
www.py4e.com/code3/romeo.txt. 
Create a list of unique words, which will contain the final result. 
Write a program to open the file romeo.txt and read it line by line.
 For each line, split the line into a list of words using the split
 function. For each word, check to see if the word is already
   in the list of unique words. If the word is not in the list of 
   unique words, add it to the list. When the program completes, 
   sort and print the list of unique words in alphabetical order.”

'''
counts = dict()
file_name = input('Enter the name of the file: ')
fhandle = open(file_name)
for line in fhandle:
    word = line.split()
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] = counts[word] + 1
    print(counts)
