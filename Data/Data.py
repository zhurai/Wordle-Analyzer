# Python 3.10.4
import config
import getData
import sys

# main function
def main():
	# open file into memory
	if config.config.has_option("GETDATA","source_file"):
		thedata=getData.openFile("./english-words/"+config.config.get('GETDATA','source_file'))
	else:
		config.debug("Unable to find 'source_file' entry in the configuration file")
		sys.exit(1)

	# filter the list for words that are word_length long
	if config.config.has_option("GETDATA","word_length"):
		wordlength=int(config.config['GETDATA']['word_length'])
		thedata=getData.filterData(thedata,wordlength)
	else:
		config.debug("Unable to find 'word_length' entry in the configuration file")
		sys.exit(1)

	# print current data
	print("Total Length of File "+str(getData.OriginalTotalLength))
	print("Edited Length of File "+str(getData.EditedTotalLength))

# check for proper environment to run main() function automatically
if __name__ == '__main__':
	main()

