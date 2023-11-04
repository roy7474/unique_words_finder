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

fname = input("Enter file name: ")      #ask user for file name
fh = open(fname)
lst = list()                            #make a list

for line in fh:
    word_split = line.split()
    for word in word_split:             
        if word not in lst:             # if the word is not in the list, add to the list
            lst.append(word)
        else:                           # otherwise, continue
            continue

print(sorted(lst))                      #print list