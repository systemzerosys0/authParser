#!/usr/bin/env python3
import re
import sys
from operator import itemgetter 

firstArray = []
logArray = []
knownIPs = {}
# Declaring variables
 
with open(sys.argv[1]) as file:
    for line in file:
        firstArray += re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
# Opens the text file provided and looks for IP addresses. Should be noted that this
#regex expression does not check if the IP address is valid or not. 
        
for i in firstArray:
    logArray.append(i)
# Iterates through firstArray and adds each IP address to logArray.  
for i in logArray:
    if i in knownIPs:
        continue
    else:
        knownIPs[i] = 0
# Iterates through the now filled logArray, and adds each unique IP to
#the knownIPs dictionary as a key:value pair. The value for that key is set to 0.
for i in knownIPs:
    for j in logArray:
        if i == j:
            knownIPs[i] += 1
            continue
# Iterates through the knownIPs dictionary. For each value in knownIPs,
#also iterate through logArray. Then, check if logArray at the 2nd loop's
#iterated value is in knownIPs. If it is, increment that key's value by 1.
# In non-Deep Speech, this part of the code counts the frequency of the IP
#addresses we see.

percent = 0
ipTotal = 0
frequency = 0
address = ''
frequencyArray = knownIPs.values()
solveList = []
# Declaring some more variables we'll use in the following code.

for i in frequencyArray:
    if i != '0.0.0.0':
        ipTotal += i
# annoying little piece of code, but it works miracles. dictionaries
#are unpleasant to work with.

for i in knownIPs:
    # iterate once more through knownIPs
        
    frequency =  knownIPs[i]
    if ipTotal != 0:
        percent = round((float(frequency/ipTotal) * 100), 5)
    else:
        continue
    tempList = []
    tempList.append(percent)
    tempList.append(frequency)
    tempList.append(i)
    solveList.append(tempList)
# Iterates once more through knownIPs, and uses the 
#Key:value pairs to calculate some useful statistics.

if __name__ == "__main__":
    p = ['Percent', 'Count', 'IP']
    q = ['Total', ipTotal]
    
    sortedList = sorted(solveList, key=itemgetter(1))
    
    print("{: >20} {: >20} {: >20}".format(*p))
    for i in sortedList:
        print("{: >20} {: >20} {: >20}".format(*i))
    print("{: >20} {: >20}".format(*q))
# Boilerplate that prettifies the code. kirakira
    
#==================================================

#Pseudocode. Leaving this here for clarity's sake. You can delete it if you want, idc
# Create an empty array
# Open the file 
# Iterate through each line
#import re
# ip = re.compile(r'\d{*}.\d{*}.\d{*}.\d{*})
# Search the line for something that matches ip
# Add that IP address to the array 
# Repeat that process to the end of the file


# pt 2
# iterate through logArray
# for each IP, check if the address is in knownIP
# if not, add it to knownIP
# iterate through knownIP (i)
# make a variable for that ip called [ip]Count 
# iterate through logArray (j)
# for i in j, [ip]Count ++1
# 

# Pt 3
# Create a variable called percent, frequency, and address
# Frequency == number of times IP appears in the array
# Percent == float(frequency/array.length)
# Address, an empty string