# Python 3.10.4
import config
import string

# Collect Information on the data
def getInformation(thedata,length,edited):
	theinfo = {}
	wordlength=int(config.config.get('GETDATA','word_length'))

	# Number of words in lexicon
	config.debug("getInformation: get number of words in lexicon: " + str(length))
	theinfo['length'] = length

	# Number of words containing each letter of the word at least once
	config.debug("getInformation: get the number of words with a specific letter appearing once/multiple times")
	for letter in list(string.ascii_lowercase):
		count=0
		countmult=0
		for item in thedata:
			if item.count(letter) == 1:
				count=count+1
			if item.count(letter) > 1:
				countmult=countmult+1
		theinfo['once-'+letter]=count
		theinfo['multi-'+letter]=countmult

	# Only continue on if it is the edited version (based off word_length)
	config.debug("getInformation: check if edited, if so: continue, if not: return data here")
	if edited is False:
		return theinfo

	# Number of words with each letter in position 1..x
	config.debug("getInformation: check the number of words with each letter for each position")
	for position in range(0,wordlength):
		# position 0 = 1st position on wordle!
		for letter in list(string.ascii_lowercase):
			count=0
			for item in thedata:
				if item[position] == letter:
						count=count+1
			theinfo['position-'+str(position+1)+'-'+letter]=count
	
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
			thelength=thelength+1
	return thedata2,thelength

# open file into memory, returns the data
def openFile(sourcefile):
	config.debug("openFile: Opening sourcefile: " + sourcefile) 
	thedata=[]
	thelength=0
	with open(sourcefile,'r') as f:
		for line in f:
			entry=line.strip('\n')
			thedata.append(entry)
			thelength=thelength+1
	return thedata,thelength
