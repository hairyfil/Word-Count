# 
# Testing SCM with GitHUb
# Open a file and count how many occurences of each word
# print the results in a variety of forms
#

import operator
import re
import sys
import os

print "--------------------------------------"
print

#print('sys.argv[0] =', sys.argv[0])
PATHNAME = os.path.dirname(sys.argv[0])
#print('path =', pathname)
#print('full path =', os.path.abspath(pathname))

os.chdir(os.path.abspath(PATHNAME))
CWD = os.getcwd()
print "Current Working Directory is - " + CWD

MYINPUTFILE = open("text.txt", "r")

# dictionary is an unordered key/value pair list
# define the wordcount dictionary to store words in
WORDCOUNT = {}

# populate the dictionary with ALL words from the file
#for word in file.read().split():
#    if word.lower() not in wordcount:
#        wordcount[word.lower()] = 1
#    else:
#        wordcount[word.lower()] += 1

# populate the dictionary with ALL words from the file
# all non [a-zA-Z] characters stripped out and changed to lowercase

for word in MYINPUTFILE.read().split():
    trackedword = re.sub("[^a-zA-Z]+", "", word.lower())
    if trackedword not in WORDCOUNT:
        WORDCOUNT[trackedword] = 1
    else:
        WORDCOUNT[trackedword] += 1

# simple print loops
# Print the dictionary- style #1
#for w, c in wordcount.items():
#    print(w, c)
#
# Print the dictionary- style #2
#for w, c in wordcount.items():
#    print("{}\t{}".format(w, c))


print
print "-----------------------------------------"
print "Sorted by key - alphabetically"
print "-----------------------------------------"
print
print
print "Word\t\tCount"
print "----\t\t-----"
# long form version of the one actually being used
# for key, value in sorted(wordcount.items(), key=operator.itemgetter(0)):
# the key=operator.itemgetter(0) isn't required and is assumed to be the default if omitted

for key, value in sorted(WORDCOUNT.items()):
    if len(key) > 8:
        print "{}\t{}".format(key, value)
    else:
        print "{}\t\t{}".format(key, value)

print
print "-----------------------------------------"
print "Sorted by value - small to large"
print "-----------------------------------------"
print
print
print "Word\t\tCount"
print "----\t\t-----"

for key, value in sorted(WORDCOUNT.items(), key=operator.itemgetter(1)):
    if len(key) > 8:
        print "{}\t{}".format(key, value)
    else:
        print "{}\t\t{}".format(key, value)
print
print "-----------------------------------------"
print "Sorted by value - large to small"
print "-----------------------------------------"
print
print "Word\t\tCount"
print "----\t\t-----"

for key, value in sorted(WORDCOUNT.items(), key=operator.itemgetter(1), reverse=True):
    if len(key) > 8:
        print "{}\t{}".format(key, value)
    else:
        print "{}\t\t{}".format(key, value)

MYINPUTFILE.close()
