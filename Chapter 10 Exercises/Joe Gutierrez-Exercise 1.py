#Joe Gutierrez - 2/1/18 - Chapter 10 - Exercise 1

#Revise a previous program as follows: Read and parse the "From" lines and pull out the addresses from the line. 
#Count the number of messages from each person using a dictionary.

file = input('Enter file name: ')

try :
    fhand = open(file)
except :
    print ('Cant open file: ', file, '.', 'retry.')
    exit ()

counts = dict()

for line in fhand :
    if not line.startswith('From ') : continue
    stuff = line.split()
    stuff = stuff[1]
    counts[stuff] = counts.get(stuff, 0) + 1

lst = list()    
for key, val in counts.items() :
    lst.append( (val, key))  

lst.sort(reverse=True)

val, key = lst[0]
print (key, val)

