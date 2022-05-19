# Python 3.10.4
import config
import sys

# filter data
def filterData(thedata,wordlength):
	global EditedTotalLength 
	config.debug("filterData: convert wordlength to int (just in case)")
	wordlength=int(wordlength)
	thedata2=[]
	EditedTotalLength=0
	for item in thedata:
		if len(item)==wordlength:
			thedata2.append(item)
			EditedTotalLength += 1
	return thedata2

# open file into memory, returns the data
def openFile(sourcefile):
	global OriginalLength
	config.debug("openFile: Opening sourcefile: " + sourcefile) 
	thedata=[]
	OriginalLength=0
	with open(sourcefile,'r') as f:
		for line in f:
			entry=f.readline()
			entry=entry.strip('\n')
			thedata.append(entry)
			OriginalLength += 1
	return thedata

# main function
def main():
	# open file into memory
	if config.config.has_option("GETDATA","source_file"):
		thedata=openFile("./english-words/"+config.config.get('GETDATA','source_file'))
	else:
		config.debug("Unable to find 'source_file' entry in the configuration file")
		sys.exit(1)

	# filter the list for words that are word_length long
	if config.config.has_option("GETDATA","word_length"):
		wordlength=int(config.config['GETDATA']['word_length'])
		thedata=filterData(thedata,wordlength)
	else:
		config.debug("Unable to find 'word_length' entry in the configuration file")
		sys.exit(1)

	# print current data
	print("Total Length of File "+str(OriginalLength))
	print("Edited Length of File "+str(EditedTotalLength))

# check for proper environment to run main() function automatically
if __name__ == '__main__':
	main()

