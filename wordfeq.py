# The following program implements part of a text processing library
# importing sys module to use sys.exit() method
import sys


# converts a string to integer and returns integer value
def mk_int(s):
    s = s.strip()
    return int(s) if s else 0


# converts input text into a list sorted by most frequently occurring words
def CalFreqWords(text):
        from collections import Counter
        words = (text.lower().replace(',', ' ').replace('.', ' ')).split(" ")
        count = Counter(words)
        return sorted(count.items(), key=lambda x: (-x[1], x[0]))


# Class has 03 function definitions for implementing text processing logic
class IWordFreqAnalyzer:

    # function to compute the highest frequency
    def CalHighestFreq(self, text):
        return CalFreqWords(text)[0][1]

    # function to count the freq of a specified word within the input text
    def CalFreqForWord(self, text, word):
        listw = CalFreqWords(text)
        for i in range(0, len(listw)):
            if listw[i][0] == word.lower():
                return listw[i][1]

    # function to compute a list of the n most frequently occurring words
    def CalMostFreqNWords(self, text, n):
        listw = CalFreqWords(text)
        return [x for x in listw[:n]]


# Counter variable to track of the number of times user has given invalid text
ctrt = 0

# loop to accept user-defined text which runs until user provides valid string
while True:
    text = input('Enter the text:')
    ctrt = ctrt+1
    if ((not text) and ctrt < 4):
        print("please enter some value for text")
        continue
    else:
        break
if(ctrt == 4):
    print("no input text was entered")
    sys.exit()

# Counter to track of the o.r of times user has given invalid word input
ctrw = 0
# loop to acceptuser-defined word which runs until valid string
while True:
    word = input('Enter the word to find Frequency:')
    ctrw = ctrw+1
    if ((not word) and ctrw < 4):
        print("please enter some value for word")
        continue
    else:
        break

# Counter to keep track of the number of times user has given invalid input
ctrf = 0

# loop to accept a user-defined frequency until a valid string
while True:
    fs = input('Enter the no of frequency words to be displayed(0 for none):')
    ctrf = ctrf+1
    if ((not fs) and ctrf < 4):
        print("please enter some value for frequency")
        continue
    elif (mk_int(fs) < 0 and ctrf < 4):
        print("please enter values greater than 0 for displaying frequency ")
        continue
    else:
        break

# converts user input string frequency to integer frequency
fi = mk_int(fs)
# object of class IWordFreqAnalyzer
obj = IWordFreqAnalyzer()
print('The most repeated word is:', CalFreqWords(text)[0][0])

if(ctrw < 4):
    print('The frequency for entered word is:', obj.CalFreqForWord(text, word))
if(ctrf == 4):
    print('The list of all words from entered text:', CalFreqWords(text))
else:
    print('The most frequency words:', obj.CalMostFreqNWords(text, fi))
