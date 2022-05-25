# Python 3.10.4
import config
import string

# Collect Information on the data
def getInformation(thedata,length):
	theinfo = {}

	# Number of words in lexicon
	theinfo['length'] = length

	# Number of words containing each letter of the word at least once
	for letter in list(string.ascii_lowercase):
		count=0
		countmult=0
		for item in thedata:
			if item.count(letter) >= 1:
				count=count+1
			if item.count(letter) > 1:
				countmult=countmult+1
		theinfo['once-'+letter]=count
		theinfo['multi-'+letter]=countmult
	
	return theinfo

# filter data
def filterData(thedata,wordlength):
	config.debug("filterData: convert wordlength to int (just in case)")
	wordlength=int(wordlength)
	thedata2=[]
	thelength=0
	for item in thedata:
		if len(item)==wordlength:
			thedata2.append(item)
			EditedTotalLength += 1
	return thedata2,thelength

# open file into memory, returns the data
def openFile(sourcefile):
	config.debug("openFile: Opening sourcefile: " + sourcefile) 
	thedata=[]
	thelength=0
	with open(sourcefile,'r') as f:
		for line in f:
			entry=f.readline()
			entry=entry.strip('\n')
			thedata.append(entry)
			OriginalTotalLength += 1
	return thedata,thelength
