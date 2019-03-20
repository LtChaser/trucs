# To use the input params, simply use d["videoTime"] 
# Your code here

import re



TimeslotOCR = "Fri 2 Mar / 09:1 5-0950"

formatted = re.sub(' ', '', TimeslotOCR)


formatted = re.sub(";", ":", formatted)

	
try:
	formatted = re.findall('..:..-..:..', formatted)[0]
except IndexError:
	try:
		formatted = re.findall('\d\d.*?\d\d\-\d\d.*?\d\d', formatted)[0]
	except:
		pass
		
z = "'|"
x = "?"
y = "O"
ym = "o"
w = "Q"
c = "Z"
cm = "z"

try:
	if z in formatted or x in formatted or y in formatted or ym in formatted or w in formatted or c in formatted or cm in formatted: # OCR sometimes identify " 1"  as " '| "
		if z in formatted:
			formatted = re.sub("\'\|", "1", formatted) #make the replacement
		if x in formatted:
			formatted = re.sub("\?", "7", formatted)
		if y in formatted or ym in formatted:
			formatted = re.sub("O|o", "0", formatted)
		if w in formatted:
			formatted = re.sub("Q", "9", formatted)
		if c in formatted or cm in formatted:
			formatted = re.sub("Z|z", "2", formatted)
		TimeslotStandarised = formatted
	
	else:
		TimeslotStandarised = formatted

except IndexError:
	TimeslotStandarised = TimeslotOCR

if TimeslotStandarised[2] != ':' or TimeslotStandarised[8] != ':':    #Verify that the format is not something such as : 14215-14230
	TimeslotStandarised = TimeslotStandarised[0:2] + ':' + TimeslotStandarised[3:8] + ':' + TimeslotStandarised[8:11]	
	
	
print TimeslotStandarised