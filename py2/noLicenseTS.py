
import re

timeslotBegin = "08:00-08:35"
timeslotEnd = "08:35-09:15"

timeslotBegin = re.sub(' ', '', timeslotBegin) # Remove space from string
timeslotEnd = re.sub(' ', '', timeslotEnd)

timeslotBegin = re.findall('\d\d.\d\d:')
print timeslotBegin


z = "'|"
x = "?"
y = "O"
ym = "o"
w = "Q"
c = "Z"
cm = "z"

if z in strNospace or x in strNospace or y in strNospace or ym in strNospace or w in strNospace or c in strNospace or cm in strNospace: # OCR sometimes identify " 1"  as " '| "
	if z in strNospace:
		strNospace = re.sub("\'\|", "1", strNospace) #make the replacement
	if x in strNospace:
		strNospace = re.sub("\?", "7", strNospace)
	if y in strNospace or ym in strNospace:
		strNospace = re.sub("O|o", "0", strNospace)
	if w in strNospace:
		strNospace = re.sub("Q", "9", strNospace)
	if c in strNospace or cm in strNospace:
		strNospace = re.sub("Z|z", "2", strNospace)
	TimeslotOCR = strNospace
	
else:
    TimeslotOCR = strNospace
	
try:
	stripit = re.findall('\d\d.\d\d\-\d\d.\d\d', TimeslotOCR)[0] #  filtrate string to keep only the appropriate format
	TimeslotStandarised = re.sub('[a-zA-Z]', ':', stripit) # Replace " : "  if needed
except IndexError:
	TimeslotStandarised = TimeslotOCR



ret_dict = {}
ret_dict["TimeslotStandarised"] = TimeslotStandarised
ret_dict["returncode"] = 0 # set to 1 to output on the FAILURE output

return ret_dict
