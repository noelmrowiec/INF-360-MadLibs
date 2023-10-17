# Mad Libs program
#author: Noel Mrowiec
# Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file

from pathlib import Path
import re

#Read text file
is_valid_filename = False
fileMadlib = None
textMadlib = ''

fileMadlib = open(input("Enter a file name: "), 'r')

textMadlib = fileMadlib.read();
fileMadlib.close()

print(textMadlib)

#split text into list in order to find blanks
textMadlibList = textMadlib.split()


# find parts of speech
# parts of speech must be uppercase in textfile
#below not needed because just check list now
#regex = r"\b[A-Z]*\b"
#blanks = re.findall(regex, textMadlib)

# enter the parts of speech ex) below
for index, blank in enumerate(textMadlibList):
     if blank.isupper():
         textMadlibList[index] = input(f'Enter a(n) {blank} ')

finished = ' '.join(textMadlibList)

fileMadlib = open("madlibnew.txt", 'w')
fileMadlib.write(finished)

#close file
fileMadlib.close()