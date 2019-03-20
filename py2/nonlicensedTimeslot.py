import re

timeslotBegin = "08:00-08:35"
timeslotEnd = "09:15-10:00"

timeslotBegin_Nospace = re.sub(' ', '', timeslotBegin) # Remove space from string
timeslotEnd_Nospace = re.sub(' ', '', timeslotEnd)


#print "timeslotBegin_Nospace:" + timeslotBegin_Nospace

timeslotBegin = re.findall('-\d\d.\d\d', timeslotBegin_Nospace)[0]
timeslotBegin = re.findall('\d\d.\d\d', timeslotBegin)[0]

timeslotEnd = re.findall('\d\d.\d\d-', timeslotEnd_Nospace)[0]
timeslotEnd = re.findall('\d\d.\d\d', timeslotEnd)[0]


z = "'|"
x = "?"
y = "O"
ym = "o"
w = "Q"
c = "Z"
cm = "z"

if z in timeslotBegin or x in timeslotBegin or y in timeslotBegin or ym in timeslotBegin or w in timeslotBegin or c in timeslotBegin or cm in timeslotBegin: # OCR sometimes identify " 1"  as " '| "
	if z in timeslotBegin:
		timeslotBegin = re.sub("\'\|", "1", timeslotBegin) #make the replacement
	if x in timeslotBegin:
		timeslotBegin = re.sub("\?", "7", timeslotBegin)
	if y in timeslotBegin or ym in timeslotBegin:
		timeslotBegin = re.sub("O|o", "0", timeslotBegin)
	if w in timeslotBegin:
		timeslotBegin = re.sub("Q", "9", timeslotBegin)
	if c in timeslotBegin or cm in timeslotBegin:
		timeslotBegin = re.sub("Z|z", "2", timeslotBegin)

		
if z in timeslotEnd or x in timeslotEnd or y in timeslotEnd or ym in timeslotEnd or w in timeslotEnd or c in timeslotEnd or cm in timeslotEnd: # OCR sometimes identify " 1"  as " '| "
	if z in timeslotEnd:
		timeslotEnd = re.sub("\'\|", "1", timeslotEnd) #make the replacement
	if x in timeslotEnd:
		timeslotEnd = re.sub("\?", "7", timeslotEnd)
	if y in timeslotEnd or ym in timeslotEnd:
		timeslotEnd = re.sub("O|o", "0", timeslotEnd)
	if w in timeslotEnd:
		timeslotEnd = re.sub("Q", "9", timeslotEnd)
	if c in timeslotEnd or cm in timeslotEnd:
		timeslotEnd = re.sub("Z|z", "2", timeslotEnd)


timeslotNonLicensed = timeslotBegin + "-" + timeslotEnd

print timeslotNonLicensed

#ret_dict = {}
#ret_dict["timeslotNonLicensed"] = ""
#ret_dict["returncode"] = 0 # set to 1 to output on the FAILURE output

#return ret_dict
