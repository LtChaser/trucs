# To use the input params, simply use d["videoTime"] 
# Your code here

import re

#TimeslotOCR = "Mon 26 Mar/1440-15:10/"
TimeslotOCR = ", 12:35 - 12:45 . Anim"
	#Mon 26 Mar/13:00-13z55 /
	#15:35 - 'l5:55

strNospace = re.sub(' ', '', TimeslotOCR) # Remove space from string

z = "'|"
v = "'l"
x = "?"
y = "O"
ym = "o"
w = "Q"
c = "Z"
cm = "z"

if z in strNospace or x in strNospace or y in strNospace or ym in strNospace or w in strNospace or c in strNospace or cm in strNospace or v in strNospace: # OCR sometimes identify " 1"  as " '| "
	if z in strNospace or v in strNospace:
		strNospace = re.sub("\'\||'l", "1", strNospace) # replace '| by 1 or 'l by 1
	if x in strNospace:
		strNospace = re.sub("\?", "7", strNospace)
	if y in strNospace or ym in strNospace:
		strNospace = re.sub("O|o", "0", strNospace)
	if w in strNospace:
		strNospace = re.sub("Q", "9", strNospace)
	if c in strNospace:
		strNospace = re.sub("Z", "2", strNospace)
	if cm in strNospace:
		strNospace = re.sub("z", ":", strNospace)
	TimeslotOCR = strNospace
	
else:
    TimeslotOCR = strNospace

print TimeslotOCR
	
try:
    stripit = re.findall('\d\d:*\d\d\-\d\d:*\d\d', TimeslotOCR)[0] #  filtrate string to keep only the appropriate format
    print "stripit:", stripit
    TimeslotStandarised = re.sub('[a-zA-Z]', ':', stripit) # Replace " : "  if needed
    if TimeslotStandarised[2] != ':' or TimeslotStandarised[8] != ':':    #Verify that the format is not something such as : 14215-14230
        TimeslotStandarised = TimeslotStandarised[0:2] + ':' + TimeslotStandarised[3:8] + ':' + TimeslotStandarised[8:11]
except IndexError:
    TimeslotStandarised = TimeslotOCR



print TimeslotStandarised


