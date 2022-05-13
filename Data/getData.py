# Python 3.10.4
import config

# filter data
def filterData(thedata,wordlength):
	config.debug("filterData: convert wordlength to int (just in case)")
	wordlength=int(wordlength)

# open file into memory, returns the data
def openFile(sourcefile):
	config.debug("openFile: Opening sourcefile: " + sourcefile) 
	thedata=[]
	with open(sourcefile,'r') as f:
		thedata.append(f.readlines())
	return thedata

# main function
def main():
	# open file into memory
	if config.config.has_option("GETDATA","source_file"):
		thedata=openFile("./english-words/"+config.config['GETDATA']['source_file'])
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

# check for proper environment to run main() function automatically
if __name__ == '__main__':
	main()

