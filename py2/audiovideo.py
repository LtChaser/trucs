import re

MOSData = "{'videoMOS': {'blockinessScore': 0, 'blurrinessScore': 0, 'jerkinessScore': 0, 'videoMOSScore': 1.4144444435834885}, 'audioMOS': {'loudnessScore': 78, 'saturationScore': 1.0891610110702459, 'bandwidth': 14.827702684304677, 'audioMOSScore': 467, 'silenceScore': 0.189}, 'mediametrie': []}"
expectedFloat = re.compile(r'\d.\d') # Regex for .search If statements
simpleInt = re.compile(r'\d')

### Video Presence Check ####
if "videoMOSScore" in MOSData:
    
	xtract = re.findall("'videoMOSScore': \d...", MOSData)[0]
	print(xtract)
	if expectedFloat.search(xtract): # VideoMOS usually has a Floating Point
		VideoScore = float(re.findall("\d\.\d", xtract)[0])
  
	elif simpleInt.search(xtract):
		VideoScore = int(re.findall("\d", xtract)[0])
    		   
	if VideoScore > 1.5 :
		VideoPresence = True     #    Bool used in Final Post
		intVideoPresence = 1    #    int used in Small Post
		print("here")
        
	else: 
		VideoPresence = False
		intVideoPresence = 0   
else:
    
    VideoPresence = False
    intVideoPresence = 0

### Audio Presence Check ###

if "audioMOSScore" in MOSData:
    
    xtract = re.findall("'audioMOSScore': \d..", MOSData)[0]
    AudioScore = int(re.findall("\d", xtract)[0]) # Audio Score is always an Int
     
    if AudioScore > 0:
        AudioPresence = True
        intAudioPresence = 1
        
    else: 
        AudioPresence = False
        intAudioPresence = 0

else:
    
    AudioPresence = False
    intAudioPresence = 0

print "Audio: ", intAudioPresence
print "Video: ", intVideoPresence



