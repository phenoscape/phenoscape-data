#!/usr/bin/env python2.6
import sys,time

print "stripMatrix.py - Andrew Melo <andrew.melo@gmail.com>"
print "Copy-paste a matrix, hit CTRL-D when done:"

# get data
input = sys.stdin.readlines()

# strip newlines and spaces
cleanLineList = [ x.strip().replace(" ","") for x in input ]
data          = "".join(cleanLineList)
# begin reading
readingName = True
readingCol  = False
complexCol  = ""
currentName = ""
currentData = []
output      = []
for char in data:
    if readingName:
        if char.isalpha():
            currentName += char
        else:
            readingName = False
            currentData = [ char ]
    else: # not reading a name
        if not char.isalpha():
            if char == '{':
                readingCol = True
            elif char == '}':
                currentData.append( complexCol )
                complexCol = ""
                readingCol = False
            elif readingCol == True:
                complexCol += char
            else:
                currentData.append( char )
        else:
            readingName = True
            if readingCol == True:
                complexCol = ""
                readingCol = False
            output.append( ( currentName,currentData ) )
            currentName = char

output.append( (currentName, currentData) )

filename = "%s.csv" % int(time.time())
handle = open(filename, "w")
for k,v in output:
    handle.write("%s, %s\n" % (k, ",".join(v)))

handle.close()
print "Output is in %s. Import as a .CSV into excel" % filename

